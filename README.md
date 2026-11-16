# DaltchyBuxx — Termos e Privacidade

Site público: https://daltchybuxx.github.io/

## Como atualizar pelo GitHub

Abra um dos arquivos abaixo, clique no lápis, faça a alteração e use **Commit changes** na branch `main`. Não é necessário instalar programas ou gerar PDFs manualmente.

| Arquivo para editar | Finalidade |
| --- | --- |
| [config.json](config.json) | Link do Discord, versão e datas |
| [documentos/termos.md](documentos/termos.md) | Texto dos termos |
| [documentos/privacidade.md](documentos/privacidade.md) | Política de privacidade e exclusão de dados |

### Configurações

```json
{
  "discord_url": "https://discord.gg/5mzW2VyNDD",
  "version": "2.1.0",
  "updated_at": "16/11/2026",
  "effective_at": "23/11/2026"
}
```

- Use datas no formato `DD/MM/AAAA` e versão como `2.1.0`.
- `updated_at` é a data da revisão; `effective_at` é quando ela entra em vigor.
- Os valores não mudam sozinhos: escolha versão e datas a cada revisão de conteúdo. Uma troca de convite não precisa alterar a versão dos termos.
- A data de vigência não pode ser anterior à atualização.
- Para alterações relevantes, observe a comunicação antecipada prevista nos termos.

### Textos e marcadores

Edite os parágrafos e mantenha os títulos numerados (`## 1. ...`, `### 11.1. ...`). Preserve a numeração existente para os links do índice continuarem funcionando.

Nos textos, `{{DISCORD_URL}}` é substituído pelo convite de `config.json`, inclusive no PDF. Não troque esse marcador por um convite fixo.

Em `termos.md`, mantenha exatamente um marcador `{{PRIVACIDADE}}`. Ele inclui automaticamente o texto de `privacidade.md` nos termos completos e no PDF. Assim, a política é editada uma única vez. O conteúdo jurídico foi preservado na separação dos arquivos.

## Publicação automática

Após cada commit em `main`, o workflow **Gerar site e PDF**:

1. Lê as configurações e compõe os documentos.
2. Gera as três páginas HTML e o PDF com os mesmos textos, versão, datas e convite.
3. Verifica o PDF, os links internos e as âncoras do índice.
4. Publica somente o pacote validado no GitHub Pages.

As configurações, os scripts e as fontes Markdown não são expostos como arquivos de configuração no pacote publicado. O site oferece o PDF e uma cópia Markdown completa já processada.

**Configuração inicial única:** em **Settings → Pages → Build and deployment → Source**, escolha **GitHub Actions**. A automação usa o `GITHUB_TOKEN` do próprio GitHub; não é necessário criar ou compartilhar tokens pessoais.

Veja o andamento na aba **Actions**. Aguarde o workflow terminar com sucesso antes de conferir o site. Se houver falha, a última publicação bem-sucedida permanece disponível; corrija o erro indicado e faça outro commit. Também é possível executar manualmente por **Actions → Gerar site e PDF → Run workflow**.

Os HTMLs e o PDF presentes na branch são cópias geradas durante a migração. A publicação automática usa um pacote novo em `dist/`, e não essas cópias. Não edite os arquivos gerados: altere as fontes acima. Os resultados de cada execução ficam no artefato `github-pages` do workflow.

## Links publicados

- Início: https://daltchybuxx.github.io/
- Termos: https://daltchybuxx.github.io/termos/
- Privacidade: https://daltchybuxx.github.io/privacidade/
- PDF: https://daltchybuxx.github.io/documentos/termos.pdf

O endereço do PDF permanece fixo; seu conteúdo acompanha cada publicação.

## Desenvolvimento local

Requer Python 3.12 ou superior, LibreOffice Writer, fontes Liberation e `pdfinfo` (Poppler).

```bash
python3 scripts/build_site.py
python3 -m http.server 8000 --directory dist
```

O comando completo gera o pacote `dist/`, sem fazer commit ou push. Para gerar apenas as páginas, use `python3 scripts/build.py`. Para gerar apenas o PDF, use `python3 scripts/build_pdf.py`.
