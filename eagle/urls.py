from django.urls import include, path
from classroom import views
from django.contrib import admin
from classroom import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('pay/<int:pk>', views.Pay, name='pay'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('save_vehicle/', views.save_vehicle, name='save_vehicle'),
    path('logout/', views.logout_view, name='logout'),
    path('vehicle/', views.Vehicle.as_view(), name='vehicle'),
    path('users/', views.UserView.as_view(), name='users'),
    path('listvehicle/', views.ListVehicle.as_view(), name='listvehicle'),
    path('view_vehicle/<int:pk>', views.VehicleReadView.as_view(), name='view_vehicle'),
    path('view_car/<int:pk>', views.CarReadView.as_view(), name='view_car'),
    path('view_user/<int:pk>', views.UserReadView.as_view(), name='view_user'),
    path('update_vehicle/<int:pk>', views.VehicleUpdateView.as_view(), name='update_vehicle'),
    path('update_car/<int:pk>', views.CarUpdateView.as_view(), name='update_car'),
    path('delete_vehicle/<int:pk>', views.VehicleDeleteView.as_view(), name='delete_vehicle'),
    path('delete_car/<int:pk>', views.CarDeleteView.as_view(), name='delete_car'),
    path('inoice/<int:pk>', views.GeneratePdf.as_view(), name='invoice'),
    path('user_update/<int:pk>', views.UserUpdateView.as_view(), name='user_update'),
    path('delete_user/<int:pk>', views.DeleteUser.as_view(), name='delete_user'),
    path('create/create', views.create, name='create'),





]
