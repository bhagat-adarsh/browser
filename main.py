import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import * 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()#Parent class ke sath super connection banata hai
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http;//google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()#bbrowser ko maximize karne ke liye
        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        #Back button
        back_btn = QAction('Piche Chale',self)#|<>
        back_btn.triggered.connect(self.browser.back)#When pressed prev browser par jayega
        navbar.addAction(back_btn)
        
        #Forward button
        forward_btn = QAction('Aage badho',self)#|<>
        forward_btn.triggered.connect(self.browser.forward)#When pressed next browser par jayega
        navbar.addAction(forward_btn)
        
        #refressh btn
        refresh_btn = QAction('Ghumao Re!',self)#|<>
        refresh_btn.triggered.connect(self.browser.reload)#When pressed next browser par jayega
        navbar.addAction(refresh_btn)
        
        #Home button
        home_btn = QAction('GHAR',self)#|<>
        home_btn.triggered.connect(self.navigate_home)#When pressed next browser par jayega
        navbar.addAction(home_btn)
        #search area
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        
        self.browser.urlChanged.connect(self.update_url)

        
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self, q):
        self.url_bar.setText(q.toString())
        
        
app = QApplication(sys.argv)
QApplication.setApplicationName('My Chrome')#NAME karan
window = MainWindow()
app.exec_()#for execution
