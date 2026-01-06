from django.shortcuts import render


def dashboard(request):

    return render(
        request,
        "dashboard/dashboard.html",
    )


def login(request):

    return render(
        request,
        "dashboard/login.html",
    )
