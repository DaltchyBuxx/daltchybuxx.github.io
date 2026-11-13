# DaltchyBuxx — Termos e Privacidade

Páginas públicas de Termos de Uso e Política de Privacidade da loja. Versão 2.0.0, com atualização e vigência em **13/11/2026**.

## Endereços no GitHub Pages

- Início: https://daltchybuxx.github.io/daltchybuxx-web/
- Termos: https://daltchybuxx.github.io/daltchybuxx-web/termos/
- Privacidade: https://daltchybuxx.github.io/daltchybuxx-web/privacidade/

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
