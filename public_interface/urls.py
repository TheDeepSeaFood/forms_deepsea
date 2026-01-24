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
    path("thank-you-the-deep-seafood/", views.thank_you_thedeepseafood, name="thank_you_thedeepseafood"),
    path("thank-you-oceano/", views.thank_you_oceano, name="thank_you_oceano"),
]
