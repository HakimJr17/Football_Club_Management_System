from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    TeamViewSet, 
    PlayerViewSet, 
    MatchViewSet, 
    IncomeViewSet, 
    ExpensesViewSet, 
    EquipmentViewSet, 
    AssignmentViewSet, 
    TrainingSessionViewSet
)

# Creating the router and registering the ViewSets with it
router = DefaultRouter()
router.register(r'team', TeamViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'match', MatchViewSet)
router.register(r'income', IncomeViewSet)
router.register(r'expenses', ExpensesViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'assignment', AssignmentViewSet)
router.register(r'trainingsession', TrainingSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
