from .models import News,Category

def latest_news(request):
    latest_news = News.objects.all().order_by('publish_time')[:10]
    category_list = Category.objects.all()[:10]


    context ={
        'latest_news': latest_news,
        'category_list': category_list
    }

    return context