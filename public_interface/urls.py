from django.urls import path

from dashboard.views import dashboard
from public_interface import views

# from django.views.generic import RedirectView


urlpatterns = [
    # path(
    #     "",
    #     RedirectView.as_view(url="https://www.thedeepseafood.com", permanent=False),
    #     name="home-redirect",
    # ),
    path("", dashboard, name="dashboard"),
    path("visitorsfeedback/", views.visitor_feedback, name="visitorsfeedback"),
]
