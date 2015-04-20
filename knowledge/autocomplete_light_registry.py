import autocomplete_light

from .models import Question


class QuestionAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['title']
    autocomplete_js_attributes = {'placeholder': 'Select a question', }
    choices = Question.objects.all()
    order_by = ['title']
    split_words = True

autocomplete_light.register(Question, QuestionAutocomplete)


