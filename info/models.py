from django.db import models

# Create your models here.
class Quote(models.Model):
  text = models.CharField(max_length=1000, default="")

  # string representation of this class
  def __str__(self):
    return self.text
