from PySide6 import QtWidgets, QtCore, QtGui
from typing import Optional

from ..constants import DEFAULT_PROPERTIES_GRID


class Grid:
    def __init__(self, scene: QtWidgets.QGraphicsScene, properties: dict = DEFAULT_PROPERTIES_GRID):
        self.scene = scene
        self.properties = properties

        self._color = QtGui.QColor(*self.properties["color"])
        self._thickness = self.properties["thickness"]
        self._size = self.properties["size"]

    def draw(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        pen = QtGui.QPen(self._color, self._thickness)
        painter.setPen(pen)

        for x in range(int(rect.left()), int(rect.right()), self._size):
            painter.drawLine(x, rect.top(), x, rect.bottom())

        for y in range(int(rect.top()), int(rect.bottom()), self._size):
            painter.drawLine(rect.left(), y, rect.right(), y)
        
    
