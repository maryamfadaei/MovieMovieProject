from django.contrib import admin
from moviedatabase.models import movie
# Register your models here.
class movieDetailAdmin(admin.ModelAdmin):
    list_display = ("movie_name", "release_date", "duration", "genre", "plot", "director", "cast", "producer", "writer", "trailer", "gallery1", "gallery2", "gallery3", "gallery4")

admin.site.register(movie, movieDetailAdmin)#put the model and display into admin
