from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QPushButton,QVBoxLayout,QMainWindow, QLineEdit, QHBoxLayout
import sys
from PyQt5.QtCore import pyqtSlot, QUrl, Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
import sys,time
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QScrollBar,QSplitter,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit
from PyQt5.QtCore import QCoreApplication
import socket
from threading import Thread 
from socketserver import ThreadingMixIn 
import test_client_chat
import encrypt_header
import json 
from _thread import *
import threading 


#The following will be the Gui

class Start(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        #Here is the beginning window in which the person may add their name
        #and the person they wish to contact
        self.lbl1 = QLabel("Your name for today?")

        self.btn = QPushButton("Connect to person", self)
        self.btn2 = QPushButton("This name", self)
        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        #HBox was used due to how simple small the window is
        #and how little time the user spends with it. Should look really simple.
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.textbox2)
        vbox.addWidget(self.btn2)
        
        vbox.addWidget(self.lbl1)
        self.setLayout(vbox)
        self.btn.clicked.connect(self.on_click)
        self.btn2.clicked.connect(self.on_click_2)
        #The two above lines activate your name declaration and the 
        #encrypted chat window to activate.
        self.setWindowTitle('Encrpted Chat')
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        #Will activate the encryption chat window ot open
        tmp_key = test_client_chat.con_2_person(self.textbox.text())
        print("tmp_key:",tmp_key)
        self.displaySecond = Window(self.textbox.text(),tmp_key)
        self.displaySecond.show()

    def on_click_2(self):
        #Displays the user's chosen name.
        self.lbl1.setText(self.textbox2.text())
    
class Window(QDialog):
    def __init__(self, name,tmp_key):
        super().__init__()
        #Inputted name of user
        self.name = name
        #The following is the set up for the Qdialog box
        #and the button and input area the user has.
        self.flag=0
        #Ths is for the input line
        self.chatTextField=QLineEdit(self)
        self.chatTextField.resize(480,75)
        self.chatTextField.move(10,350)
        #This is for the sending button
        self.btnSend=QPushButton("Send",self)
        self.btnSend.resize(480,30)
        self.btnSendFont=self.btnSend.font()
        self.btnSendFont.setPointSize(15)
        self.btnSend.setFont(self.btnSendFont)
        self.btnSend.move(10,460)
        self.btnSend.setStyleSheet("background-color: #606060")
        #This connect button function is for sending messages
        self.btnSend.clicked.connect(self.send)
        self.chatBody=QVBoxLayout(self)
        #This designates that the window shown is an actual window
        #with plottable objects.
        splitter=QSplitter(QtCore.Qt.Vertical)
        #This makes the viewing area as only viewable
        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        #The following add our window attributes
        splitter.addWidget(self.chat)
        splitter.addWidget(self.chatTextField)
        splitter.setSizes([400,100])
 
        splitter2=QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter)
        splitter2.addWidget(self.btnSend)
        splitter2.setSizes([200,10])
 
        self.chatBody.addWidget(splitter2)
        self.setWindowTitle(name)
        self.resize(500, 500)
        self.listen_thread = threading.Thread(target = test_client_chat.listen, args = (self,tmp_key,7),daemon=True)
        self.listen_thread.start()#,4)
        print("line 102")

    def update(self,message):
        #DON'T remove 'k' I don't know what it does but it don't work without it
        #This is where the text is updated for new text/message
        print("line 106")
        text="<"+self.name+"> "+message
        font=self.chat.font()
        font.setPointSize(13)
        self.chat.setFont(font)
        textFormatted='{:>80}'.format(text)
        self.chat.append(textFormatted)
        self.chatTextField.setText("")
       

    def send(self):
        #The following is the method for the user
        #to send a message to the other person
        text=self.chatTextField.text()
        test_client_chat.send_message(text,self.name)
        font=self.chat.font()
        font.setPointSize(13)
        self.chat.setFont(font)
        textFormatted='{:>80}'.format(text)
        self.chat.append(textFormatted)

        self.chatTextField.setText("")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start() 
    sys.exit(app.exec_())
