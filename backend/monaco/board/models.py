from django.db import models


class Member(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'posts'
# Create your models here.
