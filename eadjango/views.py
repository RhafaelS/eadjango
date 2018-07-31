from django.shortcuts import render

def post_list(request):
    return render(request, 'eadjango/post_list.html', {})