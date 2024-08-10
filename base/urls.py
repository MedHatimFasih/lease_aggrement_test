
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import reserve_property, reservation_view

urlpatterns = [
   
    path('',views.home,name="home"),
    path('room/',views.room,name="room"),
    path('search/', views.search_view, name='search'),
    path('city/<str:city_name>/', views.city_properties, name='city_properties'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete-account/', views.delete_account_view, name='delete_account'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add-property/', views.add_property, name='add_property'),
    path('property/success/', views.property_success, name='property_success'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<str:city>/', views.city_properties, name='city_properties'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('reserve/<int:property_id>/', reserve_property, name='reserve_property'),
    path('property/<int:property_id>/reservation/', reservation_view, name='reservation'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 