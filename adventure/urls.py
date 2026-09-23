from django.urls import path
from . import views

app_name = "adventure"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.ChoiceView.as_view(), name="detail"),
]
