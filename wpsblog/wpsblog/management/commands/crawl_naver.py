import requests
from bs4 import BeautifulSoup as bs

from django.core.management.base import BaseCommand
from wpsblog.models import NaverPost


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('query', type=str)

    def handle(self, *args, **options):
        query = options['query']

        self.stdout.write("네이버에서 {query}크롤링을 진행합니다.".format(
            query=query
        ))

        result_list = []

        url = "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=" + query

        response = requests.get(url)
        dom = bs(response.content, 'html.parser')
        post_elements = dom.select('li.sh_blog_top')

        for post in post_elements:
            result_list.append(NaverPost(
                    title=post.select_one('a.sh_blog_title').get('title'),
                    thumbnail_image_url=post.select_one('img.sh_blog_thumbnail').get('src'),
                    content=post.select_one('dd.sh_blog_passage').get_text(),
                    original_url=post.select_one('a.sh_blog_title').get('href'),
            ))

        NaverPost.objects.bulk_create(result_list)
