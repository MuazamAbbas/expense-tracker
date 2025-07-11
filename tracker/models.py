from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Salary', 'Salary'),
    ('Bills', 'Bills'),
    ('Transport', 'Transport'),
    ('Other', 'Other'),
]

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} ({self.amount}) - {self.category}"