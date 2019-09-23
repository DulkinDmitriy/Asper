import collections
from validation import validate_int, validate_text, validate_structure

from asper.shared.request_objects import ValidRequest, InvalidRequest


class ValueBaseRequest(ValidRequest):
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_dict(cls, adict):
        invalid_request = InvalidRequest()

        if 'value' not in adict:
            invalid_request.add_error('value', "Missed requirement parameter.")

        if invalid_request.has_errors():
            return invalid_request

        return cls(value=adict['value'])

    def validate(self):
        raise NotImplementedError


class TargetBaseRequest(ValidRequest):
    def __init__(self, oid):
        self.oid = oid

    @classmethod
    def from_dict(cls, adict):
        invalid_request = InvalidRequest()

        if 'oid' not in adict:
            invalid_request.add_error('oid', "Missed requirement parameter.")

        if invalid_request.has_errors():
            return invalid_request

        return cls(oid=adict['oid'])

    def validate(self):
        validate_text(self.oid, min_length=1)


class TargetBaseValueRequest(ValidRequest):
    def __init__(self, oid, value):
        self.oid = oid
        self.value = value

    @classmethod
    def from_dict(cls, adict):
        invalid_request = InvalidRequest()

        if 'oid' not in adict:
            invalid_request.add_error('oid', "Missed requirement parameter.")

        if 'value' not in adict:
            invalid_request.add_error('value', "Missed requirement parameter.")

        if invalid_request.has_errors():
            return invalid_request

        return cls(oid=adict['oid'], value=adict['value'])

    def validate(self):
        validate_text(self.oid, min_length=1)


class PostListRequest(ValueBaseRequest):
    def validate(self):
        validate_structure(self.value, schema={
            'with_likes': validate_int(min_value=0, max_value=1),
            'with_comments': validate_int(min_value=0, max_value=1),
            'count': validate_int(min_value=0)
        })


class PostAddRequest(ValueBaseRequest):
    def validate(self):
        validate_structure(self.value, schema={
            "title": validate_text(min_length=1, max_length=150),
            "content": validate_text(min_length=1, max_length=3000)
        })


class PostSingleRequest(TargetBaseValueRequest):
    def validate(self):
        super().validate()
        validate_structure(self.value, schema={
            'with_likes': validate_int(min_value=0, max_value=1),
            'with_comments': validate_int(min_value=0, max_value=1)
        })


class PostUpdateRequest(TargetBaseValueRequest):
    def validate(self):
        super().validate()
        validate_structure(self.value, schema={
            'title': validate_text(min_length=1, max_length=150),
            'content': validate_text(min_length=1, max_length=3000)
        })


class CommentCreateRequest(TargetBaseValueRequest):
    def validate(self):
        super().validate()
        validate_structure(self.value, schema={
            'owner': validate_text(min_length=1),
            'content': validate_text(min_length=1, max_length=250)
        })


class CommentUpdateRequest(TargetBaseValueRequest):
    def validate(self):
        super().validate()
        validate_structure(self.value, schema={
            'content': validate_text(min_length=1, max_length=250)
        })


class LikeToCommentRequest(TargetBaseValueRequest):
    def validate(self):
        super().validate()
        validate_structure(self.value, schema={
            'owner': validate_text(min_length=1)
        })


class LikeToPostRequest(TargetBaseValueRequest):
    def validate(self):
        super().validate()
        validate_structure(self.value, schema={
            'owner': validate_text(min_length=1)
        })
