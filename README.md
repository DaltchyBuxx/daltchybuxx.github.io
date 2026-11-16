# DaltchyBuxx — Termos e Privacidade

Páginas públicas de Termos de Uso e Política de Privacidade da loja. Versão 2.1.0, atualizada em **16/11/2026**, com vigência em **23/11/2026**.

## Endereços no GitHub Pages

- Início: https://daltchybuxx.github.io/
- Termos: https://daltchybuxx.github.io/termos/
- Privacidade: https://daltchybuxx.github.io/privacidade/

## Ativar a publicação

Em **Settings → Pages → Build and deployment**, selecione **Deploy from a branch**, a branch **main** e a pasta **/(root)**. Salve. A publicação depende da configuração do GitHub Pages e não apenas do envio dos arquivos ao repositório.

## Atualizar o conteúdo

O texto completo fica em `documentos/termos.md`. A página de privacidade usa as seções 11 e 12 desse mesmo documento para evitar versões divergentes. O site é estático e não utiliza banco, formulário de coleta, analytics ou bibliotecas externas.

Após editar o Markdown, gere novamente as páginas com Python 3:

```bash
python3 scripts/build.py
```

A versão e a data exibidas nas páginas são definidas no começo de `scripts/build.py`. Faça commit dos arquivos HTML gerados junto com o texto atualizado.

Para visualização local:

```bash
python3 -m http.server 8000
```

## Contato

https://discord.gg/5mzW2VyNDD — acesse o canal de suporte para iniciar um atendimento.

## Nome do repositório

Para servir na raiz do domínio, use o nome `daltchybuxx.github.io` na organização `DaltchyBuxx`. O gerador usa `BASE = ''`; os links canônicos apontam para a raiz. Preserve Pages em `main` / `/(root)`.

## PDF para download

As páginas oferecem `documentos/termos.pdf`. Ao alterar os termos, gere novamente o HTML com `python3 scripts/build.py` e o PDF com `python3 scripts/build_pdf.py` (requer LibreOffice instalado). Envie ambos os resultados no mesmo commit. O Markdown continua sendo a fonte do conteúdo.

## Alterações da versão 2.1.0

Inclusão da seção 11.11, Transferência de conta, sobre solicitação pelo suporte, verificação de titularidade, transferência ou mesclagem de registros e benefícios, exclusão do cadastro antigo e irreversibilidade. As demais cláusulas permanecem inalteradas. Divulgue a atualização nos canais oficiais antes da vigência em 23/11/2026.
