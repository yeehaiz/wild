from django.db import models

# Create your models here.
class A(models.Model):
    x = models.CharField(max_length=20)


class B(models.Model):
    y = models.CharField(max_length=20)
    z = models.ForeignKey(A)
