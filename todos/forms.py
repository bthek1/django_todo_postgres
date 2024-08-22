from django import forms
from .models import ToDo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ToDoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('Add todo', 'Add todo'))
        
    class Meta:
        model = ToDo
        fields = ['title', 'description', 'completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
