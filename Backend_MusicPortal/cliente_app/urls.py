from django.urls import path
from cliente_app import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('saveCli/',views.saveCli,name="saveCli"),
    path('editCli/',views.saveCli,name="editCli"),
    path('selCli/',views.saveCli,name="selCli"),
    path('delCli/',views.saveCli,name="delCli"),
]