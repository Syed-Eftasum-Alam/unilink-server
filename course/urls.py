from django.urls import path
from .views import *

urlpatterns = [
    path('', get_courses, name='get_courses'),
    path('create/', create_course, name='create_course'),
    path('delete/', delete_course, name='delete_course'),
    path('section/<int:section_id>', get_section, name='get_section'),
    path('sections/<int:course_id>', get_course_sections, name='get_course_sections'),
    path('section/create/', create_section, name='create_section'),
    path('section/update/', update_section, name='create_section'),
    path('section/delete/', delete_section, name='delete_section'),
]
