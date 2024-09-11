import uuid
from django.db import models
from .constants import *

class Task(models.Model):
  
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
  title = models.CharField(max_length=200)
  description = models.TextField()
  priority = models.CharField(max_length=6, choices=PRIORITY)
  status = models.CharField(max_length=12, choices=STATUS)

  def __str__(self):
      return self.title


