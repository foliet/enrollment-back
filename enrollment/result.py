from django.http import JsonResponse


class Result:
    def __init__(self, code=0, message="Succeed", data=None, status=True, data_message=""):
        self.code = code
        self.message = message
        if data is None:
            data = {}
        data['status'] = status
        data["message"] = data_message
        self.data = data

    def to_dict(self):
        _dict = {
            "code": self.code,
            "message": self.message,
        }
        if self.code == 0:
            _dict['data'] = self.data
        return _dict

    def to_response(self):
        return JsonResponse(self.to_dict())


class Results:
    illegal_argument = Result(message="Fail:请求参数非法", code=1).to_response()
    wrong_method = Result(message="Fail:错误的请求方式", code=2).to_response()
    not_login = Result(message="Fail:未登录用户", code=3).to_response()
