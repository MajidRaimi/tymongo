import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from the .env file
try:
    if load_dotenv() == False:
        raise Exception("Failed to load .env file")

    # Retrieve MongoDB connection details from environment variables
    url, name = os.getenv('DATABASE_URL'), os.getenv('DATABASE_NAME')

    # Ensure that the DATABASE_URL and DATABASE_NAME are defined
    if url is None:
        raise Exception("DATABASE_URL is not defined")
    if name is None:
        raise Exception("DATABASE_NAME is not defined")

    # Connect to the MongoDB database using MongoClient
    client = MongoClient(url)
    database = client[name]

    # Check if the specified database exists, and create it if not
    if name not in client.list_database_names():
        print(f"Created a new database named {name} ✅")

except Exception as e:
    # Handle exceptions and print an error message
    print(e)
    print("Database connection failed ❌")
    exit(1)
