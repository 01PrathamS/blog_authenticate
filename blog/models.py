from unittest.util import _MAX_LENGTH
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
