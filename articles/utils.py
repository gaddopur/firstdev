import string
import random
from .models import Article,  ArticleComment

def link_generator(size=10, chars=string.ascii_uppercase + string.digits):
    slug = "".join(random.choice(chars) for x in range(size))
    try:
        Article.objects.get(slug=slug)
        link_generator()
    except:
        return slug

def dfs(root, comments):
    comments.append(root)
    for child in root.child.all():
        if child != root.parent:
            dfs(child, comments)

def get_commnets(post):
    comments = []
    roots = ArticleComment.objects.filter(post=post, parent=None)
    for root in roots:
        dfs(root, comments)
    return comments
