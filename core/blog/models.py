from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    """
    This is a class to define posts for blog app
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # todo: set upload to
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL,
                                 null=True, related_name="posts")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    This is a class to define post category for blog app
    """
    name = models.CharField(max_length=250)
    parent = models.ForeignKey("Category", on_delete=models.SET_NULL,
                               null=True, blank=True, related_name="sub_categories")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name
