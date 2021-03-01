from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Service, Request, Project, SERVICE_TYPE, Contact
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()[:3]
    context = {
        'services': services,
        'projects': projects
    }
    return render(request, 'index.html', context)


def request_service(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    req = Request(name=name, email=email, phone=phone)
    req.save()
    send_mail(
        'رسالة جديدة',
        f'{name}تم استلام رسالة جديدة من ',
        'mail@mail.com',
        ('mail@mail.com',)
    )
    return render(request, 'request_success.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        contact = Contact(name=request.POST['name'], phone=request.POST['phone'],
                          email=request.POST['email'], message=request.POST['message'])
        contact.save()
        return render(request, 'request_success.html')
    return render(request, 'contact.html')


def privacy(request):
    return render(request, 'privacy.html')


def projects(request):
    projects = Project.objects.all()
    choices = SERVICE_TYPE
    return render(request, 'projects.html', {'projects': projects, 'choices': choices})


def project(request, slug):
    project = Project.objects.all().get(slug=slug)

    return render(request, 'project.html', {'project': project})


############################## admin views #######################

@user_passes_test(lambda u: u.is_superuser)
def incoming_requests(request):
    requests = Request.objects.all().order_by('-time')
    messages = Contact.objects.all().order_by('-time')
    return render(request, 'admin/requests.html', {'requests': requests, 'messages': messages})


def message_details(request, id):
    message = Contact.objects.get(pk=id)
    return render(request, 'admin/request_details.html', {'message': message})


def request_details(request, id):
    service_request = Request.objects.get(pk=id)
    return render(request, 'admin/request_details.html', {'service_request': service_request})
