from django.urls import path
from . import views


app_name='thecars'

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.CarListView.as_view(), name='car-list'),
    path('brand/<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('brands/', views.BrandListView.as_view(), name='brand-list'),
    path('search/', views.search, name='search'),
    # path('', views.BootstrapFilter, name='filter'),
    path('search/page/', views.search_page, name='search-page'),
    path('type/<int:pk>/', views.TypeDetailView.as_view(), name='type-detail'),
    # path('likelist/add/<int:car_id>/', views.add_car_to_likelist, name='likelist-add'),
    # path('likelist/rmv/<int:car_id>/', views.remove_car_from_likelist, name='likelist-rmv'),
    path('logout/user/', views.logout_user, name='logout-user'),
    path('login/page/', views.login_page, name='login-page'),
    path('login/user/', views.login_user, name='login-user'),
    path('types/', views.TypeListView.as_view(), name='type-list'),
    path('comment/add/<int:car_id>/', views.add_comment, name='comment-add'),
    path('car/<slug:slug>/', views.CarDetailView.as_view(), name='car-detail'),
    #API
    path('api/car/list/', views.CarListApiView.as_view(), name='api-car-list'),
]