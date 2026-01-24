from django.shortcuts import redirect, render

from public_interface.forms import (
    CustomerDataCollectionForm,
    OceanoSpinnerDrawForm,
    VisitorFeedbackForm,
)
from public_interface.models import PurposeOption


def visitor_feedback(request):
    if request.method == "POST":
        form = VisitorFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print("Feedback submitted:", form.instance)
            return redirect("visitor_feedback")
    else:
        form = VisitorFeedbackForm()

    # if you want to filter/change purpose choices, you can still touch the field:
    form.fields["purpose"].queryset = PurposeOption.objects.all()

    return render(
        request,
        "public_interface/forms/visitor_feedback.html",
        {
            "form": form,
        },
    )


def user_data_collection(request):
    if request.method == "POST":
        form = CustomerDataCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you_thedeepseafood")
    else:
        form = CustomerDataCollectionForm()

    return render(
        request, "public_interface/forms/user_data_collection.html", {"form": form}
    )


def oceano_spinner_draw(request):
    if request.method == "POST":
        form = OceanoSpinnerDrawForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you_oceano")
    else:
        form = OceanoSpinnerDrawForm()
    return render(
        request,
        "public_interface/forms/oceano_spinner_draw.html",
        {"form": form},
    )


def thank_you_thedeepseafood(request):
    return render(request, "public_interface/thank_you_thedeepseafood.html")


def thank_you_oceano(request):
    return render(request, "public_interface/thank_you_oceano.html")
