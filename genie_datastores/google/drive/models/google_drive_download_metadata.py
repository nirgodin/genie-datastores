import os.path
from dataclasses import dataclass


@dataclass
class GoogleDriveDownloadMetadata:
    local_path: str
    file_id: str

    @classmethod
    def from_drive_file(cls, file: dict, local_dir: str) -> "GoogleDriveDownloadMetadata":
        local_path = os.path.join(local_dir, file["name"])
        return cls(local_path=local_path, file_id=file["id"])
