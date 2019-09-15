import os
import json
from flaskr.post import Post, PostWithLikes, PostWithComments
from flaskr.comment import Comment
from flaskr.pyson import convert_to_json
from pymongo import *
from flask import *

from bson.json_util import *
from bson.objectid import ObjectId


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    mongo_client = MongoClient()
    database = mongo_client.get_database('asper')
    posts = database.get_collection('posts')
    comments = database.get_collection('comments')
    likes = database.get_collection('likes')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/api/getAllPosts', methods=['GET'])
    def get_all_posts():
        with_likes = request.args.get("with_likes")
        with_comments = request.args.get("with_comments")
        str_counts = request.args.get("counts")

        counts = int(str_counts) if str_counts != None else 0

        response = []

        for post in posts.find().limit(counts):
            res = Post(posts, post)
            oid = res.get_id()
            res = PostWithLikes(res, likes) if with_likes else res
            res = PostWithComments(res, comments) if with_comments else res

            res.load(oid)

            response.append(res.read())

        return jsonify({"response": response})

    @app.route('/api/getPost', methods=['GET'])
    def get_post():
        oid = request.args.get("id")
        with_likes = request.args.get("with_likes")
        with_comments = request.args.get("with_comments")

        p = Post(posts)
        p = PostWithLikes(p, likes) if with_likes else p
        p = PostWithComments(p, comments) if with_comments else p

        p.load(oid)

        return jsonify(p.read())

    @app.route('/api/createPost', methods=['POST'])
    def create_post():
        json = request.get_json(True)

        p = Post(posts, json)
        p.create()

        return jsonify(p.read())

    @app.route('/api/updatePost', methods=['PUT'])
    def update_post():
        json = request.get_json(True)
        oid = json["_id"]
        p = Post(posts, json)

        result = p.update()

        if result.modified_count == 0:
            return jsonify({
                "error": "Item not found",
                "details": "Collection has no contain item with this id",
                "_id": oid})

        return jsonify(p.read())

    @app.route('/api/deletePost', methods=['DELETE'])
    def delete_post():
        oid = request.args.get("id")
        p = Post(posts, {"_id": oid})

        result = p.delete()

        if result.deleted_count == 0:
            return jsonify({
                "error": "Item not found",
                "details": "Collection has no contain item with this id",
                "_id": oid})

        return jsonify({"message": "Item was deleted", "_id": oid})

    @app.route('/api/createComment', methods = ['POST'])
    def create_comment():
        json = request.get_json(True)
        c = Comment(comments, json)
        c.create(posts)

        return jsonify(c.read())

    @app.route('/api/updateComment', methods = ['PUT'])
    def update_comment():
        json = request.get_json(True)
        oid = json["_id"]
        c = Comment(comments, json)

        result = c.update()

        if result.modified_count == 0:
            return jsonify({
                "error": "Item not found",
                "details": "Collection has no contain item with this id",
                "_id": oid})
        
        return jsonify(c.read())

    @app.route('/api/deleteComment', methods = ['DELETE'])
    def delete_comment():
        oid = request.args.get("id")
        c = Comment(comments, {"_id": oid})
        result = c.delete()

        if result.deleted_count == 0:
            return jsonify({
                "error": "Item not found",
                "details": "Collection has no contain item with this id",
                "_id": oid})

        return jsonify({"message": "Item was deleted", "_id": oid})

    return app
