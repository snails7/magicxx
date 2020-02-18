from django.shortcuts import render
from .models import News, NewsCategory
from django.http import Http404
# Create your views here.
def index(request):
    newses = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {
        'newses': newses,
        'categories': categories
    }
    return render(request, 'news/homepage/index.html', context=context)


#def news_detail(request,news_id):

#    news = News.objects.get(pk=news_id)
#    context = {
 #       'news': news
#    }
#    return render(request,'news/detailpage/details.html', context=context)

def news_detail(request,news_id):
    try:
        news = News.objects.get(pk=news_id)
        context = {
            'news': news
        }
        return render(request,'news/detailpage/details.html',context=context)
    except:
        raise Http404