from revealpy import LayoutType, Presentation, Content, ContentType


def slide_titulo(pres, titulo, subtitulo):
    pres.create_slide(titulo) \
        .set_layout(LayoutType.TITLE) \
        .configure_layout(title_size="h1", content_align="center", background="#212121") \
        .add_text(subtitulo)


def slide_texto(pres, titulo, texto, bullets=None):
    slide = pres.create_slide(titulo).add_text(texto)
    if bullets:
        slide.add_bullet_points(bullets)


def slide_imagem(pres, titulo, url, legenda=""):
    pres.create_slide(titulo) \
        .set_layout(LayoutType.IMAGE_WITH_CAPTION) \
        .add_image(url=url, caption=legenda)


def slide_tabela(pres, titulo, headers, rows):
    pres.create_slide(titulo).add_table(headers=headers, rows=rows)


def slide_codigo(pres, titulo, codigo):
    pres.create_slide(titulo).add_code(codigo)


def slide_equacao(pres, titulo, equacao, descricao):
    pres.create_slide(titulo).add_equation(equation=equacao, description=descricao)


# Cria a apresentação
pres = Presentation(theme="moon", transition="zoom", enable_pdf_export=True)

# Título da apresentação
slide_titulo(pres, "Apresentação com RevealPy", "Automatizando apresentações de forma programática")

# Slide explicativo: O que é RevealPy?
slide_texto(pres, "O que é RevealPy?",
            "RevealPy é uma biblioteca em Python que facilita a criação de apresentações interativas.",
            ["Criação programática de slides.", "Suporte a diversos tipos de conteúdo.", "Exportação para HTML e PDF."])

# Slide de imagem: Exemplo do resultado
slide_imagem(pres, "Exemplo de Slide com Imagem:",
             "https://revealjs.com/images/logo/reveal-black-text.svg",
             "Reveal.js: A base visual das apresentações geradas pelo RevealPy.")

# Slide de código: Exemplo mínimo
slide_codigo(pres, "Exemplo de Slide com Código:", """
from revealpy import Presentation

# Criar apresentação com tema "black" e transição "fade"
presentation = Presentation(theme="black", transition="fade")

# Criar slide inicial
slide = presentation.create_slide("Criando Apresentações com RevealPy")
slide.add_text("Fácil e rápido!")

# Exportar
presentation.export("minha_apresentacao.html")
""")

# Slide de tabela: Principais recursos
slide_tabela(pres, "Recursos Principais",
             ["Recurso", "Descrição"],
             [["Layouts", "Vários layouts prontos como 'Título', 'Duas Colunas', 'Imagem com Legenda'."],
              ["Conteúdos", "Texto, listas, código, equações, tabelas, diagramas e mídia."],
              ["Exportação", "Exporta para HTML e formato PDF com facilidade."]])

# Slide de equação: Possibilidades avançadas
slide_equacao(pres, "Exemplo de Slide com Equações", "E = mc^2",
              {"E": "Energia", "m": "Massa", "c": "Velocidade da luz"})

# Slide de comparação: RevealPy vs Métodos Manuais
pres.create_slide("RevealPy vs Criação Manual") \
    .set_layout(LayoutType.COMPARISON) \
    .add_comparison("Criação Manual", "Com RevealPy") \
    .add_to_column(0, Content(ContentType.IMAGE, {
            'url': "https://img.buzzfeed.com/buzzfeed-static/static/2017-07/21/13/asset/buzzfeed-prod-fastlane-02/anigif_sub-buzz-22253-1500656718-1.gif",
            'caption': "Criação demorada e trabalhosa."
        })) \
    .add_to_column(1, Content(ContentType.IMAGE, {
            'url': "https://gifdb.com/images/high/dexters-laboratory-day-for-science-oo5ar2xf119ufgfb.gif",
            'caption': "Automação e organização de código."
        }))

pres.create_slide("Exemplo de Slide com Vídeo") \
    .add_media(
        url="https://www.youtube.com/watch?v=VuUcNIxLmiQ",
        media_type="video"
    )

pres.create_slide(".").add_markdown("""
## Comece a Usar RevealPy Agora!
#### Links úteis para começar:
- [GitHub](https://github.com/)
- [pypi.org](https://pypi.org/project/revealpy/)
- [Documentação Oficial](https://revealpy.org)
""")

# Exportação da apresentação
pres.export("output/apresentacao_revealpy.html")
