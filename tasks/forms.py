from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Aaj kya karna hai?",
                "class": "task-input",
                "maxlength": "200",
                "autofocus": True,
            })
        }
        labels = {"title": ""}
