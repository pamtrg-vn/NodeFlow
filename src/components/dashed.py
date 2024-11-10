from PySide6 import QtWidgets, QtCore, QtGui
from typing import Optional

from ..constants import DEFAULT_PROPERTIES_DASHED


class Dashed:
    def __init__(self, scene: QtWidgets.QGraphicsScene, properties: dict = DEFAULT_PROPERTIES_DASHED):
        self.scene = scene
        self.properties = properties

        self._color = QtGui.QColor(*self.properties["color"])
        self._thickness = self.properties["thickness"]
        self._size = self.properties["size"]

    def draw(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        pen = QtGui.QPen(self._color, self._thickness)
        pen.setStyle(QtCore.Qt.PenStyle.DashLine)
        painter.setPen(pen)
        lines = []

        first_left = int(rect.left()) - (int(rect.left()) % self._size)
        first_top = int(rect.top()) - (int(rect.top()) % self._size)

        for x in range(first_left, int(rect.right()), self._size):
            lines.append(QtCore.QLineF(x, rect.top(), x, rect.bottom()))
        for y in range(first_top, int(rect.bottom()), self._size):
            lines.append(QtCore.QLineF(rect.left(), y, rect.right(), y))
        
        painter.drawLines(lines)

        