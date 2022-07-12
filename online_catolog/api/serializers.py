from rest_framework import serializers
from api.models import Employee
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Данный email уже существует!")
        return lower_email

    def save(self, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'Пароли не совпадают!'})
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }
