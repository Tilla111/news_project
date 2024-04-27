from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import News,Category
from .forms import ContactForm


def news_list(request):
    news_list = News.objects.all()
    context = {
        "news_list": news_list
    }
    return render(request, 'news/news_list.html', context)


def homePageview(request):
    categories = Category.objects.all()
    news_list = News.objects.all().order_by('-publish_time')[:5]
    local_news = News.objects.all().filter(category__name="Mahalliy").order_by('-publish_time')[0:5]
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news
    }
    return render(request, 'news/index.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.all().order_by('-publish_time')[:5]
        context['local_news'] = News.objects.all().filter(category__name="Mahalliy").order_by('-publish_time')[0:5]
        context['foreign_news'] = News.objects.all().filter(category__name="Xorij").order_by('-publish_time')[0:5]
        context['sport_news'] = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[0:5]
        context['technology_news'] = News.objects.all().filter(category__name="Texnologiya").order_by('-publish_time')[0:5]
        return context




class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun rahmat! <h2/>")
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)



def single_page(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/single_page.html', context)



def errorPageView(request):
    context = {

    }
    return render(request, 'news/404.html', context)



class LocalPageView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'local_news_1'

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Mahalliy")
        return news


class TechnologyPageView(ListView):
    model = News
    template_name = 'news/technology.html'
    context_object_name = 'technology_news'

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Texnologiya")
        return news


class SportPageView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Sport")
        return news


class ForeignPageView(ListView):
    model = News
    template_name = 'news/foreign.html'
    context_object_name = 'foreign_news'

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Xorij")
        return news



