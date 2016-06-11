import requests

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from wpsblog.models import Post


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username, num = options["username"].split(".")

        user = User.objects.get(username=username)

        self.stdout.write("Bulk Post Create({num}) for {username}".format(
            num=num,
            username=username
        ))

        for i in range(int(test)):
            Post.objects.create(
                user=user,
                title="BulkTest" + str(i),
                content="BulkTest_content" + str(i)
            )

        self.stdout.write("Finish Bulk Post")
