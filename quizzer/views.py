from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NotesForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        form = NotesForm()
    else:
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = form.cleaned_data['notes']
            """Logic here"""
            return render(request, 'quizzer/questions.html')
    return HttpResponseRedirect(request, 'quizzer/index.html')