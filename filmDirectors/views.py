from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, Author
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == 'POST':
        return redirect('directorDetail', request.POST['dir'].title().strip())

    films = Film.objects.all()
    return render(request, 'index.html', {
        'films': films
    })


def directors(request):
    if request.method == 'POST':
        return redirect('directorDetail', request.POST['dir'].title().strip())

    dirs = Author.objects.all()
    return render(request, 'directors.html', {
        'dirs': dirs
    })


def film(request, title):
    if request.method == 'POST':
        return redirect('directorDetail', request.POST['dir'].title().strip())

    film = get_object_or_404(Film, title=title)
    return render(request, 'filmDetail.html', {
        'film': film
    })


def addfilm(request):
    if request.method == 'POST':
        formFile = request.FILES['upload']
        fss = FileSystemStorage(location='media/filmPosters/', base_url='filmPosters/')
        file = fss.save(formFile.name, formFile)
        file_url = fss.url(file)

        formTitle = request.POST['formTitle'].title().strip()
        formSyn = request.POST['formSyn'].strip()
        formDate = request.POST['formDate']
        Film.objects.create(
            poster=file_url,
            title=formTitle,
            synopsis=formSyn,
            author=Author.objects.get(name=request.POST['formDir']),
            releaseDate=formDate
        )
        return redirect('filmDetail', formTitle)

    directors = Author.objects.all()
    return render(request, 'addfilm.html', {
        'directors': directors
    })


def director(request, name):
    if request.method == 'POST':
        return redirect('directorDetail', request.POST['dir'].title().strip())

    director = get_object_or_404(Author, name=name)
    films = Film.objects.filter(author_id=director.id)
    return render(request, 'directorDetail.html', {
        'director': director,
        'films': films
    })


def add_director(request):
    if request.method == 'POST':
        formFile = request.FILES['upload']
        fss = FileSystemStorage(location='media/directors/', base_url='directors/')
        file = fss.save(formFile.name, formFile)
        file_url = fss.url(file)

        formName = request.POST['formName'].title().strip()
        formInfo = request.POST['formInfo'].strip()
        Author.objects.create(
            image=file_url,
            name=formName,
            information=formInfo,
        )
        return redirect('directorDetail', formName)
    return render(request, 'add_director.html')
