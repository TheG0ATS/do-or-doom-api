from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    completed = models.BooleanField()
    due = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add =True)
    # May or may not use:
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title