from . import views
from django.urls import path

urlpatterns =[
    path('search/', views.search,),                     #args = (urltail, reference to logic funtion, variable name for this list item  )
    path('home/', views.home_dashboard),
    path('products/', views.products),
    path('detail/', views.detail_view),
    path('signup/', views.signup),
    path('login/', views.login),
    path('watchlist', views.watchlist),
    path('admin/', views.adminview),
    ]