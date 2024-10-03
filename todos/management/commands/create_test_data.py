# accounts/management/commands/create_test_data.py
from django.core.management.base import BaseCommand
from todos.factories import CustomUserFactory, ToDoFactory

class Command(BaseCommand):
    help = 'Create five users, each with five todos'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating 5 users...\n'))
        users = CustomUserFactory.create_batch(5)

        for idx, user in enumerate(users, start=1):
            self.stdout.write(self.style.SUCCESS(f'User {idx}: {user.email} created.'))
        
        self.stdout.write(self.style.SUCCESS('\nCreating 5 todos for each user...\n'))
        for idx, user in enumerate(users, start=1):
            ToDoFactory.create_batch(5, user=user)
            self.stdout.write(self.style.SUCCESS(f'5 todos created for User {idx}: {user.email}'))
        
        self.stdout.write(self.style.SUCCESS('\nData creation completed successfully!'))
