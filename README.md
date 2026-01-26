Inventory ERP – Sistema de Controle de Estoque

Inventory ERP é um sistema de controle de estoque focado em organização, rastreabilidade e consistência de dados para pequenas e médias empresas.

Este projeto nasce como um backend-first em Python, utilizando Flask e MySQL, totalmente testável via Postman, sem interface gráfica inicial.

Além de servir como **projeto de portfólio**, este repositório foi estruturado para funcionar como um **plano de estudos prático**, permitindo consolidar conceitos essenciais de backend profissional em um ciclo intensivo de 7 dias.

Conceito

O sistema permite o controle completo de produtos, categorias e fornecedores, garantindo que toda movimentação de estoque seja registrada e validada por regras de negócio claras.

Não existe movimentação sem histórico.  
Não existe estoque negativo.  
Toda alteração é persistente e auditável.

O foco está em:

Programação Orientada a Objetos  
Design de domínio  
Arquitetura limpa  
Regras de negócio reais  
Persistência consistente  

Estrutura do Projeto

O sistema é dividido em camadas bem definidas:

Configuração  
Banco de dados  
Modelos  
Repositórios  
Serviços  
Rotas  
Schemas  
Exceções  
Testes  

Essa separação garante baixo acoplamento, alta coesão e facilita tanto o aprendizado quanto a evolução do sistema.

Status Atual

🟡 Em desenvolvimento — Fundação do projeto

Plano Diário de Desenvolvimento (7 Dias)

Dia 1 — Fundação do Projeto  
[x] Criação do repositório  
[x] Estrutura de pastas  
[x] Configuração inicial do Flask  
[x] Arquivo `.env` e configurações básicas  

Dia 2 — Banco de Dados e Infraestrutura  
[x] Configuração do MySQL  
[x] Conexão com SQLAlchemy  
[x] Setup de migrations  
[x] Criação do banco  

Dia 3 — Modelagem do Domínio  
[ ] Model `Product`  
[ ] Model `Category`  
[ ] Model `Supplier`  
[ ] Relacionamentos entre entidades  

Dia 4 — Movimentação de Estoque  
[ ] Model `StockMovement`  
[ ] Repositórios  
[ ] Registro de movimentações  
[ ] Histórico persistente  

Dia 5 — Regras de Negócio  
[ ] ProductService  
[ ] InventoryService  
[ ] StockMovementService  
[ ] Validação de estoque negativo  
[ ] Alerta de estoque mínimo  

Dia 6 — API REST  
[ ] Rotas de produtos  
[ ] Rotas de categorias  
[ ] Rotas de fornecedores  
[ ] Rotas de estoque  
[ ] Schemas de validação  

Dia 7 — Testes e Finalização  
[ ] Testes de serviços  
[ ] Testes de regras críticas  
[ ] Documentação da API (Postman)  
[ ] Revisão geral  
[ ] Projeto finalizado  

Visão de Futuro

Inventory ERP é pensado como um projeto técnico sólido, realista e evolutivo, servindo simultaneamente como:

- Material de estudo prático em backend Python  
- Demonstração clara de Programação Orientada a Objetos aplicada a domínio real  
- Projeto de portfólio alinhado com padrões de mercado  

O objetivo é consolidar fundamentos fortes e entregar um sistema funcional, organizado e profissional em curto prazo.
