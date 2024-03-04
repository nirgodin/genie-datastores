from random import randint, uniform

from genie_common.utils import random_alphanumeric_string, random_enum_value, random_boolean

from genie_datastores.postgres.models import Case, CaseProgress, PlaylistEndpoint


class PostgresMockFactory:
    @staticmethod
    def case(**kwargs) -> Case:
        return Case(
            id=kwargs.get("id", random_alphanumeric_string()),
            endpoint=kwargs.get("endpoint", random_enum_value(PlaylistEndpoint)),
            playlist_id=kwargs.get("playlist_id", random_alphanumeric_string())
        )

    @staticmethod
    def case_progress(**kwargs) -> CaseProgress:
        return CaseProgress(
            id=kwargs.get("id", randint(1, 1000)),
            case_id=kwargs.get("case_id", random_alphanumeric_string()),
            has_exception=kwargs.get("has_exception", random_boolean()),
            status=kwargs.get("status", random_alphanumeric_string()),
            time_took=kwargs.get("time_took", uniform(0, 30)),
            exception_details=kwargs.get("exception_details", random_alphanumeric_string())
        )
