from rest_framework import serializers
from .models import Role, Profile, Player, Match, Income, Expenses, Equipment, Assignment, TrainingSession

                   

                                # Serializer for Role  Model
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']
        
                                # Serializer for Profile  Model

class ProfileSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'roles']

                                # Serializer for Player Model

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

                                # Serializer for Match Model

class MatchSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Match
        fields = '__all__'

                                # Serializer for Income Model

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

                                # Serializer for Expenses Model

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

                                # Serializer for Equipment Model

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

                                # Serializer for Assignment Model

class AssignmentSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField(read_only=True)
    equipment = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Assignment
        fields = '__all__'

                                # Serializer for TrainingSession Model

class TrainingSessionSerializer(serializers.ModelSerializer):
    players_attended = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TrainingSession
        fields = '__all__'