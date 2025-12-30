from rest_framework import serializers
from .models import Event, Task,Attendance
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='staff'), write_only=True, source='assigned_to')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'assigned_to_id', 'event', 'completed', 'due_date']


class AttendanceSerializer(serializers.ModelSerializer):
    staff = UserSerializer(read_only=True)
    staff_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='staff'), write_only=True, source='staff')

    class Meta:
        model = Attendance
        fields = ['id', 'event', 'staff', 'staff_id', 'present']



class EventSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'date', 'created_by', 'tasks']
