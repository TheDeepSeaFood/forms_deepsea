from django.urls import path

# from django.views.generic import RedirectView

from public_interface import views

urlpatterns = [
    # path(
    #     "",
    #     RedirectView.as_view(url="https://www.thedeepseafood.com", permanent=False),
    #     name="home-redirect",
    # ),
    path(
        "", views.visitor_feedback, name="visitor_feedback"
    ),  # Temporary placeholder for home view
    path("visitor-feedback/", views.visitor_feedback, name="visitor_feedback"),
]
