from django.urls import path
from . views import tasklist,create,Update,Delete,view
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('iteam',tasklist.as_view(),name='items'),
    path('create',create.as_view(),name='item-create'),
    path('update/<int:pk>',Update.as_view(),name = 'item-update'),
    path('delete/<int:pk>',Delete.as_view(),name = 'item-delete'),
    path('view/<int:pk>',view.as_view(),name = 'item-view'),
]
