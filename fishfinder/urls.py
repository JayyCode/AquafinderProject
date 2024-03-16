from . import views
from django.urls import path

urlpatterns =[
    path('', views.index,),                     #args = (urltail, reference to logic funtion, variable name for this list item  )
    path('divesearch/', views.divesearch,),
    path('discovery/', views.discovery)
    ]