from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='제목')
    content = models.TextField(max_length=256, verbose_name='내용')

    class Meta:
        db_table = 'buptle_post'
