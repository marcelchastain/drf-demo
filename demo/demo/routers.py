from rest_framework import routers
from notes.viewsets import NoteViewSet

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
