from django import forms
from .models import Profile,Project,Rating

numrate =[(x, x) for x in range(0, 11)]


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['uploaded_by', 'date',]


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['user','project','date','score']
        widgets={'usability': forms.Select(choices=numrate) , 'design': forms.Select(choices=numrate) , 'content': forms.Select(choices=numrate) , 'creativity': forms.Select(choices=numrate)}

class ProfileForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['fullname'].widget=forms.TextInput()
   class Meta:
       model=Profile
       exclude=['username']
