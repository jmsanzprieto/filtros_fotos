# Filtros Analógicos para Imágenes

Este proyecto utiliza FastAPI para crear una API web que aplica filtros fotográficos analógicos a imágenes subidas por el usuario. Los filtros incluyen simulaciones de los famosos filmes fotográficos: Kodak Portra 400, Fujifilm Pro 400H, Ilford HP5 Plus 400 y Kodak Tri-X 400.

## Requisitos

- Python 3.7 o superior
- FastAPI
- Uvicorn
- Pillow (PIL Fork)
- OpenCV
- jQuery
- Bootstrap

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local.

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/filtros-analogicos.git
   cd filtros-analogicos
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scriptsctivate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecutar la aplicación

Para ejecutar la aplicación localmente, usa Uvicorn:

```bash
uvicorn main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000`.

### Subir una imagen y aplicar los filtros

1. Accede a la página principal de la aplicación en `http://127.0.0.1:8000`.
2. Sube una imagen usando el formulario de carga.
3. Una vez cargada la imagen, se aplicarán automáticamente los filtros y se mostrarán las versiones procesadas.

### Filtros disponibles

- **Kodak Portra 400**: Simula tonos cálidos, un buen contraste y una ligera mejora en el brillo.
- **Fujifilm Pro 400H**: Simula tonos fríos con un tinte verdoso y un aumento de la saturación.
- **Ilford HP5 Plus 400**: Simula una imagen en blanco y negro con un amplio rango dinámico.
- **Kodak Tri-X 400**: Simula una imagen en blanco y negro con alto contraste y un grano fuerte.

## Estructura del Proyecto

```
filtros-analogicos/
│
├── static/
│   ├── uploads/         # Carpeta donde se almacenan las imágenes subidas
│   └── processed/       # Carpeta donde se almacenan las imágenes procesadas
│
├── templates/           # Carpeta donde se encuentran las plantillas HTML
│   └── index.html       # Página principal de carga de imágenes
│
├── main.py              # Código fuente de la aplicación FastAPI
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Este archivo
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto

- Autor: https://github.com/jmsanzprieto/
