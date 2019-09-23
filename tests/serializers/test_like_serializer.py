import json

from bson.objectid import ObjectId

from asper.domains.like import PostLike
from asper.serializers.like_serializer import PostLikeEncoder

def test_like_at_post_serializer_loads():
    like = PostLike.from_dict({
        '_id': ObjectId("5d83c1c6d06aa71b04d0ed5c"),
        'owner': 'Gleb',
        'post_id': ObjectId("5d83c1c6d06aa71b04d0ed5c")
    })

    expected_json = """
        {
            "_id": "5d83c1c6d06aa71b04d0ed5c",
            "owner": "Gleb",
            "post_id": "5d83c1c6d06aa71b04d0ed5c"
        }
    """

    assert json.loads(json.dumps(like, cls=PostLikeEncoder)) == json.loads(expected_json)


def test_like_at_post_serializer_dumps():
    like = PostLike.from_dict({
        '_id': ObjectId("5d83c1c6d06aa71b04d0ed5c"),
        'owner': "Gleb",
        'post_id': ObjectId("5d83c1c6d06aa71b04d0ed5c")
    })

    expected_json = {
        "_id": "5d83c1c6d06aa71b04d0ed5c",
        "owner": "Gleb",
        "post_id": "5d83c1c6d06aa71b04d0ed5c"
    }

    assert json.dumps(like, cls=PostLikeEncoder) == json.dumps(expected_json)
