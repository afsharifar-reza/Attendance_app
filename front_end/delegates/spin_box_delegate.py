# front_end/delegates/spin_box_delegate.py

from PySide6.QtWidgets import QStyledItemDelegate, QSpinBox
from PySide6.QtCore import Qt

class SpinBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, min_value=0, max_value=300):
        super().__init__(parent)
        self.min_value = min_value
        self.max_value = max_value

    def createEditor(self, parent, option, index):
        spin = QSpinBox(parent)
        spin.setRange(self.min_value, self.max_value)
        return spin

    def setEditorData(self, editor, index):
        value = index.data()
        editor.setValue(int(value) if value else 0)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.value())

