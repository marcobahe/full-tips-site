# Exploração Real — Filtros Avançados de Contatos (Full Funnel / GHL)

> **Data da exploração:** 11/02/2026  
> **Conta:** FABIO RAMOS DE ASSIS's Account (HFHL3EedRisAuTeXs5zj)  
> **Total de contatos na conta:** 3.517  
> **URL:** `https://go.fullfunnel.app/v2/location/HFHL3EedRisAuTeXs5zj/contacts/smart_list/All`

---

## 1. Visão Geral da Tela de Contatos

### Layout principal
- **Título:** "Contatos" (heading H1)
- **Abas superiores:** Listas inteligentes | Ações em massa | Tarefas | Empresas | (ícone engrenagem → campos personalizados)
- **Sidebar esquerda:** Lista de Smart Lists (ex: "Todos") + botão "Adicionar lista inteligente"
- **Barra de ferramentas acima da tabela:**
  - **Esquerda:** Botão **"Filtros avançados"** (com ícone de funil) + **"Classificar"** (com ícone de setas)
  - **Direita:** Campo de busca "Pesquisar Contatos" + botão **"Gerenciar campos"**
- **Botões no topo direito:** "Importar" + "Adicionar Contato" + menu ⋮ (ações extras)
- **Aviso informativo:** Banner dizendo que "Gerenciar listas inteligentes" e "Restaurar" foram movidos para o menu ⋮

### Tabela de contatos — Colunas padrão
1. **Checkbox** (seleção)
2. **Nome de Contato** (com avatar/iniciais)
3. **Telefone**
4. **E-mail**
5. **Nome da empresa**
6. **Criado (-03)** (data de criação, fuso -03)
7. **Última atividade (-03)**
8. **Tags**

### Paginação
- "Página 1 de 176"
- Seletor de tamanho da página: **20** (padrão) | 50 | 100
- Botões: Prev | 1 | Next

---

## 2. O Botão "Filtros Avançados"

### Localização
- Acima da tabela de contatos, à esquerda
- Ícone de funil + texto **"Filtros avançados"**
- Ao lado do botão "Classificar" (sort)

### Comportamento ao clicar
- Abre um **dialog/modal** com título **"Advanced Filters"**
- O dialog mostra um **campo de busca** ("Search Field") para filtrar os campos disponíveis
- Os campos são organizados em **categorias colapsáveis** (cada uma com ícone de seta para expandir/colapsar)

---

## 3. TODAS as Categorias e Campos Disponíveis para Filtro

### 📋 Categoria: Informações de contato
| Campo | Tipo provável |
|-------|--------------|
| Atribuído | Seleção (usuário) |
| Cidade | Texto |
| Código postal | Texto |
| Criado | Data |
| Criado por | Seleção |
| Data de nascimento | Data |
| Data do último clique no e-mail | Data |
| E-mail | Texto/Email |
| E-mail válido | Booleano |
| Endereço | Texto |
| Estado | Texto |
| Facebook Id | Texto |
| Fonte | Texto |
| Fuso horário | Seleção |
| Google Id | Texto |
| Idade | Número |
| Instagram Id | Texto |
| Marcação (Tags) | Seleção múltipla |
| Nome completo | Texto |
| Nome da empresa | Texto |
| Nome da empresa (duplicado?) | Texto |
| Nome da rua | Texto |
| Nome do curinga | Texto |
| País | Texto/Seleção |
| Primeiro nome | Texto |
| Seguidores | Número |
| Site | Texto/URL |
| Sobrenome | Texto |
| Telefone | Texto/Telefone |
| TikTok LeadId | Texto |
| Tipo | Seleção |
| Tipo de fonte | Seleção |
| Última atualização por | Seleção |
| Última data de abertura do e-mail | Data |
| Whatsapp válido | Booleano |

**Total: 35 campos**

### 🚫 Categoria: DND (Do Not Disturb)
| Campo |
|-------|
| DND de entrada |
| DND todos |
| E-mail |
| FB Messenger |
| GMB Messenger |
| Ligações e voicemails |
| SMS |
| WhatsApp |

