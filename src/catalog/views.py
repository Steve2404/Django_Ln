from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre


# Create your views here.
def index(request):
    num_book = Book.objects.filter(genre__name__exact="Mangas").count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.all().filter(status__exact='a').count()
    
    num_authors = Author.objects.count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    
    context = {
        'num_books': num_book, 
        'num_instances':num_instances,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
        'num_visits': num_visits,
    }

    
    
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 2
    
    
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(title__icontains='du')
    
class BookDetailView(generic.DetailView):
    model = Book
    context_object_name ='book'
    
    
class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'authors'
    
class AuthorDetailView(generic.DetailView):
    model = Author