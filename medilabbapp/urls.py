
from django.contrib import admin
from django.urls import path

def include(param):
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medilabbapp.urls')),

]
