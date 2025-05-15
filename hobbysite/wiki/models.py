from django.db import models
from django.urls import reverse
from user_management.models import Profile
# from django.contrib.auth.models import User


class ArticleCategory(models.Model):
    name = models.CharField(
        max_length=255,
        null=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        # 'user_management.Profile',
        Profile,
        # User,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        related_name='articles'
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles'
    )
    entry = models.TextField()
    header_image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True
        )
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:article_detail', args=[self.pk])

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(
        # 'user_management.Profile',
        Profile,
        # User,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        related_name='comments'
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=True,
        related_name='comments',
        editable=False

    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
