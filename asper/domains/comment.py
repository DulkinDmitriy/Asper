class Comment:
    def __init__(self, oid, owner, content, edited, created_datetime, likes_count, post_id):
        self.oid = oid
        self.owner = owner
        self.content = content
        self.edited = edited
        self.created_datetime = created_datetime
        self.likes_count = likes_count
        self.post_id = post_id
        self.likes = []

    @classmethod
    def from_dict(cls, adict):
        comment = cls(
            oid=adict['_id'],
            owner=adict['owner'],
            content=adict['content'],
            edited=adict['edited'],
            created_datetime=adict['created_datetime'],
            likes_count=adict['likes_count'],
            post_id=adict['post_id']
        )

        return comment
