from django.conf import settings
from django.core.management.base import BaseCommand

from apps.webhook.telegram import bot


class Command(BaseCommand):
    help = 'Register Telegram webhook'

    def handle(self, *args, **options):
        result = bot.set_webhook(
            url=settings.WEBHOOK_URL,
            secret_token=settings.WEBHOOK_SECRET,
            max_connections=20,
            allowed_updates=[
                'message',
                'callback_query',
            ],
        )

        if result:
            self.stdout.write(self.style.SUCCESS('Webhook registered successfully'))
        else:
            self.stderr.write(self.style.ERROR('Webhook registration failed'))
