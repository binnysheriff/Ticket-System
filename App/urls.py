from django.urls import path

from . import views

urlpatterns = [
    path("", views.ticket_list, name="index"),  # Assuming Index is your homepage
    path("create-ticket/", views.create_ticket, name="create_ticket"),
    path("ticket-list/", views.Index.as_view(), name="ticket_list"),
    path("ticket/<int:ticket_id>/", views.view_ticket, name="view_ticket"),
    path("close-ticket/<int:ticket_id>/", views.close_ticket, name="close_ticket"),
    path("submit-ticket/", views.SubmitTicketView.as_view(), name="submit_ticket"),

]
# views.ticket_list

# views.Index.as_view()

