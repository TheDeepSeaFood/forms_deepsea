from django import forms

from public_interface.models import (
    CustomerDataCollection,
    OceanoSpinnerDraw,
    VisitorFeedback,
)

RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
COMMON_RADIO_ATTRS = {"class": "flex gap-4 items-center"}


class VisitorFeedbackForm(forms.ModelForm):
    class Meta:
        model = VisitorFeedback
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your first name",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your last name",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "company_name": forms.TextInput(
                attrs={
                    "placeholder": "Your Company Name",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
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
            "other_purpose": forms.TextInput(
                attrs={
                    "placeholder": "Please specify other purpose",
                    "class": "input-3d w-full px-4 py-3 sm:py-4 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "facility_cleanliness": forms.RadioSelect(
                choices=RATING_CHOICES,
                attrs=COMMON_RADIO_ATTRS,
            ),
            "layout_flow": forms.RadioSelect(
                choices=RATING_CHOICES, attrs=COMMON_RADIO_ATTRS
            ),
            "food_safety": forms.RadioSelect(
                choices=RATING_CHOICES, attrs=COMMON_RADIO_ATTRS
            ),
            "employee_hygiene": forms.RadioSelect(
                choices=RATING_CHOICES, attrs=COMMON_RADIO_ATTRS
            ),
            "temperature_control": forms.RadioSelect(
                choices=RATING_CHOICES, attrs=COMMON_RADIO_ATTRS
            ),
            "documentation": forms.RadioSelect(
                choices=RATING_CHOICES, attrs=COMMON_RADIO_ATTRS
            ),
            "responsiveness": forms.RadioSelect(
                choices=RATING_CHOICES, attrs=COMMON_RADIO_ATTRS
            ),
            "overall_impression": forms.RadioSelect(
                choices=RATING_CHOICES, attrs=COMMON_RADIO_ATTRS
            ),
            "strengths": forms.Textarea(
                attrs={
                    "placeholder": "Enter strengths and good practices observed",
                    "rows": 4,
                    "class": "input-3d w-full px-4 py-3 sm:py-4 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "improvements": forms.Textarea(
                attrs={
                    "placeholder": "Enter areas for improvement",
                    "rows": 4,
                    "class": "input-3d w-full px-4 py-3 sm:py-4 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "comments": forms.Textarea(
                attrs={
                    "placeholder": "Enter any additional comments (optional)",
                    "rows": 4,
                    "class": "input-3d w-full px-4 py-3 sm:py-4 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
        }


class CustomerDataCollectionForm(forms.ModelForm):
    class Meta:
        model = CustomerDataCollection
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your full name",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "placeholder": "Enter your phone number",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email address",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "team_to_contact": forms.Select(
                attrs={
                    "class": "input-3d w-full px-4 py-3 sm:py-4 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 cursor-pointer border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "other_team_description": forms.TextInput(
                attrs={
                    "placeholder": "Please specify the team you want to contact",
                    "class": "input-3d w-full px-4 py-3 sm:py-4 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        team = cleaned_data.get("team_to_contact")
        other_desc = cleaned_data.get("other_team_description")

        if team == "other" and not other_desc:
            self.add_error(
                "other_team_description", "Please specify the team you want to contact."
            )


class OceanoSpinnerDrawForm(forms.ModelForm):
    class Meta:
        model = OceanoSpinnerDraw
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your full name",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "placeholder": "Enter your phone number",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email address",
                    "class": "input-3d w-full px-5 py-3 sm:py-4 pl-12 border-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 border-gray-300 bg-white hover:border-blue-400",
                }
            ),
        }
