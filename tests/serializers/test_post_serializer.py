from datetime import datetime
import pytest
import json

from asper.serializers import post_serializer as srs
from asper.domains.post import Post


def test_serialize_domain_post():
    date = datetime.now()
    post = Post(
        oid='1q2w3e4r5t6y7u8i9o',
        title='Init title',
        content='Init content',
        created_datetime=date,
        comments_count=17,
        likes_count=138
    )

    expected_json = {
        "_id": "1q2w3e4r5t6y7u8i9o",
        "title": "Init title",
        "content": "Init content",
        "created_datetime": str(date),
        "comments_count": 17,
        "likes_count": 138
    }

    assert json.loads(json.dumps(post, cls=srs.PostEncoder)) == expected_json


def test_serialize_domain_post_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.now(), cls=srs.PostEncoder)
