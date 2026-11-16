## 11. Privacidade e tratamento de dados pessoais dos clientes

### 11.1. Responsável e contato

**Nanyus** é responsável pela administração do bot e pela gestão dos dados utilizados em seu funcionamento. Essa função é distinta da responsabilidade pelo fornecimento dos produtos vendidos pela DaltchyBuxx. Para enviar solicitações ou esclarecer dúvidas sobre privacidade, entre no [servidor oficial no Discord]({{DISCORD_URL}}), acesse o **canal de suporte** e inicie um atendimento. Informe que a solicitação é sobre dados pessoais, para encaminhamento a **Nanyus**.

### 11.2. Dados tratados

Esta seção descreve o tratamento de dados pessoais dos clientes da DaltchyBuxx. Conforme os recursos utilizados pelo cliente, o bot e a equipe tratam:

- **Identificação no Discord:** identificador do cliente, nome e informações de perfil disponibilizados pelo Discord quando necessários ao atendimento, cargos relacionados a benefícios do cliente e referências de servidores, canais e mensagens associados ao seu pedido.
- **Pedidos e entrega:** nome de usuário Roblox, informações de Gamepass e experiência, produto, quantidade, valores, descontos, cupons, datas, situação e histórico de compras.
- **Pagamentos:** identificadores e situação das cobranças, valores, dados do Pix e referências de pagamento e comprovantes necessários à confirmação e conciliação do pedido.
- **Atendimento:** mensagens e anexos enviados pelo cliente nos tickets, referências da conversa de atendimento e registros de abertura, acompanhamento e encerramento.
- **Avaliações de atendimento:** notas e justificativas fornecidas pelo cliente, seu identificador e datas das avaliações.
- **Aceitação dos termos:** registro da aceitação e respectiva data, quando coletados pelo bot.

O usuário deve evitar enviar dados sensíveis ou informações de terceiros que não sejam necessárias ao atendimento. Senhas, códigos de recuperação e códigos de autenticação não devem ser enviados nos tickets.

### 11.3. Finalidades

Os dados são utilizados para processar pedidos e pagamentos, realizar entregas, prestar atendimento, registrar e consultar o histórico de operações, registrar as avaliações de atendimento enviadas pelos clientes, aplicar benefícios de fidelidade e descontos, restaurar cargos de fidelidade quando um cliente retorna ao servidor, verificar ocorrências e resolver disputas.

### 11.4. Histórico das conversas

Ao encerrar um ticket, o bot pode gerar uma cópia da conversa, chamada transcript, contendo mensagens, identificação dos participantes, datas e referências a anexos. Essa cópia permite consultar o atendimento posteriormente.

O bot processa temporariamente as conversas para gerar o arquivo e o envia aos canais de registro no Discord. A DaltchyBuxx não mantém cópias permanentes desses arquivos fora do Discord.

Atualmente, não há uma opção específica para recusar previamente a geração desse histórico. Antes de enviar informações, o cliente pode esclarecer dúvidas pelo contato indicado na seção 11.1. A solicitação posterior de exclusão é tratada conforme a seção 12.

### 11.5. Armazenamento e acesso

Dados dos clientes relacionados a pedidos, pagamentos, tickets e avaliações são armazenados em um banco de dados externo ao Discord. As cópias das conversas ficam nos canais de registro do Discord, sujeitas às permissões desses canais.

O acesso aos dados dos clientes e aos registros de atendimento é restrito à **administração do servidor**, composta pelo **Fornecedor, Desenvolvedor, Gerente e Diretor**, conforme a necessidade de suas funções.

### 11.6. Serviços envolvidos

A operação utiliza o Discord para atendimento e registros, o Mercado Pago para pagamentos e a Roblox para consultas e operações relacionadas aos produtos. Também utiliza serviços de hospedagem e armazenamento para manter o bot e os registros dos pedidos.

Cada serviço recebe os dados necessários às operações realizadas e possui seus próprios termos e políticas de privacidade.

### 11.7. Limites de uso

Os dados dos clientes são utilizados para as finalidades descritas nesta seção. A aceitação destes Termos não representa uma autorização irrestrita para qualquer uso das informações.

### 11.8. Conservação

Atualmente, não há prazo fixo de exclusão automática dos registros de pedidos e históricos de atendimento, ressalvada a limpeza de cadastros descrita abaixo. Esses registros permanecem armazenados por prazo indeterminado, e o cliente pode solicitar sua exclusão pelo contato indicado na seção 11.1, observadas as condições da seção 12.

