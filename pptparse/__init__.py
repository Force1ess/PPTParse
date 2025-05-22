"""PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides.

This package provides tools to automatically generate presentations from documents,
following a two-phase approach of Analysis and Generation.

For more information, visit: https://github.com/icip-cas/PPTAgent
"""

__version__ = "0.0.1"
__author__ = "Hao Zheng"
__email__ = "wszh712811@gmail.com"

from packaging.version import Version
from pptx import __version__ as PPTXVersion

try:
    PPTXVersion, Mark = PPTXVersion.split("+")
    assert Version(PPTXVersion) >= Version("1.0.4") and Mark == "PPTAgent"
except:
    raise ImportError(
        "You should install the customized `python-pptx` for this project: Force1ess/python-pptx, but got %s."
        % PPTXVersion
    )


from .presentation import Presentation, SlidePage
from .shapes import (
    SHAPECAST,
    Background,
    Closure,
    ClosureType,
    Fill,
    Font,
    FreeShape,
    GroupShape,
    Line,
    Paragraph,
    Picture,
    Placeholder,
    SemanticPicture,
    ShapeElement,
    StyleArg,
    TextBox,
    TextFrame,
    UnsupportedShape,
)
from .utils import Config

__all__ = [
    "Presentation",
    "SlidePage",
    "SHAPECAST",
    "Background",
    "Config",
    "Closure",
    "ClosureType",
    "Fill",
    "Font",
    "FreeShape",
    "GroupShape",
    "Line",
    "Paragraph",
    "Picture",
    "Placeholder",
    "SemanticPicture",
    "ShapeElement",
    "StyleArg",
    "TextBox",
    "TextFrame",
    "UnsupportedShape",
]
