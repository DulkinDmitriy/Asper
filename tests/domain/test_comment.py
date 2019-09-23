from bson.objectid import ObjectId
from datetime import datetime
from asper.domains.comment import Comment

def test_domain_comment_init():
    date = datetime.now()
    comment = Comment(
        oid="5d83c1c6d06aa71b04d0ed5c",
        owner="Glob",
        content="Content",
        edited=True,
        created_datetime=date,
        likes_count=132,
        post_id="5d83c1c6d06aa71b04d0ed5d"
    )

    assert comment.oid == "5d83c1c6d06aa71b04d0ed5c"
    assert comment.owner == "Glob"
    assert comment.content == "Content"
    assert comment.edited == True
    assert comment.created_datetime == date
    assert comment.likes_count == 132
    assert comment.post_id == "5d83c1c6d06aa71b04d0ed5d"
    assert comment.likes == []

def test_domain_comment_init_with_ObjectId():
    date = datetime.now()
    comment = Comment(
        oid=ObjectId("5d83c1c6d06aa71b04d0ed5c"),
        owner="Glob",
        content="Content",
        edited=True,
        created_datetime=date,
        likes_count=132,
        post_id=ObjectId("5d83c1c6d06aa71b04d0ed5d")
    )

    assert comment.oid == ObjectId("5d83c1c6d06aa71b04d0ed5c")
    assert comment.owner == "Glob"
    assert comment.content == "Content"
    assert comment.edited == True
    assert comment.created_datetime == date
    assert comment.likes_count == 132
    assert comment.post_id == ObjectId("5d83c1c6d06aa71b04d0ed5d")
    assert comment.likes == []


def test_domain_comment_from_dict():
    date = datetime.now()
    comment = Comment.from_dict({
        '_id': "5d83c1c6d06aa71b04d0ed5c",
        'owner': "Glob",
        'content': "Content",
        'edited': True,
        'created_datetime': date,
        'likes_count': 132,
        'post_id': "5d83c1c6d06aa71b04d0ed5d"
    })

    assert comment.oid == "5d83c1c6d06aa71b04d0ed5c"
    assert comment.owner == "Glob"
    assert comment.content == "Content"
    assert comment.edited == True
    assert comment.created_datetime == date
    assert comment.likes_count == 132
    assert comment.post_id == "5d83c1c6d06aa71b04d0ed5d"
    assert comment.likes == []

def test_domain_comment_from_dict_with_ObjectId():
    date = datetime.now()
    comment = Comment.from_dict({
        '_id': ObjectId("5d83c1c6d06aa71b04d0ed5c"),
        'owner': "Glob",
        'content': "Content",
        'edited': True,
        'created_datetime': date,
        'likes_count': 132,
        'post_id': ObjectId("5d83c1c6d06aa71b04d0ed5d")
    })

    assert comment.oid == ObjectId("5d83c1c6d06aa71b04d0ed5c")
    assert comment.owner == "Glob"
    assert comment.content == "Content"
    assert comment.edited == True
    assert comment.created_datetime == date
    assert comment.likes_count == 132
    assert comment.post_id == ObjectId("5d83c1c6d06aa71b04d0ed5d")
    assert comment.likes == []