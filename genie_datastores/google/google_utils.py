import json
import os
from typing import Dict

from genie_datastores.google.google_consts import SERVICE_ACCOUNT_SECRETS_PATH, GOOGLE_SERVICE_ACCOUNT_CREDENTIALS


def load_google_credentials() -> Dict[str, str]:
    if os.path.exists(SERVICE_ACCOUNT_SECRETS_PATH):
        with open(SERVICE_ACCOUNT_SECRETS_PATH, "r") as f:
            return json.load(f)

    elif GOOGLE_SERVICE_ACCOUNT_CREDENTIALS in os.environ.keys():
        return json.loads(os.environ[GOOGLE_SERVICE_ACCOUNT_CREDENTIALS])

    else:
        raise ValueError('Missing Google service account credentials')
