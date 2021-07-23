from django.db import models

class Thing(models.Model):
    name = models.CharField("Thing's name", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "thing"
        verbose_name_plural = "things"
