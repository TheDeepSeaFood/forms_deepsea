from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from public_interface.models import VisitorFeedback


@login_required(login_url="login")
def dashboard(request):
    feedback_list = VisitorFeedback.objects.select_related('purpose').order_by('-created_at')
    context = {
        'feedback_list': feedback_list
    }
    return render(request, "dashboard/dashboard.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")
        context = {"error": "Invalid username or password"}
    else:
        context = {}
    return render(request, "dashboard/login.html", context)
