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
            
            keywords = ["""ADD KEYWORDS HERE"""]
            questions = ["""HOLDER"""]
            answers = ["""HOLDER"""]


            periodIndex = 0
            sentence = ""
            tempString = ""
            keywordIndex = 0
            q = ""
            a = ""
            while (not notes==""):
                periodIndex = notes.find(".")
                sentence = notes[0:periodIndex]
                for i in keywords:
                    if sentence.find(i)>=0:
                        keywordIndex = sentence.find(i)
                a = sentence[0, keywordIndex-1]
                answers.append(a)
                q = sentence[keywordIndex, len(sentence)-1]
                questions.append(q)
                notes = notes[len(sentence), len(notes)-1]




































            return render(request, 'quizzer/questions.html')
    return HttpResponseRedirect(request, 'quizzer/index.html')