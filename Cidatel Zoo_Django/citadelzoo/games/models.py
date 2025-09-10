from django.db import models
from django.contrib.auth.models import User

class GameSession(models.Model):
    GAME_TYPES = [
        ('sumas', 'Sumas'),
        ('restas', 'Restas'),
        ('multiplicacion', 'Multiplicación'),
        ('division', 'División'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_type = models.CharField(max_length=20, choices=GAME_TYPES)
    level = models.PositiveIntegerField(default=1)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    correct = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=10)

    def score_pct(self):
        return round((self.correct / max(1, self.total)) * 100, 1)

class Question(models.Model):
    session = models.ForeignKey(GameSession, related_name='questions', on_delete=models.CASCADE)
    prompt = models.CharField(max_length=100)
    answer = models.IntegerField()
    user_answer = models.IntegerField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
