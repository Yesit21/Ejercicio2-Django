# División del Trabajo - 3 Personas

## 👤 PERSONA 1: Autenticación y Usuarios (1.5 pts)

### Responsabilidades:
- **App**: `usuarios/`
- **Archivos a trabajar**:
  - `usuarios/views.py` - Vistas de login/logout
  - `usuarios/forms.py` - Formularios de autenticación
  - `usuarios/urls.py` - URLs de autenticación
  - `templates/usuarios/login.html` - Template de login
  - `templates/base/base.html` - Navbar con menú según rol

### Tareas específicas:
1. ✅ Implementar sistema de login/logout
2. ✅ Crear grupos "Estudiante" y "Docente"
3. ✅ Implementar decoradores en `proyectos/decorators.py`:
   - `@estudiante_required`
   - `@docente_required`
4. ✅ Configurar permisos por grupo
5. ✅ Crear comando de management para crear grupos automáticamente
6. ✅ Template de login con crispy_forms
7. ✅ Navbar dinámico según usuario autenticado

### Entregables:
- Sistema de autenticación funcional
- Decoradores de permisos
- Templates de login/logout
- Documentación de cómo crear usuarios de prueba

---

## 👤 PERSONA 2: Gestión de Proyectos (1.5 pts)

### Responsabilidades:
- **App**: `proyectos/`
- **Archivos a trabajar**:
  - `proyectos/models.py` - Modelo Proyecto
  - `proyectos/views.py` - Vistas CBV (CRUD)
  - `proyectos/forms.py` - Formularios con crispy_forms
  - `proyectos/urls.py` - URLs del CRUD
  - `proyectos/admin.py` - Configuración del admin
  - `templates/proyectos/` - Todos los templates

### Tareas específicas:
1. ✅ Crear modelo `Proyecto` con todos los campos especificados
2. ✅ Implementar vistas basadas en clases:
   - `ProyectoListView` (con filtros por estado y estudiante)
   - `ProyectoCreateView` (solo estudiantes)
   - `ProyectoUpdateView` (estudiantes: sus proyectos, docentes: estado/calificación)
   - `ProyectoDeleteView` (solo estudiantes, solo sus proyectos)
   - `ProyectoDetailView`
3. ✅ Formularios con crispy_forms:
   - `ProyectoForm` (para estudiantes)
   - `ProyectoRevisionForm` (para docentes - solo estado y calificación)
4. ✅ Validaciones:
   - Estudiante solo puede editar/eliminar sus proyectos
   - Docente puede cambiar estado y calificación
5. ✅ Templates con Bootstrap/crispy_forms
6. ✅ Registrar modelo en admin

### Entregables:
- Modelo Proyecto completo
- CRUD funcional con permisos
- Formularios con crispy_forms
- Templates responsivos
- Filtros funcionales

---

## 👤 PERSONA 3: Comentarios y Reportes (2.0 pts)

### Responsabilidades:
- **App**: `comentarios/`
- **Archivos a trabajar**:
  - `comentarios/models.py` - Modelo Comentario
  - `comentarios/views.py` - Vistas de comentarios
  - `comentarios/forms.py` - Formulario de comentario
  - `comentarios/urls.py` - URLs de comentarios
  - `proyectos/views.py` - Agregar exportación CSV/PDF
  - `proyecto_academico/settings.py` - Configurar email

### Tareas específicas:
1. ✅ Crear modelo `Comentario`:
   - proyecto (FK a Proyecto)
   - usuario (FK a User)
   - texto (TextField)
   - fecha_creacion (DateTimeField)
2. ✅ Implementar sistema de comentarios:
   - Vista para crear comentario
   - Validación: no permitir comentarios si proyecto está "Aprobado"
   - Enviar email al estudiante cuando se crea un comentario
3. ✅ Configurar envío de emails en `settings.py`
4. ✅ Implementar exportación a CSV:
   - Vista `exportar_proyectos_csv`
   - Incluir todos los campos del proyecto
5. ✅ Implementar exportación a PDF:
   - Vista `exportar_proyectos_pdf`
   - Usar ReportLab
   - Diseño profesional con tabla
6. ✅ Integrar comentarios en `proyecto_detail.html`
7. ✅ Agregar botones de exportación en `proyecto_list.html`

### Entregables:
- Sistema de comentarios funcional
- Notificaciones por email
- Exportación CSV funcional
- Exportación PDF funcional
- Bloqueo de comentarios en proyectos aprobados

---

## 📋 Coordinación entre Personas

### Dependencias:
1. **Persona 1** debe terminar primero:
   - Los decoradores son necesarios para Persona 2
   - El sistema de autenticación es base para todos

2. **Persona 2** puede trabajar en paralelo después de Persona 1:
   - Necesita los decoradores de permisos
   - Debe dejar el modelo Proyecto listo para Persona 3

3. **Persona 3** necesita:
   - Modelo Proyecto de Persona 2
   - Sistema de autenticación de Persona 1

### Reuniones de coordinación:
- **Día 1**: Persona 1 completa autenticación
- **Día 2**: Persona 2 completa CRUD, Persona 3 inicia comentarios
- **Día 3**: Persona 3 completa reportes, todos integran y prueban

---

## 🧪 Testing Conjunto

Cada persona debe probar:
1. Sus propias funcionalidades
2. La integración con las otras partes
3. Los permisos y roles

### Casos de prueba mínimos:
- ✅ Login como estudiante y docente
- ✅ Estudiante crea proyecto
- ✅ Docente revisa y comenta proyecto
- ✅ Email de notificación se envía
- ✅ Docente aprueba proyecto
- ✅ No se pueden agregar más comentarios
- ✅ Exportar a CSV y PDF funciona
- ✅ Filtros funcionan correctamente

---

## 📦 Entrega Final

### Checklist:
- [ ] Todas las funcionalidades implementadas
- [ ] Migraciones aplicadas
- [ ] Superusuario creado
- [ ] Grupos "Estudiante" y "Docente" creados
- [ ] Al menos 2 usuarios de prueba (1 estudiante, 1 docente)
- [ ] 3 proyectos de ejemplo en diferentes estados
- [ ] README.md actualizado con instrucciones
- [ ] requirements.txt completo
- [ ] Código comentado y limpio
- [ ] Git con commits descriptivos por persona

### Comando para crear datos de prueba:
```bash
python manage.py crear_datos_prueba
```
(Persona 1 puede crear este comando de management)
