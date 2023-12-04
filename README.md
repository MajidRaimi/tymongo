# TyMongo 🐍📦

TyMongo is a Python package designed to simplify your interaction with MongoDB by leveraging the power of [pymongo](https://pymongo.readthedocs.io/) for database connectivity and [pydantic](https://pydantic-docs.helpmanual.io/) for efficient modeling and type creation through classes.

## Features
- Seamless connection to MongoDB using pymongo. 🌐
- Data modeling and type creation with pydantic classes. 🧱
- Automatic data validation and type conversion. ✅
- Automatic data serialization and deserialization. 📦

## Installation 📥
To install TyMongo, simply use pip: (for now, only from github)
```bash
pip install tymongo
```

## Setup 🛠️
All you really need to do is to create `.env` file in your project root directory and add the following variables:
```bash
DATABASE_URL=your_database_url
DATABASE_NAME=your_database_name
```
And now you're ready to go! 🚀

## Usage 📝
### Creating a Model
To create a model, simply inherit from `TyMongoModel` and define your fields:
```python
class User(TyMongoModel):
    name: str
    age: int

    class Config:
        collection = "users"
```
- Will work 100% like `BaseModel` from pydantic, but with some extra features. 🤩
- Make sure you define inner class `Config` and set `collection` to the name of the collection you want to use in your database. 📁
- You don't have to define `_id` field, it will be automatically created for you. 🆔

### Creating a User
```python
user = User(name="Majid", age=21)
# or
user_dict = {"name": "Majid", "age": 21}
user = User(**user_dict)
```
- You can pass any value to any field, it will be automatically converted to the type you defined. 🔄
- You can also pass a dictionary to the model, it will be automatically converted to the model. 🔄

### Saving a User
```python
user.save()
```
Now you have a new user in your database! 🎉

### Editing a User
```python
user.age = 22
user.save()
```
Now your user's age is 22 in your database! 🎉

### Deleting a User
```python
user.delete()
```
Now your user is deleted from your database! 🎉

## Extra Features 🤩
### Querying & Fields Validation
```python
query = {"age": 22}
users = User.find(query)
```
Just like pymongo, you can pass a query to `find` method and it will return a list of all the users that match the query as a list of models, just make sure the dictionary keys match the model fields. 🔑

```python
query = {
    'x': 'some value',
    'age': 21,
}
users = User.find(query)
```
This will raise an error because `x` is not a field in the model. ❌

### Get a Single Document by ID
```python
user = User.get("xxxxxxxxxxxxxxxxxxxxxxxx")
```

### Get a Single Document by Query
```python
q = {
    'name' : 'Majid'
}
user = User.find_one(q)
```

### What if I want to use pymongo directly? 🤔
You can access the collection object directly from the model:
```python
collection = User.__collection__()
users = collection.find({"age": 22})
```

## License
TyMongo is licensed under the terms of the [MIT License](LICENSE).


## Contributing 🤝
- [Majid Saleh Al-Raimi](https://www.majidraimi.com/)

## Contact 📧
- [Email](mailto:majidsraimi@gmail.com)

## Acknowledgements 🙏
- [pymongo](https://pymongo.readthedocs.io/)
- [pydantic](https://pydantic-docs.helpmanual.io/)


Thank you for using TyMongo! 🙌 happy coding! 🚀
