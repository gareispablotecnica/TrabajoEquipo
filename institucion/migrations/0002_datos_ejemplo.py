from django.db import migrations

ESPECIALIDADES = [
    {'nombre': 'Informática', 'icono': '</>', 'orden': 1,
     'descripcion': 'Desarrollo de software, redes y soporte técnico. Formamos profesionales capaces de crear soluciones digitales para los desafíos del mundo actual.'},
    {'nombre': 'Electrónica', 'icono': 'Hz', 'orden': 2,
     'descripcion': 'Diseño, montaje y mantenimiento de circuitos y sistemas electrónicos, con prácticas en laboratorios especializados.'},
    {'nombre': 'Mecánica', 'icono': 'RPM', 'orden': 3,
     'descripcion': 'Fabricación, reparación y mantenimiento de máquinas y estructuras metálicas, con sólida formación en taller.'},
    {'nombre': 'Construcciones', 'icono': '2D', 'orden': 4,
     'descripcion': 'Cálculo, dibujo técnico y ejecución de obras, preparando técnicos para el sector de la construcción y la infraestructura.'},
]

NOTICIAS = [
    {'titulo': 'Inscripción al ciclo lectivo 2027', 'fecha': '2026-10-10',
     'resumen': 'Ya está abierta la inscripción para primer año. Consultá requisitos y fechas en la sección secretaría de la escuela.'},
    {'titulo': 'Feria de Ciencias y Tecnología', 'fecha': '2026-09-28',
     'resumen': 'Los estudiantes de sexto año presentaron proyectos de electrónica e informática en la feria institucional.'},
    {'titulo': 'Taller de robótica extracurricular', 'fecha': '2026-09-15',
     'resumen': 'Iniciamos un taller extracurricular de robótica y programación abierto a toda la comunidad estudiantil.'},
]


def cargar_datos(apps, schema_editor):
    Especialidad = apps.get_model('institucion', 'Especialidad')
    Noticia = apps.get_model('institucion', 'Noticia')
    for datos in ESPECIALIDADES:
        Especialidad.objects.get_or_create(nombre=datos['nombre'], defaults=datos)
    for datos in NOTICIAS:
        Noticia.objects.get_or_create(titulo=datos['titulo'], defaults=datos)


def eliminar_datos(apps, schema_editor):
    Especialidad = apps.get_model('institucion', 'Especialidad')
    Noticia = apps.get_model('institucion', 'Noticia')
    Especialidad.objects.filter(nombre__in=[d['nombre'] for d in ESPECIALIDADES]).delete()
    Noticia.objects.filter(titulo__in=[d['titulo'] for d in NOTICIAS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_datos, eliminar_datos),
    ]
