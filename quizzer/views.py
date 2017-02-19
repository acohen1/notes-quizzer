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

            text_file = open("static/verbs.dat", "r")
            keywords = text_file.read().split(',')
            print (keywords)
            print (len(keywords))
            text_file.close()

            string = notes
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
                        answers.append(temp[:wordIndex])
                        questions.append(temp[wordIndex+1:])
                        string = string[perIndex+1:]
                        while(string[:1] == " " or string[:1] == "\n"):
                            string = string[1:]
                        perIndex = string.find(".")
                        temp = string[:perIndex]

            return render(request, 'quizzer/questions.html', {'questions': questions, 'answers': answers})
    return render(request, 'quizzer/index.html', {'form': form})

def about(request):
    return render(request,'quizzer/about.html')