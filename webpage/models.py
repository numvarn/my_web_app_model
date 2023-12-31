from django.db import models

# Create your models here.
prefix_choices = (
    (1, "นาย"),
    (2, "นางสาว"),
    (3, "นาง"),
)


class Major(models.Model):
    """Model definition for Major."""

    # TODO: Define fields here
    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Major."""

        verbose_name = 'Major'
        verbose_name_plural = 'Majors'

    def __str__(self):
        """Unicode representation of Major."""
        return self.name


class Student(models.Model):
    """Model definition for Student."""

    # TODO: Define fields here
    std_id = models.IntegerField()
    prefix = models.IntegerField(choices=prefix_choices, default=1)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=1)

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        return self.name + " " + self.lastname
