from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Measure

def home(request):
    context = {
        'measures' : Measure.objects.all()
    }
    return render(request, 'measure/home.html', context)

class MeasureListView(ListView):
    model = Measure
    template_name = 'measure/home.html'
    context_object_name = 'measures'
    ordering = ['acronym']

class MeasureDetailView(DetailView):
    model = Measure


class MeasureCreateView(CreateView):
    model = Measure
    fields = ['title', 'acronym', 'description', 'population', 'exclusions', 'denominator', 'numerator']

def about(request):
    return render(request, 'measure/about.html',  {'title': 'About'})