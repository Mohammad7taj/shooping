from django.shortcuts import render, redirect, get_object_or_404
from book.models import Book, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm , AhtorForms , BookForm



def listbook(request):
    books = Book.objects.all()
    return render(request, 'book/booklist.html', {'books':books})





def bookditale(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book/bookditale.html', {'book':book})


def creatcategory(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin")
    else:
        form=CategoryForm
    return render(request, "book/new_category.html", {"form": form})


def createahoter(request):
    form = AhtorForms()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("admin")
    else:
        form=AhtorForms
    return render(request, 'book/new_author.html', {'form':form})


def creatbook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin")
    else:
        form=BookForm
    return render(request, 'book/new_book.html', {'form':form})


def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookditale" , id=id)

    return render(request, "book/book_edit.html", context={"form": form, "book": book})