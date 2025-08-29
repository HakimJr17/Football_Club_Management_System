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
    # These fields are for POST requests, allowing you to use the names.
    equipment_name = serializers.CharField(write_only=True)
    assigned_to_name = serializers.CharField(write_only=True)

    # These fields are for the API response, making it human-readable.
    assigned_to = serializers.StringRelatedField(read_only=True)
    equipment = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Assignment
        fields = '__all__'

    def create(self, validated_data):
        equipment_name = validated_data.pop('equipment_name')
        assigned_to_name = validated_data.pop('assigned_to_name')

        try:
            equipment = Equipment.objects.get(name=equipment_name)
        except Equipment.DoesNotExist:
            raise serializers.ValidationError({"equipment_name": "Equipment with this name does not exist."})
        try:
            assigned_to = Player.objects.get(name=assigned_to_name)
        except Player.DoesNotExist:
            raise serializers.ValidationError({"assigned_to_name": "Player with this name does not exist."})
        
        validated_data['equipment'] = equipment
        validated_data['assigned_to'] = assigned_to
        return super().create(validated_data)

                                # Serializer for TrainingSession Model

class TrainingSessionSerializer(serializers.ModelSerializer):
    players_attended = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TrainingSession
        fields = '__all__'