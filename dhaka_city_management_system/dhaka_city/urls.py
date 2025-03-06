from django.urls import path
from .views import home,people_info,add_person,update_person,delete_person
urlpatterns = [
    path('', home, name="home"),
    path('people/', people_info, name="people_info_u"),
    path('add_person/', add_person, name="add_person_u"),
    path('update_person/<int:id>', update_person, name="update_person_u"),
    path('delete_person/<int:id>', delete_person, name="delete_person_u"),

]
