# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from .models import Post
from myserver.forms import PostModelForm

def post_list_view(request):
    qs = Post.objects.published() #qs = Post.objects.all()[:] 
    if request.user.is_authenticated:
        my_qs = Post.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template = 'blog/list.html'
    context = { "posts": qs }
    return render(request, template, context)

@staff_member_required  # prompt user log in
def post_create_view(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():

        # data = form.cleaned_data
        # p = Post(title=data['title'])
        # p.slug = data['slug']
        # p.content = data['content']
        # p.save()

        # p = Post.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

    template = 'blog/create.html'
    context = { "form": form }
    return render(request, template, context)

def post_detail_view(request, slug):
    # p = get_object_or_404(Post, slug=slug)
    querySet = Post.objects.filter(slug=slug)
    if querySet.count() == 0:
        raise Http404
    else:
        p = querySet.first()

    context = {"post": p}
    template = 'blog/detail.html'
    return render(request, template, context)

def post_update_view(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template = 'home/form.html'
    context = { "form": form, 'title': f"Update: {obj.title}" }
    return render(request, template, context)

@staff_member_required  # prompt user log in
def post_delete_view(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    template = 'blog/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect("/blog/")
    return render(request, template)