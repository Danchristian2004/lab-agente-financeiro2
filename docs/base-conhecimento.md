Base de Conhecimento
[!TIP]
Quer um dataset mais robusto? Você pode utilizar datasets públicos do Hugging Face relacionados a finanças, desde que sejam adequados ao contexto do desafio.

Adaptações nos Dados
Para o funcionamento do B-Fin, os dados de transacoes.csv foram agrupados por categoria para permitir que o agente responda perguntas como "Quanto gastei com transporte?". Além disso, cruzamos o prazo das metas com a indicado_para dos produtos financeiros.

Estratégia de Integração
Como os dados são carregados?
Os arquivos JSON e CSV são carregados em DataFrames no início da sessão e servidos como contexto para a LLM.

Como os dados são usados no prompt?
Os dados são injetados dinamicamente no prompt do sistema como uma "tabela de fatos", garantindo que a IA consulte os valores reais de João antes de responder.

Exemplo de Contexto Montado
Plaintext
Dados do Cliente:
- Nome: João Silva
- Perfil: moderado (Risco: Baixo/Médio)
- Meta 1: Reserva de Emergência (Faltam R$ 5.000)

Produtos Recomendados:
- CDB Liquidez Diária (102% CDI)
- Tesouro Selic