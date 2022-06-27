from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.CharField('Email', max_length=50)
    projects = models.ManyToManyField('Project')

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuário'


class Project(models.Model):
    title = models.CharField(max_length=180, blank=False, null=False)
    description = models.CharField(max_length=280, blank=False, null=False)
    users = models.ManyToManyField(User)
    times = models.ManyToManyField('Time', related_name='project_many_time')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


class Time(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='time_user')
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL, related_name='time_project')

    def __str__(self):
        return f"{self.started_at}"

    class Meta:
        verbose_name = 'Registro de tempo'
        verbose_name_plural = 'Registros de tempo'