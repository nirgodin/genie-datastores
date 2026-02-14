from enum import Enum


class LyricsSectionType(Enum):
    INTRO = "intro"
    VERSE = "verse"
    PRE_CHORUS = "pre_chorus"
    CHORUS = "chorus"
    POST_CHORUS = "post_chorus"
    BRIDGE = "bridge"
    OUTRO = "outro"
    OTHER = "other"
