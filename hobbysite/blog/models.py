from django.db import models
from django.urls import reverse
from profile.models import Profile


# Create your models here.
class ArticleCategory(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
            Profile,
            on_delete=models.SET_NULL,
            null=True,
            editable=False
        )
    category = models.ForeignKey(
            ArticleCategory,
            on_delete=models.SET_NULL,
            null=True,
            related_name='articles'
        )
    entry = models.TextField()
    header_image = models.ImageField(upload_to='images/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.pk])

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(
            Profile,
            on_delete=models.SET_NULL,
            null=True,
            related_name="blog_comments"
        )
    article = models.ForeignKey(
            Article,
            on_delete=models.CASCADE,
            related_name='comments'
        )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
