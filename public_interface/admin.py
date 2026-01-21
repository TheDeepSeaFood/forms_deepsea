from django.contrib import admin
from django.utils.html import format_html

from public_interface.models import (
    CustomerDataCollection,
    OceanoSpinnerDraw,
    PurposeOption,
    VisitorFeedback,
)


@admin.register(PurposeOption)
class PurposeOptionAdmin(admin.ModelAdmin):
    list_display = ("code", "description")
    search_fields = ("code", "description")


@admin.register(VisitorFeedback)
class VisitorFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "company_name",
        "purpose",
        "visit_date",
        "overall_impression",
        "created_at",
    )

    list_filter = (
        "purpose",
        "visit_date",
        "overall_impression",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "company_name",
        "strengths",
        "improvements",
        "comments",
    )

    # make signature + created date read-only
    readonly_fields = ("signature_preview", "created_at")

    fieldsets = (
        (
            "Visitor Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "company_name",
                    "purpose",
                    "other_purpose",
                    "visit_date",
                )
            },
        ),
        (
            "Ratings (1–5)",
            {
                "fields": (
                    "facility_cleanliness",
                    "layout_flow",
                    "food_safety",
                    "employee_hygiene",
                    "temperature_control",
                    "documentation",
                    "responsiveness",
                    "overall_impression",
                )
            },
        ),
        (
            "Feedback",
            {
                "fields": (
                    "strengths",
                    "improvements",
                    "comments",
                )
            },
        ),
        (
            "Signature (View Only)",
            {
                "fields": ("signature_preview",),
            },
        ),
        (
            "System",
            {
                "fields": ("created_at",),
            },
        ),
    )

    def signature_preview(self, obj):
        if obj.signature:
            return format_html(
                """
                <div style="
                    background: #fff;
                    border: 1px solid #ccc;
                    padding: 10px;
                    display: inline-block;
                ">
                    <img src="{}" style="max-width: 350px;" />
                </div>
                """,
                obj.signature,
            )
        return "No signature"

    signature_preview.short_description = "Signature Preview"


@admin.register(CustomerDataCollection)
class CustomerDataCollectionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "email",
        "team_to_contact",
        "other_team_description",
        "created_at",
    )
    list_filter = ("team_to_contact", "created_at")
    search_fields = ("name", "phone_number", "email", "other_team_description")
    ordering = ("-created_at",)


@admin.register(OceanoSpinnerDraw)
class OceanoSpinnerDrawAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email", "created_at")
    search_fields = ("name", "phone_number", "email")
    ordering = ("-created_at",)
