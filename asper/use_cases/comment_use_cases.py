import json

from bson.objectid import ObjectId
from datetime import datetime

from asper.shared import use_case as uc
from asper.shared import response_object as res

from asper.serializers.comment_serializer import CommentEncoder
from asper.domains.comment import Comment


class CommentCreateUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        post_entity = self.repo['posts'].find_one(
            {'_id': ObjectId(request.oid)})

        if not post_entity:
            return res.ResponseFailure.build_parameters_error("Object was not found")

        request.value['edited'] = False
        request.value['created_datetime'] = datetime.now()
        request.value['likes_count'] = 0
        request.value['post_id'] = ObjectId(request.oid)

        self.repo['comments'].insert_one(request.value)

        return res.ResponseSuccess({
            "message": "Comment was added.",
            "comment": json.loads(json.dumps(Comment.from_dict(request.value), cls=CommentEncoder))
        })


class CommentUpdateUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['comments'].find_one({'_id': ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Object was not found")

        comment = Comment.from_dict(entity)
        comment.content = request.value['content']
        comment.edited = True

        self.repo['comments'].update_one({'_id': ObjectId(request.oid)}, {
            "$set": {
                "content": comment.content,
                "edited": comment.edited
            }
        })

        return res.ResponseSuccess({
            "message": "Comment was edited.",
            "comment": json.loads(json.dumps(comment, cls=CommentEncoder))
        })


class CommentDeleteUseCase(uc.UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request):
        entity = self.repo['comments'].find_one({'_id': ObjectId(request.oid)})

        if not entity:
            return res.ResponseFailure.build_parameters_error("Object was not found.")

        comment = Comment.from_dict(entity)

        self.repo['comments'].delete_one({'_id': ObjectId(request.oid)})
        self.repo['posts'].update_one({'_id': ObjectId(comment.post_id)}, {
                                      "$inc": {"comments_count": -1}})

        return res.ResponseSuccess({
            "message": "Comment was deleted.",
            "comment_id": request.oid,
            "post_id": str(comment.post_id)
        })
