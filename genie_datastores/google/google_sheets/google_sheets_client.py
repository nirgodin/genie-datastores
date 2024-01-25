from typing import Optional, List, Union

import gspread
from genie_common.tools import logger
from gspread import Client, Spreadsheet, Worksheet
from gspread.exceptions import APIError
from pandas import DataFrame

from genie_datastores.google.google_sheets.models.share_settings import ShareSettings
from genie_datastores.google.google_utils import load_google_credentials


class GoogleSheetsClient:
    def __init__(self, client: Client):
        self._client = client

    @classmethod
    def create(cls) -> "GoogleSheetsClient":
        credentials = load_google_credentials()
        gspread_client = gspread.service_account_from_dict(credentials)

        return cls(gspread_client)

    def create_spreadsheet(self,
                           title: str,
                           folder_id: Optional[str] = None,
                           share_settings: Optional[List[ShareSettings]] = None) -> Spreadsheet:
        logger.info(f"Starting to create spreadsheet")
        spreadsheet = self._client.create(title, folder_id)
        logger.info(f"Successfully created spreadsheet with url `{spreadsheet.url}`")

        if share_settings is not None:
            self.share(spreadsheet, *share_settings)

        return spreadsheet

    def delete(self, worksheet_name: str, spreadsheet: Union[Spreadsheet, str]) -> None:
        worksheet = self._get_worksheet(worksheet_name=worksheet_name, spreadsheet=spreadsheet)
        logger.info(f"Deleting worksheet `{worksheet_name}` from spreadsheet `{spreadsheet.url}`")
        spreadsheet.del_worksheet(worksheet)
        logger.info(f"Successfully deleted worksheet")

    @staticmethod
    def list_worksheets(spreadsheet: Spreadsheet) -> List[str]:
        return [worksheet.title for worksheet in spreadsheet.worksheets()]

    def read(self, worksheet_name: str, spreadsheet: Union[Spreadsheet, str]) -> DataFrame:
        worksheet = self._get_worksheet(
            worksheet_name=worksheet_name,
            spreadsheet=spreadsheet,
        )
        records = worksheet.get_all_records()

        return DataFrame.from_dict(records)

    @staticmethod
    def share(spreadsheet: Spreadsheet, *share_settings: ShareSettings) -> None:
        logger.info(f"Sharing spreadsheet with {len(share_settings)}")

        for setting in share_settings:
            spreadsheet.share(**setting.to_kwargs())

        logger.info(f"Finished sharing spreadsheet")

    def write(self,
              spreadsheet: Union[Spreadsheet, str],
              worksheet_name: str,
              data: DataFrame,
              overwrite: bool = False) -> None:
        spreadsheet = self._get_spreadsheet(spreadsheet)
        logger.info(f"Writing data to spreadsheet `{spreadsheet.url}`")

        if worksheet_name in self.list_worksheets(spreadsheet):
            self._handle_existing_worksheet(
                spreadsheet=spreadsheet,
                worksheet_name=worksheet_name,
                overwrite=overwrite
            )

        self._add_worksheet(
            worksheet_name=worksheet_name,
            data=data.fillna("").applymap(str),
            spreadsheet=spreadsheet
        )

    def _get_spreadsheet(self, spreadsheet: Union[str, Spreadsheet]) -> Spreadsheet:
        if isinstance(spreadsheet, str):
            return self._client.open_by_url(spreadsheet)

        return spreadsheet

    def _get_worksheet(self, worksheet_name: str, spreadsheet: Union[Spreadsheet, str]) -> Worksheet:
        try:
            spreadsheet = self._get_spreadsheet(spreadsheet)
            return spreadsheet.worksheet(worksheet_name)

        except APIError:
            raise Exception(f'The service does not have permissions to read the sheet. '
                            f'Please share your sheet with the account: {self._client.auth.signer_email}')

    def _handle_existing_worksheet(self, spreadsheet: Spreadsheet, worksheet_name: str, overwrite: bool):
        if overwrite:
            logger.info("Found existing worksheet with the same name. Deleting it as `overwrite=True`")
            self.delete(worksheet_name=worksheet_name, spreadsheet=spreadsheet)

        else:
            raise ValueError(
                f'A worksheet named `{worksheet_name}` already exists in this spreadsheet. Set `overwrite=True` to '
                f'overwrite it'
            )

    @staticmethod
    def _add_worksheet(spreadsheet: Spreadsheet, worksheet_name: str, data: DataFrame) -> Worksheet:
        logger.info(f"Adding worksheet to spreadsheet `{spreadsheet.url}`")
        worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows=data.shape[0] + 2, cols=data.shape[1] + 1)
        worksheet.format('A1:AZ1', {'textFormat': {'bold': True}})
        worksheet.format("A:AZ", {"wrapStrategy": "CLIP"})
        worksheet.append_rows([data.columns.values.tolist()] + data.values.tolist())
        logger.info(f"Successfully written data to spreadsheet `{spreadsheet.url}`")

        return worksheet
