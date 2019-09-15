from flaskr.pyson import *
from pymongo.collection import Collection
from bson.objectid import ObjectId
from datetime import datetime


class Comment:

    def __init__(self, collection, json={}):
        self.collection = collection
        self.json = json

    def create(self, post_collection):
        validate_result = validate_fields(
            self.json, ["author", "content", "post_id"])

        if not validate_result.result:
            return bad_request("Wrong json template.", details=f"Json request has no '{validate_result.field}' field.")

        post_id = ObjectId(self.json["post_id"])

        doc = {
            "author": self.json["author"],
            "content": self.json["content"],
            "created_datetime": datetime.now(),
            "likes_count": 0,
            "edited": False,
            "post_id": post_id
        }

        self.json = doc
        post_collection.update_one({"_id": post_id}, {"$inc": {"comments_count": 1}})
        self.collection.insert_one(doc)

    def update(self):
        validate_result = validate_fields(self.json, ["_id", "content"])

        if not validate_result.result:
            return bad_request("Wrong json template.", details=f"Json request has no '{validate_result.field}' field.")

        doc = {
            "$set": {
                "content": self.json["content"],
                "edited": True
            }
        }

        return self.collection.update_one({"_id": ObjectId(self.json["_id"])}, doc)

    def delete(self):
        validate_result = validate_fields(self.json, ["_id"])

        if not validate_result.result:
            return bad_request("Wrong json template.", details=f"Json request has no '{validate_result.field}' field.")

        return self.collection.delete_one({"_id": ObjectId(self.json["_id"])})

    def read(self):
        return convert_to_json(self.json)
