import json

from bson.objectid import ObjectId
from asper.domains.like import PostLike, CommentLike
from asper.domains.post import Post
from asper.domains.comment import Comment
from asper.serializers.post_serializer import PostEncoder
from asper.serializers.like_serializer import PostLikeEncoder, CommentLikeEncoder
from asper.serializers.comment_serializer import CommentEncoder
from asper.shared import response_object as res
from asper.shared import use_case as uc


class LikeToPostUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['posts'].find_one({'_id': ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Item wasn`t found in database")

        post = Post.from_dict(entity)

        likes = self.repo['likes'].find({'post_id': ObjectId(post.oid)})

        for item in likes:
            like = PostLike.from_dict(item)
            if like.owner == request.value['owner']:
                return res.ResponseFailure.build_parameters_error(f"Like with owner:{like.owner} already exist.")

        request.value['post_id'] = ObjectId(request.oid)

        self.repo['likes'].insert_one(request.value)
        self.repo['posts'].update_one({'_id': ObjectId(post.oid)}, {
                                      "$inc": {"likes_count": 1}})

        return res.ResponseSuccess({
            'message': "Like was placed",
            'like': json.loads(json.dumps(PostLike.from_dict(request.value), cls=PostLikeEncoder)),
            'post': json.loads(json.dumps(post, cls=PostEncoder))
        })


class LikeFromPostUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['likes'].find_one({'_id': ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Item wasn`t found in database")

        like = PostLike.from_dict(entity)

        self.repo['likes'].delete_one({'_id': like.oid})
        self.repo['posts'].update_one({'_id': ObjectId(like.post_id)}, {
                                      "$inc": {"likes_count": -1}})

        return res.ResponseSuccess({
            'message': "Like was deleted",
            'like_id': str(like.oid),
            'post': str(like.post_id)
        })


class LikeToCommentUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['comments'].find_one({'_id': ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Item wasn`t found in database")

        comment = Comment.from_dict(entity)

        likes = self.repo['likes'].find({'comment_id': ObjectId(comment.oid)})

        for item in likes:
            like = CommentLike.from_dict(item)
            if like.owner == request.value['owner']:
                return res.ResponseFailure.build_parameters_error(f"Like with owner:{like.owner} already exist.")

        request.value['comment_id'] = ObjectId(request.oid)

        self.repo['likes'].insert_one(request.value)
        self.repo['comments'].update_one({'_id': ObjectId(comment.oid)}, {
                                         "$inc": {"likes_count": 1}})

        return res.ResponseSuccess({
            'message': "Like was placed",
            'like': json.loads(json.dumps(CommentLike.from_dict(request.value), cls=CommentLikeEncoder)),
            'comment': json.loads(json.dumps(comment, cls=CommentEncoder))
        })


class LikeFromCommentUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['likes'].find_one({'_id': ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Item wasn`t found in database")

        like = CommentLike.from_dict(entity)

        self.repo['likes'].delete_one({'_id': like.oid})
        self.repo['comments'].update_one({'_id': ObjectId(like.comment_id)}, {
                                         "$inc": {"likes_count": -1}})

        return res.ResponseSuccess({
            'message': "Like was deleted",
            'like_id': str(like.oid),
            'comment': str(like.comment_id)
        })
