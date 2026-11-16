"""Configuração única e composição dos documentos."""
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'config.json').read_text(encoding='utf-8'))
for key in ('discord_url', 'version', 'updated_at', 'effective_at'):
    if not isinstance(CONFIG.get(key), str) or not CONFIG[key].strip():
        raise ValueError(f'config.json: preencha {key}')
DISCORD = CONFIG['discord_url'].strip()
url = urlsplit(DISCORD)
if url.scheme != 'https' or url.hostname not in {'discord.gg', 'discord.com'} or any(c in DISCORD for c in '\"<>\n\r'):
    raise ValueError('discord_url deve ser um convite HTTPS do Discord')
VERSION = CONFIG['version'].strip()
if not re.fullmatch(r'\d+\.\d+\.\d+', VERSION):
    raise ValueError('version deve seguir o formato 2.1.0')
DATE = CONFIG['updated_at']
EFFECTIVE_DATE = CONFIG['effective_at']
updated = datetime.strptime(DATE, '%d/%m/%Y')
effective = datetime.strptime(EFFECTIVE_DATE, '%d/%m/%Y')
if effective < updated:
    raise ValueError('effective_at não pode ser anterior a updated_at')


def source(name):
    return (ROOT / 'documentos' / name).read_text(encoding='utf-8').replace('{{DISCORD_URL}}', DISCORD)


def privacy_text():
    return source('privacidade.md')


def full_terms():
    terms = source('termos.md')
    if terms.count('{{PRIVACIDADE}}') != 1:
        raise ValueError('Mantenha exatamente um marcador {{PRIVACIDADE}} em termos.md')
    result = terms.replace('{{PRIVACIDADE}}', privacy_text().strip())
    if '{{' in result or '}}' in result:
        raise ValueError('Marcador desconhecido nos documentos')
    return result
