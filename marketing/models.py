from django.db import models
from django.conf import settings

# Create your models here.
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Subscriber(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    confirmation_num = models.CharField(max_length=15, default=123456)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='media/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for subscriber in subscribers:
            message = Mail(from_email=settings.FROM,
                           to_emails=subscriber.email,
                           subject=self.subject,
                           html_content=contents + (
                               '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
                               request.build_absolute_uri('/delete/'),
                               subscriber.email,
                               subscriber.conf_num))
            sg.send(message)
