<h1>
    <p align="center">
        <!-- Logo Section -->
        <img src="./assets/revealpy_logo.webp" width="150" height="auto" alt="Logo RevealPy"/>
        <br>
        <!-- Badges -->
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
        <img src="https://img.shields.io/github/issues/davyssonlucas/revealpy" alt="Issues Abertas"/>
        <img src="https://img.shields.io/github/issues-pr/davyssonlucas/revealpy" alt="Pull Requests"/>
        <img src="https://img.shields.io/github/contributors/davyssonlucas/revealpy" alt="Contribuidores"/>
    </p>
</h1>
RevealPy is a Python library for creating beautiful and interactive presentations programmatically. It provides a simple yet powerful API to create presentations with various content types and layouts.

## Installation

```bash
pip install revealpy
```

## Quick Start

```python
from revealpy import Presentation
from revealpy import LayoutType

# Create a new presentation
presentation = Presentation(theme="black", transition="fade")

# Create a title slide
slide = presentation.create_slide("My First Presentation")
slide.add_text("Created with RevealPy")

# Export the presentation
presentation.export("my_presentation.html")
```

## Core Components

### Presentation Class

The main class for creating presentations.

```python
presentation = Presentation(
    theme="black",     # Presentation theme
    transition="fade"  # Slide transition effect
)
```

Methods:
- `create_slide(title: str) -> SlideBuilder`: Creates a new slide
- `render() -> str`: Renders the presentation as HTML
- `export(filename: str)`: Exports the presentation to HTML
- `export_pptx(filename: str)`: Exports the presentation to PowerPoint format

### SlideBuilder Class

Used to build individual slides with various content types and layouts.

#### Basic Methods

```python
slide = presentation.create_slide("Slide Title")

# Add different types of content
slide.add_text("Simple text content")
slide.add_bullet_points(["Point 1", "Point 2", "Point 3"])
slide.add_numbered_list(["First item", "Second item"])
slide.add_code("print('Hello World')", language="python")
```

#### Layout Configuration

```python
slide.set_layout(LayoutType.TWO_COLUMNS)
slide.configure_layout(
    title_size="h2",
    content_align="left",
    background="#f0f0f0",
    extra_classes=["custom-class"]
)
```

## Available Layout Types

- `TITLE`: Only title
- `TITLE_CONTENT`: Title and content
- `TWO_COLUMNS`: Title and two columns
- `TITLE_TWO_CONTENT`: Title and content in two rows
- `COMPARISON`: Title and two columns with headers
- `SECTION`: Big title for section breaks
- `BLANK`: Blank slide for custom content
- `IMAGE_WITH_CAPTION`: Centered image with caption
- `QUOTE`: Quote with optional attribution

## Content Types

### Text Content
```python
slide.add_text("Regular paragraph text")
```

### Lists
```python
slide.add_bullet_points([
    "First bullet point",
    "Second bullet point",
    "Third bullet point"
])

slide.add_numbered_list([
    "First numbered item",
    "Second numbered item"
])
```

### Code Blocks
```python
slide.add_code(
    code="def hello_world():\n    print('Hello, World!')",
    language="python"
)
```

### Images
```python
slide.add_image(
    url="path/to/image.jpg",
    caption="Optional image caption"
)
```

### Equations
```python
slide.add_equation(
    equation="E = mc^2",
    description={
        "E": "Energy",
        "m": "Mass",
        "c": "Speed of light"
    }
)
```

### Tables
```python
slide.add_table(
    headers=["Name", "Age", "City"],
    rows=[
        ["John", "25", "New York"],
        ["Alice", "30", "London"]
    ]
)
```

### Diagrams
```python
slide.add_diagram("""
    graph TD
    A[Start] --> B[Process]
    B --> C[End]
""")
```

### Media
```python
slide.add_media(
    url="path/to/video.mp4",
    media_type="video"  # or "audio"
)
```

### Markdown
```python
slide.add_markdown("""
# Markdown Title
- Point 1
- Point 2

```python
print('Code block')
```
""")
```

## Working with Two-Column Layouts

When using `TWO_COLUMNS` or `COMPARISON` layouts:

```python
slide = presentation.create_slide("Two Columns Example")
slide.set_layout(LayoutType.TWO_COLUMNS)

# Add content to left column
slide.add_to_column(0, Content(ContentType.TEXT, "Left column content"))

# Add content to right column
slide.add_to_column(1, Content(ContentType.TEXT, "Right column content"))
```

For comparison layouts:
```python
slide = presentation.create_slide("Comparison")
slide.set_layout(LayoutType.COMPARISON)
slide.add_comparison("Before", "After")
```

## Export Options

### HTML Export
```python
# Export to HTML
presentation.export("presentation.html")
```

### PowerPoint Export
```python
# Export to PowerPoint
presentation.export_pptx("presentation.pptx")
```

## Best Practices

1. **Consistent Layouts**: Use consistent layouts throughout your presentation for better visual coherence.
2. **Content Organization**: Break down complex content into multiple slides.
3. **Visual Hierarchy**: Use different title sizes and layouts to create clear visual hierarchy.
4. **Media Usage**: Optimize images and media files before adding them to the presentation.
5. **Transitions**: Use subtle transitions for professional presentations.

## Examples

### Creating a Complete Presentation

```python
from revealpy import Presentation
from revealpy import LayoutType

# Create presentation
pres = Presentation(theme="black")

# Title slide
title_slide = pres.create_slide("RevealPy Presentation")
title_slide.add_text("Created with Python")

# Content slide
content_slide = pres.create_slide("Key Features")
content_slide.add_bullet_points([
    "Easy to use API",
    "Multiple layout options",
    "Support for various content types",
    "Export to HTML and PowerPoint"
])

# Two-column slide
compare_slide = pres.create_slide("Comparison")
compare_slide.set_layout(LayoutType.COMPARISON)
compare_slide.add_comparison("Traditional", "RevealPy")
compare_slide.add_to_column(0, Content(ContentType.TEXT, "Manual creation"))
compare_slide.add_to_column(1, Content(ContentType.TEXT, "Programmatic creation"))

# Export
pres.export("example_presentation.html")
```
## 🤝 Contributing
- Contributions and bug fixes are welcome! If you'd like to contribute, fork the repository and submit a pull request. For versioning, use GitFlow.
[Cheatsheet do git-flow](https://danielkummer.github.io/git-flow-cheatsheet/index.pt_BR.html)
- If you have any questions or want to discuss something, open an issue in the repository.