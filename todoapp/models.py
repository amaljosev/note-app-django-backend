from django.db import models

# Create your models here.
class Todos(models.Model):

    Title = models.CharField(max_length=100)
    Discription = models.CharField(max_length = 100)
    Completed = models.BooleanField(default=False)
    q
    class Meta:
        db_table = "Todos"