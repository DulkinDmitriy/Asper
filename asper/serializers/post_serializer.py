import json

from asper.serializers.like_serializer import PostLikeEncoder
from asper.serializers.comment_serializer import CommentEncoder
from asper.domains.like import PostLike
from asper.domains.comment import Comment

class PostEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        try:
            to_serialize = {
                '_id': str(o.oid),
                'title': o.title,
                'content': o.content,
                'created_datetime': str(o.created_datetime),
                'comments_count': o.comments_count,
                'likes_count': o.likes_count
            }

            if o.likes:
                to_serialize['likes'] = [
                    json.loads(json.dumps(PostLike.from_dict(like), cls=PostLikeEncoder)) for like in o.likes
                ]

            if o.comments:
                to_serialize['comments'] = [
                    json.loads(json.dumps(Comment.from_dict(comment), cls=CommentEncoder)) for comment in o.comments
                ]

            return to_serialize
        except AttributeError:
            return super().default(o)
