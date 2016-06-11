from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next")

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            url = next_url if next_url != '' else reverse("home")
            return redirect(url)
        else:
            return redirect(reverse("auth:login"))

    return render(
        request,
        "auth/login.html",
        {}
    )
