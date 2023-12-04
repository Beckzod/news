from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import TemplateView, ListView


from .models import News, Category
from .forms import ContactForm


# class NewListView(generic.ListView):
#     modal = News

#     context_object_name = 'news_list'

#     queryset = News.published.all()
#     template_name = 'news/news_list.html'


def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }

    return render(request, 'news/news_list.html', context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)

    context = {
        "news": news,

    }

    return render(request, 'news/single_page.html', context)


# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-published_time')[:5]
#     local_main = News.published.filter(
#         category__name="O'zbekiston").order_by('-published_time')[:1]
#     local_news = News.published.all().filter(
#         category__name="O'zbekiston").order_by('-published_time')[1:6]
#     technology_main = News.published.filter(
#         category__name="Fan-Texnika").order_by('-published_time')[:1]
#     technology_news = News.published.all().filter(
#         category__name="Fan-Texnika").order_by('-published_time')[1:5]
#     economy_main = News.published.filter(
#         category__name="Iqtisodiyot").order_by('-published_time')[:1]
#     economy_news = News.published.all().filter(
#         category__name="Iqtisodiyot").order_by('-published_time')[1:5]
#     sport_main = News.published.filter(
#         category__name="Sport").order_by('-published_time')[:1]
#     sport_news = News.published.all().filter(
#         category__name="Sport").order_by('-published_time')[1:6]
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         'local_news': local_news,
#         'local_main': local_main,
#         "technology_main": technology_main,
#         "technology_news": technology_news,
#         "economy_main": economy_main,
#         "economy_news": economy_news,
#         'sport_main': sport_main,
#         'sport_news': sport_news,

#     }

#     return render(request, 'news/home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by(
            '-published_time')[:5]
        context['local_news'] = News.published.all().filter(
            category__name="O'zbekiston").order_by('-published_time')
        context['technology_news'] = News.published.all().filter(
            category__name="Fan-Texnika").order_by('-published_time')
        context['economy_news'] = News.published.all().filter(
            category__name="Iqtisodiyot").order_by('-published_time')
        context['sport_news'] = News.published.all().filter(
            category__name="Sport").order_by('-published_time')
        return context


class ContactView(TemplateView):
    template_name = "news/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, "news/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Sizning habaring jo'natildi.Biz bilan bog'langaningiz uchun rahmat</h2>")
        context = {

            "form": form
        }
        return render(request, 'news/contact.html', context)


def notFoundView(request):
    return render(request, "news/404.html")


def aboutView(request):
    return render(request, "news/about.html")


class LocalNewsView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name="O'zbekiston")
        return news


class ForeignNewsView(ListView):
    model = News
    template_name = 'news/foreign.html'
    context_object_name = 'foreign_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name="Jahon")
        return news


class EconomyNewsView(ListView):
    model = News
    template_name = 'news/economy.html'
    context_object_name = 'economy_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name="Iqtisodiyot")
        return news


class SocietyNewsView(ListView):
    model = News
    template_name = 'news/society.html'
    context_object_name = 'society_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name="Jamiyat")
        return news


class TechnologyNewsView(ListView):
    model = News
    template_name = 'news/technology.html'
    context_object_name = 'technology_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name="Fan-Texnika")
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name="Sport")
        return news
