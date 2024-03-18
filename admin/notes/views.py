from django.shortcuts import render
from .models import Note
# Create your views here.
def noteslist(request):
    all_Notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes' : all_Notes })