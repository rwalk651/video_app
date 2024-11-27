from urllib import parse
from django.core.exceptions import ValidationError
from django.db import models

class Video(models.Model):
    # video name
    name = models.CharField(max_length=200)
    # url of video
    url = models.CharField(max_length=400)
    # notes about video, can be empty or blank - not required to submit
    notes = models.TextField(blank=True, null=True)
    # unique YouTube ID
    """ 
    run 'python manage.py makemigrations' to alter table to include the video id field. 
    run 'python manage.py migrate' to finish migration.
    """
    video_id = models.CharField(max_length=40, unique=True)

    def save(self, *args, **kwargs):
        # extract video id from youtube url

        if not self.url.startswith('https://www.youtube.com/watch'):
            raise ValidationError(f'Not a YouTube url {self.url}')

        url_components = parse.urlparse(self.url)
        query_string = url_components.query
        if not query_string:
            raise ValidationError(f'Invalid YouTube url {self.url}')
        parameters = parse.parse_qs(query_string, strict_parsing=True)  # dictionary
        v_parameters_list = parameters.get('v') # return None if no key found
        if not v_parameters_list:   # checking if None or empty list
            raise ValidationError(f'Invalid YouTube url, missing parameters {self.url}')
        self.video_id = v_parameters_list[0]

        super().save(*args, **kwargs)

    def __str__(self):
        # returns string of object - notes restricted to first 200 characters
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}'
