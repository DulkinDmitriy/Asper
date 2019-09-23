import pytest

from unittest import mock

from asper.use_cases import request_objects as req
from asper.shared import response_object as res
from asper.use_cases import post_use_cases as uc


@pytest.fixture
def valid_post_list_request():
    return req.PostListRequest.from_dict({
        'value': {
            'with_likes': 1,
            'with_comments': 1,
            'count': 0
        }
    })


def test_post_list_handles_generic_error(valid_post_list_request):
    repo = mock.Mock()
    repo.side_effect = Exception('Just an error message')

    post_list_use_case = uc.PostListUseCase(repo)
    response = post_list_use_case.execute(valid_post_list_request)

    assert bool(response) is False
    assert 'error' in response.value['message']
    assert len(response.value['message']['traceback']) > 0


def test_post_list_handles_bad_request():
    repo = mock.Mock()

    post_list_use_case = uc.PostListUseCase(repo)
    request = req.PostListRequest.from_dict({'filters': 5})

    response = post_list_use_case.execute(request)

    assert bool(response) is False
    assert response.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': [
            'value: Missed requirement parameter.'
        ]
    }
