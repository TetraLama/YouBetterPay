import motor.motor_asyncio
from bson.objectid import ObjectId
from .config import Config

# DB Connection
client = motor.motor_asyncio.AsyncIOMotorClient(Config.mongo_uri)
database = client.youbetterpay
accounts_collection = database.get_collection("accounts_collection")

###
# HELPERS
###
def account_helper(account) -> dict:
    return {
        "id": str(account["_id"]),
        "name": account["name"],
    }

###
# CRUD
###
### ACCOUNTS
# Retrieve all accounts present in the database
async def retrieve_accounts():
    accounts = []
    async for account in accounts_collection.find():
        accounts.append(account_helper(account))
    return accounts


# Add a new account into to the database
async def add_account(account_data: dict) -> dict:
    account = await accounts_collection.insert_one(account_data)
    new_account = await accounts_collection.find_one({"_id": account.inserted_id})
    return account_helper(new_account)


# Retrieve a account with a matching ID
async def retrieve_account(id: str) -> dict:
    account = await accounts_collection.find_one({"_id": ObjectId(id)})
    if account:
        return account_helper(account)


# Update a account with a matching ID
async def update_account(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    account = await accounts_collection.find_one({"_id": ObjectId(id)})
    if account:
        updated_account = await accounts_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_account:
            return True
        return False


# Delete a account from the database
async def delete_account(id: str):
    account = await accounts_collection.find_one({"_id": ObjectId(id)})
    if account:
        await accounts_collection.delete_one({"_id": ObjectId(id)})
        return True