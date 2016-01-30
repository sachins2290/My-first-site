from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Personalinfo
from .forms import PersonalinfoForm
from django.shortcuts import redirect 

def info_detail(request, pk):
    info = get_object_or_404(Personalinfo, pk=pk)
    return render(request, 'resume/info_detail.html', {'info': info})

def info_new(request):
    if request.method == "POST":
        form = PersonalinfoForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.email = request.user
            info.published_date = timezone.now()
            info.save()
            return redirect('info_detail', pk=info.pk)
    else:
        form = PersonalinfoForm()
    return render(request, 'resume/index.html',{'form':form})
# Create your views here.
