from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import member
from .forms import memberform
from django.contrib import messages
from django.urls import reverse

def home(request):

    all_members=member.objects.all()

    return render(request,'homepage.html',{"all":all_members})


def formpage(request):
    form = memberform()
    if request.method == "POST":
         form=memberform(request.POST or None)
         if form.is_valid():
           form.save()
    context={'forms':form}
    return render(request,"lap.html",context)
    # else:
    #      return redirect("/")



