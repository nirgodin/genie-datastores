from typing import List

from genie_datastores.mongo.models.base_document import BaseDocument


class AboutParagraphDocument(BaseDocument):
    about_id: str
    embedding: List[float]
    number: int
    text: str

    class Settings:
        name = "about_paragraphs"
