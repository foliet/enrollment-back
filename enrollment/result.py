class Result:
    def __init__(self, code=0, message="Succeed", data=None, status=True, data_message=""):
        self.code = code
        self.message = message
        if data is not None:
            data['status'] = status
            data["message"] = data_message
        self.data = data

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data,
        }


class Results:
    illegal_argument = Result(message="Fail:请求参数非法", code=1).to_dict()
