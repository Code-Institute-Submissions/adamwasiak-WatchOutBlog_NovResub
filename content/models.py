from django.db import models


class Content(models.Model):

    class Meta:
        verbose_name_plural = 'Content'

    email = models.EmailField()
    content_type = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
