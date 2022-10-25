from rest_framework import serializers
from .models import Employee
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password


class CreateEmployeeSerializer(serializers.ModelSerializer):
    """Serializer used to create new instances of employees."""

    password1 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Employee
        fields = (
            'email', 'first_name', 'last_name',
            'position', 'password1', 'password2',
        )

    def create(self, validated_data):
        password1 = self.validated_data.get('password1')
        password2 = self.validated_data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError(
                "Passwords must be the same."
            )

        validate_password(password1)
        password = make_password(password1)

        del validated_data['password1']
        del validated_data['password2']
        validated_data['password'] = password

        return super().create(validated_data)
