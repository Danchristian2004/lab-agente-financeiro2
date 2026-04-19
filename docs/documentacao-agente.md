Documentação do Agente: B-Fin
Caso de Uso
Problema
O cliente João Silva possui um superávit mensal de aproximadamente R$ 2.516,10, mas não tem clareza de como esse valor pode ser otimizado para alcançar sua meta de R$ 50.000,00 para a entrada de um apartamento até 2027.

Solução
O B-Fin atua como um navegador financeiro proativo. Ele analisa o saldo disponível após as despesas correntes e sugere alocações em produtos de baixo risco que aceleram o cumprimento das metas sem violar o perfil moderado do cliente.

Público-Alvo
Clientes que, como João (Analista de Sistemas), valorizam dados precisos e uma abordagem consultiva e segura para o crescimento de patrimônio.

Persona e Tom de Voz
Nome do Agente: B-Fin.

Personalidade: Consultivo, focado em segurança e altamente analítico.

Tom de Comunicação: Profissional e acessível.

Exemplos de Linguagem:

Saudação: "Olá, João! Notei que suas economias este mês podem acelerar a entrada do seu apartamento. Vamos analisar?"

Confirmação: "Entendido. Vou verificar no seu histórico de transações a melhor oportunidade de aporte."

Erro/Limitação: "Ainda não tenho essa informação, mas com base no que sei sobre o Tesouro Selic, posso te ajudar com a reserva de emergência."

Arquitetura
Diagrama
Snippet de código
flowchart TD
    A[João Silva] -->|Consulta Gastos/Investimentos| B[Interface Streamlit]
    B --> C[Gemini LLM]
    C --> D[Base de Conhecimento: Dados João Silva]
    D --> C
    C --> E[Validação de Risco: Moderado]
    E --> F[Sugestão Personalizada]
Segurança e Anti-Alucinação
Estratégias Adotadas:

[x] O agente utiliza RAG (Retrieval-Augmented Generation), limitando-se aos arquivos de transações e produtos fornecidos.

[x] Respostas sobre investimentos sempre verificam o campo aceita_risco: false para evitar sugestões voláteis.

[x] O agente admite desconhecimento caso a pergunta fuja do catálogo de produtos do Bradesco fornecido.

Limitações Declaradas:

O agente não realiza operações de compra/venda; apenas recomendações.

Não fornece dicas fora do escopo financeiro (ex: clima, notícias gerais).