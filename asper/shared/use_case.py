import json
import traceback
import sys
from asper.shared import response_object as res


class UseCase:
    def execute(self, request):
        if not request:
            return res.ResponseFailure.from_invalid_request(request)

        try:
            request.validate()
        except Exception as ex:
            return res.ResponseFailure.build_parameters_error(
                f"{ex.__class__.__name__}: {ex}"
            )

        try:
            return self.process_request(request)
        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            return res.ResponseFailure.build_system_error({ 
                "error": f"{ex.__class__.__name__}: {ex}", 
                "traceback": [
                    repr(trace) for trace in traceback.extract_tb(exc_traceback)
                ]
            })

    def process_request(self, request):
        raise NotImplementedError(
            "process_request not implemented by UseCase class")
