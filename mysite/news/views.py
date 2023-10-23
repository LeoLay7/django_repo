from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Category  # НЕ ЗАБЫТЬ ИМПОРТ
from .forms import NewsForm, UserRegisterForm, UserLoginForm


# Create your views here.


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Новости'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by('-pk')
    
    
class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
        
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):

    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home') редирект на какой-то юрл
    # login_url = '/home/' если человек перешел по ссылке, но он не авторизован, редирект на home
    raise_exception = True  # тупо выдаст 404 и соси бибу


def register(request):
    if request.method == 'POST':
        print(request.POST)
        print('isteacher' in request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация успешна')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


"""
def index(request):  # функция, вызывающая показ шаблона на сайт
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {'title': 'Новости за сегодня', 'categories': categories, 'news': news}
    return render(request, 'news/index.html', context)



def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.filter(id=category_id)
    context = {'title': 'Новости за сегодня', 'categories': categories, 'news': news, 'current_category': current_category}
    return render(request, 'news/category.html', context)



def view_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {'title': 'Новость', 'news_item': news}
    return render(request, 'news/view_news.html', context)
"""


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             #  ЭТО ПРИ ФОРМЕ НЕ СВЯЗАННОЙ С МОДЕЛЬЮ
#             # news = News.objects.create(**form.cleaned_data)
#             # return redirect(news)
#
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
