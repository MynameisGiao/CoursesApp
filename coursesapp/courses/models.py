from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null = True)
    updated_date = models.DateTimeField(auto_now=True, null = True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null= False)

    def __str__(self):
        return self.name

class Courses(BaseModel):
    subject = models.CharField(max_length=255, null = False)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')

class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null= False)
    content = models.TextField()
    image = models.ImageField(upload_to='lessons/%Y/%m')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'course')

class Tag(BaseModel):
    name = models.CharField(max_length= 50, unique= True)
