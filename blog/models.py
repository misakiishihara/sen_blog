from django.db import models

class Category(models.Model):
    name = models.CharField("Category", max_length=30)
    slug = models.SlugField(unique=True)


class Post(models.Model):
    title = models.CharField("Title", max_length=200)
    content = models.TextField("Text")
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    is_published = models.BooleanField("IsPublished", default=False)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title