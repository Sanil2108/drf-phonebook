from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 100, blank = True, default = '')
    last_name = models.CharField(max_length = 100, blank = True, default = '')
    email = models.CharField(primary_key = True, max_length = 200)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name