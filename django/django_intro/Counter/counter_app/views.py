from django.shortcuts import render,redirect

def index (request):
    if "counter" not in request.session:
        request.session["counter"]=0
    else:
        request.session["counter"]+=1
    return render(request,"index.html")
def delete(request):
    del request.session['counter']
    return redirect('/')

# Create your views here.

