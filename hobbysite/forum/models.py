from django.db import models
from django.urls import reverse
from user_management.models import User


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Thread Categories"


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        editable=False
    )
    category = models.ForeignKey(
        ThreadCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    entry = models.TextField()
    optional_image = models.ImageField(
        upload_to='media/images/',
        blank=True,
        null=True,
        verbose_name="Optional Image",
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:thread_detail', args=[self.pk])

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']