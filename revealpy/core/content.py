# core/content.py
from dataclasses import dataclass
from typing import List, Optional, Union
from enum import Enum

from revealpy.core.layouts import LayoutType, LayoutConfig


class ContentType(Enum):
    TEXT = "text"
    BULLET_LIST = "bullet_list"
    NUMBERED_LIST = "numbered_list"
    EQUATION = "equation"
    IMAGE = "image"
    CODE = "code"
    TABLE = "table"
    DIAGRAM = "diagram"
    MEDIA = "media"
    MARKDOWN = "markdown"  # New content type


@dataclass
class Content:
    type: ContentType
    value: Union[str, List[str], dict]


class SlideBuilder:
    """
    Builder class for creating and configuring slides.

    The SlideBuilder provides a fluent interface for adding content and configuring
    the layout of individual slides. It supports various types of content and
    layout options.

    Args:
        title (str): The title of the slide.
        layout (LayoutType, optional): The layout type for the slide.
            Defaults to LayoutType.TITLE_CONTENT.

    Examples:
        >>> slide = presentation.create_slide("My Slide")
        >>> slide.add_text("Some content")
        >>>
        >>> # Using method chaining
        >>> slide = presentation.create_slide("Two Columns") \\
        ...     .set_layout(LayoutType.TWO_COLUMNS) \\
        ...     .add_to_column(0, Content(ContentType.TEXT, "Left content")) \\
        ...     .add_to_column(1, Content(ContentType.TEXT, "Right content"))
    """
    def __init__(self, title: str, layout: LayoutType = LayoutType.TITLE_CONTENT):
        self.title = title
        self.layout = layout
        self.layout_config = LayoutConfig(type=layout)
        self.contents: List[Content] = []
        self.columns: List[List[Content]] = [[], []]  # For two-column layouts
        self.is_markdown = False  # New flag for markdown slides

    def set_layout(self, layout: LayoutType) -> 'SlideBuilder':
        """
        Sets the layout type for the slide.

        Args:
            layout (LayoutType): The desired layout type.
                See LayoutType enum for available options.

        Returns:
            SlideBuilder: The slide builder instance for method chaining.

        Examples:
            >>> slide.set_layout(LayoutType.TWO_COLUMNS)
        """
        self.layout = layout
        self.layout_config.type = layout
        return self

    def configure_layout(self,
                         title_size: str = "h2",
                         content_align: str = "left",
                         background: Optional[str] = None,
                         extra_classes: Optional[List[str]] = None) -> 'SlideBuilder':
        """
        Configures the layout options for the slide.

        Args:
            title_size (str, optional): Size of the title. Defaults to "h2".
                Options: "h1", "h2", "h3"
            content_align (str, optional): Content alignment. Defaults to "left".
                Options: "left", "center", "right"
            background (str, optional): Background color or image URL.
                Can be hex color (#ff0000), named color (red), or URL.
            extra_classes (List[str], optional): Additional CSS classes to apply.

        Returns:
            SlideBuilder: The slide builder instance for method chaining.

        Examples:
            >>> slide.configure_layout(
            ...     title_size="h1",
            ...     content_align="center",
            ...     background="#f0f0f0",
            ...     extra_classes=["custom-slide", "dark-mode"]
            ... )
        """
        self.layout_config = LayoutConfig(
            type=self.layout,
            title_size=title_size,
            content_align=content_align,
            background=background,
            extra_classes=extra_classes or []
        )
        return self

    def add_to_column(self, column: int, content: Content) -> 'SlideBuilder':
        """
        Adds content to a specific column in two-column layouts.

        Args:
            column (int): The column index (0 for left, 1 for right).
            content (Content): The content to add to the column.

        Returns:
            SlideBuilder: The slide builder instance for method chaining.

        Raises:
            ValueError: If the slide layout is not TWO_COLUMNS or COMPARISON,
                or if the column index is not 0 or 1.

        Examples:
            >>> slide.set_layout(LayoutType.TWO_COLUMNS)
            >>> slide.add_to_column(0, Content(ContentType.TEXT, "Left side"))
            >>> slide.add_to_column(1, Content(ContentType.TEXT, "Right side"))
        """
        if self.layout not in [LayoutType.TWO_COLUMNS, LayoutType.COMPARISON]:
            raise ValueError("Column-specific content only available in two-column layouts")
        if column not in [0, 1]:
            raise ValueError("Column must be 0 or 1")
        self.columns[column].append(content)
        return self

    def add_comparison(self, left_title: str, right_title: str) -> 'SlideBuilder':
        """
        Sets up a comparison slide with column headers.

        Args:
            left_title (str): The title for the left column.
            right_title (str): The title for the right column.

        Returns:
            SlideBuilder: The slide builder instance for method chaining.

        Raises:
            ValueError: If the slide layout is not COMPARISON.

        Examples:
            >>> slide.set_layout(LayoutType.COMPARISON)
            >>> slide.add_comparison("Before", "After")
            >>> slide.add_to_column(0, Content(ContentType.TEXT, "Old version"))
            >>> slide.add_to_column(1, Content(ContentType.TEXT, "New version"))
        """
        if self.layout != LayoutType.COMPARISON:
            raise ValueError("Comparison headers only available in comparison layout")
        self.comparison_headers = (left_title, right_title)
        return self

    def add_text(self, text: str) -> 'SlideBuilder':
        """
        Adds text content to the slide.

        Args:
            text (str): The text content to add.

        Returns:
            SlideBuilder: The slide builder instance for method chaining.

        Examples:
            >>> slide.add_text("This is a paragraph of text.")
        """
        self.contents.append(Content(ContentType.TEXT, text))
        return self

    def add_bullet_points(self, points: List[str]) -> 'SlideBuilder':
        """
        Adds a bullet point list to the slide.

        Args:
            points (List[str]): List of bullet points.

        Returns:
            SlideBuilder: The slide builder instance for method chaining.

        Examples:
            >>> slide.add_bullet_points([
            ...     "First point",
            ...     "Second point",
            ...     "Third point"
            ... ])
        """
        self.contents.append(Content(ContentType.BULLET_LIST, points))
        return self

    def add_numbered_list(self, items: List[str]) -> 'SlideBuilder':
        self.contents.append(Content(ContentType.NUMBERED_LIST, items))
        return self

    def add_equation(self, equation: str, description: Optional[dict] = None) -> 'SlideBuilder':
        self.contents.append(Content(ContentType.EQUATION, {
            'equation': equation,
            'description': description or {}
        }))
        return self

    def add_image(self, url: str, caption: Optional[str] = None) -> 'SlideBuilder':
        self.contents.append(Content(ContentType.IMAGE, {
            'url': url,
            'caption': caption
        }))
        return self

    def add_code(self, code: str, language: str = "python") -> 'SlideBuilder':
        """
        Adds a code block to the slide.

        Args:
            code (str): The code content.
            language (str, optional): The programming language for syntax highlighting.
                Defaults to "python".

        Returns:
            SlideBuilder: The slide builder instance for method chaining.

        Examples:
            >>> slide.add_code('''
            ... def hello_world():
            ...     print("Hello, World!")
            ... ''', language="python")
        """
        self.contents.append(Content(ContentType.CODE, {
            'code': code,
            'language': language
        }))
        return self

    def add_table(self, headers: List[str], rows: List[List[str]]) -> 'SlideBuilder':
        self.contents.append(Content(ContentType.TABLE, {
            'headers': headers,
            'rows': rows
        }))
        return self

    def add_diagram(self, diagram_code: str) -> 'SlideBuilder':
        self.contents.append(Content(ContentType.DIAGRAM, diagram_code))
        return self

    def add_media(self, url: str, media_type: str = "video") -> 'SlideBuilder':
        if media_type not in ["video", "audio"]:
            raise ValueError("media_type must be either 'video' or 'audio'")
        self.contents.append(Content(ContentType.MEDIA, {
            'url': url,
            'type': media_type
        }))
        return self


    def add_markdown(self, markdown_content: str) -> 'SlideBuilder':
        """
        Adds markdown content to the slide.

        The markdown content will be processed by Reveal.js's markdown parser.
        Supports standard markdown syntax including headers, lists, code blocks,
        and more.

        Args:
            markdown_content (str): The markdown formatted content.

        Returns:
            SlideBuilder: The slide builder instance for method chaining.
        """
        self.is_markdown = True
        self.contents.append(Content(ContentType.MARKDOWN, markdown_content))
        return self