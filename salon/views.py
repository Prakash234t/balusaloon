import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Booking

@ensure_csrf_cookie
def index(request):
    return render(request, 'salon/index.html')

def book_appointment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            phone = data.get('phone')
            service = data.get('service')
            
            if not all([name, phone, service]):
                return JsonResponse({'error': 'Missing data'}, status=400)
                
            booking = Booking.objects.create(
                name=name,
                phone=phone,
                service=service
            )
            
            return JsonResponse({'message': 'Booking successful', 'id': booking.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
