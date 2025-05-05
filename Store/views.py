from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Book
import random
import os
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    total_len = Book.objects.all().count()
    books = list(Book.objects.all())
    random_books = random.sample(books, min(3, len(books)))
    context={
        'books': random_books,
        'total_len': total_len,
    }
    return render(request, 'home.html', context)

def add(request):
    if request.method =="POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        desc = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        if Book.objects.filter(title=title).exists():
            messages.error(request, 'Book with this title already exists')
            return redirect('add')
        book = Book(title=title, author=author, genre=genre, description=desc, price=price, image=image)
        book.save()
        messages.success(request, 'Book added successfully')
        return redirect('add')
    return render(request, 'add.html')

def display(request):
    books = Book.objects.all()
    return render(request, 'display.html',{'books':books})

def details(request,name):
    book = get_object_or_404(Book, slug=name)
    return render(request, 'details.html', {'book': book})

def delete(request,name):
    book = get_object_or_404(Book, slug=name)
    if book.image:  # assuming the field name is `image`
        image_path = os.path.join(settings.MEDIA_ROOT, str(book.image))
        if os.path.exists(image_path):
            os.remove(image_path)
    book.delete()
    messages.success(request, 'Book deleted successfully')
    return redirect('home')

def edit(request,name):
    book_1 = get_object_or_404(Book, slug=name)
    if request.method == "POST":
        if Book.objects.filter(title= request.POST.get('title')).exclude(pk=book_1.pk).exists():
            messages.error(request, 'Book with this title already exists')
            return redirect('edit',name=book_1.slug)
        book_1.title = request.POST.get('title')
        book_1.author = request.POST.get('author')
        book_1.genre = request.POST.get('genre')
        book_1.description = request.POST.get('description')
        book_1.price = request.POST.get('price')
        if request.FILES.get('image'):
            book_1.image = request.FILES.get('image')
        book_1.save()
        return redirect('details',name=book_1.slug)
    book = Book.objects.get(slug=name)
    return render(request, 'add.html', {'book': book_1})