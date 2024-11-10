from PySide6 import QtWidgets, QtCore, QtGui
from typing import Optional

from ..constants import DEFAULT_PROPERTIES_DOT


class Dot:
    def __init__(self, scene: QtWidgets.QGraphicsScene, properties: dict = DEFAULT_PROPERTIES_DOT):
        self.scene = scene
        self.properties = properties

        self._color = QtGui.QColor(*self.properties["color"])
        self._size = self.properties["size"]

    def draw(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        pen = QtGui.QPen(self._color)
        painter.setPen(pen)

        first_left = int(rect.left()) - (int(rect.left()) % self._size)
        first_top = int(rect.top()) - (int(rect.top()) % self._size)

        for x in range(first_left, int(rect.right()), self._size):
            for y in range(first_top, int(rect.bottom()), self._size):
                painter.drawPoint(x, y)

