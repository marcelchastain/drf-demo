from .models import Note
from .serializers import NoteSerializer
from rest_framework import viewsets
from rest_framework.response import Response
 
class ManualNoteViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Note.objects.all()
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, pk=None):
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # automatically get the functionality of:
    # .create() 
    # .update() 
    # .list()
    # .delete()
    # .retrieve()
