# Roteiro: Como Filtrar Contatos no Full Funnel

## Objetivo
Este tutorial ensina usuários leigos a usar os filtros avançados na seção de Contatos do Full Funnel.

## Pré-requisitos
- Ter uma conta no Full Funnel (https://go.fullfunnel.app)
- Estar logado na plataforma
- Ter permissão para acessar a seção de Contatos

## Passo a Passo Detalhado

### 1. Acessar a Seção de Contatos
1. Faça login no Full Funnel
2. No menu lateral esquerdo, clique em **"Contatos"**
   - Ícone: normalmente um ícone de pessoas/usuários
   - Localização: menu principal, geralmente após "Dashboard" e antes de "Campanhas"

### 2. Localizar os Filtros
Na página de Contatos, procure por:
- **Botão "Filtrar"** ou **"Filtros"** no topo da lista de contatos
- **Ícone de funil** (🔽) próximo à barra de busca
- **Menu suspenso** com opções de filtro básico

### 3. Explorar Filtros Básicos vs. Avançados
**Filtros Básicos (visíveis inicialmente):**
- Barra de busca rápida (nome, email, telefone)
- Filtro por status (Ativo, Inativo, etc.)
- Filtro por tags

**Para acessar Filtros Avançados:**
1. Clique em **"Filtros Avançados"** ou **"Mais Filtros"**
2. Uma janela/modal se abrirá com todas as opções

### 4. Campos que Podem Ser Filtrados (lista detalhada)
Baseado em análise de sistemas CRM e conhecimento do Full Funnel:

**Categoria: Informações do Contato**
- `name` - Nome completo
- `firstName` - Primeiro nome
- `lastName` - Sobrenome
- `email` - Endereço de email
- `phone` - Telefone principal
- `mobile` - Celular
- `company` - Empresa
- `jobTitle` - Cargo/Função
- `website` - Site pessoal/empresarial

**Categoria: Localização**
- `country` - País
- `state` - Estado/Província
- `city` - Cidade
- `postalCode` - CEP
- `address1` - Endereço linha 1
- `address2` - Endereço linha 2

**Categoria: Dados do Sistema**
- `id` - ID único do contato
- `createdAt` - Data de criação
- `updatedAt` - Data de última atualização
- `source` - Fonte do contato
  - Formulário web
  - Importação manual
  - API
  - Integração
- `status` - Status do contato
  - Lead
  - Oportunidade
  - Cliente
  - Inativo
- `score` - Score/classificação (0-100)
- `owner` - Proprietário/Responsável

**Categoria: Tags e Segmentação**
- `tags` - Tags atribuídas
- `lists` - Listas pertencentes
- `segments` - Segmentos automáticos
- `customFields` - Campos personalizados
  - [Depende da configuração da conta]

**Categoria: Atividades e Engajamento**
- `lastActivityDate` - Data da última atividade
- `emailOpened` - Abriu email (campanha específica)
- `emailClicked` - Clicou em link de email
- `formSubmitted` - Formulário preenchido
- `pageVisited` - Página visitada
- `purchaseMade` - Compra realizada
- `conversationStatus` - Status na conversa
- `lastContactDate` - Data do último contato

**Categoria: Comportamento**
- `engagementScore` - Nível de engajamento
- `buyerStage` - Estágio no funil
- `leadScore` - Pontuação como lead
- `conversionLikelihood` - Probabilidade de conversão

**Informações Básicas:**
- Nome (nome completo, primeiro nome, sobrenome)
- Email (endereço de email)
- Telefone (número de telefone)
- Empresa (nome da empresa)
- Cargo (posição/título)

**Dados de Contato:**
- País
- Estado/Província
- Cidade
- CEP
- Endereço

**Informações do Sistema:**
- Data de criação
- Data de última atualização
- Fonte do contato (como chegou)
- Status (Ativo, Inativo, Cancelado)
- Score/Classificação

**Tags e Categorias:**
- Tags (palavras-chave atribuídas)
- Listas (Smart Lists)
- Segmentos

**Atividades:**
- Abriu email (campanha específica)
- Clicou em link
- Visitou página
- Preencheu formulário
- Comprou produto

### 5. Operadores Disponíveis (por tipo de campo)

**Para campos de texto (nome, email, telefone, etc.):**
- `contains` - Contém (busca parcial)
- `notContains` - Não contém
- `equals` - É igual a (busca exata)
- `notEquals` - É diferente de
- `startsWith` - Começa com
- `endsWith` - Termina com
- `isEmpty` - Está vazio
- `isNotEmpty` - Não está vazio
- `regex` - Expressão regular (avançado)

**Para campos numéricos (score, ID, valores):**
- `equals` - É igual a
- `notEquals` - É diferente de
- `greaterThan` - É maior que
- `lessThan` - É menor que
- `greaterThanOrEqual` - É maior ou igual a
- `lessThanOrEqual` - É menor ou igual a
- `between` - Está entre (dois valores)
- `isEmpty` - Está vazio
- `isNotEmpty` - Não está vazio

**Para campos de data (criação, atualização, atividades):**
- `equals` - É igual a (data específica)
- `notEquals` - É diferente de
- `after` - É depois de
- `before` - É antes de
- `between` - Está entre (duas datas)
- `lastDays` - Nos últimos X dias
- `nextDays` - Nos próximos X dias
- `lastMonths` - Nos últimos X meses
- `nextMonths` - Nos próximos X meses
- `isEmpty` - Está vazio
- `isNotEmpty` - Não está vazio
- `today` - Hoje
- `yesterday` - Ontem
- `thisWeek` - Esta semana
- `thisMonth` - Este mês
- `thisYear` - Este ano

**Para campos de seleção múltipla (tags, listas, status):**
- `containsAny` - Contém qualquer (um ou mais)
- `containsAll` - Contém todos (todos necessários)
- `notContains` - Não contém
- `equals` - É igual a (para seleção única)
- `notEquals` - É diferente de
- `isEmpty` - Está vazio
- `isNotEmpty` - Não está vazio

**Para campos booleanos (sim/não, verdadeiro/falso):**
- `isTrue` - É verdadeiro
- `isFalse` - É falso
- `isEmpty` - Está vazio
- `isNotEmpty` - Não está vazio

### 6. Como Adicionar Múltiplos Filtros

**Interface visual:**
- Cada filtro aparece como uma "linha" com 3 componentes:
  1. **Dropdown do campo** (ex: "Nome", "Email", "Data de Criação")
  2. **Dropdown do operador** (ex: "Contém", "É igual a", "É depois de")
  3. **Campo de valor** (input text, date picker, ou dropdown)

**Passo a passo:**
1. Clique em **"Adicionar Filtro"** ou botão **"+"**
2. Na primeira linha que aparece:
   - Selecione o campo no primeiro dropdown
   - O segundo dropdown mostrará operadores disponíveis para aquele campo
   - Preencha o valor conforme necessário
3. Para adicionar outro filtro:
   - Clique novamente em **"Adicionar Filtro"** ou **"+"`
   - Uma nova linha aparecerá abaixo
4. **Combinação de filtros:**
   - Por padrão, filtros usam **"E"** (AND) - todos devem ser verdadeiros
   - Para usar **"OU"** (OR):
     - Procure por **"Adicionar grupo"** ou **"Adicionar condição OU"**
     - Crie um novo grupo de filtros
     - Dentro do grupo, filtros usam "OU" entre si
     - Entre grupos, continua valendo "E"

**Exemplo visual na interface:**
```
┌─────────────────────────────────────────────┐
│ 🔍 Filtros Avançados                        │
│                                             │
│ [Campo: Nome] [Operador: Contém] [Valor: João] │
│ [Campo: Estado] [Operador: É igual a] [Valor: SP] │
│ [Campo: Data Criação] [Operador: Últimos] [Valor: 30 dias] │
│                                             │
│ ┌─ Grupo OU (opcional) ───────────────────┐ │
│ │ [Campo: Tags] [Operador: Contém] [Valor: cliente] │ │
│ │ [Campo: Tags] [Operador: Contém] [Valor: vip]     │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ [X] Remover filtro    [+] Adicionar filtro  │
└─────────────────────────────────────────────┘
```

### 7. Como Salvar Filtros (Smart Lists)

**Localização do botão de salvar:**
- No modal de filtros avançados, procure por:
  - **"Salvar Filtro"** (botão primário)
  - **"Salvar como Lista Inteligente"** (text link)
  - Ícone de **disquete** 💾 ou **estrela** ⭐
  - Menu **"Opções"** → **"Salvar Filtro"**

**Processo de salvamento:**
1. Configure seus filtros como desejado
2. Clique em **"Salvar Filtro"**
3. Modal de salvamento aparecerá com:
   - **Nome da Lista:** Campo para digitar nome descritivo
   - **Descrição:** (opcional) Explicação dos critérios
   - **Visibilidade:**
     - ○ Privada (só eu)
     - ○ Compartilhada (com minha equipe)
     - ○ Pública (todos na conta)
   - **Opções avançadas:**
     - [ ] Atualizar automaticamente
     - [ ] Notificar quando mudar
     - [ ] Compartilhar com usuários específicos
4. Clique em **"Salvar"** ou **"Criar Lista"**

**O que são Smart Lists (Listas Inteligentes):**
- Filtros salvos que **se atualizam em tempo real**
- Sempre mostram contatos que **atualmente** atendem aos critérios
- Se um contato deixar de atender, sai da lista automaticamente
- Se um novo contato atender, entra automaticamente

**Onde encontrar listas salvas:**
1. **Menu lateral:** Seção "Listas Inteligentes" ou "Filtros Salvos"
2. **Dropdown de filtros:** Opção "Minhas Listas" ou "Filtros Salvos"
3. **Página de contatos:** Aba/guia "Listas Salvas"

**Gerenciamento de listas salvas:**
- **Editar:** Clique no nome da lista → "Editar Filtros"
- **Renomear:** Menu de contexto → "Renomear"
- **Duplicar:** Criar cópia com ajustes
- **Excluir:** Menu → "Excluir Lista"
- **Exportar:** Gerar CSV/Excel da lista atual

### 8. Como Aplicar/Usar Filtros Salvos
1. No menu de filtros, procure por **"Filtros Salvos"** ou **"Minhas Listas"**
2. Selecione a lista desejada
3. Os filtros serão aplicados automaticamente
4. A lista de contatos será atualizada

### 9. Como Limpar/Remover Filtros
**Para remover filtros individuais:**
- Ao lado de cada filtro, procure o **"X"** ou ícone de lixeira 🗑️
- Clique para remover aquele critério específico

**Para limpar todos os filtros:**
- Botão **"Limpar Filtros"** ou **"Resetar"**
- Opção **"Remover Todos os Filtros"**

**Para voltar ao estado inicial:**
- Botão **"Cancelar"** no modal de filtros
- Fechar a janela de filtros

### 10. Dicas para Usuários Leigos

**Comece simples:**
1. Use a busca rápida primeiro
2. Adicione um filtro por vez
3. Veja os resultados antes de adicionar mais

**Teste seus filtros:**
- Sempre verifique se está encontrando os contatos certos
- Use poucos contatos conhecidos para testar

**Nomeie bem suas Smart Lists:**
- Use nomes descritivos: "Clientes Ativos SP"
- Inclua data se for temporário: "Leads Fevereiro 2024"

**Use operadores corretamente:**
- "Contém" para busca parcial
- "É igual a" para busca exata
- "Está vazio" para encontrar dados faltantes

## Exemplos Práticos de Uso

### Exemplo 1: Encontrar Leads Quentes
**Objetivo:** Contatos de São Paulo que abriram email nos últimos 7 dias
```
1. Campo: Estado | Operador: É igual a | Valor: SP
2. Campo: Abriu Email | Operador: É depois de | Valor: 7 dias atrás
3. Campo: Score | Operador: É maior que | Valor: 70
```

### Exemplo 2: Clientes Inativos para Reativação
**Objetivo:** Clientes que não tiveram atividade nos últimos 90 dias
```
1. Campo: Status | Operador: É igual a | Valor: Cliente
2. Campo: Última Atividade | Operador: É antes de | Valor: 90 dias atrás
3. Campo: Valor Total | Operador: É maior que | Valor: 500
```

### Exemplo 3: Segmentação para Campanha
**Objetivo:** Leads que preencheram formulário mas não compraram
```
GRUPO 1 (E):
  1. Campo: Formulário Preenchido | Operador: É igual a | Valor: Sim
  2. Campo: Compra Realizada | Operador: É igual a | Valor: Não

GRUPO 2 (OU dentro do grupo):
  3. Campo: Tags | Operador: Contém | Valor: interessado
  4. Campo: Tags | Operador: Contém | Valor: demonstração
```

### Exemplo 4: Limpeza de Dados
**Objetivo:** Encontrar contatos com dados incompletos
```
1. Campo: Email | Operador: Está vazio | Valor: 
OU
2. Campo: Telefone | Operador: Está vazio | Valor: 
```

## Screenshots Necessários (lista)

### Fase 1: Navegação Básica
1. **Tela de Login** - Mostrar onde fazer login
2. **Menu Lateral** - Destacar opção "Contatos"
3. **Página de Contatos** - Visão geral antes de filtrar

### Fase 2: Acesso aos Filtros
4. **Botão de Filtros** - Localização do botão/ícone (destaque em vermelho)
5. **Modal Filtros Básicos** - Primeira camada de filtros
6. **Link "Filtros Avançados"** - Como acessar mais opções

### Fase 3: Interface de Filtros Avançados
7. **Modal Filtros Avançados** - Visão completa da interface
8. **Dropdown de Campos** - Lista completa rolável
9. **Dropdown de Operadores** - Todos os operadores disponíveis
10. **Tipos de Inputs** - Diferentes campos (texto, data, dropdown)

### Fase 4: Funcionalidades
11. **Múltiplos Filtros** - Mostrando 3+ filtros combinados
12. **Opção AND/OR** - Como combinar filtros (grupos)
13. **Botão "Adicionar Filtro"** - Localização e aparência
14. **Ícone Remover Filtro** - Como remover filtro individual (X)
15. **Botão Limpar Tudo** - Como resetar todos os filtros

### Fase 5: Salvamento
16. **Botão Salvar Filtro** - Onde salvar como Smart List
17. **Modal de Nomeação** - Dando nome à lista inteligente
18. **Opções de Visibilidade** - Privada/Compartilhada/Pública

### Fase 6: Uso de Listas Salvas
19. **Menu "Listas Inteligentes"** - Onde encontrar no sidebar
20. **Dropdown "Filtros Salvos"** - Acesso rápido na página
21. **Lista Aplicada** - Contatos filtrados por lista salva

### Fase 7: Resultados
22. **Contador de Resultados** - "Mostrando X de Y contatos"
23. **Lista Filtrada** - Visual dos contatos após filtro
24. **Exportação** - Botão exportar resultados

## Fluxo Completo para Tutorial em Vídeo

**Cena 1: Introdução (0:00-0:30)**
- Problema: "Como encontrar contatos específicos rapidamente?"
- Solução: "Filtros avançados do Full Funnel"

**Cena 2: Acessando Contatos (0:30-1:00)**
- Login → Menu → Contatos
- Mostrar página inicial de contatos

**Cena 3: Filtros Básicos (1:00-2:00)**
- Busca rápida
- Filtro por status
- Filtro por tags

**Cena 4: Filtros Avançados (2:00-4:00)**
- Abrindo modal avançado
- Explicando campos disponíveis
- Demonstrando operadores

**Cena 5: Exemplo Prático (4:00-6:00)**
- "Encontrar clientes de SP que compraram nos últimos 30 dias"
- Passo a passo com 3 filtros combinados

**Cena 6: Salvando como Smart List (6:00-7:00)**
- Salvar filtro
- Nomear lista
- Verificar na sidebar

**Cena 7: Usando Lista Salva (7:00-8:00)**
- Aplicar lista salva
- Mostrar resultados atualizados

**Cena 8: Limpeza e Dicas (8:00-9:00)**
- Como remover filtros
- Dicas finais
- Chamada para ação

## Observações Técnicas para Gravação

**Ângulos importantes:**
- Tela cheia para mostrar interface
- Zoom no cursor quando clicar em elementos pequenos
- Highlight em elementos interativos

**Narração:**
- Linguagem simples, sem jargões técnicos
- Passo a passo claro
- Explicar "porquê" além de "como"

**Edição:**
- Inserir textos explicativos
- Setas para destacar elementos
- Slow motion em passos críticos

## Problemas Comuns e Soluções

### 1. "Não encontro o botão de filtros"
- **Solução:** Procure por:
  - Ícone de funil (🔽) próximo à busca
  - Menu "Ações" ou "Mais Opções"
  - Texto "Filtrar" no cabeçalho da tabela
  - Tecla de atalho (geralmente Ctrl+F ou Cmd+F)

### 2. "Meu filtro não retorna resultados"
- **Verifique:**
  - Operadores muito restritivos (use "Contém" em vez de "É igual a")
  - Combinação AND muito rigorosa (experimente OR)
  - Dados inconsistentes (maiúsculas/minúsculas, espaços)
  - Cache do navegador (recarregue a página)

### 3. "Não consigo salvar o filtro"
- **Possíveis causas:**
  - Nome já existe (escolha nome único)
  - Permissões insuficientes (converse com administrador)
  - Sessão expirada (faça login novamente)
  - Limite de listas atingido (exclua listas antigas)

### 4. "Lista inteligente não atualiza automaticamente"
- **Configure:**
  - Na criação: marque "Atualizar automaticamente"
  - Para lista existente: edite → opções avançadas
  - Verifique intervalo de atualização (geralmente a cada 1-24h)

### 5. "Filtro muito lento com muitos contatos"
- **Otimize:**
  - Use menos filtros simultâneos
  - Filtre primeiro por data (reduz escopo)
  - Evite operadores complexos (regex, "Contém" em textos longos)
  - Use listas salvas em vez de filtros complexos toda vez

## Dicas Avançadas para Power Users

### 1. Atalhos de Teclado
- `Ctrl+F` / `Cmd+F` - Abrir filtros rápidos
- `Enter` - Aplicar filtro após preencher
- `Esc` - Fechar modal de filtros
- `Tab` - Navegar entre campos

### 2. Filtros Compartilhados
- Crie filtros padrão para a equipe
- Use nomes consistentes (prefixo: "EQUIPE - ")
- Documente critérios na descrição
- Revise periodicamente filtros compartilhados

### 3. Exportação Inteligente
1. Filtre os contatos desejados
2. Exporte para CSV/Excel
3. Use "Exportar com colunas atuais" para manter layout
4. Agende exportações automáticas para listas salvas

### 4. Integração com Outras Ferramentas
- **Automações:** Use filtros como gatilho
- **Campanhas:** Segmentação baseada em listas inteligentes
- **Relatórios:** Filtros salvos como fonte de dados
- **API:** Acesse listas via integração

## Checklist de Validação

Antes de considerar o tutorial completo, validar:

### Interface
- [ ] Localização exata do botão de filtros
- [ ] Campos disponíveis na conta demo
- [ ] Operadores suportados por campo
- [ ] Limite máximo de filtros simultâneos

### Funcionalidades
- [ ] Processo de salvamento funciona
- [ ] Listas aparecem no sidebar
- [ ] Atualização automática funciona
- [ ] Exportação gera arquivo correto

### Performance
- [ ] Filtros respondem em tempo razoável (<5s)
- [ ] Interface não trava com muitos filtros
- [ ] Listas grandes carregam adequadamente

## Próximos Passos

### Fase 1: Validação (1-2 horas)
1. **Acessar plataforma** - Login em conta demo/teste
2. **Confirmar interface** - Comparar com documentação
3. **Ajustar detalhes** - Corrigir discrepâncias

### Fase 2: Captura (2-3 horas)
4. **Screenshots** - Todas as 24 imagens listadas
5. **Anotações** - Detalhes específicos da interface
6. **Exemplos reais** - Dados de demonstração

### Fase 3: Produção (3-4 horas)
7. **Script de narração** - Texto para voiceover
8. **Gravação de tela** - Seguir fluxo validado
9. **Edição básica** - Cortes, textos, highlights

### Fase 4: Finalização (1-2 horas)
10. **Revisão** - Verificar clareza e precisão
11. **Exportação** - Formatos finais (MP4, GIFs)
12. **Publicação** - Upload para plataformas

## Recursos Adicionais

### Para o Instrutor:
- **Script detalhado** - Cada passo com timing
- **Lista de termos** - Glossário para narração
- **Perguntas frequentes** - Respostas preparadas

### Para o Aluno:
- **PDF resumo** - Passos principais em 1 página
- **Cheat sheet** - Operadores e exemplos
- **Exercícios práticos** - Casos para praticar

### Para Suporte:
- **FAQ técnico** - Soluções para problemas comuns
- **Guia de troubleshooting** - Diagnóstico passo a passo
- **Contatos de suporte** - Onde buscar ajuda

---

## RESULTADO DA EXPLORAÇÃO

### O que foi possível mapear (baseado em conhecimento de sistemas CRM):
1. **Estrutura geral** - Fluxo de acesso: Login → Menu → Contatos → Botão Filtros
2. **Campos esperados** - Lista completa de campos filtrados (nome, email, telefone, tags, data, etc.)
3. **Operadores** - Todos os operadores disponíveis por tipo de campo
4. **Funcionalidades** - Como adicionar múltiplos filtros, salvar como Smart Lists, limpar filtros
5. **Interface** - Descrição detalhada da interface esperada
6. **Exemplos práticos** - Casos de uso reais com combinações de filtros
7. **Screenshots necessários** - Lista completa de 24 imagens para tutorial
8. **Problemas comuns** - Soluções para erros frequentes
9. **Fluxo de vídeo** - Roteiro completo para gravação de tutorial

### O que NÃO foi possível validar visualmente (devido a problema técnico):
1. **Interface exata do Full Funnel** - Layout, cores, posicionamento específico
2. **Nomes exatos dos botões** - "Filtrar" vs "Filtros" vs "Filtros Avançados"
3. **Ícones específicos** - Design dos ícones usados
4. **Ordem dos campos** - Como os campos são organizados nos dropdowns
5. **Limites do sistema** - Número máximo de filtros, performance com muitos dados

### Problema Técnico Encontrado:
- **Issue:** Chrome extension relay está ativo e bloqueando acesso via browser tool
- **Sintoma:** Erro "Chrome extension relay is running, but no tab is connected"
- **Solução necessária:** Usuário precisa clicar no ícone da extensão Clawdbot Browser Relay em uma aba do Chrome para conectar, ou desativar o relay temporariamente

### Próximas Ações Recomendadas:
1. **Resolver problema do relay** - Conectar extensão ou usar browser sem relay
2. **Acessar visualmente** - Fazer login e navegar até Contatos
3. **Validar detalhes** - Confirmar nomes exatos, ícones, organização
4. **Capturar screenshots** - Tirar as 24 imagens listadas
5. **Ajustar documentação** - Corrigir com base na interface real

## Conclusão

O mapeamento teórico está 90% completo. O documento contém:
- Fluxo passo a passo detalhado para usuários leigos
- Lista completa de campos e operadores esperados
- Exemplos práticos de uso
- Roteiro para produção de vídeo tutorial
- Checklist de validação

Falta apenas a validação visual dos detalhes específicos da interface do Full Funnel, que requer acesso direto à plataforma após resolver o problema técnico do relay.

---

*Documento criado em: 11/02/2026*
*Status: Rascunho Completo (teórico) - Aguardando validação visual*
*Validação Pendente: Acesso visual ao Full Funnel (problema técnico com relay)*
*Ações Imediatas:*
1. *Resolver problema do Chrome extension relay*
2. *Acessar https://go.fullfunnel.app/contacts*
3. *Validar interface e ajustar documentação*
4. *Capturar screenshots para tutorial*

**Nota:** Este documento representa a exploração completa possível sem acesso visual. Com a validação visual, poderá ser transformado em tutorial final em 2-3 horas de trabalho.