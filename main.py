from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
import cv2
import numpy as np
import shutil

app = FastAPI()

# Configurar carpetas
UPLOAD_FOLDER = Path("static/uploads")
OUTPUT_FOLDER = Path("static/processed")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Configurar Jinja2
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def apply_kodak_portra(image: Image.Image):
    """Simula Kodak Portra 400: Tonos cálidos, mejor contraste y menos saturación"""
    image = ImageEnhance.Color(image).enhance(1.1)  # Aumentar calidez
    image = ImageEnhance.Contrast(image).enhance(1.05)  # Suave aumento de contraste
    image = ImageEnhance.Brightness(image).enhance(1.05)  # Ligeramente más luminosa
    return image

def apply_fujifilm_pro(image: Image.Image):
    """Simula Fujifilm Pro 400H: Tonos fríos, tinte verdoso y aumento de saturación"""
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Aplicar corrección de color para tonos fríos con tinte verde
    lut = np.array([i * 0.9 if i > 100 else i for i in range(256)]).astype(np.uint8)
    image[:, :, 1] = cv2.LUT(image[:, :, 1], lut)  # Ajuste del canal verde
    image[:, :, 2] = cv2.LUT(image[:, :, 2], lut)  # Ajuste del canal azul
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    return Image.fromarray(image)

def apply_ilford_hp5(image: Image.Image):
    """Simula Ilford HP5 Plus 400: Blanco y negro con tonos suaves y amplio rango dinámico"""
    image = ImageOps.grayscale(image)
    image = ImageEnhance.Contrast(image).enhance(1.2)  # Ajustar el contraste
    return image

def apply_kodak_trix(image: Image.Image):
    """Simula Kodak Tri-X 400: Blanco y negro con alto contraste y grano fuerte"""
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Aumentar contraste
    image = cv2.equalizeHist(image)

    # Simular grano añadiendo ruido gaussiano
    noise = np.random.normal(0, 1, image.shape).astype(np.uint8)
    image = cv2.add(image, noise)

    return Image.fromarray(image)

def create_thumbnail(image: Image.Image, size=(800, 600)):
    """Genera una miniatura de la imagen con el tamaño dado."""
    image.thumbnail(size)
    return image

@app.get("/", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process/")
async def process_image(file: UploadFile = File(...)):
    """Recibe una imagen, aplica los filtros y guarda las versiones procesadas."""
    img_path = UPLOAD_FOLDER / file.filename
    with img_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image = Image.open(img_path).convert("RGB")

    filters = {
        "kodak_portra.jpg": apply_kodak_portra(image),
        "fujifilm_pro.jpg": apply_fujifilm_pro(image),
        "ilford_hp5.jpg": apply_ilford_hp5(image),
        "kodak_trix.jpg": apply_kodak_trix(image),
    }

    processed_paths = []
    for name, img in filters.items():
        # Crear miniatura de cada imagen procesada
        thumbnail = create_thumbnail(img)
        thumbnail_name = f"thumb_{name}"
        thumbnail_path = OUTPUT_FOLDER / thumbnail_name
        thumbnail.save(thumbnail_path)
        processed_paths.append(f"/static/processed/{thumbnail_name}")

    return {"images": processed_paths}
