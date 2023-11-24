# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserLocation
import json

@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Save the location to the database
        UserLocation.objects.create(latitude=latitude, longitude=longitude)

        return JsonResponse({'message': 'Location updated successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)
