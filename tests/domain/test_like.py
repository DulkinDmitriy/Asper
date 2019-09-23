from bson.objectid import ObjectId
from asper.domains.like import PostLike, CommentLike


def test_domain_like_to_post_init():
    like = PostLike("5d83c1c6d06aa71b04d0ed5c",
                    "Gleb", "5d83c1c6d06aa71b04d0ed5c")

    assert like.oid == "5d83c1c6d06aa71b04d0ed5c"
    assert like.owner == "Gleb"
    assert like.post_id == "5d83c1c6d06aa71b04d0ed5c"


def test_domain_like_to_post_init_with_ObjectId():
    like = PostLike(ObjectId("5d83c1c6d06aa71b04d0ed5c"),
                    "Gleb", ObjectId("5d83c1c6d06aa71b04d0ed5c"))

    assert like.oid == ObjectId("5d83c1c6d06aa71b04d0ed5c")
    assert like.owner == "Gleb"
    assert like.post_id == ObjectId("5d83c1c6d06aa71b04d0ed5c")


def test_domain_like_to_post_from_dict():
    like = PostLike.from_dict({
        '_id': "5d83c1c6d06aa71b04d0ed5c",
        'owner': 'Gleb',
        'post_id': "5d83c1c6d06aa71b04d0ed5c"
    })

    assert like.oid == "5d83c1c6d06aa71b04d0ed5c"
    assert like.owner == "Gleb"
    assert like.post_id == "5d83c1c6d06aa71b04d0ed5c"


def test_domain_like_to_post_from_dict_with_ObjectId():
    like = PostLike.from_dict({
        '_id': ObjectId("5d83c1c6d06aa71b04d0ed5c"),
        'owner': 'Gleb',
        'post_id': ObjectId("5d83c1c6d06aa71b04d0ed5c")
    })

    assert like.oid == ObjectId("5d83c1c6d06aa71b04d0ed5c")
    assert like.owner == "Gleb"
    assert like.post_id == ObjectId("5d83c1c6d06aa71b04d0ed5c")


def test_domain_like_to_comment_init():
    like = CommentLike("5d83c1c6d06aa71b04d0ed5c",
                    "Gleb", "5d83c1c6d06aa71b04d0ed5c")

    assert like.oid == "5d83c1c6d06aa71b04d0ed5c"
    assert like.owner == "Gleb"
    assert like.comment_id == "5d83c1c6d06aa71b04d0ed5c"


def test_domain_like_to_comment_init_with_ObjectId():
    like = CommentLike(ObjectId("5d83c1c6d06aa71b04d0ed5c"),
                    "Gleb", ObjectId("5d83c1c6d06aa71b04d0ed5c"))

    assert like.oid == ObjectId("5d83c1c6d06aa71b04d0ed5c")
    assert like.owner == "Gleb"
    assert like.comment_id == ObjectId("5d83c1c6d06aa71b04d0ed5c")


def test_domain_like_to_comment_from_dict():
    like = CommentLike.from_dict({
        '_id': "5d83c1c6d06aa71b04d0ed5c",
        'owner': 'Gleb',
        'comment_id': "5d83c1c6d06aa71b04d0ed5c"
    })

    assert like.oid == "5d83c1c6d06aa71b04d0ed5c"
    assert like.owner == "Gleb"
    assert like.comment_id == "5d83c1c6d06aa71b04d0ed5c"


def test_domain_like_to_comment_from_dict_with_ObjectId():
    like = CommentLike.from_dict({
        '_id': ObjectId("5d83c1c6d06aa71b04d0ed5c"),
        'owner': 'Gleb',
        'comment_id': ObjectId("5d83c1c6d06aa71b04d0ed5c")
    })

    assert like.oid == ObjectId("5d83c1c6d06aa71b04d0ed5c")
    assert like.owner == "Gleb"
    assert like.comment_id == ObjectId("5d83c1c6d06aa71b04d0ed5c")
