from django.urls import path
from . import views

urlpatterns = [

    path("",views.index,name="anasayfa"),
    path("albumler",views.albumler,name="albumler"),
    path("anilar",views.anilar,name="anilar"),
    path("blogs/<int:id>",views.blog_details),
    path("bbk",views.bbk,name="bbk"),
    path("istanbul",views.istanbul,name="istanbul"),
    path("notlar",views.notlar,name="notlar"),
    path("piknik",views.piknik,name="piknik"),
    
]
