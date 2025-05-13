from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal text"
    BOLD_TEXT = "**Bold text**"
    ITALIC_TEXT = "_Italic text_"
    CODE_TEXT = "`Code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"
    FIRE_BENDER = "fire"
