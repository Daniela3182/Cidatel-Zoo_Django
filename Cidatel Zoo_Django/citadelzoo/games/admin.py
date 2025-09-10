from django.contrib import admin
from .models import GameSession, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0

@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('id','user','game_type','level','correct','total','started_at','finished_at')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','session','prompt','answer','user_answer','is_correct')
