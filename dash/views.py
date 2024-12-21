from django.shortcuts import render, redirect
from .forms import DataForm
from .models import approvals

# Create your views here.
def index(request):
    if request.method == 'POST':
       form = DataForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('dash-pred')
    else:
        form = DataForm()
    context = {
        'form':form,
    }
    return render(request, 'dash/index.html', context)

def pred(request):
    predicted_loans = approvals.objects.all()
    context = {
       'predicted_loans': predicted_loans 
    }
    return render(request, 'dash/pred.html',context)