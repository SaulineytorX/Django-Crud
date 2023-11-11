from django.shortcuts import render

def home_REST(request):
    return render(request, 'projects/home.html')  # Asegúrate de estar renderizando la plantilla correcta para 'projects'
