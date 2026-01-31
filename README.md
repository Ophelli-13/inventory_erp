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
[x] Model `Product`  
[x] Model `Category`  
[x] Model `Supplier`  
[x] Relacionamentos entre entidades  

Dia 4 — Movimentação de Estoque  
[x] Model `StockMovement`  
[x] Repositórios  
[x] Registro de movimentações  
[x] Histórico persistente  

Dia 5 — Regras de Negócio  
[x] ProductService  
[x] InventoryService  
[x] StockMovementService  
[x] Validação de estoque negativo  
[x] Alerta de estoque mínimo  

Dia 6 — API REST  
[x] Rotas de produtos  
[x] Rotas de categorias  
[x] Rotas de fornecedores  
[x] Rotas de estoque  
[x] Schemas de validação  

Dia 7 — Testes e Finalização  
[x] Testes de serviços  
[x] Testes de regras críticas  
[x] Documentação da API (Postman)  
[x] Revisão geral  
[x] Projeto finalizado  

Visão de Futuro

Inventory ERP é pensado como um projeto técnico sólido, realista e evolutivo, servindo simultaneamente como:

- Material de estudo prático em backend Python  
- Demonstração clara de Programação Orientada a Objetos aplicada a domínio real  
- Projeto de portfólio alinhado com padrões de mercado  

O objetivo é consolidar fundamentos fortes e entregar um sistema funcional, organizado e profissional em curto prazo.


## 🚀 Como rodar o projeto
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Configure o `.env` com suas credenciais MySQL.
5. Execute: `python run.py`.

## 🛣️ Endpoints Principais
| Rota | Método | Descrição |
| :--- | :--- | :--- |
| `/api/products` | GET | Lista todos os produtos |
| `/api/products` | POST | Cadastra um novo produto |
| `/api/stock/move` | POST | Realiza entrada/saída de estoque |
| `/api/categories` | GET | Lista categorias |

## 🛡️ Regras de Negócio Implementadas
- Validação de saldo insuficiente (Erro 400).
- Registro automático de histórico para cada movimentação.
- Alerta de estoque crítico no log do servidor.
 