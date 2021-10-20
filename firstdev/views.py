from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
from django.contrib import messages


def home(request, nouse=0):
    articles = Article.objects.all().order_by('date')
    articles = articles.reverse()
    return render(request, 'articles/article_list.html', {'articles':articles})

def search(request):
    template = "search.html"
    query = request.GET['query']
    large = False
    if len(query) > 100:
        large = True
        articles = Article.objects.none()
    else:
        title = Article.objects.filter(title__icontains=query)
        text = Article.objects.filter(text__icontains=query)
        articles = title.union(text)
    if articles.count() == 0:
        messages.warning(request, "No search result found. Please refine your query")
    context = {'articles' : articles, 'query': query, 'large': large}
    return render(request, template, context)
