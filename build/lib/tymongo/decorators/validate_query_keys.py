from bson import ObjectId
from functools import wraps

def validate_query_keys(func):
    @wraps(func)
    def wrapper(cls, query = {}):
        if not isinstance(query, dict):
            raise TypeError("query must be a dict")

        for key in query.keys():
            if key not in cls.model_fields.keys():
                raise KeyError(f"key '{key}' is not in model fields, make sure to use the fields defined in the model")

        if "id" in query:
            query["_id"] = ObjectId(str(query.pop("id")))

        return func(cls, query)

    return wrapper