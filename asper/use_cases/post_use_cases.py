import json

from datetime import datetime
from bson.objectid import ObjectId

from asper.shared import response_object as res
from asper.shared import use_case as uc
from asper.serializers.post_serializer import PostEncoder
from asper.domains.post import Post


class PostListUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        posts = self.repo['posts'].find().limit(request.value['count'])

        result = []

        for post in posts:
            entity = Post.from_dict(post)

            if request.value['with_likes']:
                entity.likes = self.repo['likes'].find({"post_id": entity.oid})

            if request.value['with_comments']:
                entity.comments = self.repo['comments'].find(
                    {"post_id": entity.oid})

            result.append(entity)

        return res.ResponseSuccess(json.dumps(result, cls=PostEncoder))


class PostSingleUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['posts'].find_one({"_id": ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Object wasn`t found in database.")

        post = Post.from_dict(entity)

        if request.value['with_likes']:
            post.likes = self.repo['likes'].find({"post_id": post.oid})

        if request.value['with_comments']:
            post.comments = self.repo['comments'].find({"post_id": post.oid})

        return res.ResponseSuccess(json.dumps(post, cls=PostEncoder))


class PostAddUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        request.value['created_datetime'] = datetime.now()
        request.value['likes_count'] = 0
        request.value['comments_count'] = 0

        self.repo['posts'].insert_one(request.value)

        return res.ResponseSuccess(json.dumps(Post.from_dict(request.value), cls=PostEncoder))


class PostUpdateUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['posts'].find_one({"_id": ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Object wasn`t found in database.")

        post = Post.from_dict(entity)
        post.title = request.value['title']
        post.content = request.value['content']

        self.repo['posts'].update_one({"_id": post.oid}, {
            "$set": {'title': post.title, 'content': post.content}
        })

        return res.ResponseSuccess(json.dumps(post, cls=PostEncoder))


class PostDeleteUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['posts'].find_one({"_id": ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Object wasn`t found in database.")

        self.repo['posts'].delete_one({"_id": ObjectId(request.oid)})

        return res.ResponseSuccess({
            'message': 'Object was deleted',
            'object_id': request.oid
        })
