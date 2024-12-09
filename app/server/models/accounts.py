from typing import Optional

from pydantic import BaseModel, Field


class AccountSchema(BaseModel):
    name: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Bourso Bank",
            }
        }


class UpdateAccountModel(BaseModel):
    name: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Hello Bank!",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}