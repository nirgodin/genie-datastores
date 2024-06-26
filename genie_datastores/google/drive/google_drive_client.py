from typing import List

from genie_common.tools import logger
from genie_common.utils import load_google_service_account_info
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from genie_datastores.google.drive.models.google_drive_download_metadata import GoogleDriveDownloadMetadata
from genie_datastores.google.drive.models.google_drive_upload_metadata import GoogleDriveUploadMetadata
from genie_datastores.google.google_consts import PARENTS, FILES, ID


class GoogleDriveClient:
    def __init__(self, drive_service: Resource):
        self._drive_service = drive_service

    @classmethod
    def create(cls) -> "GoogleDriveClient":
        service_account_info = load_google_service_account_info()
        credentials = Credentials.from_service_account_info(service_account_info)
        drive_service = build(
            serviceName='drive',
            version='v3',
            credentials=credentials
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
        files = self.list_dir_files(folder_id)
        files_metadata = [GoogleDriveDownloadMetadata.from_drive_file(file, local_dir) for file in files]

        self.download(*files_metadata)

    def list_dir_files(self, folder_id: str) -> List[dict]:
        logger.info(f"Starting to list all `{folder_id}` files")
        query = f"'{folder_id}' in {PARENTS}"
        results = self._drive_service.files().list(q=query).execute()

        return results.get(FILES, [])

    def clean_folder(self, folder_id: str) -> None:
        query = f"'{folder_id}' in {PARENTS} and trashed=false"
        results = self._drive_service.files().list(q=query).execute()
        files = results.get(FILES, [])

        for file in files:
            self._drive_service.files().delete(fileId=file[ID]).execute()

        logger.info(f"All folder `{folder_id}` contents deleted successfully!")
