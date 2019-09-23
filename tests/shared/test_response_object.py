import pytest

from asper.shared import response_object as res
from asper.use_cases import request_objects as req


@pytest.fixture
def response_value():
    return {'key': ['value1', 'value2']}


@pytest.fixture
def response_type():
    return 'ResponseError'


@pytest.fixture
def response_message():
    return 'This is a response error'


def test_response_success_is_true(response_value):
    assert bool(res.ResponseSuccess(response_value)) is True


def test_response_failure_is_false(response_type, response_message):
    assert bool(res.ResponseFailure(response_type, response_message)) is False


def test_response_success_contain_value(response_value):
    resp = res.ResponseSuccess(response_value)

    assert resp.value == response_value


def test_response_failure_has_type_and_msg(response_type, response_message):
    resp = res.ResponseFailure(response_type, response_message)

    assert resp.type == response_type
    assert resp.message == response_message


def test_response_failure_contains_value(response_type, response_message):
    resp = res.ResponseFailure(response_type, response_message)

    assert resp.value == {'type': response_type, 'message': response_message}


def test_response_failure_init_with_exception():
    resp = res.ResponseFailure(
        response_type, Exception('Just an error message'))

    assert bool(resp) is False
    assert resp.type == response_type
    assert resp.message == "Exception: Just an error message"


def test_response_failure_from_invalid_request_object():
    resp = res.ResponseFailure.from_invalid_request(req.InvalidRequest())

    assert bool(resp) is False


def test_response_failure_from_invalid_request_with_errors():
    request = req.InvalidRequest()
    request.add_error('path', 'Is mandatory')
    request.add_error('path', "can't be blank")

    response = res.ResponseFailure.from_invalid_request(request)

    assert bool(response) is False
    assert response.type == res.ResponseFailure.PARAMETERS_ERROR
    assert response.message == [
        "path: Is mandatory",
        "path: can't be blank"
    ]


def test_response_build_resource_error():
    resp = res.ResponseFailure.build_resource_error("Test message")

    assert bool(resp) is False
    assert resp.type == res.ResponseFailure.RESOURCE_ERROR
    assert resp.message == "Test message"


def test_response_build_system_error():
    resp = res.ResponseFailure.build_system_error("Test message")

    assert bool(resp) is False
    assert resp.type == res.ResponseFailure.SYSTEM_ERROR
    assert resp.message == "Test message"


def test_response_build_parameters_error():
    resp = res.ResponseFailure.build_parameters_error("Test message")

    assert bool(resp) is False
    assert resp.type == res.ResponseFailure.PARAMETERS_ERROR
    assert resp.message == "Test message"


def test_valid_request_object_cannot_be_used():
    with pytest.raises(NotImplementedError):
        req.ValidRequest.from_dict({})
