from django import forms

class NotesForm(forms.Form):
    notes = forms.CharField(required=False)

    def notes(self):
        notes = self.cleaned_data.get('notes')
        """Logic for notes processing"""
        return notes
        """Remove above line"""