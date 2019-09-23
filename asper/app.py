from flask import Flask, request
import pymongo

from asper.settings import DevelopmentConfig
from asper.use_cases import request_objects as req
from asper.use_cases import post_use_cases as p_uc
from asper.use_cases import like_use_cases as l_uc
from asper.use_cases import comment_use_cases as c_uc


def create_app(test_config=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(test_config)

    db = pymongo.MongoClient().get_database('asper')

    @app.route('/api/posts', methods=['GET'])
    def all_posts():
        w_likes = request.args.get('with_likes')
        w_comments = request.args.get('with_comments')
        count = request.args.get('count')
        post_request = req.PostListRequest.from_dict(
            {
                "value": {
                    'with_likes': request.args.get('with_likes', default=0, type=int),
                    'with_comments': request.args.get('with_comments', default=0, type=int),
                    'count': request.args.get('count', default=0, type=int)
                }
            }
        )

        response = p_uc.PostListUseCase(db).execute(post_request)

        return response.value

    @app.route('/api/post', methods=['GET'])
    def get_post():
        oid = request.args.get('oid')

        post_request = req.PostSingleRequest.from_dict({
            'oid': request.args.get('oid', default="", type=str),
            'value': {
                'with_likes': request.args.get('with_likes', default=0, type=int),
                'with_comments': request.args.get('with_comments', default=0, type=int)
            }
        })

        response = p_uc.PostSingleUseCase(db).execute(post_request)

        return response.value

    @app.route('/api/post', methods=['POST'])
    def add_post():
        post_request = req.PostAddRequest.from_dict(
            request.get_json(force=True))
        response = p_uc.PostAddUseCase(db).execute(post_request)

        return response.value

    @app.route('/api/post', methods=['PUT'])
    def update_post():
        post_request = req.PostUpdateRequest.from_dict(
            request.get_json(force=True))
        response = p_uc.PostUpdateUseCase(db).execute(post_request)

        return response.value

    @app.route('/api/post', methods=['DELETE'])
    def delete_post():
        post_request = req.TargetBaseRequest(
            request.args.get('oid', default="", type=str))
        response = p_uc.PostDeleteUseCase(db).execute(post_request)

        return response.value

    @app.route('/api/post/comment', methods=['POST'])
    def add_comment_to_post():
        comment_request = req.CommentCreateRequest.from_dict(
            request.get_json(force=True))
        response = c_uc.CommentCreateUseCase(db).execute(comment_request)

        return response.value

    @app.route('/api/comment', methods=['PUT'])
    def update_comment():
        comment_request = req.CommentUpdateRequest.from_dict(
            request.get_json(force=True))
        response = c_uc.CommentUpdateUseCase(db).execute(comment_request)

        return response.value

    @app.route('/api/comment', methods=['DELETE'])
    def delete_comment():
        comment_request = req.TargetBaseRequest(
            request.args.get('oid', default="", type=str))
        response = c_uc.CommentDeleteUseCase(db).execute(comment_request)

        return response.value

    @app.route('/api/comment/like', methods=['POST'])
    def add_comment_like():
        like_request = req.LikeToCommentRequest.from_dict(
            request.get_json(force=True))
        response = l_uc.LikeToCommentUseCase(db).execute(like_request)

        return response.value

    @app.route('/api/comment/like', methods=['DELETE'])
    def delete_comment_like():
        like_request = req.TargetBaseRequest(
            request.args.get('oid', default="", type=str))
        response = l_uc.LikeFromCommentUseCase(db).execute(like_request)

        return response.value

    @app.route('/api/post/like', methods=['POST'])
    def add_post_like():
        like_request = req.LikeToPostRequest.from_dict(
            request.get_json(force=True))
        response = l_uc.LikeToPostUseCase(db).execute(like_request)

        return response.value

    @app.route('/api/post/like', methods=['DELETE'])
    def delete_post_like():
        like_request = req.TargetBaseRequest(
            request.args.get('oid', default="", type=str))
        response = l_uc.LikeFromPostUseCase(db).execute(like_request)

        return response.value

    return app
