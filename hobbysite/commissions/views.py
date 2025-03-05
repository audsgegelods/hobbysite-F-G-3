from django.shortcuts import render
from .models import Commission, Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ComListView(ListView):
    model = Commission
    template_name = 'commission-list.html'


class ComDetailView(DetailView):
    model = Comment
    template_name = 'commission-comment.html'