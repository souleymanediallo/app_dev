from django.shortcuts import render
from django.http import HttpResponse
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


# Create your views here.
def home(request):
    return render(request, "projects/index.html")


def project_list(request):
    context = {'projects': projectsList}
    return render(request, "projects/project_list.html", context)


def project_detail(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, "projects/project_detail.html", {"project": projectObj})
