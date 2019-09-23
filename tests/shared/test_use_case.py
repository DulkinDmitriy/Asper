from unittest import mock

from asper.shared import request_objects as req, response_object as res
from asper.shared import use_case as uc


def test_use_case_cannot_process_valid_request():
    valid_request = mock.MagicMock()
    valid_request.__bool__.return_value = True

    use_case = uc.UseCase()
    response = use_case.execute(valid_request)

    assert not response
    assert response.type == res.ResponseFailure.SYSTEM_ERROR
    assert response.value['message']['error'] == 'NotImplementedError: \
process_request not implemented by UseCase class'

    assert len(response.value['message']['traceback']) > 0


def test_use_case_can_process_invalid_request_and_return_failure_response():
    invalid_request = req.InvalidRequest()
    invalid_request.add_error('first_param', 'first_message')
    invalid_request.add_error('second_param', 'second_message')

    use_case = uc.UseCase()
    response = use_case.execute(invalid_request)

    assert not response
    assert response.type == res.ResponseFailure.PARAMETERS_ERROR
    assert response.message == [
        'first_param: first_message',
        'second_param: second_message'
    ]


def test_use_case_can_manage_generic_exceptions_from_process_request():
    use_case = uc.UseCase()

    class TestException(Exception):
        pass

    use_case.process_request = mock.Mock()
    use_case.process_request.side_effect = TestException('somemessage')
    response = use_case.execute(mock.Mock())

    assert not response
    assert response.type == res.ResponseFailure.SYSTEM_ERROR
    assert 'error' in response.value['message']
    assert len(response.value['message']['traceback']) > 0
