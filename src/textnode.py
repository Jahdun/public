from enum import Enum

class TextType(Enum):
    Normal = "Normal Text"
    Bold = "Bold Text"
    Italic = "Italic Text"
    Code = "Code Text"
    Links = "Links"
    Images = "Images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url 
    
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url   
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

