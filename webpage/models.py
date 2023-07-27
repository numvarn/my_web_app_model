from django.db import models

# Create your models here.


class Student(models.Model):
    """Model definition for Student."""

    # TODO: Define fields here
    std_id = models.IntegerField()
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        pass
