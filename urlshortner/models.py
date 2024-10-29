from django.db import models
import random, string
# Create your models here.

def generate_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortenedUrl(models.Model):
    original_url = models.URLField()
    short_key = models.CharField(max_length=6, unique=True, default= generate_key)
    created_at = models.DateTimeField(auto_now=True)

