from django.db import models

class Video(models.Model):
    # video name
    name = models.CharField(max_length=200)
    # url of video
    url = models.CharField(max_length=400)
    # notes about video, can be empty or blank - not required to submit
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        # returns string of object - notes restricted to first 200 characters
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}'
