from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("close/<int:ticket_id>/", views.close_ticket, name="close_ticket"),
    path("submit_ticket/", views.SubmitTicketView.as_view(), name="submit_ticket"),
]
