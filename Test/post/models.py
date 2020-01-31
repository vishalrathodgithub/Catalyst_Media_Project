from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_details = models.TextField()
    post_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_title}'

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})