from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from articles.templatetags import extrafilter

from .models import Article,  ArticleComment
from . import utils
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')
    articles = articles.reverse()
    return render(request, 'articles/article_list.html', {'articles':articles})

def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    comments = utils.get_commnets(post=article)
    comment = forms.CommentForm()
    context = {
        'article':article,
        'comment':comment,
        'comments':comments
    }
    template = 'articles/article_details.html'
    return render(request, template, context)

@login_required(login_url = "/accounts/login")
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.slug = utils.link_generator()
            instance.save()
            return redirect("articles:articles_list")
    else:
        form = forms.CreateArticle()
    return render(request, "articles/article_create.html", {'form':form})

@login_required(login_url = "/accounts/login")
def postcomment(request):
    if request.method == "POST":
        comment = forms.CommentForm(request.POST)
        if comment.is_valid():
            instance = comment.save(commit=False)
            instance.user = request.user
            post_slug = request.POST.get('post_slug')
            par_id = request.POST.get('par_id')
            if par_id != None:
                par_comment = ArticleComment.objects.get(id=par_id)
                instance.parent = par_comment
                instance.height = par_comment.height+20
            post = Article.objects.get(slug=post_slug)
            instance.post = post
            instance.save()
            instance = ArticleComment.objects.get(id=instance.id)
            if par_id != None:
                par_comment.child.add(instance)
            return redirect(post.get_absolute_url())
