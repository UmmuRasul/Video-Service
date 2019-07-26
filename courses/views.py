from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Course

class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course

