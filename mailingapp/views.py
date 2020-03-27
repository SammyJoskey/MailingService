from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.core.mail import send_mail


from .models import Mail
from .forms import MailForm

# # Create your views here.
# def asd(request):
#     return render(request, 'mailingapp/index.html', context={'text': 'qwsdfhdfghdfghdfg'})

class CreateMail(CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailingapp:list_mail')
    template_name = 'index.html'

class ListMail(ListView):
    model = Mail
    context_object_name = 'mails'
    template_name = 'list_mail.html'

    # def get_queryset(self):
    #     print(Mail.objects.all())
    #     return Mail.objects.all()

# def asdf(request):
#     qw = send_mail('dfsdfsdfsd', 'fasdfasdfasd', '3434455@mail.ru', ['kalinkaufa@mail.ru'], fail_silently=False)
#     return render(request, 'mailingapp/index1.html', context={'text': qw})
    