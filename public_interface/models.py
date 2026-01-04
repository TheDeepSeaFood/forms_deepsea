from django.db import models
from signature_pad import SignaturePadField


class PurposeOption(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class VisitorFeedback(models.Model):
    # Visitor info

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, blank=True)

    purpose = models.ForeignKey(PurposeOption, on_delete=models.SET_NULL, null=True)
    other_purpose = models.CharField(max_length=255, blank=True)
    visit_date = models.DateField()

    # Ratings (1–5)
    facility_cleanliness = models.PositiveSmallIntegerField()
    layout_flow = models.PositiveSmallIntegerField()
    food_safety = models.PositiveSmallIntegerField()
    employee_hygiene = models.PositiveSmallIntegerField()
    temperature_control = models.PositiveSmallIntegerField()
    documentation = models.PositiveSmallIntegerField()
    responsiveness = models.PositiveSmallIntegerField()
    overall_impression = models.PositiveSmallIntegerField()

    # Feedback
    strengths = models.TextField()
    improvements = models.TextField()
    comments = models.TextField(blank=True)

    # Signature (base64 image)
    signature = SignaturePadField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.visit_date}"
