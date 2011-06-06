from django.db import models
from datetime import datetime

class Poll(models.Model):
    name = models.CharField(max_length=255)
    visable = models.BooleanField(default=False)
    publish_date = models.DateTimeField()

    def is_visable(self):
        if self.publish_date < datetime.now():
            return False
        return True


