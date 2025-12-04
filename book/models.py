from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    birthdate = models.DateField(verbose_name='تاریخ تولد')
    biografi = models.TextField(blank=True, verbose_name='بیوگرافی')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    kholase = models.TextField(default='خلاصه')
    cover = models.ImageField(upload_to='pic_book', default='default.jpg')
    pages = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'