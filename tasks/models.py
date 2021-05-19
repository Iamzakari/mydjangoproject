from django.db import models

# Create your models here.
class NewTasksForms(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.ImageField(label="Priority", min_value=1, max_value=10)
