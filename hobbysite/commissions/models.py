from django.db import models
from django.urls import reverse
from user_management.models import Profile


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               related_name="author")
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('full', 'Full'),
        ('completed', 'Completed'),
        ('discontinued', 'Discontinued'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='open')
    people_required = models.IntegerField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:detail', args=[self.pk])

    class Meta:
        ordering = ['created_on']

        verbose_name = 'commission'
        verbose_name_plural = 'commissions'


class Job(models.Model):
    commission = models.ForeignKey(Commission,
                                   on_delete=models.CASCADE,
                                   related_name='commission')
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('full', 'Full'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='open')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['status', '-manpower_required', 'role']

        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class JobApplication(models.Model):
    job = models.ForeignKey(Job,
                            on_delete=models.CASCADE,
                            related_name='job')
    applicant = models.ForeignKey(Profile,
                                  on_delete=models.CASCADE,
                                  related_name='applicant')
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', 'applied_on']
