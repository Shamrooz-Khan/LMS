
from django import forms
from .models import Course
from django import forms
from .models import CustomUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'country', 'phone']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
