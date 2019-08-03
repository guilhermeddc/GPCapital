from string import Template
from django.shortcuts import render

from django.conf import settings
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from django.utils.safestring import mark_safe

from app_gp.models import *
from django.views.generic import TemplateView, ListView, FormView
from django.forms.models import ModelForm
from django.forms.widgets import Widget, CheckboxSelectMultiple

from django.forms.models import inlineformset_factory, modelformset_factory


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        return context


class ModelsView(TemplateView):
    template_name = 'models.html'

    def get_context_data(self, **kwargs):
        context = super(ModelsView, self).get_context_data(**kwargs)
        return context


# class CityListView(TemplateView):
#     template_name = 'table.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(CityListView, self).get_context_data(**kwargs)
#         return context


# def list_city(request):
#     cities = City.objects.all()
#
#     form = MyForm(request.POST, None)
#     show_value = request.POST.get('show_number', 5)
#     paginator = Paginator(cities, show_value)
#     page = request.GET.get('page')
#     cities = paginator.get_page(page)

    # if request.method == 'POST':
    #     # show_value = request.POST.get('show_number', '')
    #     paginator = Paginator(cities, show_value)
    #     page = request.GET.get('page')
    #     cities = paginator.get_page(page)
    #     return render(request, 'table.html', {'object_list': cities, 'form': form})
    #
    # else:
    #     paginator = Paginator(cities, show_value)
    #     page = request.GET.get('page')
    #     cities = paginator.get_page(page)

    # return render(request, 'table.html', {'object_list': cities, 'form': form})


# class CityView(FormView):
#     template_name = 'table.html'
#     form_class = MyForm
#     success_url = reverse_lazy('table')
#
#     def get_context_data(self, **kwargs):
#         context = super(CityView, self).get_context_data(**kwargs)
#         # form = MyForm()
#         context['object_list'] = City.objects.all()
#         context['table_name'] = 'City'
#         # context['form'] = form
#         return context
#
#     def form_valid(self, form):
        # form = MyForm(data=self.request.POST)
        # form = MyForm(data=form.cleaned_data)
        # form.show_number = form.cleaned_data["show_number"]
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        # print "form is valid"
        # return super(CityView, self).form_valid(form)


# class CityListView(ListView):
#     model = City
#     template_name = 'table.html'
#     paginate_by = 2
#     # queryset = City.objects.all()
#
#     table_name = 'CITY INFO'
#
#     def get_context_data(self, **kwargs):
#         context = super(CityListView, self).get_context_data(**kwargs)
#         context['table_name'] = self.table_name
#         return context
#
#     def teste(self, request):
#         if request.method == "POST":
#             form = MyForm(request.POST, None)
#             if form.is_valid():
#                 self.paginate_by = form.show_number

    # def get_paginate_by(self, queryset):
    #     return self.kwargs['items_per_page']


# class Thumbnail(Widget):
#     def __init__(self, height=150, width=150):
#         super(Thumbnail, self).__init__()
#         self.height = height
#         self.width = width
#
#     def render(self, name, value, attrs=None, renderer=None):
#         html = Template("""<img src="$media$link" height="$height" width="$width"/>""")
#         return mark_safe(html.substitute(media=settings.MEDIA_URL, link=value, height=self.height, width=self.width))
#
#
# class ClientForm(ModelForm):
#     class Meta:
#         model = Client
#         # fields = ('name', 'image_profile')
#         exclude = ('name',)
#         widgets = {
#             'image_profile': Thumbnail(150, 150),
#         }
