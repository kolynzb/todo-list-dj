from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str(self):
        return self.title