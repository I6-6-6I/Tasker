from django.db import models

# Create your models here.

STATUS = (
    ('TODO', 'TODO'),
    ('In Progress', 'InProgress'),
    ('Make It In Feature', 'Make It In Feature'),
    ('Done', 'Done')
)


class Worker(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Task(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=32, choices=STATUS, default='TODO')

    def __str__(self):
        return self.title
