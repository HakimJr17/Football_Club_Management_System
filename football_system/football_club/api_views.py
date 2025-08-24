from rest_framework import viewsets
from .models import Team, Player, Match, Income, Expenses, Equipment, Assignment, TrainingSession
from .serializers import TeamSerializer, PlayerSerializer, MatchSerializer, IncomeSerializer, ExpensesSerializer, EquipmentSerializer, AssignmentSerializer, TrainingSessionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsCaptainOrManagerSecretaryCoachReadOnly, IsCaptainOrIsManagerOrIsCoach, IsManagerOrReadOnly, IsClubSecretaryOrManagerReadOnly, IsCaptainOrIsCoachOrManagerSecretaryReadOnly

                                            # API viewset for Team model

# Only logged-in managers can perform unsafe operations to the team models
# All other users can only view the data

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsManagerOrReadOnly | IsAdminUser]

                                        # API viewset for Player model

# only mamagers can perform unsafe operations on the data
# all other logged in users have view access only

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsManagerOrReadOnly | IsAdminUser]

                                        # API ViewSet for Match model

# captains, managers, and coach can perform unsafe operations on the data
# all other users only have read access

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCaptainOrIsManagerOrIsCoach | IsAdminUser]

                                        # API ViewSet for Income Model

# Logged in club secretary can perform unsafe operations on the data, team manager can view the data 
# all other users are declined access to the data
 
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsClubSecretaryOrManagerReadOnly | IsAdminUser]

                                        # API ViewSet for Expenses Model

# Logged in club secretary can perform unsafe operations on the data, team manager can view the data 
# all other users are declined access to the data

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsClubSecretaryOrManagerReadOnly | IsAdminUser]

                                        # API ViewSet for Equipment Model

# Logged in captains and Managers can perform unsafe operations,                                        

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCaptainOrManagerSecretaryCoachReadOnly | IsAdminUser]

                                        # API ViewSet for Assignment Model

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCaptainOrManagerSecretaryCoachReadOnly | IsAdminUser]

                                        # API endpoint for TrainingSession

class TrainingSessionViewSet(viewsets.ModelViewSet):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCaptainOrIsCoachOrManagerSecretaryReadOnly | IsAdminUser]