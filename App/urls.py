from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('ticket/close/<int:ticket_id>/', views.close_ticket, name='close_ticket'),
    
    path('submit_ticket/', views.SubmitTicketView.as_view(), name='submit_ticket'),
    #path('submit_ticket/', views.submit_ticket, name="submit_ticket"), 
]