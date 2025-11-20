from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import User, EmailOTP


password_validator = RegexValidator(
    regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$',
    message="Password must contain uppercase, lowercase, number, symbol and 8 chars minimum."
)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[password_validator])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'dob', 'password', 'role']

    def validate(self, attrs):
        # نستخدم الإيميل كـ username داخلي
        attrs['username'] = attrs['email']
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        # المستخدم غير مفعل حتى يتحقق الـ OTP
        user.is_active = False
        user.save()
        return user


class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)


class UserSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'dob',
            'age',
            'role',
            'assigned_doctor',
            'last_activity',
        ]
