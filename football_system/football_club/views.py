from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Player, Match, Income, Expenses, Equipment, Assignment, TrainingSession


                                    # Views Associated with the Player model

# view listing all players belonging to a team
class PlayerListView(ListView):
    model = Player
    template_name = 'football_club/players_list.html'
    context_object_name = 'players' # what the name of the list object should be in the template

# view for a player's details 
class PlayerDetailView(DetailView):
    model = Player
    template_name = 'football_club/player_detail.html'
    context_object_name = 'player'

# view for creating a new player
class PlayerCreateView(CreateView):
    model = Player
    template_name = 'football_club/create_player.html'
    fields = '__all__'

#view for updating an existing player
class PlayerUpdateView(UpdateView):
    model = Player
    template_name = 'football_club/update_player.html'
    fields = '__all__'

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'football_club/delete_player.html'
    context_object_name = 'delete_player'

                                    # Views Associated with the Match model

# view for showing creating a new match object
class MatchCreateView(CreateView):
    model = Match
    template_name = 'football_club/create_match.html'
    fields = '__all__'

# view for showing details of a match model
class MatchDetailView(DetailView):
    model = Match
    template_name = 'football_club/match_details.html'
    context_object_name = 'view_match'

# view for updating an existing match model
class MatchUpdateView(UpdateView):
    model = Match
    template_name = 'football_club/update_match.html'
    fields = '__all__'

# view for updating an existing match model
class MatchDeleteView(DeleteView):
    model = Match
    template_name = 'football_club/delete_match.html'
    context_object_name = 'delete_match'

# view for listing all matches played by a team
class MatchListView(ListView):
    model = Match
    template_name = 'football_club/matches_played.html'
    context_object_name = 'matches_played'

                                    # Views Associated with the Income model

# view for listing all incomes
class IncomeListView(ListView):
    model = Income
    template_name = 'football_club/list_income.html'
    context_object_name = 'list_income'

# view for seeing details of a specific income
class IncomeDetailView(DetailView):
    model = Income
    template_name = 'football_club/view_income.html'
    context_object_name = 'view_income_details'

# view for creating a new income
class IncomeCreateView(CreateView):
    model = Income
    template_name = 'football_club/create_income.html'
    fields = '__all__'

#view for updating an income
class IncomeUpdateView(UpdateView):
    model = Income
    template_name = 'football_club/update_income.html'
    fields = '__all__'

#view for deleting an income
class IncomeDeleteView(DeleteView):
    model = Income
    template_name = 'football_club/delete_income.html'
    context_object_name = 'delete_income'

                                    # Views Associated with the Expenses Model

# view for listing all expenses
class ExpensesListView(ListView):
    model = Expenses
    template_name = 'football_club/list_expenses.html'
    context_object_name = 'list_expenses'

# view for seeing details of a specific expense
class ExpensesDetailView(DetailView):
    model = Expenses
    template_name = 'football_club/view_expenses.html'
    context_object_name = 'view_expense_details'

# view for creating a new expense
class ExpenseCreateView(CreateView):
    model = Expenses
    template_name = 'football_club/create_expense.html'
    fields = '__all__'

#view for updating an expense
class ExpenseUpdateView(UpdateView):
    model = Expenses
    template_name = 'football_club/update_expense.html'
    fields = '__all__'

#view for deleting an expense
class ExpenseDeleteView(DeleteView):
    model = Expenses
    template_name = 'football_club/delete_expense.html'
    context_object_name = 'delete_expense'

                                     # Views Associated with the Equipment Model

# view for listing all equipment
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'football_club/list_equipment.html'
    context_object_name = 'list_equipment'

# view for seeing details of a specific equipment
class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'football_club/view_equipment.html'
    context_object_name = 'view_equipment_details'

# view for creating a new equipment
class EquipmentCreateView(CreateView):
    model = Equipment
    template_name = 'football_club/create_equipment.html'
    fields = '__all__'

# view for updating an eqiupment
class EquipmentUpdateView(UpdateView):
    model = Equipment
    template_name = 'football_club/update_equipment.html'
    context_object_name = 'update_equipment'
    fields = '__all__'

#view for deleting an equipment
class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'football_club/delete_equipment.html'
    context_object_name = 'delete_equipment'   

                                    # Views Associated with the Assignment Model

# view for listing all assignments
class AssignmentListView(ListView):
    model = Assignment
    template_name = 'football_club/list_assignment.html'
    context_object_name = 'list_assignment'

# view for seeing details of a specific assignment
class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'football_club/view_assignment.html'
    context_object_name = 'view_assignment_details'

# view for creating a new assignment
class AssignmentCreateView(CreateView):
    model = Assignment
    template_name = 'football_club/create_assignment.html'
    fields = '__all__'

# view for updating an assignment
class AssignmentUpdateView(UpdateView):
    model = Assignment
    template_name = 'football_club/update_assignment.html'
    fields = '__all__'

# view for deleting an assignment
class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = 'football_club/delete_assignment.html'
    context_object_name = 'delete_assignment'   

                                    # Views Associated with the TrainingSession Model

# view for listing all training sessions
class TrainingSessionListView(ListView):
    model = TrainingSession
    template_name = 'football_club/list_trainingsession.html'
    context_object_name = 'training_session'

# view for seeing details of a specific training session
class TrainingSessionDetailView(DetailView):
    model = TrainingSession
    template_name = 'football_club/view_trainingsession.html'
    context_object_name = 'view_training_session_details'

# view for creating a new training session
class TrainingSessionCreateView(CreateView):
    model = TrainingSession
    template_name = 'football_club/create_trainingsession.html'
    fields = '__all__'

# view for updating an training session
class TrainingSessionUpdateView(UpdateView):
    model = TrainingSession
    template_name = 'football_club/update_trainingsession.html'
    fields = '__all__'

# view for deleting a training session
class TrainingSessionDeleteView(DeleteView):
    model = TrainingSession
    template_name = 'football_club/delete_trainingsession.html'
    context_object_name = 'delete_training_session' 