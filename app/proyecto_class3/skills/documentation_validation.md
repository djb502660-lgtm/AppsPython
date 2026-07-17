# SKILL: Documentation Validation

## Objetivo
Asegurar que todas las especificaciones (SPECS) creadas cumplan con los estándares definidos en la metodología "Spec as Skill" antes de solicitar aprobación y pasar a codificación.

## Entradas
- Archivo Markdown (`.md`) de la especificación a validar.
- Archivo `Promtps_master.md` con las reglas obligatorias.

## Reglas
1. La especificación debe estar en la carpeta `/spec`.
2. El nombre del archivo debe ser descriptivo y en minúsculas.
3. El documento debe contener secciones claras y estar formateado en Markdown.

## Checklist
- [ ] ¿El documento describe claramente el "Qué" y el "Por qué"?
- [ ] ¿Están definidos los requisitos funcionales y no funcionales?
- [ ] ¿Si aplica, se incluyen diagramas (Mermaid)?
- [ ] ¿No se incluye código de implementación (solo diseño)?

## Validaciones
- **Automática:** Análisis sintáctico del Markdown.
- **Manual:** Revisión por pares o por el "Technical Writer".

## Resultado Esperado
Un reporte indicando `PASS` si cumple todos los criterios, o una lista de correcciones necesarias. Solo los que obtengan `PASS` pueden ser presentados para aprobación.
