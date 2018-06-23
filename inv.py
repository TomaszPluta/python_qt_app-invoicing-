#!/usr/bin/env python


#odwracanie listy - zrobic w pythonie

import sys

from PyQt4 import QtCore
from PyQt4 import QtGui


lineLenght = 65




def fill_line():
	return "".ljust(lineLenght,"-") + "\n"

def fill_empty():
	return "".ljust(lineLenght," ") + "\n"


class Item:
	name = ""
	amount = 5
	netto = 0
	#netto_accu = 0
	value = 0
	brutto = 0.0
	tax = 0

	def __init__ (self, name_, netto_, tax_):
		self.name = name_
		self.netto = netto_
		self.value = self.netto * self.amount
		self.tax = tax_
		self.brutto = float(self.value) + float(self.value) * float(self.tax)/100.0

	def __str__ (self):
		return ( "| " + self.name[0:8].ljust(8, ' ') +
		" | " + str(self.netto).rjust(8, ' ')   +
		" | " + str(self.amount).rjust(8, ' ')   +
		" | " + str(self.value).rjust(8, ' ')   +
		" | " +  str(self.tax).rjust(8, ' ')    +
		" | " + str(self.brutto).rjust(8, ' ') + " |" )
		





class Seller(object):
	name = ""
	address = ""
	nip = ""
	ID = 0
	data = ""
	def __init__ (self, name_, adress_, nip_):
		self.name = name_
		self.address = adress_
		self.nip = nip_
		self.data = self.name + '\n' + self.address  + '\n' + self.nip 



class Invoice:
	item = []
	seller = None	
	buyer  = None
	value_sum = 0
	brutto_sum = 0
	tableHeader = ""

	def __init__ (self, seller_):
		self.seller = seller_
	def add_item (self, item_):
		self.item.append(item_)
	def init_buyer (self, buyer_):
		self.buyer = buyer_
	def print_header(self):
		#print	
		r_offset = lineLenght - len(self.seller.name)
		s = "%s %*s\n" % (self.seller.name, r_offset, self.buyer.name) 
		
		r_offset = lineLenght - len(self.seller.address)
		s = s + "%s %*s\n" % (self.seller.address, r_offset, self.buyer.address) 
		
		r_offset = lineLenght - len(self.seller.nip)
		return s + "%s %*s\n" % (self.seller.nip, r_offset, self.buyer.nip) +'\n'
	def print_table(self):
		fill_line()
		
		self.tableHeader =  "| item     |   amount |    netto |    value |     tax  |   brutto |\n"
		self.tableHeader = self.tableHeader + fill_line()
		for i in range (len(self.item)):
			self.tableHeader =  self.tableHeader + str(self.item[i]) + "\n"
			value_sum =  self.item[i].value
			brutto_sum =  self.item[i].brutto
		self.tableHeader = fill_line() +  self.tableHeader + fill_line() + '\n'
		return self.tableHeader
	def print_signature (self):
		buyer_s = "Buyer signature"
		seller_s = "Seller signature"
		r_offset = lineLenght - len(seller_s)
		#print
		#print
		return "%s %*s\n" % (buyer_s, r_offset, seller_s) 

	def print_invoice(self):
		return self.print_header() + self.print_table() + self.print_signature()







us = Seller("ComapnyFromSzmatany", "streetsk", "959-457-25")
ie = Invoice(us)
c = Seller("janekMuzykant", "klk", "1212112")
p = Item("milkerstone", 10, 22)
s = Item("silk", 20, 22)
r = Item("w", 30, 5)




ie.init_buyer(c)
ie.add_item(p)
ie.add_item(s)
ie.add_item(r)
print ie.print_invoice()



################################################################################
#function definittion
################################################################################
# -*- coding: utf-8 -*-
#

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore





