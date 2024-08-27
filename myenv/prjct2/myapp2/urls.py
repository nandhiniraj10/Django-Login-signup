from django.urls import path
from . import views
urlpatterns=[
    #path(' ',views.nav),
    path('',views.login),
    path('signup',views.signup),
    path('success',views.success),
    path('create',views.create),
    
    
]