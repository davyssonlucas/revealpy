def load_template(theme: str, transition: str, slides_content: str, pdf_export: bool = False, auto: bool = False) -> str:
    """
    Load and fill the HTML template for the presentation.

    Args:
        theme (str): Theme name
        transition (str): Transition effect
        slides_content (str): HTML content of all slides
        pdf_export (bool): Whether to include PDF export functionality
        auto (bool): Auto slides.
    """
    auto_slides = """
        autoSlide: 15000,
        loop: true,
    """ if auto else ""
    pdf_plugin = """
        // PDF Export Plugin
    let pdfExportPlugin = { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/pdf-export/pdfexport.js', async: true };
    """ if pdf_export else ""

    pdf_button = """
        <button onclick="exportPDF()" class="pdf-btn">Export to PDF</button>
    """ if pdf_export else ""

    pdf_script = """
        function exportPDF() {
            // Instructions alert
            alert('Para exportar como PDF:\\n\\n' +
                  '1. Pressione Ctrl+P (Cmd+P no Mac)\\n' +
                  '2. Mude o destino para "Salvar como PDF"\\n' +
                  '3. Em Mais configurações:\\n' +
                  '   - Ative a opção "Gráficos em segundo plano"\\n' +
                  '   - Defina a orientação como "Paisagem"\\n' +
                  '   - Defina as margens como "Nenhuma"\\n' +
                  '4. Clique em Salvar');

            // Trigger print dialog
            window.print();
        }
    """ if pdf_export else ""

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/theme/{theme}.min.css">

        <script src="https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js"></script>

        <!-- Code syntax highlighting -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/highlight/monokai.min.css">

        <style>
            .reveal img {{
                max-width: auto;
                height: auto;
            }}

            .pdf-btn {{
                position: fixed;
                top: 30px;
                right: 30px;
                z-index: 100;
                padding: 10px 20px;
                background: #333;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }}
            .pdf-btn:hover {{
                background: #555;
            }}
            @media print {{
                .pdf-btn {{
                    display: none;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="reveal">
            <div class="slides">
                {slides_content}
            </div>
        </div>

        {pdf_button}

        <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/markdown/markdown.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/highlight/highlight.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/math/math.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/zoom/zoom.min.js"></script>

        <script>
            {pdf_script}

            {pdf_plugin}
            
            Reveal.initialize({{
                {auto_slides}
                view: 'scroll',
                scrollProgress: true,
                hash: true,
                transition: '{transition}',
                plugins: [
                    RevealMarkdown,
                    RevealHighlight,
                    RevealMath,
                    RevealZoom,
                    pdfExportPlugin
                ]
            }});
        </script>
    </body>
    </html>
    """