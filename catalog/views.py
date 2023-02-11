# Create your views here.

from django.shortcuts import render

from .models import ProfileDetails,NgoDetails
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_users = ProfileDetails.objects.all().count()

    context = {
        'num_users': num_users,       
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class ProfileListView(generic.ListView):
    model=ProfileDetails
    context_object_name = 'user'
    template_name='catalog\profile_list.html'

class ProfileDetailView(generic.DetailView):
    model = ProfileDetails
    context_object_name = 'user'
    template_name = 'catalog\profile_detail.html'

class NgoListView(generic.ListView):
    model = NgoDetails
    context_object_name = 'user'  # your own name for the list as a template variable
    template_name = 'catalog\ngo_list.html'  # Specify your own template name/location

class NgoDetailView(generic.DetailView):
    model = NgoDetails
    context_object_name = 'user'
    template_name = 'catalog\ngo_detail.html'