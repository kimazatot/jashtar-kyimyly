import random
import logging
from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from account.models import SMSVerification
from django.contrib.auth import get_user_model


logger = logging.getLogger(__name__)
User = get_user_model()


@shared_task(bind=True, max_retries=3)
def send_code(self, email, code):
    try:
        send_mail(
            subject=f'Код подтверждения для {email}',
            message=f'Ваш код подтверждения: {code}',
            from_email='fatimaakbva@yandex.ru',
            recipient_list=[email]
        )
        logger.info(f"Email с кодом {code} отправлен на {email}")
    except Exception as e:
        logger.error(f"Ошибка при отправке email на {email}: {e}")
        raise self.retry(exc=e, countdown=10)


@shared_task
def save_code_in_db(email, code):
    sms_verification, created = SMSVerification.objects.update_or_create(
        email=email,
        defaults={'code': code}
    )

    if created:
        logger.info(f"Создана запись в БД для {email}")
    else:
        logger.info(f"Обновлён код в БД для {email}")


@shared_task
def generate_and_save_and_send_code(email):
    code = f"{random.randint(1000, 9999)}"

    send_code.delay(email, code)
    cache.set(f'sms_code_{email}', code, timeout=180)
    save_code_in_db.delay(email, code)

    logger.info(f"Код {code} сгенерирован и отправлен для {email}")
    return code
