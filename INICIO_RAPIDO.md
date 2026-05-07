# 🚀 Inicio Rápido

## 1. Configuración Inicial (Hacer UNA SOLA VEZ)

### Instalar dependencias:
```bash
pip install -r requirements.txt
```

### Aplicar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Crear superusuario:
```bash
python manage.py createsuperuser
```

### Ejecutar servidor:
```bash
python manage.py runserver
```

Acceder a: http://127.0.0.1:8000/admin

---

## 2. Estructura de Carpetas

```
proyecto_academico/
│
├── proyecto_academico/          # Configuración principal
│   ├── settings.py              # ⚙️ Configuración (apps, BD, email)
│   └── urls.py                  # 🔗 URLs principales
│
├── proyectos/                   # 📁 App de proyectos (PERSONA 2)
│   ├── models.py                # Modelo Proyecto
│   ├── views.py                 # Vistas CBV (CRUD)
│   ├── forms.py                 # Formularios con crispy_forms
│   ├── urls.py                  # URLs del CRUD
│   ├── admin.py                 # Admin de Django
│   └── decorators.py            # Decoradores de permisos
│
├── usuarios/                    # 👤 App de autenticación (PERSONA 1)
│   ├── views.py                 # Login/Logout
│   ├── forms.py                 # Formularios de auth
│   └── urls.py                  # URLs de auth
│
├── comentarios/                 # 💬 App de comentarios (PERSONA 3)
│   ├── models.py                # Modelo Comentario
│   ├── views.py                 # Crear comentario + email
│   ├── forms.py                 # Formulario de comentario
│   └── urls.py                  # URLs de comentarios
│
├── templates/                   # 🎨 Plantillas HTML
│   ├── base/
│   │   └── base.html            # Template base
│   ├── proyectos/
│   │   ├── proyecto_list.html   # Lista de proyectos
│   │   ├── proyecto_form.html   # Formulario crear/editar
│   │   └── proyecto_detail.html # Detalle + comentarios
│   └── usuarios/
│       └── login.html           # Login
│
├── static/                      # 📦 Archivos estáticos
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
│
└── media/                       # 📤 Archivos subidos
    └── proyectos/               # PDFs de proyectos
```

---

## 3. Orden de Trabajo Recomendado

### ✅ PASO 1: PERSONA 1 - Autenticación (Día 1)
1. Implementar login/logout en `usuarios/views.py`
2. Crear formularios en `usuarios/forms.py`
3. Configurar URLs en `usuarios/urls.py`
4. Crear template `login.html`
5. Implementar decoradores en `proyectos/decorators.py`
6. Crear grupos "Estudiante" y "Docente"

**Entregable**: Sistema de login funcional + decoradores

---

### ✅ PASO 2: PERSONA 2 - CRUD Proyectos (Día 2)
1. Crear modelo `Proyecto` en `proyectos/models.py`
2. Hacer migraciones: `python manage.py makemigrations && python manage.py migrate`
3. Implementar vistas CBV en `proyectos/views.py`
4. Crear formularios en `proyectos/forms.py`
5. Configurar URLs en `proyectos/urls.py`
6. Crear templates en `templates/proyectos/`
7. Registrar en admin: `proyectos/admin.py`

**Entregable**: CRUD completo con permisos

---

### ✅ PASO 3: PERSONA 3 - Comentarios y Reportes (Día 3)
1. Crear modelo `Comentario` en `comentarios/models.py`
2. Hacer migraciones: `python manage.py makemigrations && python manage.py migrate`
3. Implementar vistas en `comentarios/views.py`
4. Configurar email en `settings.py`
5. Agregar exportación CSV en `proyectos/views.py`
6. Agregar exportación PDF en `proyectos/views.py`
7. Integrar comentarios en `proyecto_detail.html`

**Entregable**: Comentarios + notificaciones + reportes

---

## 4. Comandos Útiles

### Crear migraciones:
```bash
python manage.py makemigrations
```

### Aplicar migraciones:
```bash
python manage.py migrate
```

### Ejecutar servidor:
```bash
python manage.py runserver
```

### Crear superusuario:
```bash
python manage.py createsuperuser
```

### Acceder al shell de Django:
```bash
python manage.py shell
```

### Crear grupos desde el shell:
```python
from django.contrib.auth.models import Group
Group.objects.create(name='Estudiante')
Group.objects.create(name='Docente')
```

---

## 5. Checklist de Integración

Antes de entregar, verificar:

- [ ] Las 3 apps están en `INSTALLED_APPS` (settings.py)
- [ ] Las URLs están descomentadas en `proyecto_academico/urls.py`
- [ ] Todas las migraciones están aplicadas
- [ ] Existen grupos "Estudiante" y "Docente"
- [ ] Hay al menos 1 usuario de cada tipo
- [ ] El login funciona
- [ ] Se pueden crear proyectos
- [ ] Se pueden agregar comentarios
- [ ] Los emails se envían (o se muestran en consola)
- [ ] La exportación CSV funciona
- [ ] La exportación PDF funciona
- [ ] Los permisos funcionan correctamente

---

## 6. Solución de Problemas Comunes

### Error: "No module named 'crispy_forms'"
```bash
pip install django-crispy-forms crispy-bootstrap4
```

### Error: "Table doesn't exist"
```bash
python manage.py makemigrations
python manage.py migrate
```

### Error: "STATIC_ROOT"
Agregar en settings.py:
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### Los emails no se envían
En desarrollo, están configurados para mostrarse en consola. Revisar la terminal donde corre el servidor.

---

## 7. Datos de Prueba

### Crear usuarios manualmente:
```bash
python manage.py createsuperuser
```

### Desde el admin (http://127.0.0.1:8000/admin):
1. Crear 2 usuarios: `estudiante1` y `docente1`
2. Asignar al grupo correspondiente
3. Crear 2-3 proyectos de prueba
4. Agregar comentarios

---

## 📞 Contacto entre el Equipo

- **Persona 1**: Avisar cuando los decoradores estén listos
- **Persona 2**: Avisar cuando el modelo Proyecto esté migrado
- **Persona 3**: Coordinar con Persona 2 para integrar comentarios

**¡Éxito en el proyecto! 🎉**
