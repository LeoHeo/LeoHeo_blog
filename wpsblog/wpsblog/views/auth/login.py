from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next") or reverse("auth:mypage")

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect(next_url)

        return redirect(reverse("auth:login"))

    return render(
        request,
        "auth/login.html",
        {}
    )
