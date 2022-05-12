from django.db import models

class Team(models.Model):
    title = models.CharField(max_length=50,)
    members = models.IntegerField(default=1)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
    




