# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from .models import Server


class ServerForm(forms.Form):
    my_default_errors = {
        'required': 'Campo requerido',
        'invalid': 'Valores inválidos'
    }
    direccion = forms.CharField(label='Dirección', max_length=100, error_messages=my_default_errors)
    usuario = forms.CharField(label='Usuario', max_length=100, error_messages=my_default_errors)
    contrasena = forms.CharField(label='Contraseña', max_length=100, error_messages=my_default_errors)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/multimedia/crear/'
    helper.add_input(Submit('Agregar', 'Agregar', css_class='btn-primary'))
