from django.shortcuts import render
# from requests import Response
from django.http import HttpResponse
from .models import *
# Create your views here.

def hello(request):
    text="""<h1>Welcome to Kyrgyzstan!</h1>"""
    return HttpResponse(text)

def index(request):
    all_news = News.objects.all()
    sorted_news = News.objects.order_by("created_at")

    # res = "<h2> List of all news </h2>"
    # for news in all_news:
    #     res += f'<h4>{news.title}</h4><br><p>{news.content}' \
    #            f'</p><br><u>{news.created_at}</u><hr>'
    # return HttpResponse(res)

    """practice"""
    # second_news = News.objects.get(pk=2)
    # result = f'<h1>{second_news.title}</h1>'
    # return HttpResponse(result)

    # return render(request, "firstapp/index.html", {'newsAll': all_news,
    #                                                'titleInHTML': 'List of all news'})
    categories = Category.objects.order_by('title')
    content = {'newsAll': sorted_news,
               'titleInHTML': 'List of all news',
               'categories': categories
               }

    return render(request, template_name="firstapp/index.html", context=content)

def about(request):
    title = 'Page about us. Welcome!'
    content = {
        'title': title,
    }
    return render(request, 'firstapp/about.html', context=content)

def contactus(request):
    title = 'Please, contact us 24/7'
    content = {
        'title': title,
    }
    return render(request, 'firstapp/contact.html', context=content)

def get_category(request, category_id):
    news = News.objects.filter(pk=category_id)
    categories = Category.objects.order_by('title')
    category = Category.objects.get(pk=category_id)

    content = {'news': news,
               'allCategories': categories,
               'category': category}
    return render(request, 'firstapp/category.html', content)