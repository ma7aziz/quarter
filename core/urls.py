from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('request_service', views.request_service, name='request_service'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name="contact"),
    path('projects', views.projects, name="projects"),
    path('project/<str:slug>', views.project, name='project'),
    path('privacy', views.privacy, name="privacy"),
    path('incoming_requests', views.incoming_requests, name='requests'),
    path('message/<int:id>', views.message_details, name='message'),
    path('contact_request/<int:id>', views.request_details, name='request')
]
