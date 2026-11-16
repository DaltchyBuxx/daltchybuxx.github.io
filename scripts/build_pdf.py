#!/usr/bin/env python3
"""Gera o PDF dos termos com LibreOffice instalado no sistema."""
from pathlib import Path
from html import escape
import subprocess
import tempfile

from build import ROOT, DATE, EFFECTIVE_DATE, VERSION, render_markdown, full_terms


def build_pdf():
    content, _ = render_markdown(full_terms())
    with tempfile.TemporaryDirectory(prefix='daltchy-pdf-') as directory:
        temp = Path(directory)
        html = temp / 'termos.html'
        html.write_text('''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<style>@page{size:A4;margin:20mm}body{font-family:"Liberation Sans",Arial,sans-serif;font-size:11pt;color:#292326;line-height:1.5}h1{font-size:26pt;color:#a50810}h2{font-size:15pt;color:#a50810;page-break-after:avoid}h3{font-size:12pt;page-break-after:avoid}p,li{orphans:3;widows:3}a{color:#8c161c}li{margin-bottom:6pt}.meta{color:#686469;font-size:10pt}</style>
</head><body><p><b>DALTCHYBUXX</b> / DOCUMENTOS DA LOJA</p>
<h1>Termos de Uso e Condições Gerais</h1><p class="meta">Versão ''' + escape(VERSION) + ' · Atualização: ' + escape(DATE) + ' · Vigência: ' + escape(EFFECTIVE_DATE) + '</p><hr>' + content + '</body></html>')
        subprocess.run(['libreoffice', '-env:UserInstallation=' + (temp / 'profile').as_uri(), '--headless', '--convert-to', 'pdf:writer_pdf_Export', '--outdir', str(temp), str(html)], check=True, timeout=120)
        pdf = temp / 'termos.pdf'
        data = pdf.read_bytes()
        if not data.startswith(b'%PDF-'):
            raise ValueError('PDF inválido')
        (ROOT / 'documentos/termos.pdf').write_bytes(data)


if __name__ == '__main__':
    build_pdf()
