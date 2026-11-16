#!/usr/bin/env python3
"""Gera e valida um pacote publicável; não publica resultados incompletos."""
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

from build import build
from build_pdf import build_pdf
from settings import ROOT, VERSION, DATE, EFFECTIVE_DATE, full_terms, privacy_text


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])


def main():
    build()
    build_pdf()
    dist = ROOT / 'dist'
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir()
    for directory in ('assets', 'termos', 'privacidade'):
        shutil.copytree(ROOT / directory, dist / directory)
    for name in ('index.html', '.nojekyll'):
        shutil.copy2(ROOT / name, dist / name)
    documents = dist / 'documentos'
    documents.mkdir()
    shutil.copy2(ROOT / 'documentos/termos.pdf', documents / 'termos.pdf')
    header = f'# DaltchyBuxx — Termos de Uso\n\nVersão {VERSION}\nAtualização: {DATE}\nVigência: {EFFECTIVE_DATE}\n\n'
    (documents / 'termos.md').write_text(header + full_terms(), encoding='utf-8')
    (documents / 'privacidade.md').write_text(privacy_text(), encoding='utf-8')
    for file in dist.rglob('*.html'):
        page = Links()
        page.feed(file.read_text(encoding='utf-8'))
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = ((dist if parsed.path.startswith('/') else file.parent) / unquote(parsed.path).lstrip('/')).resolve() if parsed.path else file
            if not target.is_relative_to(dist):
                raise ValueError(f'Link fora do site: {link}')
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                raise ValueError(f'Link quebrado em {file}: {link}')
            if parsed.fragment and target.suffix == '.html':
                destination = Links()
                destination.feed(target.read_text(encoding='utf-8'))
                if unquote(parsed.fragment) not in destination.ids:
                    raise ValueError(f'Âncora inexistente em {file}: {link}')
    subprocess.run(['pdfinfo', str(documents / 'termos.pdf')], check=True, stdout=subprocess.DEVNULL)
    print(f'Site e PDF validados: versão {VERSION}, vigência {EFFECTIVE_DATE}')


if __name__ == '__main__':
    main()
