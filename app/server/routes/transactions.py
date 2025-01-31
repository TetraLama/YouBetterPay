from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_transaction,
    delete_transaction,
    retrieve_transaction,
    retrieve_transactions,
    update_transaction,
)
from app.server.models.transactions import (
    ErrorResponseModel,
    ResponseModel,
    TransactionSchema,
    UpdateTransactionModel,
)

router = APIRouter()

@router.post("/", response_description="Transaction data added into the database")
async def add_transaction_data(transaction: TransactionSchema = Body(...)):
    transaction = jsonable_encoder(transaction)
    new_transaction = await add_transaction(transaction)
    return ResponseModel(new_transaction, "Transaction added successfully.")

@router.get("/", response_description="Transactions retrieved")
async def get_transactions():
    transactions = await retrieve_transactions()
    if transactions:
        return ResponseModel(transactions, "Transactions data retrieved successfully")
    return ResponseModel(transactions, "Empty list returned")


@router.get("/{id}", response_description="Transaction data retrieved")
async def get_transaction_data(id):
    transaction = await retrieve_transaction(id)
    if transaction:
        return ResponseModel(transaction, "Transaction data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Transaction doesn't exist.")

@router.put("/{id}")
async def update_transaction_data(id: str, req: UpdateTransactionModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_transaction = await update_transaction(id, req)
    if updated_transaction:
        return ResponseModel(
            "Transaction with ID: {} name update is successful".format(id),
            "Transaction name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the transaction data.",
    )

@router.delete("/{id}", response_description="Transaction data deleted from the database")
async def delete_transaction_data(id: str):
    deleted_transaction = await delete_transaction(id)
    if deleted_transaction:
        return ResponseModel(
            "Transaction with ID: {} removed".format(id), "Transaction deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Transaction with id {0} doesn't exist".format(id)
    )
