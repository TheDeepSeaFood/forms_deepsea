from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from public_interface.models import (
    VisitorFeedback,
    OceanoSpinnerDraw,
    CustomerDataCollection,
)


def user_login(request):
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


@login_required(login_url="login")
def dashboard(request):
    feedback_list = VisitorFeedback.objects.select_related("purpose").order_by(
        "-created_at"
    )
    context = {"feedback_list": feedback_list}
    return render(request, "dashboard/dashboard.html", context)


@login_required(login_url="login")
def feedback_list(request):
    feedback_list = VisitorFeedback.objects.select_related("purpose").order_by(
        "-created_at"
    )
    print(feedback_list)
    context = {"feedback_list": feedback_list}
    return render(request, "dashboard/feedback_list.html", context)


@login_required(login_url="login")
def user_data_collection_list(request):
    user_data_list = CustomerDataCollection.objects.order_by("-created_at")
    context = {"user_data_list": user_data_list}
    return render(request, "dashboard/user_data_collection.html", context)


@login_required(login_url="login")
def oceano_spinner_draw_list(request):
    oceano_spinner_data_list = OceanoSpinnerDraw.objects.order_by("-created_at")
    print(oceano_spinner_data_list)
    context = {"oceano_spinner_data_list": oceano_spinner_data_list}
    return render(request, "dashboard/oceano_spinner_data.html", context)
