from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import Appointment

class CityView(ViewSet):
    def retrieve(self, request, pk=None):
        """
        Retrieve a single city record based on the primary key in the request URL.
        """
        appointment = Appointment.objects.get(pk=pk)
        serialized = AppointmentSerializer(appointment, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)
    def list(self, _):
        """
        Retrieve all city records from the database.
        """
        appointments = Appointment.objects.all()
        serialized = AppointmentSerializer(appointments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    class AppointmentSerializer(seaarlizers.ModelSerializer):
        class Meta:
            model = Appointment
            fields = ('id', 'date', 'time', 'reason', 'patient_id', 'provider_id', 'location_id', 'created_at', 'updated_at'
