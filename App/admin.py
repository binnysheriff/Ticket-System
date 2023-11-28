from django.contrib import admin
from .models import Ticket, Comment
# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass