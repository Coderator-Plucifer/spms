from rest_framework import viewsets, permissions
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'STUDENT':
            return Attendance.objects.filter(student__user=user)
        # Teachers and Admins can see all (filtering can be added later)
        return Attendance.objects.all()

    def perform_create(self, serializer):
        # Optional: Add logic to validate teacher creates attendance
        serializer.save()
