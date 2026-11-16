#!/usr/bin/env python3
"""Gera páginas estáticas dos termos revisados, sem dependências externas."""

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DISCORD = 'https://discord.gg/5mzW2VyNDD'
BASE = ''
DATE = '16/11/2026'
EFFECTIVE_DATE = '23/11/2026'
VERSION = '2.1.0'
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
    toc_parts = []
    index = 0
    while index < len(entries):
        anchor, label, level = entries[index]
        children = []
        index += 1
        while index < len(entries) and entries[index][2] > level:
            child_anchor, child_label, _ = entries[index]
            children.append(f'<li><a href="#{child_anchor}">{escape(child_label)}</a></li>')
            index += 1
        link = f'<a href="#{anchor}">{escape(label)}</a>'
        if children:
            toc_parts.append('<li class="toc-group">' + link + '<details><summary>Ver subseções de privacidade</summary><ol>' + ''.join(children) + '</ol></details></li>')
        else:
            toc_parts.append(f'<li>{link}</li>')
    toc = ''.join(toc_parts)
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
  <link rel="stylesheet" href="{asset}style.css?v=8">
  <script src="{asset}document-nav.js?v=1" defer></script>
  <link rel="canonical" href="https://daltchybuxx.github.io{BASE}/{canonical_path}">
</head>
<body>
  <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
  <header class="site-header"><div class="header-inner">
    <a class="brand" href="{home}" aria-label="DaltchyBuxx — início"><img src="{asset}favicon.svg" alt="" width="44" height="44"><span>DALTCHY<strong>BUXX</strong><small>DOCUMENTOS DA LOJA</small></span></a>
    <nav aria-label="Navegação principal">{links}<a class="support-link" href="{DISCORD}">Suporte <span aria-hidden="true">↗</span></a></nav>
  </div></header>
  {body}
  <footer class="site-footer"><div class="footer-inner">
    <div class="footer-brand"><strong>DALTCHYBUXX <span>LOJA OFICIAL</span></strong><p>Robux, Gamepasses e atendimento pelo Discord.<br>Consulte as informações da loja antes de comprar.</p></div>
    <div><h2>Comunidade</h2><p>Novidades e atendimento no servidor oficial.</p><a href="{DISCORD}">Canal oficial no Discord ↗</a></div>
    <nav aria-label="Navegação do rodapé"><h2>Navegação</h2><a href="{home}">Página inicial</a><a href="{home}termos/">Termos de Uso</a><a href="{home}privacidade/">Política de Privacidade</a></nav>
    <p class="footer-bottom">DaltchyBuxx · Termos e privacidade <span>Versão {VERSION} · Vigência: {EFFECTIVE_DATE}</span></p>
  </div></footer>
