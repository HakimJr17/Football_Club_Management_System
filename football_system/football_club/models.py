from django.db import models


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length = 200, unique = True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length = 50)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    license_number = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team_name = models.CharField(max_length = 200)
    home_score = models.IntegerField(default = 0)
    away_score = models.IntegerField(default = 0)
    match_start_time = models.DateTimeField()
    is_league_match = models.BooleanField(default=False)
    players = models.ManyToManyField(Player) 

    def __str__(self):
        return f"{self.home_team} vs {self.away_team_name}"

    # A method to determine the winner    
    def get_winner(self):
        if self.home_score > self.away_score:
            return self.home_team.name
        elif self.away_score > self.home_score:
            return self.away_team_name
        return "Draw"

# The related_name is used because it allows me to access related objects from the other side of a 
# ForeignKey relationship. Since this match model has two foreign keys pointing to the same model (Team)
# Django would be confused on which field to use. By using related_name, each relationship now has
# a unique name meaning its now possible to find matches where a team played as the home or away team.

class Income(models.Model):
    source = models.CharField(max_length = 200)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.amount} from {self.source}"
    

class Expenses(models.Model):
    EXPENSE_TYPES = (
        ('T', 'Transport'),
        ('E', 'Equipment'),
        ('F', 'Fees'),
        ('M', 'Miscellaneous'),
    )
    expense_type = models.CharField(max_length=1, choices=EXPENSE_TYPES)
    amount = models.IntegerField()
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} on {self.date}"


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(max_length=50, 
        choices=[
            ('Good', 'Good'),
            ('Fair', 'Fair'),
            ('Poor', 'Poor'),
            ('Broken', 'Broken')
        ],
        default='Good'
    )
    
    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Player, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.equipment.name} assigned to {self.assigned_to.name}"
    

class TrainingSession(models.Model):
    date = models.DateField()
    players_attended = models.ManyToManyField(Player)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Training on {self.date}"
    