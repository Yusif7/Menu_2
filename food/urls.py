from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:pk>', views.Detail.as_view(), name='detail'),
    path('create/', views.CreateItem.as_view(), name='create'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete')
]
