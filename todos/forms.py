from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Field, HTML

class ToDoForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        required=False
    )
    complete = forms.BooleanField(
        label='',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(HTML('<p>Title</p>'), css_class='text-right col-md-2'),  # Label column
                Column(Field('title'), css_class='col-md-10'),     # Field column
                css_class='form-row'
            ),
            Row(
                Column(HTML('<p>Completed</p>'), css_class='text-right col-md-2'),  # Label column
                Column(Field('complete'), css_class='col-md-10'),     # Field column
                css_class='form-row'
            ),
            Row(
                Column(HTML('<p>description</p>'), css_class='text-right col-md-2'),  # Label column
                Column(Field('description'), css_class='col-md-10'),     # Field column
                css_class='form-row'
            ),
            Submit('submit', 'Add ToDo', css_class='btn btn-primary mt-3')
        )

    def save(self, user):
        # Manually save the form data to the ToDo model
        todo = ToDo(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            completed=self.cleaned_data['completed'],
            user=user
        )
        todo.save()
        return todo
