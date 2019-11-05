from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=False)
    birthday = models.DateField()
    age = models.IntegerField(null=True, blank=True)
    notes = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name