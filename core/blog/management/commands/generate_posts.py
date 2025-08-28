import random

from faker import Faker

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

from blog.models import Post, Category

User =get_user_model()

class Command(BaseCommand):
    help = 'Generate fake posts'

    def handle(self, *args, **options):
        fake = Faker()

        categories = Category.objects.all()
        try:
            user = User.objects.filter(is_superuser=True).first()
        except User.DoesNotExist:
            raise CommandError("No superuser found. Please create a superuser first.")
            # generate posts
        for _ in range(20):
            author = user
            title = fake.unique.word()
            content = fake.paragraph(nb_sentences=20)
            status = fake.boolean()
            published_date = fake.date_time_this_year()
            category = random.choice(categories)

            Post.objects.get_or_create(
                author=author,
                title=title,
                content=content,
                status=status,
                published_date=published_date,
                category=category,
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated 20 fake categories'))
