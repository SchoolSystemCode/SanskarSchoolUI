from django.shortcuts import render


def student_test(request):
    return render(request, 'index.html')