from bson.objectid import ObjectId

from asper.domains.post import Post
from datetime import datetime


def test_post_model_init():
    date = datetime.now()
    post = Post(
        oid="1q2w3e4r5t6y7u8421",
        title="Init title",
        content="Init content",
        created_datetime=date,
        comments_count=13,
        likes_count=138
    )

    assert post.oid == "1q2w3e4r5t6y7u8421"
    assert post.title == "Init title"
    assert post.content == "Init content"
    assert post.created_datetime == date
    assert post.comments_count == 13
    assert post.likes_count == 138
    assert post.likes == []
    assert post.comments == []


def test_post_model_from_dict():
    date = datetime.now()
    post = Post.from_dict(
        {
            '_id': "1q2w3e4r5t6y7u8421",
            'title': "Init title",
            'content': "Init content",
            'created_datetime': date,
            'comments_count': 13,
            'likes_count': 138
        }
    )

    assert post.oid == "1q2w3e4r5t6y7u8421"
    assert post.title == "Init title"
    assert post.content == "Init content"
    assert post.created_datetime == date
    assert post.comments_count == 13
    assert post.likes_count == 138
    assert post.likes == []
    assert post.comments == []

def test_post_model_from_dict_with_ObjectId():
    date = datetime.now()
    post = Post.from_dict(
        {
            '_id': ObjectId("5d83c1c6d06aa71b04d0ed5c"),
            'title': "Init title",
            'content': "Init content",
            'created_datetime': date,
            'comments_count': 13,
            'likes_count': 138
        }
    )

    assert post.oid == ObjectId("5d83c1c6d06aa71b04d0ed5c")
    assert post.title == "Init title"
    assert post.content == "Init content"
    assert post.created_datetime == date
    assert post.comments_count == 13
    assert post.likes_count == 138
    assert post.likes == []
    assert post.comments == []