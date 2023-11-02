from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО автора")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", null=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название блога")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    author = models.ForeignKey(Author, related_name="fk_author", on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")


class Image(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название картинки")
    image = models.ImageField(upload_to="blog", verbose_name="Картинка")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Блог")

    def __str__(self):
        return self.image.url
