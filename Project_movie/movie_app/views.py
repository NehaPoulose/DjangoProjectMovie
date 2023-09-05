from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def demo(request):
    movie = Movie.objects.all()
    context = {
        'list':movie
    }
    return render(request,'Home.html',context)

def details(request,movie_id):
    film = Movie.objects.get(id = movie_id)
    return render(request,'Detail_View.html',{'film_detail':film})

def add_movie(request):
    # return HttpResponse('Movie inserted succesfully')
    if request.method == 'POST':
        Name = request.POST.get('movie_name')
        Year = request.POST.get('movie_release')
        Outline = request.POST.get('movie_description')
        Image = request.POST.get('movie_image')

        New_movie = Movie(movie_name = Name,movie_release = Year, movie_description = Outline,movie_image = Image)
        New_movie.save()
    return render(request,'Add_movie.html')

def update(request,id):
    movie_class = Movie.objects.get(id = id)
    form = MovieForm(request.POST or None,request.FILES,instance = movie_class)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'Updation.html',{'key_movie':movie_class,'key_form':form})

def delete(request,id):
    if request.method=='POST':
        movie_del = Movie.objects.get(id = id)
        movie_del.delete()
        return redirect('/')
    return render(request,'Deletion.html')