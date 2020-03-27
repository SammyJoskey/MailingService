from django.urls import path
from .views import ListMail, CreateMail

app_name = 'mailingapp'
urlpatterns = [
    path('', CreateMail.as_view(), name='index'),
    path('list/', ListMail.as_view(), name='list_mail'),
]