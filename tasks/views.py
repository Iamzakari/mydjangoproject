from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Create your views here.


#tasks = [] delete hard cord tasks


class NewTasksForms(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.ImageField(label="Priority", min_value=1, max_value=10)


def index(request):
    #include tasks here
    #For user session
    if "tasks" not in request.session:
        #Use session to make each user have their own task list
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    #create a variable that take all the data that the user try to submit
    if request.method == "POST":
        form = NewTasksForms(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]#this task filed from the class
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTasksForms()
    })
