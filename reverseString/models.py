from django.db import models

class StringtoReverse(models.Model):
    phrase = models.CharField(max_length=200)

    def __str__(self):
        return self.phrase