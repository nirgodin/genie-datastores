from datetime import datetime
from typing import Optional, Iterable, Any, Dict

from gspread import Spreadsheet

from genie_datastores.google.google_consts import DEFAULT_WORKSHEET, TITLE, SHARE_SETTINGS, FOLDER_ID
from genie_datastores.google.sheets.google_sheets_client import GoogleSheetsClient
from genie_datastores.google.sheets.models import Sheet, ShareSettings


class GoogleSheetsUploader:
    def __init__(self, google_sheets_client: GoogleSheetsClient, default_settings: Optional[Dict[str, Any]] = None):
        self._google_sheets_client = google_sheets_client
        self._default_settings = default_settings or {}

    @classmethod
    def create(cls) -> "GoogleSheetsUploader":
        sheets_client = GoogleSheetsClient.create()
        return cls(sheets_client)

    def upload(self,
               sheets: Iterable[Sheet],
               title: Optional[str] = None,
               folder_id: Optional[str] = None,
               share_settings: Optional[ShareSettings] = None) -> Spreadsheet:
        spreadsheet = self._google_sheets_client.create_spreadsheet(
            title=self._supplied_value_or_default(value=title, key=TITLE),
            folder_id=self._supplied_value_or_default(value=folder_id, key=FOLDER_ID),
            share_settings=self._supplied_value_or_default(value=share_settings, key=SHARE_SETTINGS)
        )

        for sheet in sheets:
            self._google_sheets_client.write(
                spreadsheet=spreadsheet,
                worksheet_name=sheet.name,
                data=sheet.data
            )

        self._google_sheets_client.delete(worksheet_name=DEFAULT_WORKSHEET, spreadsheet=spreadsheet)
        return spreadsheet

    def _supplied_value_or_default(self, value: Optional[Any], key: str) -> Optional[Any]:
        if value is not None:
            return value

        if key in self._default_settings.keys():
            return self._default_settings[key]

        if key == TITLE:
            return datetime.now().strftime("Export output %d/%m/%Y %H:%M:%S")
