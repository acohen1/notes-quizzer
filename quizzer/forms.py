from django import forms

class NotesForm(forms.Form):
    notes = forms.CharField(required=True)

    def notes(self):
        notes = self.cleaned_data.get('notes')
        return notes