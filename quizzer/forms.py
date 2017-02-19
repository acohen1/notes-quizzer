from django import forms

class NotesForm(forms.Form):
    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your notes here'}), required=True)

    def clean_notes(self):
        notes = self.cleaned_data.get('notes')
        return notes