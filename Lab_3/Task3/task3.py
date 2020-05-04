from PyQt5 import QtWidgets
from window import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def checkLogFile(self):
		textMmessage = 'Файл лога не найден. Файл будет создан автоматически'
		reply = QtWidgets.QMessageBox.question(self, 'Уведомление', textMmessage,
		                                       QtWidgets.QMessageBox.Ok)

		if reply == QtWidgets.QMessageBox.Ok:
			logFile = open('script18.log','w')
			logFile.close()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

try:
	logFile = open('script18.log','r')
	logFile.close()
except IOError:
	application.checkLogFile()

sys.exit(app.exec())