**Total: 8 campos**

### 📊 Categoria: Atividade de contato
| Campo |
|-------|
| Atualizado |
| Campanha ativa |
| Campanha cancelada |
| Campanha concluída |
| Campanha pausada |
| Fluxo de trabalho (ativo) |
| Fluxo de trabalho (concluído) |
| Importar |
| Status da campanha |
| Última atividade |
| Última Consulta |
| Último tipo de atividade |

**Total: 12 campos**

### 🎯 Categoria: Informações sobre a oportunidade
| Campo |
|-------|
| Pipeline |
| Estágio do pipeline |
| Status do pipeline |

**Total: 3 campos**

### 🏪 Categoria: Portal do cliente
| Campo |
|-------|
| Grupo |
| Oferta |
| Produto |

**Total: 3 campos**

### 🔗 Categoria: Atribuição
| Campo |
|-------|
| Atribuição FB ClickId |
| Atribuição Google ClickId |
| Campanha de atribuição |
| Conteúdo de atribuição |
| Fonte da sessão de atribuição |
| Fonte de atribuição |
| ID da campanha de atribuição |
| ID do anúncio de atribuição |
| ID do grupo de anúncios de atribuição |
| Meio de atribuição |
| Palavra-chave de atribuição |
| Primeira Atribuição |
| Termo de Atribuição |
| Tipo de correspondência de atribuição |
| Última atribuição |

**Total: 15 campos**

### ℹ️ Categoria: Additional Info (Campos customizados)
| Campo |
|-------|
| Nome Do Produto Comprado |
| Service We Offer |
| Valor Pago |

**Total: 3 campos** *(estes são campos customizados da conta — variam por subconta)*

---

## 4. Operadores por Tipo de Campo

### Para campo tipo TAG (Marcação)
Quando selecionei "Marcação", os operadores disponíveis foram:
1. **É** — Tag é exatamente igual a X
2. **Não é** — Tag não é igual a X
3. **Não está vazio** — O contato tem alguma tag
4. **Está vazio** — O contato não tem nenhuma tag
5. **É qualquer um de** — Tag é qualquer uma de uma lista (permite múltiplas seleções)

### Para campo tipo TEXTO (Primeiro nome, E-mail, etc.)
*(Baseado no padrão GHL — não foi possível abrir este dropdown nesta sessão, mas os operadores padrão do GHL para texto são:)*
- É / Não é
- Contém / Não contém
- Começa com / Termina com
- Está vazio / Não está vazio

### Para campo tipo DATA (Criado, Última atividade, etc.)
*(Padrão GHL:)*
- É / Não é
- Antes de / Depois de
- Entre
- Está vazio / Não está vazio
- Nos últimos X dias / Antes dos últimos X dias

### Para campo tipo BOOLEANO (E-mail válido, Whatsapp válido)
*(Padrão GHL:)*
- É verdadeiro / É falso

### Para campo tipo NÚMERO (Idade, Seguidores)
*(Padrão GHL:)*
- É / Não é
- Maior que / Menor que
- Está vazio / Não está vazio

---

## 5. Estrutura de um Filtro (UI)

Quando um filtro é adicionado, o dialog mostra uma **linha de filtro** com 3 seletores:

```
[ Campo ▼ ]  [ Operador ▼ ]  [ Valor ▼/input ]  [🗑️]
```

- **Campo:** Dropdown com search para escolher o campo (com todas as categorias listadas acima)
- **Operador:** Dropdown que muda dinamicamente conforme o tipo do campo selecionado
- **Valor:** Input de texto, dropdown de seleção, ou seletor de data, conforme o tipo
- **Botão 🗑️ (X):** Remove o valor inserido naquele filtro

### Botões de ação em cada linha de filtro
- **"Add nested filter"** — Adiciona um subfiltro aninhado (para lógica AND/OR dentro de um grupo)
- **"Remove Filter"** — Remove completamente aquela linha de filtro

