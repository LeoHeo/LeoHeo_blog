from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import View


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "auth/login.html",
            {}
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next") or reverse("auth:mypage")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(next_url)

        return redirect(reverse("auth:login"))
