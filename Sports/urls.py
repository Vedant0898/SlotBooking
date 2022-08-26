from django.urls import path

from . import views

app_name = "Sports"

urlpatterns = [
    # Home Page
    path("",views.index,name='index'),

    # Sports page
    path("sport/<int:sport_id>",views.view_sport,name="sport"),
    path("sports",views.view_all_sports,name="all_sports"),
]