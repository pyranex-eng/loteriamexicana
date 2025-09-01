import fitz  # PyMuPDF

# Pedir el nombre del PDF
pdf_name = input("Escribe el nombre de tu PDF (ej: archivo.pdf): ")

# Abrir el PDF
pdf = fitz.open(pdf_name)

# Extraer imágenes de cada página
for num, page in enumerate(pdf, start=1):
    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = pdf.extract_image(xref)
        image_bytes = base_image["image"]
        ext = base_image["ext"]
        with open(f"pagina{num}_img{img_index}.{ext}", "wb") as f:
            f.write(image_bytes)

print("✅ Imágenes extraídas con éxito")
