from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField

from .models import Todo, Comment

class UserForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = ""
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'inputCreate', 'placeholder': 'Пароль'})
        
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = ""
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'inputCreate', 'placeholder': 'Повторите пароль'})
        
    class Meta:
        model = User
        
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': '',
            'password1': '',
            'password2': '',
        }
       
        help_texts = {
           'username': '',
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Фамилия'}),
            'email': forms.EmailInput(attrs={'class': 'inputCreate', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Username/Логин'}),
        }
        
class LoginForm(AuthenticationForm):
    captcha = CaptchaField(label='', error_messages={'invalid': 'Неверная капча'})
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = ""
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Username/Логин'})
        
        self.fields['password'].label = ""
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'inputCreate', 'placeholder': 'Пароль'})
        
        self.fields['captcha'].widget.attrs.update({'class': 'inputCreate', 'placeholder': 'Введите капчу'})
        
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['image', 'title', 'text', 'datecompleted', 'important', 'status', 'perform']
        labels = {
            'image': '',
            'title': '',
            'text': '',
            'datecompleted': '',
            'important': '',
            'status': '',
            'perform': '',
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'inputCreate', 'placeholder': 'Изображение'}),
            'title': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Заголовок'}),
            'text': forms.Textarea(attrs={'class': 'inputCreate', 'placeholder': 'Описание'}),
            'datecompleted': forms.DateInput(attrs={'type': 'date', 'class': 'inputCreate', 'placeholder': 'Дата выполнения'}),
            'important': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Важность'}),
            'status': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Статус'}),
            'perform': forms.Select(attrs={'class': 'inputCreate', 'placeholder': 'Выполнено'}),
        }