### Botões globais do dialog
- **"Add Filter"** — Adiciona uma nova linha de filtro (permite múltiplos filtros)
- **"Limpar todos os filtros"** — Remove todos os filtros de uma vez
- **"Cancel"** — Fecha o dialog sem aplicar mudanças
- **"Apply"** — Aplica os filtros e filtra a tabela

---

## 6. Múltiplos Filtros e Lógica AND/OR

### Como funciona
- **"Add Filter"** adiciona linhas de filtro independentes (funciona como AND entre elas)
- **"Add nested filter"** dentro de uma linha cria um grupo aninhado (permite lógica OR dentro de um grupo AND)
- A interface NÃO mostrou um toggle AND/OR explícito na versão explorada — a lógica é controlada pela estrutura de grupos (filtros no mesmo nível = AND, filtros nested = podem ser OR)

### Fluxo para adicionar múltiplos filtros
1. Clicar em **"Filtros avançados"**
2. A primeira linha de filtro aparece automaticamente
3. Selecionar Campo → Operador → Valor
4. Clicar **"Add Filter"** para adicionar outra linha
5. Repetir seleção
6. Clicar **"Apply"** para aplicar

---

## 7. Smart Lists (Listas Inteligentes)

### Sidebar esquerda
- Mostra a lista de Smart Lists criadas
- Smart List padrão: **"Todos"** (ícone de lista, mostra todos os contatos)
- Botão **"Adicionar lista inteligente"** (com ícone +) para criar nova

### Como salvar filtros como Smart List
1. Aplicar os filtros desejados via "Filtros avançados"
2. Clicar em **"Adicionar lista inteligente"** na sidebar esquerda
3. Definir nome e salvar
4. A Smart List salva os filtros como uma "vista" reutilizável

### Gerenciar Smart Lists
- As opções **"Gerenciar listas inteligentes"** e **"Restaurar"** foram movidas para o **menu ⋮** (três pontos) ao lado do botão "Adicionar Contato"

---

## 8. Outros Elementos Relevantes

### Campo de busca rápida
- **"Pesquisar Contatos"** — textbox para busca rápida por nome, email, telefone
- Fica ao lado dos filtros avançados, na barra de ferramentas

### Botão "Classificar" (Sort)
- Ao lado do botão "Filtros avançados"
- Permite ordenar a lista por diferentes campos

### Botão "Gerenciar campos"
- À direita, na mesma barra
- Permite configurar quais colunas aparecem na tabela

### Colunas sortáveis
- As colunas da tabela (Nome de Contato, Telefone, E-mail, etc.) têm ícones de seta para ordenação

---

## 9. Resumo do Fluxo Completo de Filtragem

```
1. Ir em Contatos → Listas inteligentes
2. Clicar "Filtros avançados" (ícone funil)
3. Dialog "Advanced Filters" abre
4. Selecionar CAMPO no primeiro dropdown (ex: Marcação)
5. Selecionar OPERADOR no segundo dropdown (ex: É)
6. Selecionar/digitar VALOR no terceiro campo (ex: "jornada prp 15k")
7. (Opcional) Clicar "Add Filter" para adicionar mais filtros
8. (Opcional) Clicar "Add nested filter" para criar grupo aninhado
9. Clicar "Apply" para filtrar
10. (Opcional) Salvar como Smart List clicando "Adicionar lista inteligente"
11. Para limpar: "Limpar todos os filtros" ou "Cancel"
```

---

## 10. Notas Técnicas

- A interface está **traduzida parcialmente** para português — alguns elementos ficam em inglês (ex: "Advanced Filters", "Add Filter", "Apply", "Cancel", "Please Select")
- Os campos personalizados (Additional Info) variam por subconta
- Campos de DND são per-channel (E-mail, SMS, WhatsApp, FB Messenger, GMB Messenger, Ligações)
- A pesquisa de campos no dialog ("Search Field") filtra em tempo real conforme digita
- Todas as categorias vêm expandidas por padrão no dialog
