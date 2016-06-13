from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


class MypageView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "auth/mypage.html",
            {}
        )
