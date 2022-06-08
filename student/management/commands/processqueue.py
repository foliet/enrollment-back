from django.core.management import BaseCommand
from django.conf import settings
from authentication.models import User
from enrollment import redis_conn
from university.models import Curriculum


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            user_id = int(redis_conn.brpop('enrollment_queue', 0)[1])
            curriculum_id = int(redis_conn.brpop('enrollment_queue', 0)[1])
            user = User.objects.get(pk=user_id)
            curriculum = Curriculum.objects.get(pk=curriculum_id)
            curriculum.student.add(user)
            if settings.DEBUG:
                print("用户：%s 抢到了课程：%s" % (user.username, curriculum.name))
