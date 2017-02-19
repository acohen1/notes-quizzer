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

            string = notes
            keywords = ["invented", "created", "is"]
            count = 0
            answers = []
            questions = []
            wordIndex = 0
            perIndex = string.find(".")
            temp = string[:perIndex]
            while not string == "":
                for word in keywords:
                    if temp.find(word) != -1:
                        wordIndex = temp.find(word)
                        answers.append(temp[:wordIndex-1])
                        questions.append(temp[wordIndex:])
                        string = string[perIndex+2:]
                        perIndex = string.find(".")
                        temp = string[:perIndex]

            return render(request, 'quizzer/questions.html')
    return HttpResponseRedirect(request, 'quizzer/index.html')