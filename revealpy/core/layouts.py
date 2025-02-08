from enum import Enum
from typing import List, Optional, Dict, Any
from dataclasses import dataclass

class LayoutType(Enum):
    TITLE = "title"  # Only title
    TITLE_CONTENT = "title_content"  # Title and content
    TWO_COLUMNS = "two_columns"  # Title and two columns
    TITLE_TWO_CONTENT = "title_two_content"  # Title and content in two rows
    COMPARISON = "comparison"  # Title and two columns with headers
    SECTION = "section"  # Big title for section breaks
    BLANK = "blank"  # Blank slide for custom content
    IMAGE_WITH_CAPTION = "image_with_caption"  # Centered image with caption
    QUOTE = "quote"  # Quote with optional attribution

@dataclass
class LayoutConfig:
    type: LayoutType
    title_size: str = "h2"  # Can be h1, h2, h3 for different title sizes
    content_align: str = "left"  # left, center, right
    background: Optional[str] = None
    extra_classes: List[str] = None