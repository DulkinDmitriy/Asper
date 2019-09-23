class PostLike:
    def __init__(self, oid, owner, post_id):
        self.oid = oid
        self.owner = owner
        self.post_id = post_id

    @classmethod
    def from_dict(cls, adict):
        like = cls(
            oid=adict['_id'],
            owner=adict['owner'],
            post_id=adict['post_id']
        )

        return like

class CommentLike:
    def __init__(self, oid, owner, comment_id):
        self.oid = oid
        self.owner = owner
        self.comment_id = comment_id

    @classmethod
    def from_dict(cls, adict):
        like = cls(
            oid=adict['_id'],
            owner=adict['owner'],
            comment_id=adict['comment_id']
        )

        return like
