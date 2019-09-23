import json

class PostLikeEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        try:
            to_serialize = {
                '_id': str(o.oid),
                'owner': o.owner,
                'post_id': str(o.post_id)
            }

            return to_serialize
        except AttributeError:
            return super().default(o)

class CommentLikeEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        try:
            to_serialize = {
                '_id': str(o.oid),
                'owner': o.owner,
                'comment_id': str(o.comment_id)
            }

            return to_serialize
        except AttributeError:
            return super().default(o)
