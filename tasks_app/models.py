from django.db import models


class Task(models.Model):
    class State(models.TextChoices):
        PENDING = 'PEN', 'PENDING'
        IN_PROGRESS = 'IPR', 'IN_PROGRESS'
        COMPLETED = 'CPD', 'COMPLETED'
        
    title = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=3, choices=State.choices, default=State.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.title
