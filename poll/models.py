from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=255)
    visable = models.BooleanField(default=False)
    publish_date = models.DateTimeField()

    def is_vislable(self):
        return True


