from django.shortcuts import render, redirect

def index(request):
    if 'count' not in request.session or request.session['count'] == 0:
        request.session['count'] = 1
    return render(request,'survey/index.html')

def result(request):
    return render(request,'survey/result.html')

def process(request):
    print "Processing..."
    request.session['name'] = request.POST['name']
    request.session['loc'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['count'] += 1
    print request.session
    return redirect(result)
