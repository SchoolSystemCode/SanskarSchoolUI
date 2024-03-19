from django.shortcuts import render, HttpResponse

# Create your views here.


def student_test(request):
    return HttpResponse("Hello Nepal.")
