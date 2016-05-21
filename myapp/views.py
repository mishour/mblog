from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Article
# Create your views here.


def get_page(it, page_num):
    paginator = Paginator(it, 5)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def get_articles(request):
    articles = Article.objects.all().order_by('-created_at')
    page_num = request.GET.get('page')
    articles_page = get_page(articles, page_num)
    return render(request,  'index.html', {'articles_page': articles_page})


def get_article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'article': article})


class LatestArticle(Feed):
    title = "A Blog"
    link = "/feed/"
    description = "Latest Articles"

    def items(self):
        return Article.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary
