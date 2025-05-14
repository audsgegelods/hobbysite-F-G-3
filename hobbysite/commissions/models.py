from django.db import models
from django.urls import reverse
from user_management.models import User


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name="author",
                            null=True)
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    )
    status = models.CharField(max_length=14, choices=STATUS_CHOICES)

    people_required = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('commissions:detail', args=[self.pk])

    class Meta:
        ordering = ['status', 'created_on']

        verbose_name = 'commission'
        verbose_name_plural = 'commissions'


class Job(models.Model):
    commission = models.ForeignKey(Commission,
                                   on_delete=models.CASCADE,
                                   related_name='job')
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

        verbose_name = 'job'
        verbose_name_plural = 'jobs'


class JobApplication(models.Model):
    job = models.ForeignKey(Job,
                            on_delete=models.CASCADE,
                            related_name='job')
    applicant = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='applicant',
                                  null=True) #TODO: TEMP
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', 'applied_on']

        verbose_name = 'job application'
        verbose_name_plural = 'job applications'
