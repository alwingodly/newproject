from django.urls import path

from flipkartapp import views
app_name='flipkartapp'
urlpatterns = [
    path('',views.flipkart,name='flipkart'),
    path('<slug:cslug>/',views.flipkart,name='prodbycat'),
    path('<slug:cslug>/<slug:pslug>/',views.Pdetails,name='pdetails')
]
