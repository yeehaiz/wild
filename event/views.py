from django.shortcuts import render



def lists(request):

    return render(request, 'lists.html', {'name': 'hello'})


def detail(request):

    return render(request, 'detail.html', {'name': 'hello'})
