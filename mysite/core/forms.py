from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book
from .models import Post
from .models import Question
from .models import CV


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    profile_pic = forms.ImageField()

   

    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","profile_pic","password1","password2")

    def save(self, commit=True):
        user =super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','author','pdf','cover')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','post')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question',)
class CVsForms(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('name','surname','Highest_degree_achieved','cv','Highest_Certtificate','cover_letter')
    