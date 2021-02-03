from typing import Any

from fastapi import APIRouter, Depends

from app import schemas
from app.api import deps

router = APIRouter()


@router.post("/test_post", response_model=schemas.Msg, status_code=201)
def test_post(
    msg: schemas.Msg,
    current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Mirror response.
    """
    return {"msg": f"Tasklist POST - {msg.msg}"}


@router.get("/test_get", response_model=schemas.Msg, status_code=201)
def test_get(
    current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Greeting.
    """
    return {"msg": "Tasklist GET"}
