from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union
import PySide2.QtCore
from . import utils


from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QCommonStyle
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette
from PySide2.QtGui import QPen
from PySide2.QtWidgets import QStyle


if False:
    from typing import Dict, List, Tuple, Union, Optional

class RenderSetupStyle(QCommonStyle):
    """
    This class defines the RenderSetup style and is only used when style sheets and the delegate are not sufficient.
    """
    
    
    
    def __init__(self, parent): ...
    def drawComplexControl(self, control, option, painter, widget='None'): ...
    def drawControl(self, element, option, painter, widget='None'): ...
    def drawItemPixmap(self, painter, rectangle, alignment, pixmap): ...
    def drawItemText(self, painter, rectangle, alignment, palette, enabled, text, textRole='PySide2.QtGui.QPalette.ColorRole.NoRole'): ...
    def drawPrimitive(self, element, option, painter, widget='None'):
        """
        Draws the given primitive element with the provided painter using the style options specified by option.
        """
        ...
    def generatedIconPixmap(self, iconMode, pixmap, option): ...
    def hitTestComplexControl(self, control, option, position, widget='None'): ...
    def itemPixmapRect(self, rectangle, alignment, pixmap): ...
    def itemTextRect(self, metrics, rectangle, alignment, enabled, text): ...
    def pixelMetric(self, metric, option='None', widget='None'): ...
    def polish(self, *args, **kwargs): ...
    def sizeFromContents(self, ct, opt, contentsSize, widget='None'): ...
    def styleHint(self, hint, option='None', widget='None', returnData='None'): ...
    def subControlRect(self, control, option, subControl, widget='None'): ...
    def subElementRect(self, element, option, widget='None'): ...
    def unpolish(self, *args, **kwargs): ...
    DROP_INDICATOR_COLOR : QColor
    
    DROP_INDICATOR_LEFT_OFFSET : float
    
    DROP_INDICATOR_WIDTH : float
    
    staticMetaObject : PySide2.QtCore.QMetaObject


