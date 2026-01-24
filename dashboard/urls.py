from django.urls import path

from dashboard import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.user_login, name="user_login"),
    path("feedback_list/", views.feedback_list, name="feedback_list"),
    path(
        "user_data_collection_list/",
        views.user_data_collection_list,
        name="user_data_collection_list",
    ),
    path(
        "oceano_spinner_draw_list/",
        views.oceano_spinner_draw_list,
        name="oceano_spinner_draw_list",
    ),
    path(
        "oceano_spinner_draw_detail/<int:entry_id>/",
        views.oceano_spinner_draw_detail,
        name="oceano_spinner_draw_detail",
    ),
    path(
        "oceano_spinner_draw_update/<int:entry_id>/",
        views.oceano_spinner_draw_update,
        name="oceano_spinner_draw_update",
    ),
]
