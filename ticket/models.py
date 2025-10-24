from django.db import models
import uuid
from users.models import User

# Create your models here.

class Ticket(models.Model):
    STATUS = [
        ('Pending', "Pending"),
        ('Active', "Active"),
        ('Completed', "Completed"),
    ]

    # رقم التذكرة يكون UUID فريد وغير قابل للتعديل
    number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    title = models.CharField(max_length=250)
    content = models.TextField()

    # مين اللي أنشأ التذكرة
    created_by = models.ForeignKey(User, related_name='created_tickets', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    # مين المسؤول عن التذكرة (اختياري)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')

    is_resolved = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)

    status = models.CharField(choices=STATUS, max_length=25)

    def __str__(self):
        return self.title
