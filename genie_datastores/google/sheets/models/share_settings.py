from dataclasses import dataclass
from typing import Optional, Union, Dict

from genie_datastores.google.sheets.models.permission_type import PermissionType
from genie_datastores.google.sheets.models.role import Role


@dataclass
class ShareSettings:
    email: str
    permission_type: PermissionType
    role: Role
    notify: bool = False
    notification_message: Optional[str] = None
    with_link: bool = False

    def to_kwargs(self) -> Dict[str, Union[str, bool]]:
        return {
            "email_address": self.email,
            "perm_type": self.permission_type,
            "role": self.role,
            "notify": self.notify,
            "email_message": self.notification_message,
            "with_link": self.with_link
        }
