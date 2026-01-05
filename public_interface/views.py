from django.shortcuts import redirect, render

from public_interface.models import PurposeOption

from .forms import VisitorFeedbackForm


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
        "public_interface/forms/visitor_feedback_duplicate.html",
        {
            "form": form,
        },
    )
