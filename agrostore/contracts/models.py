from django.db import models

class BaseContract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contract(BaseContract):

    def __str__(self):
        return self.created_at
