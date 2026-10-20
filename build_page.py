#!/usr/bin/env python3
"""Render the public policy as static HTML; no app code or credentials are used."""
from pathlib import Path
from html import escape
import sys
import markdown

ROOT = Path(__file__).resolve().parent
url_file = ROOT / 'site-url.txt'
url = sys.argv[1] if len(sys.argv) > 1 else (url_file.read_text().strip() if url_file.exists() else '')
if url:
    assert url.startswith('https://') and url.endswith('/')
    url_file.write_text(url + '\n')
source = (ROOT / 'privacy.md').read_text(encoding='utf-8')
# The page owns the single H1 and metadata, while the full substantive policy remains below.
lines = source.splitlines()
assert lines[0] == '# Política de Privacidade — Hippo Boost'
body_source = '\n'.join(lines[8:])
md = markdown.Markdown(extensions=['toc', 'sane_lists'])
body = md.convert(body_source)
nav = md.toc
summary = 'Informações sobre dados locais, sensores, anúncios, consentimento e contato de privacidade do jogo Hippo Boost para Android.'
absolute_meta = ''
if url:
    absolute_meta = f'<link rel="canonical" href="{escape(url, quote=True)}">\n<meta property="og:url" content="{escape(url, quote=True)}">\n<meta property="og:image" content="{escape(url + "assets/logo.webp", quote=True)}">'
html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="''' + escape(summary, quote=True) + '''">
<meta name="theme-color" content="#123552">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Hippo Boost">
<meta property="og:title" content="Política de Privacidade — Hippo Boost">
<meta property="og:description" content="''' + escape(summary, quote=True) + '''">
<meta name="twitter:card" content="summary">
''' + absolute_meta + '''
<title>Política de Privacidade — Hippo Boost</title>
<link rel="icon" href="assets/favicon.png" type="image/png">
<style>
:root{color-scheme:light;--ink:#183247;--muted:#4e6474;--blue:#086892;--line:#d8e3e9;--paper:#fff;--bg:#f0f5f7}
*{box-sizing:border-box}html{scroll-padding-top:20px}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.75 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
a{color:var(--blue);text-underline-offset:3px;overflow-wrap:anywhere}a:hover{color:#034360}a:focus-visible,summary:focus-visible{outline:3px solid #0781b8;outline-offset:4px;border-radius:3px}
.skip{position:absolute;left:16px;top:-100px;padding:12px;background:#fff;z-index:2}.skip:focus{top:12px}
header{background:#123552;color:#fff;border-bottom:5px solid #54c8e8}.masthead{max-width:1080px;margin:auto;padding:28px 30px;display:flex;align-items:center;gap:24px}.logo{width:104px;height:104px;object-fit:contain;flex:none}.brand{font-weight:750;font-size:23px;letter-spacing:.01em}.brand small{display:block;font-size:14px;letter-spacing:.08em;text-transform:uppercase;color:#bde9f7;font-weight:550}
main{max-width:1080px;margin:0 auto;padding:42px 30px 65px}.intro{margin-bottom:28px}.eyebrow{font-size:13px;font-weight:750;text-transform:uppercase;letter-spacing:.1em;color:var(--blue)}h1{font-size:clamp(31px,5vw,46px);line-height:1.18;letter-spacing:-.035em;margin:9px 0 18px}h2{font-size:24px;line-height:1.35;margin:34px 0 15px;letter-spacing:-.02em}h3{font-size:20px;line-height:1.4;margin-top:28px}.intro p{margin:6px 0;color:var(--muted)}.package{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:14px;overflow-wrap:anywhere}
.layout{display:grid;grid-template-columns:235px minmax(0,1fr);gap:32px;align-items:start}.contents{background:#e7eff3;border:1px solid var(--line);padding:18px;border-radius:12px}.contents summary{font-weight:750;cursor:pointer}.toc ul{padding-left:17px;margin:13px 0 0}.toc li{margin:8px 0;line-height:1.45;font-size:14px}.toc li ul{margin:6px 0}.toc a{text-decoration:none}.toc a:hover{text-decoration:underline}
article{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:12px 34px 34px;box-shadow:0 3px 14px #12355206;min-width:0}article p{margin:14px 0}article ul{padding-left:25px}article li{margin:9px 0}article strong{font-weight:720}article code{background:#f0f5f7;padding:2px 5px;border-radius:4px;overflow-wrap:anywhere}footer{border-top:1px solid var(--line);padding:24px 30px;color:var(--muted);text-align:center;font-size:14px}.footer-inner{max-width:1080px;margin:auto}.footer-inner p{margin:4px 0}
@media(max-width:800px){.layout{grid-template-columns:1fr;gap:20px}.masthead{padding:22px 20px;gap:18px}.logo{width:78px;height:78px}main{padding:28px 18px 42px}.contents{padding:14px 18px}article{padding:5px 22px 24px}body{font-size:16px}.brand{font-size:21px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{header{background:white;color:black;border:0}.brand small{color:#555}body{background:#fff;color:#000;font-size:11pt}.contents,.skip{display:none}.layout{display:block}main{padding:0}article{border:0;padding:0;box-shadow:none}a{color:inherit}h2,h3{break-after:avoid}footer{padding:12px 0}}
</style>
</head>
<body>
<a class="skip" href="#politica">Ir para a política</a>
<header><div class="masthead"><img class="logo" src="assets/logo.webp" width="104" height="104" alt="Logo Hippo Boost"><div class="brand">Hippo Boost<small>Privacidade do jogador</small></div></div></header>
<main>
<section class="intro" aria-labelledby="titulo"><span class="eyebrow">Informações de privacidade</span><h1 id="titulo">Política de Privacidade</h1><p><strong>Hippo Boost · Aplicativo Android</strong></p><p class="package">Pacote: com.plushdrop.mergefofo</p><p>Última atualização: <time datetime="2026-10-19">19 de outubro de 2026</time></p><p>Contato: <a href="mailto:vini.livept2@gmail.com">vini.livept2@gmail.com</a></p></section>
<div class="layout"><nav class="contents" aria-label="Seções da política"><details open><summary>Nesta página</summary>''' + nav + '''</details></nav><article id="politica" aria-label="Texto completo da política de privacidade">''' + body + '''</article></div>
</main>
<footer><div class="footer-inner"><p><strong>Hippo Boost</strong> · Política de Privacidade</p><p>Suporte e privacidade: <a href="mailto:vini.livept2@gmail.com">vini.livept2@gmail.com</a></p></div></footer>
</body>
</html>
'''
(ROOT / 'index.html').write_text(html, encoding='utf-8')
if url:
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + escape(url) + '</loc><lastmod>2026-10-19</lastmod></url></urlset>\n')
print('Página estática gerada:', ROOT / 'index.html')
