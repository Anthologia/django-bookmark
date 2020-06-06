from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm
from django.core.paginator import Paginator
import math

# Create your views here.
def show(request):
    bookmark = Bookmark.objects
    bookmarks = Bookmark.objects.all()

    paginator = Paginator(bookmarks, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if page == "" or page == None:
        page = 1
    
    page_range = 5 # 보여질 페이지 범위 지정
    current_block = math.ceil(int(page)/page_range)
    start_block = (current_block-1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]

    return render(request, 'show.html', {'bookmark':bookmark, 'posts':posts, 'p_range': p_range})
    # {'bookmark':bookmark} 를 {'bookmarks':bookmarks} 로 바꿔도 되는데, 왜 그럴끼?

def new(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = Bookmark()
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.site_url = form.cleaned_data['site_url']
            bookmark.save()
            return redirect('main:show')
    else:
        form = BookmarkForm()
    return render(request, 'new.html', {'form':form})

def edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.site_url = form.cleaned_data['site_url']
            bookmark.save()
            return redirect('main:show')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'edit.html', {'bookmark':bookmark, 'form':form})

def delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        bookmark.delete()
        return redirect("main:show")