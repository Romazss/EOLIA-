# Informe EOLIA - Estructura LaTeX Modular

Este directorio contiene la estructura modular en LaTeX para la preparación del informe completo del proyecto EOLIA.

## Estructura de Directorios

```
informe_latex/
├── main.tex                 # Archivo principal (compila todo)
├── referencias.bib          # Base de datos bibliográfica
├── README.md                # Este archivo
├── capitulos/               # Capítulos principales del informe
│   ├── 01_introduccion.tex
│   ├── 02_antecedentes.tex
│   ├── 03_propuesta_valor.tex
│   ├── 04_modelo_negocio.tex
│   ├── 05_investigacion_mercado.tex
│   ├── 06_plan_implementacion.tex
│   ├── 07_equipo.tex
│   └── 08_conclusiones.tex
├── secciones/               # Secciones especiales (portada, anexos)
│   ├── 01_portada.tex
│   └── anexo_a.tex
├── estilos/                 # Archivos de estilos personalizados
│   └── estilos.tex
└── imagenes/                # Directorio para imágenes (vacío inicialmente)
    └── (agregar imágenes aquí)
```

## Cómo Compilar

### Requisitos
- TeX Live o MiKTeX instalado
- Un editor de LaTeX (TeXstudio, VSCode con LaTeX Workshop, etc.)

### Compilación desde línea de comandos

```bash
# Compilar a PDF
pdflatex main.tex

# Incluir referencias bibliográficas
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Compilación con LaTeX Workshop en VSCode
1. Abre `main.tex`
2. Presiona `Ctrl+Alt+B` para compilar
3. El PDF aparecerá automáticamente en el visor

## Modularidad y Estructura

Cada capítulo está en un archivo separado para facilitar:
- ✅ Edición simultánea de múltiples secciones
- ✅ Control de versiones más eficiente
- ✅ Reutilización de contenido
- ✅ Mantenimiento simplificado

## Personalización

### Cambiar Colores
Edita `estilos/estilos.tex` y modifica los valores RGB de:
- `colorPrincipal` - Color principal de títulos
- `colorSecundario` - Color secundario
- `colorAcento` - Color de énfasis
- `colorTítulo` - Color de subtítulos
- `colorTexto` - Color del texto general

### Agregar Imágenes
1. Coloca las imágenes en la carpeta `imagenes/`
2. En el archivo .tex donde las necesites, usa:
   ```latex
   \includegraphics[width=0.8\textwidth]{imagenes/nombre_imagen.png}
   ```

### Agregar Referencias
1. Edita `referencias.bib` con tus fuentes
2. En el .tex, usa: `\cite{clave_referencia}`
3. Las referencias se compilarán automáticamente

## Comandos Personalizados

En `estilos/estilos.tex` se han definido comandos útiles:

```latex
\destacado{texto}           % Texto en color naranja y bold
\importante{texto}          % Texto en color azul y bold
\definicion{título}{contenido}  % Cuadro de definición

% Ejemplos:
\destacado{Esto es importante}
\importante{Esto también}
\definicion{Mi Término}{Aquí va la definición}
```

## Edición de Contenido

### Para editar un capítulo:
1. Abre el archivo correspondiente en `capitulos/`
2. Reemplaza el contenido de ejemplo con tu contenido
3. Guarda el archivo
4. Recompila `main.tex`

### Para agregar un nuevo capítulo:
1. Crea un archivo `capitulos/09_nuevo_capitulo.tex`
2. Agrega en `main.tex`:
   ```latex
   \input{capitulos/09_nuevo_capitulo.tex}
   ```

## Formato y Estilos

- **Fuente**: Sans-serif
- **Tamaño base**: 12pt
- **Papel**: A4
- **Márgenes**: 2.5cm
- **Idioma**: Español

## Notas Importantes

- El archivo `main.tex` es el punto de entrada. No edites directamente capitulos sin actualizar `main.tex`
- Los títulos de secciones se formatean automáticamente según los estilos definidos
- Las imágenes deben estar en formato .png, .jpg o .pdf para mejor compatibilidad
- Las referencias se gestionan a través de BibTeX

## Solución de Problemas

### Si la compilación falla:
1. Verifica que todos los archivos `.tex` estén en su lugar
2. Revisa que no falten caracteres especiales sin escape
3. Asegúrate de que los nombres de archivos no tengan espacios

### Si las referencias no aparecen:
1. Ejecuta: `bibtex main`
2. Luego compila dos veces: `pdflatex main.tex`

## Autor
Proyecto EOLIA - Ciclo de Ideación

## Última Actualización
Diciembre 2024
