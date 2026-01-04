from django import forms

from .models import VisitorFeedback

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]


class VisitorFeedbackForm(forms.ModelForm):
    class Meta:
        model = VisitorFeedback
        fields = "__all__"

        widgets = {
            "visit_date": forms.DateInput(attrs={"type": "date"}),
            "facility_cleanliness": forms.RadioSelect(choices=RATING_CHOICES),
            "layout_flow": forms.RadioSelect(choices=RATING_CHOICES),
            "food_safety": forms.RadioSelect(choices=RATING_CHOICES),
            "employee_hygiene": forms.RadioSelect(choices=RATING_CHOICES),
            "temperature_control": forms.RadioSelect(choices=RATING_CHOICES),
            "documentation": forms.RadioSelect(choices=RATING_CHOICES),
            "responsiveness": forms.RadioSelect(choices=RATING_CHOICES),
            "overall_impression": forms.RadioSelect(choices=RATING_CHOICES),
        }
