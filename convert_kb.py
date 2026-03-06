#!/usr/bin/env python3
"""Converte arquivos MD da KB para HTML estático."""

import os
import re
import markdown
from pathlib import Path

SOURCE_DIR = Path("/Users/macmini/clawd/docs/kb-detalhada")
OUTPUT_DIR = Path("/Users/macmini/clawd/repos/full-tips-site/kb")

# Substituições de marca
REPLACEMENTS = [
    (r'\bGoHighLevel\b', 'Full Funnel'),
    (r'\bGHL\b', 'Full Funnel'),
    (r'\bHighLevel\b', 'Full Funnel'),
    (r'\bLeadConnector\b', 'Full Funnel'),
    (r'\bgohighlevel\b', 'fullfunnel'),
    (r'\bhighlevel\b', 'fullfunnel'),
]

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <title>{title} — Full Funnel Central de Ajuda</title>
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #1a1a1a;
            background: #fafafa;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #111; margin-top: 0; font-size: 2em; border-bottom: 2px solid #0066cc; padding-bottom: 10px; }}
        h2 {{ color: #333; margin-top: 2em; font-size: 1.5em; }}
        h3 {{ color: #444; margin-top: 1.5em; font-size: 1.25em; }}
        h4 {{ color: #555; margin-top: 1em; }}
        p {{ margin: 1em 0; }}
        ul, ol {{ padding-left: 1.5em; }}
        li {{ margin: 0.5em 0; }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'SF Mono', Monaco, monospace;
            font-size: 0.9em;
        }}
        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        pre code {{ background: none; padding: 0; }}
        blockquote {{
            border-left: 4px solid #0066cc;
            margin: 1em 0;
            padding: 0.5em 1em;
            background: #f9f9f9;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1em 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        th {{ background: #f4f4f4; font-weight: 600; }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .breadcrumb {{
            margin-bottom: 20px;
            font-size: 0.9em;
        }}
        .breadcrumb a {{ color: #666; }}
        footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        strong {{ color: #111; }}
        hr {{ border: none; border-top: 1px solid #eee; margin: 2em 0; }}
    </style>
</head>
<body>
    <div class="container">
        <nav class="breadcrumb">
            <a href="/kb/">← Central de Ajuda</a>
        </nav>
        {content}
        <footer>
            © Full Funnel — Central de Ajuda
        </footer>
    </div>
</body>
</html>
'''

INDEX_TEMPLATE = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Central de Ajuda Full Funnel - Tutoriais, guias e documentação da plataforma.">
    <title>Central de Ajuda — Full Funnel</title>
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #1a1a1a;
            background: #fafafa;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #111; margin-top: 0; font-size: 2em; text-align: center; }}
        .subtitle {{ text-align: center; color: #666; margin-bottom: 30px; }}
        .categories {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px; }}
        .category {{
            background: #f9f9f9;
            border: 1px solid #eee;
            border-radius: 6px;
            padding: 15px 20px;
            transition: all 0.2s;
        }}
        .category:hover {{
            border-color: #0066cc;
            box-shadow: 0 2px 8px rgba(0,102,204,0.1);
        }}
        .category a {{
            color: #0066cc;
            text-decoration: none;
            font-weight: 500;
            display: block;
        }}
        .category a:hover {{ text-decoration: underline; }}
        .category .desc {{
            font-size: 0.85em;
            color: #666;
            margin-top: 5px;
        }}
        footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        .back {{ margin-bottom: 20px; }}
        .back a {{ color: #666; text-decoration: none; font-size: 0.9em; }}
        .back a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <nav class="back">
            <a href="/">← Voltar ao site</a>
        </nav>
        <h1>📚 Central de Ajuda</h1>
        <p class="subtitle">Documentação e tutoriais da plataforma Full Funnel</p>
        <div class="categories">
{articles}
        </div>
        <footer>
            © Full Funnel — Central de Ajuda
        </footer>
    </div>
</body>
</html>
'''

# Títulos amigáveis para os artigos
FRIENDLY_TITLES = {
    'afiliados': 'Programa de Afiliados',
    'area-membros-geral': 'Área de Membros — Visão Geral',
    'area-membros': 'Área de Membros',
    'automacao-comentarios-redes': 'Automação de Comentários em Redes',
    'automacoes-acoes': 'Automações — Ações',
    'automacoes-condicoes': 'Automações — Condições',
    'automacoes-gatilho-oportunidade': 'Automações — Gatilhos de Oportunidade',
    'automacoes-gatilhos': 'Automações — Gatilhos',
    'automacoes-geral': 'Automações — Visão Geral',
    'automacoes-introducao': 'Automações — Introdução',
    'automacoes': 'Automações Completo',
    'calendario-aulas': 'Calendário de Aulas',
    'calendario-coletivo': 'Calendário Coletivo',
    'calendario-disponibilidade': 'Calendário — Disponibilidade',
    'calendario-geral': 'Calendários — Visão Geral',
    'calendario-grupo': 'Calendário de Grupo',
    'calendario-round-robin': 'Calendário Round Robin',
    'calendario-servicos': 'Calendário de Serviços',
    'calendarios': 'Calendários Completo',
    'chat-widgets': 'Chat Widgets',
    'configuracoes-equipe': 'Configurações de Equipe',
    'contatos-acoes-massa': 'Contatos — Ações em Massa',
    'contatos-campos-personalizados': 'Contatos — Campos Personalizados',
    'contatos-duplicados': 'Contatos Duplicados',
    'contatos-listas': 'Contatos e Listas',
    'conversas-geral': 'Conversas — Visão Geral',
    'conversas-ia': 'Conversas com IA',
    'conversas': 'Conversas',
    'dominios': 'Domínios',
    'email-campanhas': 'E-mail — Campanhas',
    'email-configuracao': 'E-mail — Configuração',
    'email-geral': 'E-mail — Visão Geral',
    'facebook-anuncios': 'Facebook Anúncios',
    'facebook-geral': 'Facebook — Visão Geral',
    'facebook-messenger': 'Facebook Messenger',
    'formularios': 'Formulários',
    'funis-paginas': 'Funis e Páginas',
    'geral': 'Informações Gerais',
    'instagram-conectar': 'Instagram — Conectar',
    'instagram-geral': 'Instagram — Visão Geral',
    'instagram-mensagens': 'Instagram — Mensagens',
    'instagram-publicacoes': 'Instagram — Publicações',
    'oportunidades': 'Oportunidades (Pipeline)',
    'pagamentos': 'Pagamentos',
    'planos-precos': 'Planos e Preços',
    'relatorios': 'Relatórios',
    'reputacao': 'Reputação',
    'sites-blogs': 'Sites e Blogs',
    'sobre-fullfunnel': 'Sobre Full Funnel',
    'social-planner': 'Social Planner',
    'trigger-links': 'Trigger Links',
    'tutoriais-video': 'Tutoriais em Vídeo',
    'whatsapp-conectar': 'WhatsApp — Conectar',
    'whatsapp-geral': 'WhatsApp — Visão Geral',
    'whatsapp-precos': 'WhatsApp — Preços',
    'whatsapp-templates': 'WhatsApp — Templates',
}

def apply_replacements(text: str) -> str:
    """Aplica substituições de marca."""
    for pattern, replacement in REPLACEMENTS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def extract_description(content: str) -> str:
    """Extrai descrição do conteúdo (primeiros 160 chars do primeiro parágrafo)."""
    # Remove headers
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('*') and not line.startswith('-'):
            # Limpa markdown
            desc = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
            desc = re.sub(r'\*\*([^*]+)\*\*', r'\1', desc)
            desc = re.sub(r'\*([^*]+)\*', r'\1', desc)
            desc = desc[:160].strip()
            if len(desc) > 150:
                desc = desc[:150] + '...'
            return desc
    return 'Documentação Full Funnel'

def extract_title(content: str, filename: str) -> str:
    """Extrai título do conteúdo ou usa nome amigável."""
    # Tenta encontrar H1
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return apply_replacements(match.group(1).strip())
    # Fallback para título amigável
    return FRIENDLY_TITLES.get(filename, filename.replace('-', ' ').title())

def convert_md_to_html(md_content: str) -> str:
    """Converte Markdown para HTML."""
    # Aplica substituições antes de converter
    md_content = apply_replacements(md_content)
    
    # Converte para HTML
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
    html = md.convert(md_content)
    
    return html

def process_file(md_file: Path) -> dict:
    """Processa um arquivo MD e retorna info."""
    filename = md_file.stem
    
    # Lê conteúdo
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extrai metadados
    title = extract_title(content, filename)
    description = apply_replacements(extract_description(content))
    
    # Converte para HTML
    html_content = convert_md_to_html(content)
    
    # Gera HTML final
    final_html = HTML_TEMPLATE.format(
        title=title,
        description=description,
        content=html_content
    )
    
    # Cria diretório e salva
    output_dir = OUTPUT_DIR / filename
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / 'index.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"✓ {filename}")
    
    return {
        'slug': filename,
        'title': title,
        'description': description[:100] + '...' if len(description) > 100 else description
    }

def generate_index(articles: list):
    """Gera página de índice."""
    # Ordena por título
    articles.sort(key=lambda x: x['title'])
    
    # Gera HTML dos artigos
    articles_html = ""
    for article in articles:
        articles_html += f'''            <div class="category">
                <a href="/kb/{article['slug']}/">{article['title']}</a>
                <div class="desc">{article['description']}</div>
            </div>
'''
    
    # Gera HTML final
    final_html = INDEX_TEMPLATE.format(articles=articles_html)
    
    # Salva
    output_file = OUTPUT_DIR / 'index.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"\n✓ Índice gerado com {len(articles)} artigos")

def main():
    """Função principal."""
    print("🔄 Convertendo artigos MD para HTML...\n")
    
    # Garante que diretório de saída existe
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Processa todos os arquivos MD (exceto _index.md)
    articles = []
    for md_file in sorted(SOURCE_DIR.glob('*.md')):
        if md_file.name == '_index.md':
            continue
        
        try:
            info = process_file(md_file)
            articles.append(info)
        except Exception as e:
            print(f"✗ {md_file.name}: {e}")
    
    # Gera índice
    generate_index(articles)
    
    print(f"\n✅ Conversão completa! {len(articles)} artigos em /kb/")

if __name__ == '__main__':
    main()
