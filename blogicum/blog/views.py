from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Category, Post
from .constants import POSTS_PER_PAGE

# Вспомогательная функция принимает queryset, оптимизирует и фильтрует его
def get_published_posts(queryset):
    return queryset.select_related(
        'author', 'location', 'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template = 'blog/index.html'
    # Передаем все посты в функцию, сортировка подтянется из Meta модели Post
    page_obj = get_published_posts(Post.objects.all())[:POSTS_PER_PAGE]
    
    context = {'page_obj': page_obj}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    # Достаем посты через related_name
    post_list = get_published_posts(category.posts.all())
    
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_published_posts(Post.objects.all()),
        pk=post_id
    )
    
    context = {'post': post}
    return render(request, template, context)
