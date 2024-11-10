import sys
from PySide6 import QtWidgets, QtCore, QtGui
from typing import Optional

from ..constants import DEFAULT_PROPERTIES_SCENE
from ..enums import DisplayMode
from ..components import Grid, Dot, Dashed






class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, parent: Optional[QtWidgets.QWidget] = None, properties: dict = DEFAULT_PROPERTIES_SCENE):
        super(Scene, self).__init__(parent)

        self.properties = properties

        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(*self.properties["background"])))
        
    
        self._mode = DisplayMode(self.properties["display"]["mode"])

        self._color = QtGui.QColor(*self.properties["display"]["color"])


    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, value: DisplayMode):
        if value != self._mode:
            self._mode = value
            self.update()

    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        painter.fillRect(rect, self.backgroundBrush())
        if self._mode == DisplayMode.GRID:
            Grid(self, self.properties["grid"]).draw(painter, rect)
        elif self._mode == DisplayMode.DOTS:
            Dot(self, self.properties["dots"]).draw(painter, rect)
        elif self._mode == DisplayMode.DASHED:
            Dashed(self, self.properties["dashed"]).draw(painter, rect)


    


