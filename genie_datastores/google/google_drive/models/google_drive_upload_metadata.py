from dataclasses import dataclass

from genie_datastores.google.google_consts import NAME, PARENTS


@dataclass
class GoogleDriveUploadMetadata:
    local_path: str
    drive_folder_id: str
    file_name: str

    def __post_init__(self):
        self.metadata = {
            NAME: self.file_name,
            PARENTS: [self.drive_folder_id]
        }
