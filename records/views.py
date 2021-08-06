from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import BookForm
from .models import Publication
import requests
from django.shortcuts import render, redirect


class HomePage(TemplateView):
    template_name = 'records/main_page.html'


def book_list(request):

    books = Publication.objects.all()

    title_search = request.GET.get('title')
    author_search = request.GET.get('author')
    language_search = request.GET.get('language')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    if title_search != '' and title_search is not None:
        books = books.filter(title__icontains=title_search)
    elif author_search != '' and author_search is not None:
        books = books.filter(author__icontains=author_search)
    elif language_search != '' and language_search is not None:
        books = books.filter(language__icontains=language_search)
    elif date_from != '' and date_from is not None:
        books = books.filter(publication_date__gte=date_from)
    elif date_to != '' and date_to is not None:
        books = books.filter(publication_date__lte=date_to)

    context = {'books': books}
    return render(request, 'records/main_page.html', context)


def book_create(request):

    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            form.errors

    context = {'form': form}
    return render(request, 'records/create.html', context)


def book_edit(request, pk):

    book = Publication.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            form = BookForm

    context = {'form': form}
    return render(request, 'records/edit.html', context)


def book_del(request, pk):

    book = Publication.objects.get(id=pk)

    if request.method == "POST":
        book.delete()
        return redirect('list')

    context = {'book': book}
    return render(request, 'records/delete.html', context)


def api(request):
    # query = request.GET
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes/YyXoAAAACAAJ')
    volume = response.json()

    return render(request, 'records/search_api.html', {
        'title': volume['volumeInfo']['title'],
        'authors': volume['volumeInfo']['authors'][0],
        'publishedDate': volume['volumeInfo']['publishedDate'],
        'language': volume['volumeInfo']['language'],
        'pageCount': volume['volumeInfo']['pageCount'],
    })


