#!/usr/bin/env python3
"""Gera páginas estáticas dos termos revisados, sem dependências externas."""

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DISCORD = 'https://discord.gg/5mzW2VyNDD'
BASE = '/daltchybuxx-web'
DATE = '13/11/2026'
VERSION = '2.0.0'
TOKEN = re.compile(r'(\*\*.+?\*\*|\[[^\]]+\]\(https?://[^)]+\))')


def inline(text):
    result = []
    for part in TOKEN.split(text):
        if part.startswith('**') and part.endswith('**'):
            result.append('<strong>' + escape(part[2:-2]) + '</strong>')
        elif match := re.fullmatch(r'\[([^\]]+)\]\((https?://[^)]+)\)', part):
            result.append(f'<a href="{escape(match[2], quote=True)}">{escape(match[1])}</a>')
        else:
            result.append(escape(part))
    rendered = ''.join(result)
    return re.sub(r'\bseção (\d+(?:\.\d+)?)', lambda m: f'<a href="#secao-{m[1].replace(".", "-")}">{m[0]}</a>', rendered)


def render_markdown(source, *, privacy=False):
    blocks, paragraphs, entries = [], [], []
    in_list = False

    def flush():
        if paragraphs:
            blocks.append('<p>' + inline(' '.join(paragraphs)) + '</p>')
            paragraphs.clear()

    for raw in source.splitlines() + ['']:
        line = raw.strip()
        if not line:
            flush()
            if in_list:
                blocks.append('</ul>')
                in_list = False
            continue
        if line.startswith('#'):
            flush()
            if in_list:
                blocks.append('</ul>')
                in_list = False
            match = re.fullmatch(r'(#{2,3})\s+((\d+(?:\.\d+)*))\.\s+(.+)', line)
            if not match:
                raise ValueError(f'Título não reconhecido: {line}')
            number, title = match[2], match[4]
            anchor = 'secao-' + number.replace('.', '-')
            level = 2 if privacy or match[1] == '##' else 3
            label = title if privacy else f'{number}. {title}'
            entries.append((anchor, label, level))
            blocks.append(f'<h{level} id="{anchor}">{escape(label)}</h{level}>')
        elif line.startswith('- '):
            flush()
            if not in_list:
                blocks.append('<ul>')
                in_list = True
            blocks.append('<li>' + inline(line[2:]) + '</li>')
        else:
            paragraphs.append(line)
    toc = ''.join(
        f'<li class="toc-level-{level}"><a href="#{anchor}">{escape(label)}</a></li>'
        for anchor, label, level in entries
    )
    return '\n'.join(blocks), toc


def page(title, active, body, *, description, canonical_path=''):
    links = ''.join(
        f'<a href="{href}"' + (' aria-current="page"' if key == active else '') + f'>{label}</a>'
        for key, href, label in [('home', './' if active == 'home' else '../', 'Início'),
                                 ('terms', './termos/' if active == 'home' else '../termos/', 'Termos'),
                                 ('privacy', './privacidade/' if active == 'home' else '../privacidade/', 'Privacidade')]
    )
    asset = './assets/' if active == 'home' else '../assets/'
    home = './' if active == 'home' else '../'
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="theme-color" content="#a50810">
  <title>{escape(title)} · DaltchyBuxx</title>
  <link rel="icon" href="{asset}favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{asset}style.css">
  <link rel="canonical" href="https://daltchybuxx.github.io{BASE}/{canonical_path}">
</head>
<body>
  <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
  <header class="site-header"><div class="header-inner">
    <a class="brand" href="{home}">DALTCHY<span>BUXX</span><span class="brand-dot" aria-hidden="true">.</span></a>
    <nav aria-label="Navegação principal">{links}<a class="support-link" href="{DISCORD}">Suporte <span aria-hidden="true">↗</span></a></nav>
  </div></header>
  {body}
  <footer class="site-footer"><div class="footer-inner"><p><strong>DaltchyBuxx</strong> · Termos e privacidade</p>
    <p>Para atendimento, entre no <a href="{DISCORD}">Discord oficial</a> e acesse o canal de suporte.</p>
  </div></footer>
</body>
</html>
'''


def document(title, kind, source, intro):
    content, toc = render_markdown(source, privacy=kind == 'privacy')
    article = f'''<main id="conteudo" class="document-shell">
    <div class="document-heading"><p class="eyebrow">DOCUMENTOS DA LOJA</p><h1>{title}</h1>
      <p class="intro">{intro}</p>
      <dl class="document-meta"><div><dt>Versão</dt><dd>{VERSION}</dd></div><div><dt>Última atualização</dt><dd>{DATE}</dd></div><div><dt>Vigência</dt><dd>{DATE}</dd></div></dl>
    </div>
    <div class="document-grid"><aside class="toc"><details open><summary>Neste documento</summary><nav aria-label="Índice do documento"><ol>{toc}</ol></nav></details></aside>
      <article class="document-body" aria-label="{title}">{content}
        <div class="document-end"><a href="#conteudo">Voltar ao início ↑</a><a href="../documentos/termos.md">Baixar texto completo (.md)</a></div>
      </article>
    </div>
  </main>'''
    directory = ROOT / ('privacidade' if kind == 'privacy' else 'termos')
    directory.mkdir(exist_ok=True)
    (directory / 'index.html').write_text(page(title, kind, article, description=intro, canonical_path=directory.name + '/'))


def build():
    source = (ROOT / 'documentos/termos.md').read_text()
    terms = source[source.index('## 1. '):]
    privacy = source[source.index('### 11.1.'):source.index('## 13. ')]
    document('Termos de Uso e Condições Gerais', 'terms', terms,
             'Conheça as condições de compra, entrega, atendimento e uso dos serviços da DaltchyBuxx.')
    document('Política de Privacidade', 'privacy', privacy,
             'Saiba quais dados dos clientes são utilizados, como são conservados e como solicitar sua exclusão.')
    home = f'''<main id="conteudo" class="home-shell">
    <section class="home-intro"><p class="eyebrow">DALTCHYBUXX</p><h1>Termos e privacidade.</h1>
      <p>As informações sobre suas compras, seus dados e o atendimento da loja, em um só lugar.</p>
    </section>
    <section class="document-cards" aria-label="Documentos disponíveis">
      <a class="document-card" href="./termos/"><span class="card-number" aria-hidden="true">01</span><h2>Termos de Uso</h2><p>Compras, entrega de produtos, prazos, cancelamentos e atendimento.</p><span class="card-link">Ler os termos <span aria-hidden="true">↗</span></span></a>
      <a class="document-card" href="./privacidade/"><span class="card-number" aria-hidden="true">02</span><h2>Política de Privacidade</h2><p>Coleta, utilização, conservação e exclusão dos dados dos clientes.</p><span class="card-link">Ler a política <span aria-hidden="true">↗</span></span></a>
    </section>
    <section class="contact-block"><h2>Precisa de atendimento?</h2><p>Entre no servidor oficial do Discord, acesse o <strong>canal de suporte</strong> e inicie um atendimento.</p><a class="contact-button" href="{DISCORD}">Entrar no Discord <span aria-hidden="true">↗</span></a></section>
    <p class="home-meta">Versão {VERSION} · Vigência a partir de {DATE}</p>
  </main>'''
    (ROOT / 'index.html').write_text(page('Termos e privacidade', 'home', home,
        description='Termos de Uso e Política de Privacidade da DaltchyBuxx. Consulte condições de compra e informações sobre seus dados.'))
    (ROOT / '.nojekyll').write_text('')


if __name__ == '__main__':
    build()
