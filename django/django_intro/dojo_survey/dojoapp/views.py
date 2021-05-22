from django.shortcuts import render, HttpResponse, render

def form(request):
    return render(request, "form.html")

def result(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context={
        "name" : name,
        "location" : location,
        "language" : language,
        "comment" : comment,
    }