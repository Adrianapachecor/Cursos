from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Estudiante, Curso, Direccion, Profesor, EstudianteCurso


def index(request):
    return render(request, 'index.html') 

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "estudiantes/lista.html", {"estudiantes": estudiantes})

# Detalle de un estudiante
def detalle_estudiante(request, rut):
    estudiante = get_object_or_404(Estudiante, rut=rut)
    return render(request, "estudiantes/detalle.html", {"estudiante": estudiante})

# Crear un estudiante
def crear_estudiante(request):
    if request.method == "POST":
        # Procesar datos del formulario
        # Ejemplo: Estudiante.objects.create(...)
        pass
    return render(request, "estudiantes/crear.html")

# Lista de cursos
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos/lista.html", {"cursos": cursos})

# Inscribir estudiante en un curso
def inscribir_estudiante(request, rut, codigo_curso):
    estudiante = get_object_or_404(Estudiante, rut=rut)
    curso = get_object_or_404(Curso, codigo=codigo_curso)
    EstudianteCurso.objects.create(estudiante=estudiante, curso=curso, creado_por="admin")
    return HttpResponse(f"Estudiante {rut} inscrito en el curso {codigo_curso}")

# Lista de profesores
def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "profesores/lista.html", {"profesores": profesores})

# Direcciones asociadas
def lista_direcciones(request):
    direcciones = Direccion.objects.select_related("estudiante").all()
    return render(request, "direcciones/lista.html", {"direcciones": direcciones})
