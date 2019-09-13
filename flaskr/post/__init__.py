from pymongo.collection import Collection
from bson.objectid import ObjectId
from datetime import datetime
from flaskr.pyson import convert_to_json


class Post:

    def __init__(self, collection, json={}):
        self.collection = collection
        self.json = json

    def create(self):
        required_fields = ["title", "content"]
        validate_result = self.validate(self.json, required_fields)

        if not validate_result["result"]:
            return self.bad_request("Wrong json template", details=f"Json request has no '{validate_result['field']}' property.")

        self.json["created_datetime"] = datetime.now()
        self.json["comments_count"] = 0
        self.json["likes_count"] = 0

        self.collection.insert_one(self.json)

    def update(self):
        required_fields = ["_id", "title", "content"]
        validate_result = self.validate(self.json, required_fields)

        if not validate_result["result"]:
            return self.bad_request("Wrong json template", details=f"Json request has no '{validate_result['field']}' property.")

        self.collection.update_one({"_id": ObjectId(self.json.pop("_id"))}, {"$set": self.json})

    def delete(self):
        required_fields = ["_id"]
        validate_result = self.validate(self.json, required_fields)

        if not validate_result["result"]:
            return self.bad_request("Wrong json template", details=f"Json request has no '{validate_result['field']}' property.")

        return self.collection.delete_one({"_id": ObjectId(self.json["_id"])})

    def load(self, p_id):
        oid = {"_id": ObjectId(p_id)}
        self.json = self.collection.find_one(oid)

    def read(self):
        return convert_to_json(self.json)

    def get_id(self):
        if self.json != {}:
            return self.read()["_id"]["$oid"]

    def validate(self, json, fields):
        for field in fields:
            if field not in json:
                return {"result": False, "field": field}
        return {"result": True, "field": ""}

    def bad_request(self, error, **kwargs):
        b_request = {
            "error": error
        }

        for key, value in kwargs.items():
            b_request[key] = value

        return b_request


class PostWithLikes:

    def __init__(self, post, likes_collection):
        self.post = post
        self.likes_collection = likes_collection
        self.likes = []

    def load(self, p_id):
        post_id = {"post_id": ObjectId(p_id)}
        self.likes = self.likes_collection.find(post_id)

        if self.post.read() == {}:
            self.post.load(p_id)

    def read(self):
        response = self.post.read()
        response["likes"] = convert_to_json(self.likes)

        return response


class PostWithComments:

    def __init__(self, post, comments_collection):
        self.post = post
        self.comments_collection = comments_collection
        self.comments = []

    def load(self, p_id):
        post_id = {"post_id": ObjectId(p_id)}
        self.comments = self.comments_collection.find(post_id)
        if self.post.read() == {}:
            self.post.load(p_id)

    def read(self):
        response = self.post.read()
        response["comments"] = convert_to_json(self.comments)

        return response