A ausência de prazo fixo não autoriza a conservação de dados sem necessidade. Para os dados obtidos pela API do Discord, também se aplicam as exigências de exclusão quando deixarem de ser necessários às funcionalidades do bot, quando o Discord solicitar ou quando o bot encerrar suas atividades, salvo obrigação legal de conservação.

O bot realiza uma verificação automática periódica, programada para ocorrer a cada 6 horas, para remover cadastros de clientes que não possuem compras concluídas, inclusive compras antigas registradas, e não possuem data registrada de aceitação dos termos. Essa limpeza remove o cadastro do cliente no banco de dados; ela não exclui automaticamente tickets, mensagens ou cópias de conversas no Discord, nem outros registros mantidos separadamente. Clientes com data registrada de aceitação dos termos não são incluídos nessa limpeza apenas por não terem compras concluídas.

### 11.9. Solicitações dos titulares

O titular pode encaminhar solicitações de confirmação de tratamento, acesso, correção, informações sobre compartilhamento e exclusão ao canal indicado na seção 11.1, conforme os direitos aplicáveis. A equipe poderá solicitar informações proporcionais para verificar a identidade e localizar os registros, sem exigir senhas ou códigos de autenticação.

A análise deve abranger os registros dos pedidos e as cópias de conversas e mensagens sob controle da loja.

### 11.10. Mensagens não utilizadas em inteligência artificial

O bot da DaltchyBuxx não envia as conversas dos clientes a ferramentas de inteligência artificial, nem utiliza essas mensagens para treinar modelos de IA. Essa ausência de uso para treinamento está alinhada à [Política de Desenvolvedores do Discord](https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy), que proíbe utilizar conteúdo de mensagens obtido pelas APIs para treinar modelos de aprendizado de máquina ou inteligência artificial sem autorização expressa do Discord.

### 11.11. Transferência de conta

Para solicitar a transferência dos seus registros para outra conta do Discord, acesse a conta antiga e abra um ticket de suporte, informando o ID da nova conta.

Se você não tiver mais acesso à conta antiga, abra o ticket pela nova conta e informe os IDs de ambas. Nesse caso, serão necessárias verificações adicionais para comprovar que a conta antiga pertence a você. A solicitação estará sujeita à aprovação após essas verificações.

Após a aprovação, os registros de compras e os benefícios vinculados à conta antiga serão transferidos para a nova conta. Se a conta de destino já possuir registros, eles poderão ser mesclados. Concluída a transferência, o cadastro da conta antiga será excluído do banco de dados.

**A transferência é irreversível: após sua conclusão, não será possível desfazer a operação e restaurar os cadastros ao estado anterior.**

## 12. Solicitação de exclusão de dados

**12.1.** O cliente poderá solicitar a exclusão de seus dados pelo canal de suporte do servidor oficial, utilizando a própria conta do Discord vinculada aos registros. Caso não tenha mais acesso a essa conta, deverá apresentar informações ou comprovantes suficientes para verificar que os dados solicitados pertencem a ele, como referências de pedidos ou comprovantes de compra. Somente serão solicitadas informações necessárias à verificação; nunca serão exigidas senhas ou códigos de autenticação. A exclusão estará sujeita às hipóteses legais de conservação. 

**12.2.** Após a validação da solicitação de exclusão, haverá um período de 14 (quatorze) dias corridos para que o cliente possa cancelar o pedido. Durante esse período, os dados não serão apagados em decorrência da solicitação, mas o uso do serviço ficará bloqueado enquanto o pedido de exclusão estiver ativo. Encerrado o período sem cancelamento, será realizada a exclusão dos dados elegíveis, ressalvadas as hipóteses legais de conservação e os prazos obrigatórios aplicáveis. 

**12.3.** O cliente poderá cancelar a solicitação durante esse período pelo canal de suporte. Caso tente utilizar uma funcionalidade que salve dados, deverá confirmar expressamente o cancelamento do processo de exclusão antes de prosseguir. A tentativa de uso, por si só, não cancela o processo. Após a confirmação, o acesso ao serviço será restabelecido e os dados serão mantidos conforme a seção 11.8. O canal de suporte continuará disponível para tratar da solicitação. 

**12.4.** As cópias de segurança do banco de dados são realizadas semanalmente. Quando uma nova cópia é criada, a anterior é excluída. Por isso, dados já removidos do banco principal podem permanecer temporariamente na cópia de segurança até a próxima substituição semanal. 

**12.5.** Registros com fundamento legal de retenção poderão ser conservados pelo período necessário, com informação adequada ao titular.
