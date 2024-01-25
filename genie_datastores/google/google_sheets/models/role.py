from enum import Enum


class Role(Enum):
    OWNER = "owner"
    READER = "reader"
    WRITER = "writer"
