from typing import Annotated
from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy

from backend.core.authentication.strategy import get_database_strategy
from .access_tokens import get_access_tokens_db


def get_database_strategy_dependency(
    access_token_db: Annotated[
        "DatabaseStrategy",
        Depends(get_access_tokens_db),
    ],
) -> DatabaseStrategy:
    return get_database_strategy(access_token_db)
