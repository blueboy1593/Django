from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    past_job = models.TextField()
    profile_image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    # <Job (1)>
    # <Job 김선재>