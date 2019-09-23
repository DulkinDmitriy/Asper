import pytest
from asper.use_cases import request_objects as ro


def test_build_post_list_request_object():
    r = ro.PostListRequest(value={
        'with_likes': 0,
        'with_comments': 1,
        'count': 0
    })

    assert bool(r) is True
    assert r.value == {
        'with_likes': 0,
        'with_comments': 1,
        'count': 0
    }


def test_build_post_list_request_object_from_dict():
    r = ro.PostListRequest.from_dict({
        'value': {
            'with_likes': 0,
            'with_comments': 1,
            'count': 0
        }
    })

    assert bool(r) is True
    assert r.value == {
        'with_likes': 0,
        'with_comments': 1,
        'count': 0
    }


def test_post_list_request_raise_error_when_likes_miss():
    r = ro.PostListRequest(value={
        'w_l': 0,
        'with_comments': 1,
        'count': 0
    })

    with pytest.raises(KeyError):
        r.validate()


def test_post_list_request_raise_error_when_comments_miss():
    r = ro.PostListRequest(value={
        'with_likes': 0,
        'ws': 1,
        'count': 0
    })

    with pytest.raises(KeyError):
        r.validate()


def test_post_list_request_raise_error_when_count_missed():
    r = ro.PostListRequest(value={
        'with_likes': 0,
        'with_comments': 1,
        'ct': 0
    })

    with pytest.raises(KeyError):
        r.validate()


def test_post_list_request_raise_error_when_with_likes_wrong_value():
    r_int = ro.PostListRequest(value={
        'with_likes': 7,
        'with_comments': 1,
        'count': 0
    })

    r_wrong_type = ro.PostListRequest(value={
        'with_likes': "XYZ",
        'with_comments': 1,
        'count': 0
    })

    with pytest.raises(ValueError):
        r_int.validate()

    with pytest.raises(TypeError):
        r_wrong_type.validate()


def test_post_list_request_raise_error_when_key_comments_wrong_value():
    r = ro.PostListRequest(value={
        'with_likes': 0,
        'with_comments': 7,
        'count': 0
    })

    r_wrong_type = ro.PostListRequest(value={
        'with_likes': 1,
        'with_comments': "XYZ",
        'count': 0
    })

    with pytest.raises(ValueError):
        r.validate()

    with pytest.raises(TypeError):
        r_wrong_type.validate()


def test_post_list_request_raise_error_when_key_count_wrong_value():
    r = ro.PostListRequest(value={
        'with_likes': 0,
        'with_comments': 1,
        'count': -2
    })

    r_wrong_type = ro.PostListRequest(value={
        'with_likes': 1,
        'with_comments': 1,
        'count': "XYZ"
    })

    with pytest.raises(ValueError):
        r.validate()

    with pytest.raises(TypeError):
        r_wrong_type.validate()


def test_build_post_list_request_object_raise_on_empty_value():
    r = ro.PostListRequest(value={})

    with pytest.raises(KeyError):
        r.validate()
