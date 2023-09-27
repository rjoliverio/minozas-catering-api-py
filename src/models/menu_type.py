from django.db import models


class MenuType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
