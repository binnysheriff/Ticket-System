from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="medium"
    )


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.ticket
