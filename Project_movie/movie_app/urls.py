from  .import views
from django.urls import path
app_name = 'movie_app'

urlpatterns = [

    path('',views.demo,name = 'Demo'),
    path('movie/<int:movie_id>/',views.details,name = 'Detail'),
    path('insert/',views.add_movie,name = 'add_movie'),
    path('update/<int:id>/',views.update,name = 'Update'),
    path('delete/<int:id>/',views.delete,name = 'Delete')
]
