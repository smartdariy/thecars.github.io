import random

from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from .models import *
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.urls import reverse_lazy, reverse
from .serializers import *
from .forms import *
from random import choice

def index(request):
    context = {
    'best_types': Type.objects.order_by('-rating')[:6],
    'best_brands': Brand.objects.order_by('-rating')[:6],
    'best_cars': Car.objects.order_by('-rating')[:9],
    }
    return render(request, template_name='thecars/index.html',
                  context=context)

# class IndexView(ListView):
#     model = Car
#     queryset = Car.objects.order_by('-rating')
#     template_name = 'thecars/index.html'
#     context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    extra_context = {
        'comment_form': CommentForm(),
    }

    def get_object(self, queryset=None):
        obj = super(CarDetailView, self).get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

class CarListView(ListView):
    model = Car
    queryset = Car.objects.order_by('-rating')
    paginate_by = 6

class TypeDetailView(DetailView):
    model = Type
    template_name = 'thecars/type_detail.html'
    context_object_name = 'type'

class TypeListView(ListView):
    model = Type
    queryset = Type.objects.order_by('-rating')
    paginate_by = 4

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'thecars/brand_detail.html'
    context_object_name = 'brand'


class BrandListView(ListView):
    model = Brand
    queryset = Brand.objects.order_by('-rating')
    paginate_by = 6

class CarListApiView(generics.ListAPIView):
    queryset = Car.objects.order_by('-rating')
    serializer_class = CarSerializer1


def add_comment(request, car_id):
    user = request.user
    car = Car.objects.get(pk=car_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data.get('text')
        new_comment = Comment(author=user, car=car, text=text)
        new_comment.save()
        return HttpResponseRedirect(reverse('thecars:car-detail',
                                            kwargs={'slug': car.slug}))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('thecars:index'))

def login_page(request):
    context = {}
    if 'next' in request.GET:
        context['next'] = request.GET['next']
    else:
        return render(request, template_name='thecars/login_page.html',
                      context=context)

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    next = request.POST.get('next')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(reverse('thecars:index'))
    else:
        context = {'message': 'incorrect username or password'}
        if next:
            context['next'] = next
        return render(request, template_name='thecars/login_page.html',
                      context=context)

def search(request):
    match = request.POST.get('match')
    if match:
        car_list = Car.objects.filter(name__icontains=match)
        context = {
            'match': match,
            'car_list': car_list,
        }
        return render(request, template_name='thecars/search.html', context=context)
    else:
        return HttpResponseRedirect(reverse('thecars:index'))


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    cr = Car.objects.all()
    brands = Brand.objects.filter().order_by('name')
    brand = request.GET.get('brand')
    types = Type.objects.filter().order_by('name')
    type = request.GET.get('type')
    car_price_min = request.GET.get('car_price_min')
    car_price_max = request.GET.get('car_price_max')
    car_year_min = request.GET.get('car_year_min')
    car_year_max = request.GET.get('car_year_max')

    if is_valid_queryparam(brand) and brand != 'Choose one brand':
        cr = cr.filter(brand__name=brand)
    if is_valid_queryparam(type) and type != 'Choose one type':
        cr = cr.filter(type__name=type)
    if is_valid_queryparam(car_price_min):
        cr = cr.filter(price__gte=car_price_min)
    if is_valid_queryparam(car_price_max):
        cr = cr.filter(price__lte=car_price_max)
    if is_valid_queryparam(car_year_min):
        cr = cr.filter(year__gte=car_year_min)
    if is_valid_queryparam(car_year_max):
        cr = cr.filter(year__lte=car_year_max)

    return cr

def search_page(request):
    cr = filter(request)
    context = {
        'car_list': cr,
        'brands': Brand.objects.filter().order_by('name'),
        'types': Type.objects.filter().order_by('name')
    }
    return render(request, template_name='thecars/search_page.html', context=context)


