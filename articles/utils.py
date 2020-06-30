import string
import random
from .models import Article

def link_generator(size=10, chars=string.ascii_uppercase + string.digits):
    slug = "".join(random.choice(chars) for x in range(size))
    try:
        Article.objects.get(slug=slug)
        link_generator()
    except:
        return slug
