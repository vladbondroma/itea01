from django.shortcuts import render

def post_list(request):
    return render(request, 'app1/index.html', {})