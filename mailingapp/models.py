from django.db import models
from django.core.mail import send_mail
from datetime import timedelta, datetime, timezone
import time, threading

class Mail(models.Model):
    subject = models.CharField(max_length=50, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    email = models.EmailField()
    second = models.SmallIntegerField(verbose_name='Задержка (сек.)')
    publish = models.DateTimeField(auto_now_add=True)
    
    @property
    def published(self):
        return self.publish + timedelta(seconds=self.second)

    @property
    def send(self):
        return self.published < datetime.now(timezone.utc)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        threads = []
        def sender(subject, text, email, second):
            time.sleep(second)
            send_mail(subject, text, 'yoptie@mail.ru', [email], fail_silently=False)

        t = threading.Thread(target=sender, args=(self.subject, self.text, self.email, self.second))
        threads.append(t)
        t.start()