class SellerAddWindow(QMainWindow):
	seller_ptr = None
	textboxName = None
	textboxAddress  = None
	textboxNIP  = None


	def new_seller(self):
		self.seller_ptr.name = self.textboxName.text()
		self.seller_ptr.address = self.textboxAddress.text()
		self.seller_ptr.nip = self.textboxNIP.text()


	def __init__(self, seller):
		QMainWindow.__init__(self)
		dialogLayout = QGridLayout()
		self.seller_ptr = seller
		labelName = QLabel("Name")
		#labelName.setFixedSize(75,30)
		dialogLayout.addWidget(labelName,0,0)

		labelAddrress = QLabel("Address")
		#labelAddrress.setFixedSize(75,30)
		dialogLayout.addWidget(labelAddrress,1,0)

		labelNIP = QLabel("NIP")
		#labelNIP.setFixedSize(75,30)
		dialogLayout.addWidget(labelNIP,2,0)


		self.textboxName = QLineEdit("Jan Kowalski")
		#textboxName.setFixedSize(200,30)
		dialogLayout.addWidget(self.textboxName,0,1)

		self.textboxAddress = QLineEdit("Dluga 12")
		#textboxAddress.setFixedSize(200,30)
		dialogLayout.addWidget(self.textboxAddress,1,1)

		self.textboxNIP = QLineEdit("125412544")
		#textboxNIP.setFixedSize(200,30)
		dialogLayout.addWidget(self.textboxNIP,2,1)


		ok_button = QPushButton('Add')
		dialogLayout.addWidget(ok_button)

		cancel_button = QPushButton('You wouldn\'t understand')
		dialogLayout.addWidget(cancel_button)

		ok_button.clicked.connect(self.new_seller)
		cancel_button.clicked.connect(self.close)

		self.setFixedSize(300,200)
		w = QWidget()
		w.setLayout(dialogLayout)
		self.setCentralWidget(w)
		self.setWindowTitle("DWA")

		


class ItemsAddWindow(QMainWindow):
	item_ptr = None
	table = None
	textboxName  = None
	textboxAmount  = None
	textboxNetto  = None
	textboxVAT  = None
	textboxBrutto = None

	ItemSet = []
	actualItem =  Item("",0, 0)
	currentRow = 0
	selectedRow = 0 


	def insert(self):
		


		self.currentRow = self.table.rowCount() 
		self.table.insertRow(self.currentRow)

		print "przed = " +  str(self.currentRow)
		self.actualItem.name = self.textboxName.text()		
		self.table.setItem(self.currentRow, 0, QtGui.QTableWidgetItem(self.actualItem.name))

		self.actualItem.amount =  int(self.textboxAmount.text())
		self.table.setItem(self.currentRow, 1, QtGui.QTableWidgetItem(str(self.actualItem.amount)))

		self.actualItem.netto =  float(self.textboxNetto.text())
		self.table.setItem(self.currentRow, 2, QtGui.QTableWidgetItem(str(self.actualItem.netto)))

		self.actualItem.value =  self.actualItem.amount * self.actualItem.netto
		self.table.setItem(self.currentRow, 3, QtGui.QTableWidgetItem(str(self.actualItem.value)))

		self.actualItem.tax =  int(self.textboxVAT.text())
		self.table.setItem(self.currentRow, 4, QtGui.QTableWidgetItem(str(self.actualItem.tax)))

		self.actualItem.brutto =  self.actualItem.value * ((self.actualItem.tax/100) +1)
		self.table.setItem(self.currentRow, 5, QtGui.QTableWidgetItem(str(self.actualItem.brutto)))
		
		print "po  = " +  str(self.currentRow+1)


	def delete_row(self):
		self.table.removeRow(self.table.currentRow())
		self.currentRow = self.table.rowCount() #kasuje potem wyzej dzieki temu
	
		print "delete = " +  str(self.currentRow)
		
	def __init__(self, item, headers):
		QMainWindow.__init__(self)
		self.item_ptr = item

		###
		dialogLayout = QVBoxLayout()
		topLayout = QGridLayout()
		bottomLayout = QGridLayout()
		dialogLayout.addLayout(topLayout)
		dialogLayout.addLayout(bottomLayout)
		###
		labelName = QLabel("Name")
		labelName.setFixedHeight(10)
		topLayout.addWidget(labelName, 0,0)
		labelNetto = QLabel("Amount")
		topLayout.addWidget(labelNetto, 0,1)
		labelAmount = QLabel("Netto [pcs]")
		topLayout.addWidget(labelAmount, 0,2)
		labelVAT = QLabel("VAT")
		topLayout.addWidget(labelVAT, 0,3)
		###
		self.textboxName = QLineEdit("maslo")
		topLayout.addWidget(self.textboxName, 1,0)
		self.textboxAmount = QLineEdit("14")
		topLayout.addWidget(self.textboxAmount, 1,2)
		self.textboxNetto = QLineEdit("124")
		topLayout.addWidget(self.textboxNetto, 1,1)
		self.textboxVAT = QLineEdit("23")
		topLayout.addWidget(self.textboxVAT,1,3)
		###
		add_button = QPushButton('Add')
		add_button.setMinimumWidth(100)
		topLayout.addWidget(add_button,1,5)
		###
	#	change_button = QPushButton('Change')
	#	change_button.setMinimumWidth(100)
	#	topLayout.addWidget(change_button,0,1)
		###
		delete_button = QPushButton('Delete active')
		delete_button.setMinimumWidth(100)
		bottomLayout.addWidget(delete_button,0,1)
		#
		ok_button = QPushButton('Accept')
		ok_button.setMinimumWidth(100)
		bottomLayout.addWidget(ok_button,3,1)
		#		
		cancel_button = QPushButton('Cancel')
		cancel_button.setMinimumWidth(100)
		cancel_button.clicked.connect(self.close)
		bottomLayout.addWidget(cancel_button,4,1)
		###
		self.setMinimumWidth(750);
		self.setMinimumHeight(330);
		###
		self.table = QTableWidget()
		self.table.setRowCount(0)
		self.table.setColumnCount(6)
		tableHeader = headers.split("|")
		self.table.setHorizontalHeaderLabels(tableHeader[1:]);
		bottomLayout.addWidget(self.table,0,0,5,1)

		w = QWidget(self)
		w.setLayout(dialogLayout)
		self.setTabOrder(self.textboxName, self.textboxAmount)
		self.setTabOrder(self.textboxAmount, self.textboxNetto)
		self.setTabOrder(self.textboxNetto, self.textboxVAT)
		self.setCentralWidget(w)
		self.setWindowTitle("DWA")

		add_button.clicked.connect(self.insert)
		delete_button.clicked.connect(self.delete_row)

		#topLayout.addStretch(1)

		

