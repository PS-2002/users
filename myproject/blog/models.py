from django.db import models
from myapp.models import User
# Create your models here.

class BlogPost(models.Model):

    TYPE_CHOICES = [
        ('mental_health', 'Mental Health'),
        ('heart_disease', 'Heart Disease'),
        ('covid19', 'Covid19'),
        ('immunization', 'Immunization')
    ]

    category = models.CharField(max_length=20, choices=TYPE_CHOICES, default='mental_health')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True, null=True)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title






        # profile_picture = models.ImageField(upload_to='myapp/%Y/%m/%d', blank=True, null=True)
