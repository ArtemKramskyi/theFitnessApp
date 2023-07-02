from django.forms import ModelForm, TextInput, Textarea, Select
from .models import ExercisesCatalog, Program


class ExercisesCatalogForm(ModelForm):

    class Meta:
        model = ExercisesCatalog
        exclude = ['user']
        widgets = {'exerciseName': TextInput(attrs={
            'class': "form-control px-2 py-1.5 text-gray-700 border border-solid border-gray-300 rounded transition ease-in-out m-1 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none",
            'style': 'max-width: 20rem',
            'placeholder': 'Title',
            'id': 'exerciseNameForm'
        }),
            'exerciseDescription': Textarea(attrs={
                'class': "form-control px-2 py-1.5 text-gray-700 border border-solid border-gray-300 rounded transition ease-in-out m-1 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none",
                'cols': 40,
                'rows': 15,
                'style': 'width: 75%',
                'autocomplete': "off",
                'placeholder': 'Description',
                'label': 'Description'
            }),
            'category': Select(attrs={
                'class': "form-select px-2 py-1.5 text-base font-normal text-gray-700 border border-solid border-gray-300 rounded transition ease-in-out m-1 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none",
                'style': 'max-width: 150px',
                'id': 'categoryFormId',
                'placeholder': 'Choose'
            }),
            'exerciseImg': TextInput(attrs={
                'class': "form-control px-2 py-1.5 text-gray-700 border border-solid border-gray-300 rounded transition ease-in-out m-1 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none",
                'style': 'max-width: 300px',
                'placeholder': 'Image URL',
            })}


class ProgramForm(ModelForm):

    class Meta:
        model = Program
        fields = "__all__"
        widgets = {'programName': TextInput(attrs={
            'class': "form-control px-2 py-1.5 text-gray-700 border border-solid border-gray-300 rounded transition ease-in-out m-1 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none",
            'style': 'max-width: 20rem',
            'placeholder': 'Program name',
        })}
