from django.shortcuts import render, redirect

def index(request):
    if 'count' not in request.session or request.session['count'] == 0:
        request.session['count'] = 1
    return render(request,'survey/index.html')

def process(request):
    request.session['name'] = request.post['name']
    request.session['loc'] = request.post['loc']
    request.session['language'] = request.post['language']
    request.session['comments'] = request.post['comments']
    request.session['count'] += 1
    print request.session
    return redirect(result)

def result(request):
    return render(request,'survey/result.html')
