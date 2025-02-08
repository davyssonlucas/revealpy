from revealpy import LayoutType, Presentation, Content, ContentType

def slide_titulo(pres, titulo, subtitulo):
    pres.create_slide(titulo) \
        .set_layout(LayoutType.TITLE) \
        .configure_layout(title_size="h1", content_align="center", background="#1a237e") \
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

pres = Presentation(theme="black", transition="fade", enable_pdf_export=True)

slide_titulo(pres, "Eletricidade Básica", "Uma introdução aos conceitos fundamentais")
slide_texto(pres, "O que é Eletricidade?",
            "A eletricidade é o fluxo de cargas elétricas, sendo uma das formas fundamentais de energia.",
            ["Movimento de elétrons gera corrente elétrica.", "Transformação em calor, luz e movimento."])

slide_imagem(pres, "Exemplo de Circuito",
             "https://www.flippingphysics.com/uploads/2/1/1/0/21103672/0350-animated-gif-1-one-resistor_orig.gif",
             "Circuito básico com resistor e fonte")

slide_equacao(pres, "Lei de Ohm", "V = I \\cdot R",
              {"V": "Tensão (Volts)", "I": "Corrente (Ampères)", "R": "Resistência (Ohms)"})

slide_tabela(pres, "Unidades e Símbolos",
             ["Grandeza", "Unidade", "Símbolo"],
             [["Corrente", "Ampere", "A"],
              ["Tensão", "Volt", "V"],
              ["Resistência", "Ohm", "Ω"],
              ["Potência", "Watt", "W"]])

slide_codigo(pres, "Exemplo de Código: Lei de Ohm", """
# Cálculo da Lei de Ohm
voltage = 9  # Voltagem em Volts
resistance = 3  # Resistência em Ohms
current = voltage / resistance
print(f'Corrente: {current} A')
""")

pres.create_slide("Diagrama de Circuito") \
    .add_diagram("""
graph TD;
    A[Fonte de Energia] -->|Corrente| B[Resistor 1];
    B -->|Corrente| C[Resistor 2];
    C -->|Corrente| D[Terra];
    """)

pres.create_slide("Vídeo Didático") \
    .add_media(
        url="https://www.youtube.com/watch?v=c3KAW6LOcSY",
        media_type="video"
    )

pres.export("output/eletricidade_basica.html")
