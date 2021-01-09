from django_cache.settings import CACHE_TTL
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from .services import get_recipes_with_cache, get_recipes_without_cache


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.
@cache_page(CACHE_TTL)
def receipe_view(request):
    return render(request, 'cookbook/recipes.html', 
    {'recipes': get_recipes_with_cache()}
    )