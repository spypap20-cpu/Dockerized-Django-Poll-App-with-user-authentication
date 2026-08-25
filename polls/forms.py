from django import forms
from django.forms import inlineformset_factory 
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]
        labels = {
        "question_text": "Question",
    }
        help_texts = {
            "question_text": "Please write your question",
        }

ChoiceFormSet = inlineformset_factory(
    Question,
    Choice,
    fields=["choice_text"],
    extra=3,
    can_delete=False,
    labels={'choice_text': 'Choice'},
    help_texts={'choice_text': 'Write a possible answer'},
)
