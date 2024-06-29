from motor.motor_asyncio import AsyncIOMotorClient


class MongoClient:
    def __init__(self, motor_client: AsyncIOMotorClient):
        self._motor_client = motor_client

    def get_collection(self, db_name: str, collection_name: str):  # TODO: typing
        db = self._motor_client[db_name]
        return db[collection_name]
