# front_end/delegates/combo_box_delegate.py

from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import Qt

class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, column_options: dict, parent=None):
        """
        column_options: دیکشنری با شماره‌ی ستون و لیست گزینه‌ها
        مثال: {3: ["حاضر", "غایب", "تاخیر"], 4: ["حاضر", "غایب"], ...}
        """
        super().__init__(parent)
        self.column_options = column_options

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        options = self.column_options.get(index.column(), ["حاضر", "غایب"])  # پیش‌فرض
        combo.addItems(options)
        return combo

    def setEditorData(self, editor, index):
        current_text = index.data(Qt.DisplayRole)
        idx = editor.findText(current_text)
        if idx >= 0:
            editor.setCurrentIndex(idx)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.EditRole)
