# Sitio Web Institucional — E.E.S. Técnica N.º 1 de Esteban Echeverría

Proyecto educativo para el aula: desarrollo de una página web institucional para una
escuela secundaria técnica, utilizando **Python + Django** en el backend, **HTML, CSS y
JavaScript** en el frontend, y **SQLite3** como motor de base de datos.

El objetivo pedagógico es que los estudiantes recorran el ciclo completo de un proyecto
web real: relevamiento de necesidades, diseño de identidad visual, desarrollo backend,
maquetado frontend, integración con base de datos y pruebas de funcionamiento.

---

## Índice

1. [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
2. [Tecnologías utilizadas](#tecnologías-utilizadas)
3. [Estructura del proyecto](#estructura-del-proyecto)
4. [Requisitos previos](#requisitos-previos)
5. [Instalación y puesta en marcha](#instalación-y-puesta-en-marcha)
6. [Comandos útiles](#comandos-útiles)
7. [Rutas del sitio](#rutas-del-sitio)
8. [Autenticación](#autenticación)
9. [Modelos y contenido editable](#modelos-y-contenido-editable)
10. [Identidad visual](#identidad-visual)
11. [Actividades sugeridas para el aula](#actividades-sugeridas-para-el-aula)
12. [Criterios de evaluación sugeridos](#criterios-de-evaluación-sugeridos)
13. [Solución de problemas frecuentes](#solución-de-problemas-frecuentes)

---

## Objetivos de aprendizaje

Al finalizar el proyecto, el estudiante será capaz de:

- Comprender la arquitectura Modelo–Vista–Plantilla (MVT) de Django.
- Configurar un proyecto y una aplicación Django desde cero.
- Definir modelos y generar migraciones sobre una base de datos SQLite3.
- Crear vistas basadas en funciones y enlazarlas mediante rutas.
- Diseñar plantillas HTML reutilizables con herencia de templates.
- Aplicar una paleta cromática institucional mediante variables CSS.
- Construir interfaces responsivas y accesibles.
- Incorporar interactividad con JavaScript sin depender de frameworks externos.
- Implementar autenticación segura reutilizando el sistema nativo de Django.

---

## Tecnologías utilizadas

| Capa          | Tecnología                                   |
|---------------|----------------------------------------------|
| Backend       | Python 3.10+ y Django 5.2                    |
| Frontend      | HTML5, CSS3 y JavaScript (vanilla)           |
| Base de datos | SQLite3 (a través del ORM de Django)         |
| Plantillas    | Sistema de templates de Django               |
| Estilos       | CSS propio basado en variables institucionales |

No se utilizan React, Node.js, Express ni frameworks de frontend: toda la lógica del
servidor reside en Django y el diseño se resuelve con CSS propio.

---

## Estructura del proyecto

```text
TrabajoEquipo/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── config/                     # Configuración global del proyecto
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── institucion/                # Aplicación institucional
│   ├── models.py               # Modelos Especialidad y Noticia
│   ├── views.py                # Vistas home y bienvenida
│   ├── urls.py                 # Rutas de la aplicación
│   ├── admin.py                # Registro de modelos en el panel
│   └── migrations/
│       ├── 0001_initial.py
│       └── 0002_datos_ejemplo.py
├── templates/                  # Plantillas HTML
│   ├── base.html               # Plantilla base (header, nav, footer)
│   ├── home.html               # Página de inicio institucional
│   ├── login.html              # Inicio de sesión
│   └── bienvenida.html         # Página protegida post-login
└── static/                     # Archivos estáticos
    ├── css/
    │   └── estilos.css
    ├── js/
    │   └── main.js
    └── img/
        └── logo.svg            # Marcador de posición del escudo institucional
```

---

## Requisitos previos

- Python 3.10 o superior instalado.
- `pip` disponible en la consola.
- Un editor de código (por ejemplo, Visual Studio Code).
- Navegador web actualizado.

Verificar la instalación:

```powershell
python --version
pip --version
```

---

## Instalación y puesta en marcha

1. Clonar o descargar el proyecto y ubicarse en la carpeta raíz:

```powershell
cd TrabajoEquipo
```

2. (Recomendado) Crear y activar un entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

4. Aplicar las migraciones (crea la base `db.sqlite3` y carga los datos de ejemplo):

```powershell
python manage.py migrate
```

5. Crear un usuario administrador:

```powershell
python manage.py createsuperuser
```

6. Iniciar el servidor de desarrollo:

```powershell
python manage.py runserver
```

7. Abrir en el navegador: <http://127.0.0.1:8000/>

---

## Comandos útiles

| Acción                                  | Comando                                            |
|-----------------------------------------|----------------------------------------------------|
| Instalar dependencias                   | `pip install -r requirements.txt`                  |
| Crear archivo de migraciones            | `python manage.py makemigrations`                  |
| Aplicar migraciones                     | `python manage.py migrate`                         |
| Crear superusuario                      | `python manage.py createsuperuser`                 |
| Ejecutar servidor local                 | `python manage.py runserver`                       |
| Verificar configuración                 | `python manage.py check`                           |
| Abrir consola interactiva de Django     | `python manage.py shell`                           |

---

## Rutas del sitio

| Ruta             | Descripción                                     | Acceso               |
|------------------|-------------------------------------------------|----------------------|
| `/`              | Página de inicio institucional (Home)           | Público              |
| `/login/`        | Formulario de inicio de sesión                  | Público              |
| `/logout/`       | Cerrar sesión (método POST)                     | Usuario autenticado  |
| `/bienvenida/`   | Página de bienvenida protegida                  | Solo con sesión      |
| `/admin/`        | Panel de administración de Django               | Superusuario         |

El Home incluye navegación por anclas internas: **Inicio**, **Institución**,
**Especialidades**, **Noticias** y **Contacto**.

---

## Autenticación

El proyecto utiliza el **sistema de autenticación nativo de Django**, que aporta:

- Gestión segura de sesiones.
- Contraseñas cifradas (nunca en texto plano).
- Validación de credenciales.
- Protección CSRF en todos los formularios.

La página de bienvenida está protegida con el decorador `@login_required` y redirige al
login cuando no hay sesión activa.

El formulario de login permite mostrar u ocultar la contraseña mediante JavaScript e
informa los errores de autenticación sin abandonar la identidad visual del sitio.

---

## Modelos y contenido editable

El contenido se administra desde `/admin/` sin necesidad de tocar el código:

- **Especialidad**: nombre, descripción, icono, estado activo y orden.
- **Noticia**: título, resumen, fecha y estado de publicación.

La migración `0002_datos_ejemplo.py` carga orientaciones (Informática, Electrónica,
Mecánica, Construcciones) y noticias de muestra para que el sitio no aparezca vacío.

---

## Identidad visual

La paleta institucional se declara como variables CSS globales en
`static/css/estilos.css`:

```css
:root {
    --rojo-institucional: #8B1E1E;
    --bordo-oscuro: #5C0F0F;
    --rojo-secundario: #A62B2B;

    --gris-oscuro: #5A5555;
    --gris-medio: #7A7474;
    --gris-claro: #E6E6E6;

    --blanco: #FFFFFF;
    --negro: #000000;

    --rojo-claro: #E8C5C5;
    --rojo-suave: #C97A7A;
}
```

Criterios de diseño aplicados: predominio de fondos claros, rojo institucional para
acciones, bordó oscuro para profundidad, tarjetas con bordes sutiles y sombras
discretas, transiciones suaves y contraste adecuado para accesibilidad.

> **Sobre el logotipo:** `static/img/logo.svg` es un marcador de posición. Debe
> reemplazarse por el escudo oficial de la institución cuando esté disponible. No se debe
> sustituir por un emblema que pueda confundirse con el original.

---

## Actividades sugeridas para el aula

1. **Relevamiento y análisis**: identificar las secciones que necesita una escuela y
   justificar su organización.
2. **Identidad visual**: analizar la paleta institucional y proponer variantes de
   componentes (botones, tarjetas, formularios).
3. **Modelado de datos**: agregar un campo nuevo a `Noticia` (por ejemplo, autor) y
   generar la migración correspondiente.
4. **HTML semántico**: revisar las plantillas y verificar el uso correcto de etiquetas
   estructurales y atributos de accesibilidad (`alt`, `aria-*`, `label`).
5. **Responsive Design**: probar el sitio en distintas resoluciones y corregir la
   adaptación del menú y las grillas.
6. **JavaScript**: extender `main.js` con nuevas interacciones (por ejemplo, un contador
   o un filtro de noticias por año).
7. **Seguridad**: explicar por qué no se almacenan contraseñas en texto plano y qué rol
   cumple el token CSRF.
8. **Trabajo en equipo**: dividir el proyecto en roles (backend, frontend, contenidos,
   pruebas) y documentar los aportes.

---

## Criterios de evaluación sugeridos

| Criterio                          | Indicadores                                                        |
|-----------------------------------|--------------------------------------------------------------------|
| Funcionamiento                    | El sitio levanta, las rutas responden y la base de datos persiste. |
| Arquitectura Django               | Separación correcta de modelos, vistas, rutas y plantillas.        |
| Identidad visual                  | Uso consistente de la paleta y los componentes definidos.          |
| Responsive y accesibilidad        | Adaptación a móvil/tablet y contraste/estructura adecuados.        |
| Autenticación                     | Login funcional, página protegida y cierre de sesión.              |
| Calidad del código                | Simplicidad, claridad y ausencia de dependencias innecesarias.     |
| Documentación                     | README claro y comentarios mínimos pero útiles.                    |

---

## Solución de problemas frecuentes

- **Error de CSRF al hacer POST**: asegurate de incluir `{% csrf_token %}` dentro de cada
  formulario. Tras iniciar sesión, el token se renueva, por lo que hay que recargar la
  página antes de enviar otro formulario.
- **No cargan los estilos o el JavaScript**: verificá que `django.contrib.staticfiles`
  esté en `INSTALLED_APPS` y que `STATICFILES_DIRS` apunte a la carpeta `static/`.
- **"No such table"**: ejecutá `python manage.py migrate`.
- **No puedo entrar al admin**: es necesario crear un superusuario con
  `python manage.py createsuperuser`.
- **El formulario de login rechaza credenciales correctas**: confirmá que el usuario
  existe y que la sesión no expiró; los datos de autenticación se gestionan desde el
  admin o con `createsuperuser`.

---

Proyecto con fines educativos. Se autoriza su uso y adaptación para el trabajo áulico,
respetando la identidad institucional de la E.E.S. Técnica N.º 1 de Esteban Echeverría.
