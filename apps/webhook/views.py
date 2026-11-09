import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from apps.webhook.telegram import bot


@csrf_exempt
@require_POST
def webhook(request):
    try:
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
    except Exception as exc:
        print('Webhook error:', repr(exc), flush=True)
        raise

    return HttpResponse('OK')
