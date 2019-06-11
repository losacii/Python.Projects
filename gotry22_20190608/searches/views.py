from django.shortcuts import render
from .models import SearchQuery
from blog.models import Post

def search_view(request):
    query = request.GET.get('q', None)
    context = {"query": query }

    if query:
        SearchQuery.objects.create(user=request.user, query=query)
        posts = Post.objects.search(query=query)
        context['posts'] = posts

    template = 'searches/view.html'
    return render(request, template, context)