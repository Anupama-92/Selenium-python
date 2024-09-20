from pymongo import MongoClient

# Step 1: Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Step 2: Access the database and collection (creates if not exists)
db = client['my_database']
collection = db['my_collection']

# Insert Documents
# Inserting a single document
document = {"name": "Anu1", "age": 30, "city": "New York"}
collection.insert_one(document)

# Inserting multiple documents
documents = [
    {"name": "Saranu1", "age": 25, "city": "Los Angeles"},
    {"name": "Naga2", "age": 35, "city": "Chicago"}
]
collection.insert_many(documents)

person = collection.find_one({"name": "Anu1"})
print(person)

# Query to find multiple documents
people = collection.find({"age": {"$gt": 30}})
for person in people:
    print(person)
