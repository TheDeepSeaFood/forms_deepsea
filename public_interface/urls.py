from django.urls import path

from dashboard.views import user_login
from public_interface import views

urlpatterns = [
    path("", user_login, name="login"),
    path("visitorsfeedback/", views.visitor_feedback, name="visitorsfeedback"),
    path(
        "user-data-collection/", views.user_data_collection, name="user_data_collection"
    ),
    path("oceano-spinner-draw/", views.oceano_spinner_draw, name="oceano_spinner_draw"),
    path("thank-you/", views.thank_you, name="thank_you"),
]
