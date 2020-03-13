from django.db import models
from authentication.models import User

class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='contacts')
    phone = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name + ' -- ' + self.phone