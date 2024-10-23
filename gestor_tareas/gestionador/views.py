from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TareaRegistro
from .serializers import TareaSerializer
from django.http import JsonResponse

@api_view(['GET'])
def obtener_tareas(request):
    tareas = TareaRegistro.objects.all()
    serializer = TareaSerializer(tareas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def agregar_tarea(request):
    serializer = TareaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizar_tarea(request, identificador_tarea):
    try:
        tarea = TareaRegistro.objects.get(identificador_tarea=identificador_tarea)
    except TareaRegistro.DoesNotExist:
        return JsonResponse({'mensaje': 'Tarea no encontrada'}, status=404)
    
    serializer = TareaSerializer(tarea, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def eliminar_tarea(request, identificador_tarea):
    try:
        tarea = TareaRegistro.objects.get(identificador_tarea=identificador_tarea)
        tarea.delete()
        return JsonResponse({'mensaje': 'Tarea eliminada exitosamente'}, status=204)
    except TareaRegistro.DoesNotExist:
        return JsonResponse({'mensaje': 'Tarea no encontrada'}, status=404)
