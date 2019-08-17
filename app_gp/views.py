from string import Template
from django.shortcuts import render, get_object_or_404

from django.conf import settings
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from django.utils.safestring import mark_safe

from app_gp.models import *
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView
from django.db.models import Q
from django.forms.models import ModelForm
from django.forms.widgets import Widget, CheckboxSelectMultiple

from django.forms.models import inlineformset_factory, modelformset_factory
from app_gp.forms import *


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['photos'] = ClientPhoto.objects.filter(client=1)
        return context


class CreateClientView(CreateView):
    model = Client
    template_name = 'create_client_test.html'
    fields = ('name', )

    def get_context_data(self, **kwargs):
        context = super(CreateClientView, self).get_context_data(**kwargs)
        return context


class ClientList(ListView):

    model = Client
    context_object_name = 'clients'
    template_name = 'mdb/pages/index.html'
    # template_name = 'Client/client_list.html'
    # paginate_by = 2
    form = SearchClientForm()

    # filtro = self.request.GET.getlist(key, default=None)
    # filtro = self.request.GET.get(key, default=None)
    def get_queryset(self):

        list_filter_dict = {
            'hair_id': self.request.GET.getlist('category', default=[]),
            'genre_id': self.request.GET.getlist('genre', default=[]),
            'eye_id': self.request.GET.getlist('eye', default=[]),
            'ethnicity_id': self.request.GET.getlist('ethnicity', default=[])
        }
        # self.form = SearchClientForm(self.request.GET)
        queryset = Client.objects.actives(list_filter_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        context['client_per_row'] = 4
        return context


class ClientDetail(DetailView):

    template_name = 'mdb/pages/profile-page.html'
    model = Client

    # def get_queryset(self):
    #     self.photos = get_object_or_404(Photo, name=self.kwargs['pk'])
    #     return Photo.objects.filter(publisher=self.photos)

    # def get_context_data(self, **kwargs):
    #     context = super(ClientList, self).get_context_data(**kwargs)
        # context['photos'] = Photo.objects.filter(client=self.kwargs['pk'])
        # return context


class ClientView(CreateView):
    model = Client
    template_name = 'admin/table.html'

    # state = ModelChoiceField(queryset=ChoicesStates.objects.all())
    # city = ModelChoiceField(queryset=ChoicesCity.objects.filter(state=7))

    fields = ('name', 'fake_name')

    def get_context_data(self, **kwargs):
        context = super(ClientView, self).get_context_data(**kwargs)
        context['states'] = ChoicesStates.objects.all()
        context['cities'] = ChoicesCity.objects.all()
        return context

    # def load_cities(self, request):
    #     state_id = request.GET.get('state')
    #     cities = ChoicesCity.objects.filter(sate=state_id).order_by('name')
    #     return render(request, 'load_cities.html', {'cities': cities})


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
