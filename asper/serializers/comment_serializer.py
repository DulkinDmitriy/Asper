import json
from asper.domains.like import CommentLike
from asper.serializers.like_serializer import CommentLikeEncoder

class CommentEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        try:
            to_serialize = {
                '_id': str(o.oid),
                'owner': o.owner,
                'content': o.content,
                'edited': o.edited,
                'created_datetime': str(o.created_datetime),
                'likes_count': o.likes_count,
                'post_id': str(o.post_id)
            }

            if o.likes:
                to_serialize['likes'] = [
                    json.loads(json.dumps(CommentLike.from_dict(like), cls=CommentLikeEncoder)) for like in o.likes
                ]

            return to_serialize
        except AttributeError:
            return super().default(o)

