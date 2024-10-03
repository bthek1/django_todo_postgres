# accounts/factories.py
import factory
from django.utils import timezone
from accounts.models import CustomUser
from .models import ToDo

class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
    date_joined = timezone.now()
    password = factory.PostGenerationMethodCall('set_password', 'password123')  # Default password


class ToDoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ToDo

    title = factory.Faker('sentence')
    description = factory.Faker('paragraph')
    completed = factory.Faker('boolean')
    user = factory.SubFactory(CustomUserFactory)