class MainWindow(QMainWindow):
	invoice_ptr = None
	textbox = None
	itemsAddWindow = None
	sellerAddWindow = None

	def display_invoice(self):
		self.textbox.setText(ie.print_invoice())

	def get_seller_info(self):
		self.sellerAddWindow = SellerAddWindow(self.invoice_ptr.seller)	
		self.sellerAddWindow.show()

	def add_items(self):
		self.itemsAddWindow = ItemsAddWindow(self.invoice_ptr.item, self.invoice_ptr.tableHeader)
		#self.connect(self.itemsAddWindow,SIGNAL(self.destroyed()),self.itemsAddWindow.parent(),SLOT(close()))
		self.itemsAddWindow.show()


	
	def update_invoice(self):	
		self.textbox.setText(self.invoice_ptr.print_invoice())

	def __init__(self, invoice):
		QMainWindow.__init__(self)
		mainLayout = QGridLayout()
		optionsLayout = QVBoxLayout()


		seller_button = QPushButton('Add seller')
		optionsLayout.addWidget(seller_button)

		buyer_button = QPushButton('Add buyer')
		optionsLayout.addWidget(buyer_button)

		items_button = QPushButton('Add items')
		optionsLayout.addWidget(items_button)

		show_button = QPushButton('Show invoice')
		optionsLayout.addWidget(show_button)


		self.textbox = QTextEdit()
		self.textbox.setText(invoice.print_invoice())
		self.textbox.setDisabled(1)
		self.textbox.resize(700,400)

		mainLayout.addLayout(optionsLayout,0,0)
		mainLayout.addWidget(self.textbox,0,1,2,1)

		w = QWidget()
		w.setLayout(mainLayout)
		self.setCentralWidget(w)
		self.setWindowTitle("K&TZA")
		self.invoice_ptr = invoice
		show_button.clicked.connect(self.update_invoice)
		seller_button.clicked.connect(self.get_seller_info)
		items_button.clicked.connect(self.add_items)
	

	def closeEvent(self,event):
		#pass
		if (self.itemsAddWindow != None):
			self.itemsAddWindow.close()
		if (self.sellerAddWindow != None):
			self.sellerAddWindow.close()

		#result = QtGui.QMessageBox.question(self,
		#"Confirm Exit...",
		#"Are you sure you want to exit ?",
		#QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
		#event.ignore()

		#if result == QtGui.QMessageBox.Yes:
		event.accept()



	


if __name__ == "__main__":
	app = QApplication(sys.argv)
	#myFilter = MyEventFilter()
	#3app.installEventFilter(myFilter)
	mainWindow = MainWindow(ie)  
	mainWindow.setGeometry(300, 300, 800, 600)
	mainWindow.show()
	r1 = Item("wasd", 35, 24)
	ie.add_item(r1)
	sys.exit(app.exec_())




