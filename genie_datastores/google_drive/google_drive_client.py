import json
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from genie_common.tools import logger

from genie_datastores.google_drive.google_consts import SERVICE_ACCOUNT_SECRETS_PATH, \
    GOOGLE_SERVICE_ACCOUNT_CREDENTIALS, PARENTS, FILES, ID
from genie_datastores.google_drive.models.google_drive_download_metadata import GoogleDriveDownloadMetadata
from genie_datastores.google_drive.models.google_drive_upload_metadata import GoogleDriveUploadMetadata


class GoogleDriveClient:
    def __init__(self, drive_service: Resource):
        self._drive_service = drive_service

    @classmethod
    def create(cls) -> "GoogleDriveClient":
        drive_service = build(
            serviceName='drive',
            version='v3',
            credentials=cls._build_credentials()
        )
        return cls(drive_service)

    def download(self, *file_metadata: GoogleDriveDownloadMetadata) -> None:
        for file in file_metadata:
            logger.info(f"Starting to download file `{file.file_id}`")
            file_content = self._drive_service.files().get_media(fileId=file.file_id).execute()

            with open(file.local_path, 'wb') as f:
                f.write(file_content)

            logger.info(f'Successfully downloaded file to {file.local_path}')

    def upload(self, *file_metadata: GoogleDriveUploadMetadata) -> None:
        for file in file_metadata:
            media = MediaFileUpload(file.local_path, resumable=True)

            try:
                file = self._drive_service.files().create(body=file.metadata, media_body=media, fields='id').execute()
                logger.info(f'File `{file.get(ID)}` uploaded successfully')
            except HttpError:
                logger.exception(f"Received exception while downloading file `{file.file_name}`")
            finally:
                media.stream().close()

    def download_all_dir_files(self, folder_id: str, local_dir: str) -> None:
        logger.info(f"Starting to download all `{folder_id}` files to `{local_dir}`")
        query = f"'{folder_id}' in {PARENTS}"
        results = self._drive_service.files().list(q=query).execute()
        files = results.get(FILES, [])
        files_metadata = [GoogleDriveDownloadMetadata.from_drive_file(file, local_dir) for file in files]

        self.download(*files_metadata)

    def clean_folder(self, folder_id: str) -> None:
        query = f"'{folder_id}' in {PARENTS} and trashed=false"
        results = self._drive_service.files().list(q=query).execute()
        files = results.get(FILES, [])

        for file in files:
            self._drive_service.files().delete(fileId=file[ID]).execute()

        logger.info(f"All folder `{folder_id}` contents deleted successfully!")

    @staticmethod
    def _build_credentials() -> Credentials:
        if os.path.exists(SERVICE_ACCOUNT_SECRETS_PATH):
            return Credentials.from_service_account_file(SERVICE_ACCOUNT_SECRETS_PATH)

        elif GOOGLE_SERVICE_ACCOUNT_CREDENTIALS in os.environ.keys():
            credentials = json.loads(os.environ[GOOGLE_SERVICE_ACCOUNT_CREDENTIALS])
            return Credentials.from_service_account_info(credentials)

        else:
            raise ValueError('Missing Google service account credentials')
