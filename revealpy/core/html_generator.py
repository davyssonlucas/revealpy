# core/html_generator.py
from typing import List, Dict
from .content import Content, ContentType, SlideBuilder
from .layouts import LayoutType

class HTMLGenerator:
    """
    Utility class for converting slide content to HTML.

    This class handles the conversion of various content types to their HTML
    representation, including text, lists, code blocks, images, and more.
    It also manages the generation of complete slide HTML based on different
    layout types.
    """
    @staticmethod
    def content_to_html(content: Content) -> str:
        """
        Converts a Content object to its HTML representation.

        Args:
            content (Content): The content object to convert.

        Returns:
            str: The HTML representation of the content.

        Examples:
            >>> content = Content(ContentType.TEXT, "Hello World")
            >>> html = HTMLGenerator.content_to_html(content)
            >>> print(html)
            '<p>Hello World</p>'
        """
        if content.type == ContentType.MARKDOWN:
            # For Markdown content, we return it as-is since it will be processed by Reveal.js
            return content.value

        if content.type == ContentType.TEXT:
            return f"<p>{content.value}</p>"

        elif content.type == ContentType.BULLET_LIST:
            items = "\n".join(f"<li>{item}</li>" for item in content.value)
            return f"<ul>\n{items}\n</ul>"

        elif content.type == ContentType.NUMBERED_LIST:
            items = "\n".join(f"<li>{item}</li>" for item in content.value)
            return f"<ol>\n{items}\n</ol>"

        elif content.type == ContentType.EQUATION:
            equation = content.value['equation']
            description = content.value.get('description', {})
            desc_html = ""
            if description:
                items = "\n".join(f"<li><strong>{symbol}</strong>: {desc}</li>"
                                  for symbol, desc in description.items())
                desc_html = f"<p>Onde:</p><ul>{items}</ul>"
            return f"<p>$$\n{equation}\n$$</p>\n{desc_html}"

        elif content.type == ContentType.IMAGE:
            url = content.value['url']
            caption = content.value.get('caption', '')
            caption_html = f"<p>{caption}</p>" if caption else ""
            return f'<img src="{url}" alt="{caption}" style="max-width: 100%;">\n{caption_html}'

        elif content.type == ContentType.CODE:
            code = content.value['code']
            language = content.value.get('language', 'python')
            return f'<pre><code class="language-{language}">{code}</code></pre>'

        elif content.type == ContentType.TABLE:
            headers = content.value['headers']
            rows = content.value['rows']
            header_html = "".join(f"<th>{h}</th>" for h in headers)
            rows_html = "".join(
                "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
                for row in rows
            )
            return f"""<table>
                <thead><tr>{header_html}</tr></thead>
                <tbody>{rows_html}</tbody>
            </table>"""

        elif content.type == ContentType.DIAGRAM:
            return f'<div class="mermaid">{content.value}</div>'

        elif content.type == ContentType.MEDIA:
            url = content.value['url']
            media_type = content.value['type']

            if "youtube.com" in url:  # Identifica se o link é do YouTube
                return f'<iframe width="720" height="480" src="{url}" frameborder="0" ' \
                       f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" ' \
                       f'allowfullscreen></iframe>'

            return f'<{media_type} src="{url}" controls style="max-width: 100%;"></{media_type}>'

        return ""

    @staticmethod
    def generate_slide_html(slide: SlideBuilder) -> str:
        """
        Generates complete HTML for a slide based on its layout and content.

        Args:
            slide (SlideBuilder): The slide to generate HTML for.

        Returns:
            str: The complete HTML for the slide.

        Examples:
            >>> slide = presentation.create_slide("Example")
            >>> html = HTMLGenerator.generate_slide_html(slide)
        """
        if slide.is_markdown:
            # Handle Markdown slides differently
            markdown_content = "\n".join(
                content.value if content.type == ContentType.MARKDOWN
                else HTMLGenerator.content_to_html(content)
                for content in slide.contents
            )
            return f"""
            <section data-markdown data-auto-animate>
                <textarea data-template>
                    {markdown_content}
                </textarea>
            </section>
            """
        background = f' data-background="{slide.layout_config.background}"' if slide.layout_config.background else ''
        extra_classes = ' ' + ' '.join(slide.layout_config.extra_classes) if slide.layout_config.extra_classes else ''

        if slide.layout == LayoutType.BLANK:
            return f"""
            <section{background}{extra_classes}>
                {HTMLGenerator._generate_content_html(slide.contents)}
            </section>
            """

        elif slide.layout == LayoutType.SECTION:
            return f"""
            <section{background}{extra_classes} data-auto-animate>
                <h1>{slide.title}</h1>
            </section>
            """

        elif slide.layout in [LayoutType.TWO_COLUMNS, LayoutType.COMPARISON]:
            left_column = HTMLGenerator._generate_content_html(slide.columns[0])
            right_column = HTMLGenerator._generate_content_html(slide.columns[1])

            comparison_headers = ""
            if slide.layout == LayoutType.COMPARISON and hasattr(slide, 'comparison_headers'):
                comparison_headers = f"""
                <div class="comparison-headers">
                    <div class="left-header"><h3>{slide.comparison_headers[0]}</h3></div>
                    <div class="right-header"><h3>{slide.comparison_headers[1]}</h3></div>
                </div>
                """

            return f"""
            <section{background}{extra_classes}>
                <{slide.layout_config.title_size}>{slide.title}</{slide.layout_config.title_size}>
                {comparison_headers}
                <div class="two-columns">
                    <div class="column">{left_column}</div>
                    <div class="column">{right_column}</div>
                </div>
            </section>
            """

        elif slide.layout == LayoutType.QUOTE:
            content = slide.contents[0].value if slide.contents else ""
            attribution = slide.contents[1].value if len(slide.contents) > 1 else ""
            return f"""
            <section{background}{extra_classes}>
                <blockquote>
                    {content}
                    <cite>{attribution}</cite>
                </blockquote>
            </section>
            """

        else:  # Default TITLE_CONTENT layout
            return f"""
            <section{background}{extra_classes} data-auto-animate>
                <{slide.layout_config.title_size}>{slide.title}</{slide.layout_config.title_size}>
                <div class="content {slide.layout_config.content_align}">
                    {HTMLGenerator._generate_content_html(slide.contents)}
                </div>
            </section>
            """

    @staticmethod
    def _generate_content_html(contents: List[Content]) -> str:
        """Generate HTML for a list of content items."""
        return "\n".join(HTMLGenerator.content_to_html(content) for content in contents)