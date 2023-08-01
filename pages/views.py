#lectura de todos los articulos
from typing import Any
from django import http
from django.views.generic.list import ListView
#lectura de un solo actirulo
from django.views.generic.detail import DetailView
#creacion, modificcacion y borrado de articulos
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import  staff_member_required
from django.utils.decorators import  method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm


class StaffRequireMixin(object):
    #este mixin requerira que el usuario sea miembro del staff
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        
        return super(StaffRequireMixin,self).dispatch(request, *args, **kwargs)


# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page
@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm

    success_url = reverse_lazy('pages:pages')


#    def get_success_url(self):
 #       return reverse('pages:pages')
@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pages:pages')
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

    