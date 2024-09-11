from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status']
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title'),
            Field('description'),
            Field('priority'),
            Field('status'),
            Submit('submit', 'Add Task', css_class='btn btn-primary')
        )