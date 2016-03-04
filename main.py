import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUiType
from СalcFunc import average, geometricMean, harmonicMean, rms

app = QApplication(sys.argv)
app.setApplicationName('pyqt_calculator')
form_class, base_class = loadUiType('widget.ui')

array = []

class MainWindow(QDialog, form_class):


    def __init__(self, *args):

        super(MainWindow, self).__init__(*args)

        self.setupUi(self)
        self.numbTable.setRowCount(0)
        self.numbTable.setColumnCount(1)



    def buttonClick(self):

        if array:

            self.averageLine.setText(average(array))
            self.geometricMeanLine.setText(geometricMean(array))
            self.harmonicMeanLine.setText(harmonicMean(array))
            self.rmsLine.setText(rms(array))

        else:

            QMessageBox.question(self, 'Message', 'Для расчетав необходимо минимум два значения', QMessageBox.Ok)



    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', "Закрыть приложение?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



    def addRow(self):

        try:

            array.append(float(self.tabValue.text()))
            rowPosition = self.numbTable.rowCount()
            self.numbTable.insertRow(rowPosition)
            self.numbTable.setItem(rowPosition, 0, QTableWidgetItem(str(array[rowPosition])))
            self.tabValue.setText("")

        except ValueError:

            QMessageBox.question(self, 'Message', 'Проверь поле ввода, умник!', QMessageBox.Ok)



    def delRow(self):

        rowPosition = self.numbTable.rowCount()

        if rowPosition > 0:
            self.numbTable.removeRow(rowPosition-1)
            array.pop()



form = MainWindow()
form.setWindowTitle('Калькулятор средних величин')
form.show()
sys.exit(app.exec_())
