from django.urls import path

from dashboard.views import user_login
from public_interface import views

# from django.views.generic import RedirectView


urlpatterns = [
    # path(
    #     "",
    #     RedirectView.as_view(url="https://wwpyw.thedeepseafood.com", permanent=False),
    #     name="home-redirect",
    # ),
    path("", user_login, name="login"),
    path("visitorsfeedback/", views.visitor_feedback, name="visitorsfeedback"),
]
