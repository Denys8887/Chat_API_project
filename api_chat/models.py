from django.db import models
from django.utils import timezone


class Message(models.Model):
    author = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    text = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.date and self.update_date is None:
            self.pub_date = timezone.now()
        elif not self.date and self.update_date is not None:
            self.pub_date = None
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return self.author
