from django.contrib import admin
from .models import Estudiante, Curso, Direccion, Profesor, EstudianteCurso, ProfesorCurso

# Registra los modelos
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Direccion)
admin.site.register(Profesor)
admin.site.register(EstudianteCurso)
admin.site.register(ProfesorCurso)