</body>
</html>
'''


def document(title, kind, source, intro):
    content, toc = render_markdown(source, privacy=kind == 'privacy')
    terms_path = './' if kind == 'terms' else '../termos/'
    shortcuts = ''.join(f'<a href="{terms_path}#{anchor}">{label}</a>' for anchor, label in [
        ('secao-4', 'Entrega'), ('secao-8', 'Reembolso'),
        ('secao-12', 'Excluir dados'), ('secao-11-11', 'Transferir conta')])
    article = f'''<main id="conteudo" class="document-shell">
    <div class="document-heading"><p class="eyebrow">DOCUMENTOS DA LOJA</p><h1>{title}</h1>
      <p class="intro">{intro}</p>
      <dl class="document-meta"><div><dt>Versão</dt><dd>{VERSION}</dd></div><div><dt>Última atualização</dt><dd>{DATE}</dd></div><div><dt>Vigência</dt><dd>{EFFECTIVE_DATE}</dd></div></dl>
    </div>
    <div class="document-grid"><aside class="toc"><details class="toc-disclosure" open><summary>Navegar pelo documento</summary><nav class="quick-links" aria-label="Acesso rápido">{shortcuts}</nav><nav class="toc-list" aria-label="Índice do documento"><ol>{toc}</ol></nav></details></aside>
      <article class="document-body" aria-label="{title}">{content}
        <div class="document-end"><a href="#conteudo">Voltar ao início ↑</a><a href="../documentos/termos.pdf" download>Baixar termos completos (.pdf)</a></div>
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
  <section class="home-intro" aria-labelledby="home-title">
    <p class="hero-badge"><span aria-hidden="true">●</span> EXPERIÊNCIA DALTCHYBUXX</p>
    <h1 id="home-title">Mais clareza.<br><span>Mais confiança.</span></h1>
    <p class="hero-description">Tudo o que você precisa saber sobre suas compras,<br class="desktop-break"> seus dados e o atendimento na DaltchyBuxx.</p>
    <div class="hero-actions"><a class="primary-button" href="#documentos">Explorar os documentos <span aria-hidden="true">↓</span></a><a class="text-button" href="{DISCORD}">Conhecer a comunidade <span aria-hidden="true">↗</span></a></div>
    <div class="hero-bottom"><span>Robux e Gamepasses · Atendimento pelo Discord</span><a href="{DISCORD}" class="community-pill"><span aria-hidden="true">●</span> COMUNIDADE NO DISCORD</a></div>
  </section>
  <section class="documents-section" id="documentos" aria-labelledby="documents-title"><div class="section-inner">
    <div class="section-heading"><div><p class="eyebrow">TUDO EXPLICADO</p><h2 id="documents-title">Antes da sua próxima compra.</h2><p>Consulte as condições da loja e saiba como seus dados são utilizados.</p></div><span class="updated">Versão {VERSION} · {DATE}</span></div>
    <div class="document-cards">
      <a class="document-card terms-card" href="./termos/"><div class="card-top"><span class="card-number">01 / COMO FUNCIONA</span><span class="card-arrow" aria-hidden="true">↗</span></div><h3>Regras e Entregas</h3><p>Entenda como funcionam os pedidos de Robux e Gamepasses, os prazos e as condições antes e depois de comprar.</p><ul class="card-points"><li>Condições de compra e entrega</li><li>Cancelamentos e atendimento</li><li>Direitos e responsabilidades</li></ul><span class="card-bottom"><span class="card-link">Ler os Termos de Uso <span aria-hidden="true">→</span></span><span class="card-format">Documento completo</span></span></a>
      <a class="document-card privacy-card" href="./privacidade/"><div class="card-top"><span class="card-number">02 / SEUS DADOS</span><span class="card-arrow" aria-hidden="true">↗</span></div><h3>Privacidade e Dados</h3><p>Conheça as informações utilizadas no atendimento, as finalidades do tratamento e os procedimentos para solicitar exclusão.</p><ul class="card-points"><li>Dados utilizados e suas finalidades</li><li>Conservação das informações</li><li>Solicitações e direitos dos clientes</li></ul><span class="card-bottom"><span class="card-link">Ler a Política de Privacidade <span aria-hidden="true">→</span></span><span class="card-format">Documento completo</span></span></a>
    </div>
  </div></section>
  <section class="resource-section" aria-label="Acesso às informações"><div class="resource-card"><span class="eyebrow">PARA CONSULTAR</span><h2>Em um só lugar.</h2><p>Termos e privacidade organizados por assunto, com índice para facilitar a leitura.</p></div><a class="resource-card" href="./documentos/termos.pdf" download><span class="eyebrow">PARA GUARDAR</span><h2>Também em PDF. <span aria-hidden="true">↓</span></h2><p>Baixe os termos completos para consultar quando precisar.</p></a><div class="resource-card"><span class="eyebrow">PARA CONVERSAR</span><h2>Suporte no Discord.</h2><p>Entre no servidor oficial e acesse o canal de suporte para falar com a equipe.</p></div></section>
  <section class="contact-block"><div><p class="eyebrow">COMUNIDADE OFICIAL</p><h2>Faça parte da nossa<br class="desktop-break"> comunidade.</h2><p>Acompanhe as novidades, tire suas dúvidas e encontre o atendimento da DaltchyBuxx no nosso servidor.</p></div><a class="contact-button" href="{DISCORD}">Entrar no Discord <span aria-hidden="true">↗</span></a></section>
</main>
'''
    (ROOT / 'index.html').write_text(page('Termos e privacidade', 'home', home,
        description='Termos de Uso e Política de Privacidade da DaltchyBuxx. Consulte condições de compra e informações sobre seus dados.'))
    (ROOT / '.nojekyll').write_text('')


if __name__ == '__main__':
    build()
