from django.test import TestCase
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    send_mail(
        "Welcome!",
        "Thank you for registering!",
        "noreply@example.com",
        [email]
    )

# Create your tests here.
