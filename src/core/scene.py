import sys
from PySide6 import QtWidgets, QtCore, QtGui
from typing import Optional

from ..constants import DEFAULT_PROPERTIES_SCENE
from ..enums import DisplayMode






class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, parent: Optional[QtWidgets.QWidget] = None, properties: dict = DEFAULT_PROPERTIES_SCENE):
        super(Scene, self).__init__(parent)

        self._properties = properties
        self._mode = DisplayMode(self._properties["display"]["mode"])

        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(*self._properties["background"])))
        
    
    def set_mode(self, mode: DisplayMode):
        if self._mode != mode:
            self._mode = mode
            self.update()
            
    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        painter.fillRect(rect, self.backgroundBrush())
        if self._mode == DisplayMode.GRID:
            self._draw_grid(painter, rect)
        elif self._mode == DisplayMode.DOTS:
            self._draw_dots(painter, rect)
        elif self._mode == DisplayMode.DASHED:
            self._draw_dashed(painter, rect)
        else:
            super(Scene, self).drawBackground(painter, rect)

    def _draw_grid(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        pen = QtGui.QPen(QtGui.QColor(*self._properties["grid"]["color"]), self._properties["grid"]["thickness"])
        painter.setPen(pen)

        for x in range(int(rect.left()), int(rect.right()), self._properties["grid"]["size"]):
            painter.drawLine(x, rect.top(), x, rect.bottom())

        for y in range(int(rect.top()), int(rect.bottom()), self._properties["grid"]["size"]):
            painter.drawLine(rect.left(), y, rect.right(), y)

    def _draw_dots(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        pen = QtGui.QPen(QtGui.QColor(*self._properties["dots"]["color"]))
        painter.setPen(pen)

        first_left = int(rect.left()) - (int(rect.left()) % self._properties["dots"]["size"])
        first_top = int(rect.top()) - (int(rect.top()) % self._properties["dots"]["size"])

        for x in range(first_left, int(rect.right()), self._properties["dots"]["size"]):
            for y in range(first_top, int(rect.bottom()), self._properties["dots"]["size"]):
                painter.drawPoint(x, y)

    def _draw_dashed(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        pen = QtGui.QPen(QtGui.QColor(*self._properties["dashed"]["color"]), self._properties["dashed"]["thickness"])
        pen.setStyle(QtCore.Qt.PenStyle.DashLine)
        painter.setPen(pen)
        lines = []

        first_left = int(rect.left()) - (int(rect.left()) % self._properties["dashed"]["size"])
        first_top = int(rect.top()) - (int(rect.top()) % self._properties["dashed"]["size"])

        for x in range(first_left, int(rect.right()), self._properties["dashed"]["size"]):
            lines.append(QtCore.QLineF(x, rect.top(), x, rect.bottom()))
        for y in range(first_top, int(rect.bottom()), self._properties["dashed"]["size"]):
            lines.append(QtCore.QLineF(rect.left(), y, rect.right(), y))
        
        painter.drawLines(lines)
    


