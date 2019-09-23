
class Post:

    def __init__(self, oid, title, content, created_datetime, comments_count, likes_count):
        self.oid = oid
        self.title = title
        self.content = content
        self.created_datetime = created_datetime
        self.comments_count = comments_count
        self.likes_count = likes_count
        self.likes = []
        self.comments = []

    @classmethod
    def from_dict(cls, adict):
        post = Post(
            oid=adict['_id'],
            title=adict['title'],
            content=adict['content'],
            created_datetime=adict['created_datetime'],
            comments_count=adict['comments_count'],
            likes_count=adict['likes_count']
        )

        return post
