from django.shortcuts import render
from django.views import generic
from .models import Story

class IndexView(generic.ListView):
    template_name = 'adventure/index.html'
    context_object_name = 'latest_story_list'

    def get_queryset(self):

        return Story.objects.filter(is_start=True)
    

class ChoiceView(generic.DetailView):
    model = Story
    template_name = 'adventure/detail.html' 

