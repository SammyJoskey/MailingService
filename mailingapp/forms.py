from django import forms
from .models import Mail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import formset_factory


class MailForm(forms.ModelForm):

    
    class Meta:
        model = Mail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Отправить', css_class="btn-success"))