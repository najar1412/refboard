from django.shortcuts import render

# from .models import Question


def index(request):
    test_data = {'some': 'data', 'to': 'test'}
    context = {'data_test': test_data}

    return render(request, 'upload/index.html', context)