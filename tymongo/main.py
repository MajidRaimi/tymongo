from pydantic import BaseModel, Field
from bson import ObjectId

# Import the MongoDB database handler from the package package
from .handler import database
from .decorators import validate_query_keys

# Define a base class for PyMongo models using Pydantic
class TyMongoModel(BaseModel):
    """
    A base class for PyMongo models using Pydantic.
    """
    # Map the 'id' field to MongoDB's '_id', and set a default ObjectId
    id: ObjectId = Field(..., alias="_id", default_factory=lambda: ObjectId())

    class Config:
        arbitrary_types_allowed = True
        collection = None  # Define the MongoDB collection name starting with None

    # Access the MongoDB collection associated with the model
    @classmethod
    def __collection__(cls):
        if cls.Config.collection is None:
            raise Exception("collection is not defined")
        return database[cls.Config.collection]

    # Save the current instance to the database
    def save(self):
        self.__collection__().update_one(
            {"_id": self.id},
            {"$set": self.model_dump(by_alias=True)},
            upsert=True
        )

    # Delete the current instance from the database
    def delete(self):
        self.__collection__().delete_one({"_id": self.id})

    # Retrieve an instance by its ObjectId from the database
    @classmethod
    def get(cls, id: str):
        return cls(**cls.__collection__().find_one({"_id": ObjectId(id)}))

    # Find instances based on a query in the database
    @classmethod
    @validate_query_keys
    def find(cls, query: dict = {}):
        return [cls(**data) for data in cls.__collection__().find(query)]

    # Find a single instance based on a query in the database
    @classmethod
    @validate_query_keys
    def find_one(cls, query: dict = {}):
        def find_one(cls, query: dict = {}):
        cursor = cls.__collection__().find(query).limit(1)
        document = next(cursor, None)
            if document is None:
            return None
        return cls(**document)


    # Count instances based on a query in the database
    @classmethod
    @validate_query_keys
    def count(cls, query: dict = {}):
        return cls.__collection__().count_documents(query)
