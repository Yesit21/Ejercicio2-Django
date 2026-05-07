# Sistema de Seguimiento de Proyectos Académicos

## Descripción
Aplicación Django para gestionar proyectos académicos con roles de estudiantes y docentes.

## Estructura del Proyecto

```
proyecto_academico/
├── proyectos/          # App principal - CRUD de proyectos
├── usuarios/           # App de autenticación y roles
├── comentarios/        # App de comentarios y notificaciones
├── templates/          # Plantillas HTML
├── static/            # Archivos estáticos (CSS, JS)
└── media/             # Archivos subidos por usuarios
```

## Instalación

1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Crear superusuario:
```bash
python manage.py createsuperuser
```

5. Ejecutar servidor:
```bash
python manage.py runserver
```

## Funcionalidades a Implementar

### Persona 1 - Autenticación y Usuarios
- [ ] Sistema de login/logout
- [ ] Gestión de roles (Estudiante/Docente)
- [ ] Decoradores de permisos
- [ ] Templates de autenticación

### Persona 2 - Gestión de Proyectos
- [ ] Modelo Proyecto
- [ ] CRUD completo con CBV
- [ ] Formularios con crispy_forms
- [ ] Filtros por estado y estudiante
- [ ] Validaciones de permisos

### Persona 3 - Comentarios y Reportes
- [ ] Modelo Comentario
- [ ] Sistema de notificaciones por email
- [ ] Exportación a CSV
- [ ] Exportación a PDF
- [ ] Bloqueo de comentarios en proyectos aprobados

## Configuración de Email

Agregar en `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña'
```

## Criterios de Evaluación
- Autenticación y control de roles: 1.5 pts
- CRUD y validaciones: 1.5 pts
- Filtros y reportes: 1.0 pts
- Calidad técnica: 1.0 pts

**Total: 5.0 puntos**
