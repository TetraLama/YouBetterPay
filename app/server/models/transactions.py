from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime


class TransactionSchema(BaseModel):
    description: str = Field(...)
    target_account_id: ObjectId = Field(..., description="ID du compte cible pour cette transaction")
    source_account_id: Optional[ObjectId] = Field(None, description="ID du compte source pour cette transaction (optionnel)")
    transaction_type: str = Field(..., description="Type de la transaction: 'entrante', 'sortante', 'virement_interne'", regex="^(entrante|sortante|virement_interne)$")
    transaction_date: datetime = Field(..., description="Date de la transaction")
    is_recurrent: Optional[bool] = Field(False, description="Définit si la transaction est récurrente (optionnel)")
    recurrence_count: Optional[int] = Field(None, description="Nombre de fois que la transaction récurrente a lieu (optionnel)")
    recurrence_unit: Optional[str] = Field(None, description="Unité de récurrence: 'semaine', 'mois', 'année' (optionnel)", regex="^(semaines|mois|annees)$")
    recurrence_interval_unit: Optional[str] = Field(None, description="Unité d'intervalle entre récurrences: 'semaine', 'mois', 'année' (optionnel)", regex="^(semaines|mois|annees)$")
    recurrence_interval_value: Optional[int] = Field(None, description="Valeur de l'intervalle entre récurrences (optionnel)")


    class Config:
        schema_extra = {
            "example": {
                "description": "Achat de matériel informatique",
                "target_account_id": "64b3f1e2cfea8c7e1f3b9a10",
                "source_account_id": "64b3f1e2cfea8c7e1f3b9a11",
                "transaction_type": "sortante",
                "transaction_date": "2024-12-01T15:30:00",
                "is_recurrent": True,
                "recurrence_count": 6,
                "recurrence_unit": "mois",
                "recurrence_interval_unit": "mois",
                "recurrence_interval_value": 2,
            }
        }


class UpdateTransactionModel(BaseModel):
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "description": "Achat de matériel informatique",
                "target_account_id": "64b3f1e2cfea8c7e1f3b9a10",
                "source_account_id": "64b3f1e2cfea8c7e1f3b9a11",
                "transaction_type": "sortante",
                "transaction_date": "2024-12-01T15:30:00",
                "is_recurrent": True,
                "recurrence_count": 6,
                "recurrence_unit": "mois",
                "recurrence_interval_unit": "mois",
                "recurrence_interval_value": 2,
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