from django.contrib import admin
from .models import Team,  Player, Match, Income, Expenses, Equipment, Assignment, TrainingSession

# Register your models here.


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Income)
admin.site.register(Expenses)
admin.site.register(Equipment)
admin.site.register(Assignment)
admin.site.register(TrainingSession)