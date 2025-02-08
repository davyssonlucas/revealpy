from typing import List
from revealpy.utils.export_pptx import PPTXExporter
from revealpy.utils.helpers import load_template
from .content import SlideBuilder
from .exporter import Exporter
from .html_generator import HTMLGenerator

class Presentation:
    """
    Main class for creating and managing presentations.

    The Presentation class serves as the entry point for creating slides and managing
    the overall presentation settings. It handles the creation of slides, rendering
    of the presentation, and exporting to different formats.

    Args:
        theme (str, optional): The presentation theme. Defaults to "black".
            Available themes: "black", "white", "league", "beige", "sky", "night",
            "serif", "simple", "solarized", "moon", "dracula"
        transition (str, optional): The transition effect between slides. Defaults to "fade".
            Available transitions: "none", "fade", "slide", "convex", "concave", "zoom"

    Examples:
        >>> from revealpy import Presentation
        >>> # Create a new presentation with default theme and transition
        >>> pres = Presentation()
        >>>
        >>> # Create a presentation with custom theme and transition
        >>> pres = Presentation(theme="night", transition="slide")
    """
    def __init__(self, theme: str = "black", transition: str = "fade", enable_pdf_export: bool = False):
        """
        Initialize a new presentation.

        Args:
            theme (str): The presentation theme. Defaults to "black"
            transition (str): Slide transition effect. Defaults to "fade"
            enable_pdf_export (bool): Whether to enable PDF export functionality. Defaults to False
        """
        self.theme = theme
        self.transition = transition
        self.enable_pdf_export = enable_pdf_export
        self.slides: List[SlideBuilder] = []

    def create_slide(self, title: str) -> SlideBuilder:
        """
        Creates a new slide in the presentation.

        Args:
            title (str): The title of the slide.

        Returns:
            SlideBuilder: A builder object for adding content to the slide.

        Examples:
            >>> pres = Presentation()
            >>> # Create a simple slide
            >>> slide = pres.create_slide("Introduction")
            >>> slide.add_text("Welcome to my presentation")
        """
        slide = SlideBuilder(title)
        self.slides.append(slide)
        return slide

    def render(self, auto: bool = False) -> str:
        """
        Renders the presentation as HTML.

        Args:
            auto (bool): Auto slides.

        Returns:
            str: The complete HTML content of the presentation.

        Examples:
            >>> pres = Presentation()
            >>> html_content = pres.render()
            >>> with open('presentation.html', 'w') as f:
            ...     f.write(html_content)
        """
        return self._generate_html(auto)

    def export(self, filename: str, auto: bool = False):
        """
        Exports the presentation to an HTML file.

        Args:
            filename (str): The path where the HTML file will be saved.
                Should end with '.html' extension.
            auto (bool): Auto slides.

        Examples:
            >>> pres = Presentation()
            >>> pres.export("my_presentation.html")
        """
        html_content = self._generate_html(auto)
        Exporter.export(filename, html_content)

    def export_pptx(self, filename: str = "presentation.pptx"):
        """
        Exports the presentation to PowerPoint format.

        Args:
            filename (str, optional): The path where the PPTX file will be saved.
                Defaults to "presentation.pptx".

        Examples:
            >>> pres = Presentation()
            >>> pres.export_pptx("my_presentation.pptx")
        """
        exporter = PPTXExporter(self)
        exporter.convert_to_pptx(filename)

    def _generate_html(self, auto: bool = False) -> str:
        """
        Generate the complete HTML for the presentation.

        Args:
            auto (bool): Auto slides.
        """
        slides_html = []

        for slide in self.slides:
            contents_html = HTMLGenerator.generate_slide_html(slide)
            slides_html.append(contents_html)

        return load_template(
            self.theme,
            self.transition,
            "\n".join(slides_html),
            self.enable_pdf_export,
            auto
        )
