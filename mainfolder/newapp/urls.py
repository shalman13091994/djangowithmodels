from django.urls import path
from.views import home,formpage

urlpatterns=[
    path('',home,name='homep'),
    path('formpagu/',formpage,name='formk'),

]