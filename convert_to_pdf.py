#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para convertir archivos Markdown a PDF
Convierte el portafolio de productos de EOLIA a formato PDF
"""

from markdown_pdf import MarkdownPdf, Section
import os

def convert_markdown_to_pdf(input_file, output_file):
    """
    Convierte un archivo Markdown a PDF
    
    Args:
        input_file: Ruta al archivo Markdown
        output_file: Ruta al archivo PDF de salida
    """
    try:
        # Crear instancia de MarkdownPdf
        pdf = MarkdownPdf()
        
        # Agregar el archivo Markdown
        pdf.add_section(Section(input_file))
        
        # Guardar como PDF
        pdf.save(output_file)
        
        print(f"✅ PDF creado exitosamente: {output_file}")
        print(f"📄 Tamaño: {os.path.getsize(output_file) / 1024:.2f} KB")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al convertir: {str(e)}")
        return False

if __name__ == "__main__":
    # Rutas de archivos
    input_file = r"docs\portafolio-productos-cotizacion.md"
    output_file = r"docs\portafolio-productos-cotizacion.pdf"
    
    print("🚀 Iniciando conversión de Markdown a PDF...")
    print(f"📂 Archivo entrada: {input_file}")
    print(f"📄 Archivo salida: {output_file}")
    print("-" * 60)
    
    # Verificar que el archivo existe
    if not os.path.exists(input_file):
        print(f"❌ Error: El archivo {input_file} no existe")
    else:
        # Convertir
        success = convert_markdown_to_pdf(input_file, output_file)
        
        if success:
            print("-" * 60)
            print("✨ Conversión completada con éxito!")
            print(f"📍 Ubicación: {os.path.abspath(output_file)}")
