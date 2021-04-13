##################
#
# This file is made available under the Creative Commons CC0 1.0 
# Universal Public Domain Dedication.
# 
# CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# https://creativecommons.org/publicdomain/zero/1.0/
# 
# The person who associated a work with this deed has dedicated the 
# work to the public domain by waiving all of their rights to the work 
# worldwide under copyright law, including all related and neighboring 
# rights, to the extent allowed by law. You can copy, modify, distribute 
# and perform the work, even for commercial purposes, all without 
# asking permission.  
# 
##################
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def _isType(string, dictionary):
	for c in string:
		if c not in dictionary:
			return False
			
	return True

def _isLetter(string):
	return _isType(string, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	
def _isSymbol(string):
	return _isType(string, "!@#$%^&*()-_=+{}[];:\'\",<.>/?|\\")
	
class MainWidget(QWidget):
	def __init__(self):
		super().__init__()		
		self.__mMainLayout = QGridLayout(self)
		self.__mBinaryLabel = QLabel(self.tr("Binary:"), self)
		self.__mOctalLabel = QLabel(self.tr("Octal:"), self)
		self.__mDecimalLabel = QLabel(self.tr("Decimal:"), self)
		self.__mHexLabel = QLabel(self.tr("Hex:"), self)
		self.__mAsciiLabel = QLabel(self.tr("ASCII:"), self)
		
		self.__mBinaryEdit = QLineEdit(self)
		self.__mOctalEdit = QLineEdit(self)
		self.__mDecimalEdit = QLineEdit(self)
		self.__mHexEdit = QLineEdit(self)
		self.__mAsciiEdit = QLineEdit(self)
		
		self.__mBinaryEdit.editingFinished.connect(self.__binaryEditEnter)
		self.__mOctalEdit.editingFinished.connect(self.__octalEditEnter)
		self.__mDecimalEdit.editingFinished.connect(self.__decimalEditEnter)
		self.__mHexEdit.editingFinished.connect(self.__hexEditEnter)
		self.__mHexEdit.textChanged.connect(self.__hexEditChanged)
		self.__mAsciiEdit.editingFinished.connect(self.__asciiEditEnter)
		
		self.__mBinaryEdit.setValidator(QRegExpValidator(QRegExp("[0-1]*"), self))
		self.__mOctalEdit.setValidator(QRegExpValidator(QRegExp("[0-9]*"), self))
		self.__mDecimalEdit.setValidator(QRegExpValidator(QRegExp("[0-9]*"), self))
		self.__mHexEdit.setValidator(QRegExpValidator(QRegExp("[0-9,a-f,A-F]*"), self))
		
		self.__mMainLayout.addWidget(self.__mBinaryLabel, 0, 0, 1, 1)
		self.__mMainLayout.addWidget(self.__mBinaryEdit, 0, 1, 1, 1)
		self.__mMainLayout.addWidget(self.__mOctalLabel, 1, 0, 1, 1)
		self.__mMainLayout.addWidget(self.__mOctalEdit, 1, 1, 1, 1)
		self.__mMainLayout.addWidget(self.__mDecimalLabel, 2, 0, 1, 1)
		self.__mMainLayout.addWidget(self.__mDecimalEdit, 2, 1, 1, 1)
		self.__mMainLayout.addWidget(self.__mHexLabel, 3, 0, 1, 1)
		self.__mMainLayout.addWidget(self.__mHexEdit, 3, 1, 1, 1)
		self.__mMainLayout.addWidget(self.__mAsciiLabel, 4, 0, 1, 1)
		self.__mMainLayout.addWidget(self.__mAsciiEdit, 4, 1, 1, 1)
		
	def __binaryEditEnter(self):
		if len(self.__mBinaryEdit.text()) > 0:		
			n = int(self.__mBinaryEdit.text(), 2)
			nOctal = "{0:o}".format(n)
			nDecimal = "{0:d}".format(n)
			nHex = "{0:X}".format(n)
			nAscii = "{0:c}".format(n)
			
			self.__mOctalEdit.setText(nOctal)
			self.__mDecimalEdit.setText(nDecimal)
			self.__mHexEdit.setText(nHex)
			self.__setAscii(nAscii)
		
	def __octalEditEnter(self):
		if len(self.__mOctalEdit.text()) > 0:
			n = int(self.__mOctalEdit.text(), 8)
			nBinary = "{0:b}".format(n)
			nDecimal = "{0:d}".format(n)
			nHex = "{0:X}".format(n)
			nAscii = "{0:c}".format(n)
			
			self.__mBinaryEdit.setText(nBinary)
			self.__mDecimalEdit.setText(nDecimal)
			self.__mHexEdit.setText(nHex)
			self.__setAscii(nAscii)
		
	def __decimalEditEnter(self):
		if len(self.__mDecimalEdit.text()) > 0:
			n = int(self.__mDecimalEdit.text())
			nBinary = "{0:b}".format(n)
			nOctal = "{0:o}".format(n)
			nHex = "{0:X}".format(n)
			nAscii = "{0:c}".format(n)
			
			self.__mBinaryEdit.setText(nBinary)
			self.__mOctalEdit.setText(nOctal)
			self.__mHexEdit.setText(nHex)
			self.__setAscii(nAscii)
		
	def __hexEditEnter(self):
		if len(self.__mHexEdit.text()) > 0:
			n = int(self.__mHexEdit.text(), 16)
			nBinary = "{0:b}".format(n)
			nOctal = "{0:o}".format(n)
			nDecimal = "{0:d}".format(n)
			nAscii = "{0:c}".format(n)
			
			self.__mBinaryEdit.setText(nBinary)
			self.__mOctalEdit.setText(nOctal)
			self.__mDecimalEdit.setText(nDecimal)
			self.__setAscii(nAscii)
			
	def __hexEditChanged(self, string):
		self.__mHexEdit.setText(string.upper())
		
	def __asciiEditEnter(self):
		if len(self.__mAsciiEdit.text()) > 0:
			n = 0
			for i in range(len(self.__mAsciiEdit.text())):
				if i > 0:
					n = n << 8
				n |= ord(self.__mAsciiEdit.text()[i])
				
			nBinary = "{0:b}".format(n)
			nOctal = "{0:o}".format(n)
			nDecimal = "{0:d}".format(n)
			nHex = "{0:X}".format(n)
			
			self.__mBinaryEdit.setText(nBinary)
			self.__mOctalEdit.setText(nOctal)
			self.__mDecimalEdit.setText(nDecimal)
			self.__mHexEdit.setText(nHex)
					
	def __setAscii(self, asciiString):
		if _isLetter(asciiString) or asciiString.isdecimal() or asciiString.isdigit() or _isSymbol(asciiString):
			self.__mAsciiEdit.setText(asciiString)
		else:
			self.__mAsciiEdit.setText("-")

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("FreeBaseConverter v.1.00")
		self.setMinimumSize(300, 200)
		
		self.__mWidget = MainWidget()
		self.setCentralWidget(self.__mWidget)
		
def main():
	application = QApplication([])
	window = MainWindow()
	window.show()
	application.exec_()

if __name__ == "__main__":
	main()
