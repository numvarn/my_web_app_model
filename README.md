## เว็บแอปพลิเคชันแรก ที่พัฒนาด้วย Django Web Framework

ความรู้ที่ได้จากเรียนรู้

1. การสร้าง project ด้วย Django

```shell
> django-admin startproject <projectname>
```

2. การสร้าง python virtual environment ใน project

```shell
> cd <projectname>
> python -m venv env
```

3. การสร้าง application ใน project

```shell
> python manage.py startapp <appname>
```

Student Model

```python
class Student(models.Model):
    """Model definition for Student."""

    # TODO: Define fields here
    std_id = models.IntegerField()
    prefix = models.IntegerField(choices=prefix_choices, default=1)
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
        return self.name + " " + self.lastname

```

---

## Screen Capture

![image](https://numvarn.github.io/resume/asset/images/web/my_webapp/001.png)

![image](https://numvarn.github.io/resume/asset/images/web/my_webapp/002.png)

![image](https://numvarn.github.io/resume/asset/images/web/my_webapp/003.png)
