import json
from json import JSONDecodeError

from enrollment import redis_conn
from enrollment.result import Results, Result


def select_curriculum(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            curriculum_id = body['curriculum_id']
        except (KeyError, JSONDecodeError):
            return Results.illegal_argument
        try:
            user_id = request.session['id']
        except KeyError:
            return Results.not_login
        lua = """
            local has_selected = redis.call("sadd",KEYS[1],ARGV[1])
            if has_selected ~= 1 then
                return 1
            end
            local count = redis.call("hincrby","curriculum",ARGV[1],-1)
            if count < 0 then
                return 2
            end
            redis.call("lpush","enrollment_queue",KEYS[1],ARGV[1])
            redis.call("sadd",KEYS[1],ARGV[1])
            return 0
        """
        script = redis_conn.register_script(lua)
        res = script(keys=[user_id], args=[curriculum_id])
        if res == 0:
            return Result(data_message="抢课成功").to_response()
        elif res == 1:
            return Result(data_message="抢课失败：已选该课程", status=False).to_response()
        else:
            return Result(data_message="抢课失败：人数已达上限", status=False).to_response()
    else:
        return Results.wrong_method
