import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()

mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
mongo_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")
mongo_host = os.getenv("DB_HOST", "localhost")
mongo_port = os.getenv("MONGO_PORT", "27017")

# Construct the MongoDB connection string
connection_string = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/"
client = MongoClient(connection_string)
db = client.cats_db
collection = db.cats


def create_cat(name, age, features):
    """
    Creates a new document in the collection.
    :param name: Name of the cat (str)
    :param age: Age of the cat (int)
    :param features: List of features of the cat (list of strings)
    """
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Cat inserted with ID: {result.inserted_id}")
    except PyMongoError as e:
        print(f"Error inserting cat: {e}")


def read_all_cats():
    """
    Reads all documents from the collection.
    """
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except PyMongoError as e:
        print(f"Error reading all cats: {e}")


def read_cat_by_name(name):
    """
    Reads a single document by cat's name.
    :param name: Name of the cat to search for.
    """
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat found with the name '{name}'")
    except PyMongoError as e:
        print(f"Error reading cat by name: {e}")


def update_cat_age(name, new_age):
    """
    Updates the age of the cat with the given name.
    :param name: Name of the cat to update.
    :param new_age: New age of the cat (int).
    """
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Cat '{name}' updated successfully.")
        else:
            print(f"No cat found with name '{name}'.")
    except PyMongoError as e:
        print(f"Error updating cat age: {e}")


def add_feature_to_cat(name, feature):
    """
    Adds a new feature to the cat's features list.
    :param name: Name of the cat to update.
    :param feature: New feature to add (str).
    """
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.matched_count > 0:
            print(f"Feature '{feature}' added to cat '{name}'.")
        else:
            print(f"No cat found with name '{name}'.")
    except PyMongoError as e:
        print(f"Error adding feature: {e}")


def delete_cat_by_name(name):
    """
    Deletes a document from the collection by name.
    :param name: Name of the cat to delete.
    """
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Cat '{name}' deleted successfully.")
        else:
            print(f"No cat found with name '{name}'.")
    except PyMongoError as e:
        print(f"Error deleting cat: {e}")


def delete_all_cats():
    """
    Deletes all documents in the collection.
    """
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats from the collection.")
    except PyMongoError as e:
        print(f"Error deleting all cats: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Execute predefined tasks")
    print("2. Perform your own operation")

    try:
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            create_cat("lucky", 3, ["ходить в капці", "дає себе гладити", "рудий"])
            create_cat("margo", 5, ["любить рибу", "грає з іграшками", "білий"])

            print("\nAll Cats:")
            read_all_cats()

            print("\nFind Cat by Name:")
            read_cat_by_name("barsik")

            print("\nUpdate Cat's Age:")
            update_cat_age("margo", 7)

            print("\nAdd Feature to Cat:")
            add_feature_to_cat("lucky", "улюблений диван")

            print("\nDelete Cat by Name:")
            delete_cat_by_name("murzik")

            print("\nDelete All Cats:")
            delete_all_cats()

        elif choice == "2":
            while True:
                print("\nCRUD Operations Menu:")
                print("1. Create a cat")
                print("2. Read all cats")
                print("3. Read a cat by name")
                print("4. Update cat's age")
                print("5. Add feature to a cat")
                print("6. Delete a cat by name")
                print("7. Delete all cats")
                print("8. Exit")

                try:
                    operation = input("Choose an operation (1-8): ")

                    if operation == "1":
                        name = input("Enter cat's name: ")
                        age = int(input("Enter cat's age: "))
                        features = input("Enter cat's features (comma-separated): ").split(",")
                        create_cat(name, age, features)
                    elif operation == "2":
                        read_all_cats()
                    elif operation == "3":
                        name = input("Enter the name of the cat to read: ")
                        read_cat_by_name(name)
                    elif operation == "4":
                        name = input("Enter the name of the cat to update: ")
                        new_age = int(input("Enter the new age: "))
                        update_cat_age(name, new_age)
                    elif operation == "5":
                        name = input("Enter the name of the cat to update: ")
                        feature = input("Enter a new feature: ")
                        add_feature_to_cat(name, feature)
                    elif operation == "6":
                        name = input("Enter the name of the cat to delete: ")
                        delete_cat_by_name(name)
                    elif operation == "7":
                        delete_all_cats()
                    elif operation == "8":
                        print("Exiting CRUD Operations.")
                        break
                    else:
                        print("Invalid operation. Please choose a valid option.")
                except ValueError:
                    print("Invalid input. Please enter the correct data type.")
                except Exception as e:
                    print(f"An error occurred: {e}")

    except KeyboardInterrupt:
        print("\nOperation interrupted by the user. Exiting program.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
