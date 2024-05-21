from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import Appointment

class AppointmentView(ViewSet):
    def retrieve(self, request, pk=None):
        """
        Retrieve a single appointment record based on the primary key in the request URL.
        """
        appointment = Appointment.objects.get(pk=pk)
        
        serialized = AppointmentSerializer(appointment, context={'request': request})
                
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def list(self, _):
        """
        Retrieve all appointment records from the database.
        """
        appointments = Appointment.objects.all()
        serialized = AppointmentSerializer(appointments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'completed', 'date', 'walker')
