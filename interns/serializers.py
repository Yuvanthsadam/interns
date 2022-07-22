from rest_framework import serializers
from interns.models import employee

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'