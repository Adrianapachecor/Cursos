from django.db import models

# Modelo para estudiantes
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)  # Clave primaria
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    fecha_nac = models.DateField(blank=False, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField(
        "Curso", through="EstudianteCurso", related_name="estudiantes"
    )  # Relación muchos a muchos con Curso

# Modelo para cursos
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)  # Clave primaria única
    nombre = models.CharField(max_length=50, blank=False, null=False)
    version = models.IntegerField(blank=True, null=True)
    profesores = models.ManyToManyField(
        "Profesor", through="ProfesorCurso", related_name="cursos"
    )  # Relación muchos a muchos con Profesor

# Modelo para direcciones
class Direccion(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autonumérica
    calle = models.CharField(max_length=50, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50, blank=False, null=False)
    ciudad = models.CharField(max_length=50, blank=False, null=False)
    region = models.CharField(max_length=50, blank=False, null=False)
    estudiante = models.OneToOneField(
        Estudiante, on_delete=models.CASCADE, related_name="direccion"
    )  # Relación uno a uno con Estudiante

# Modelo para profesores
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)  # Clave primaria
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)

# Modelo intermedio para la relación Estudiante-Curso
class EstudianteCurso(models.Model):
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, related_name="estudiante_cursos"
    )
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name="curso_estudiantes"
    )
    fecha_asignacion = models.DateField(auto_now_add=True)
    nota_final = models.FloatField(blank=True, null=True)  # Campo opcional para registrar notas
    creado_por = models.CharField(max_length=50)

# Modelo intermedio para la relación Profesor-Curso
class ProfesorCurso(models.Model):
    profesor = models.ForeignKey(
        Profesor, on_delete=models.CASCADE, related_name="profesor_cursos"
    )
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name="curso_profesores"
    )
    fecha_asignacion = models.DateField(auto_now_add=True)
    creado_por = models.CharField(max_length=50)
