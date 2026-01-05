from django import forms

from .models import VisitorFeedback

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]


class VisitorFeedbackForm(forms.ModelForm):
    class Meta:
        model = VisitorFeedback
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your first name",
                    "class": "input-3d w-full px-4 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "company_name": forms.TextInput(
                attrs={
                    "placeholder": "Your Company Name",
                    "class": "input-3d w-full px-4 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "visit_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "input-3d w-full px-4 py-3 sm:py-4 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "purpose": forms.Select(
                attrs={
                    "placeholder": "Purpose of Visit",
                    "class": "input-3d w-full px-4 py-3 sm:py-4 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 cursor-pointer border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "facility_cleanliness": forms.RadioSelect(
                choices=RATING_CHOICES, attrs={"class": "form-check-inline"}
            ),
            "layout_flow": forms.RadioSelect(choices=RATING_CHOICES),
            "food_safety": forms.RadioSelect(choices=RATING_CHOICES),
            "employee_hygiene": forms.RadioSelect(choices=RATING_CHOICES),
            "temperature_control": forms.RadioSelect(choices=RATING_CHOICES),
            "documentation": forms.RadioSelect(choices=RATING_CHOICES),
            "responsiveness": forms.RadioSelect(choices=RATING_CHOICES),
            "overall_impression": forms.RadioSelect(choices=RATING_CHOICES),
        }
