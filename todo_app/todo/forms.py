from django import forms

class Todoform(forms.Form):
    todo_field = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'What to do?'}))