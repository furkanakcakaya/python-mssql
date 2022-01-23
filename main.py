from PyQt5.QtWidgets import QMessageBox,QMainWindow, QApplication, QLabel, QPushButton, QRadioButton, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
import pypyodbc


from addcategory import AddCategory
from addpharmacy import AddPharmacy
from addproduct import AddProduct
from deleteElement import DeleteElement

#MSSql connection
con = pypyodbc.connect(
    'driver={SQL Server};'
    'Server=AX;'
    'Database=E-ECZANE;'
    'Trusted_Connection=True;'
)

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        #Loading designed UI file
        uic.loadUi('python/mainMenu.ui',self)
        
        #Widget Definitions
        self.radioCategory = self.findChild(QRadioButton, "radCategory")
        self.radioPharmacy = self.findChild(QRadioButton, "radPharmacy")
        self.radioProducts = self.findChild(QRadioButton, "radProduct")
        
        self.btnInsert = self.findChild(QPushButton, "btnInsertElement")
        self.btnUpdate = self.findChild(QPushButton, "btnUpdateElement")
        self.btnDelete = self.findChild(QPushButton, "btnDeleteElement")
        self.btnRefresh = self.findChild(QPushButton, "btnUpdateTable")
        
        self.btnAll = self.findChild(QPushButton, "btnAll")
        self.btnCatPha = self.findChild(QPushButton, "btnCatPha")
        self.btnCatPro = self.findChild(QPushButton, "btnCatPro")
        self.btnPhaPro = self.findChild(QPushButton, "btnPhaPro")
        
        self.table = self.findChild(QTableWidget, "tableWidget")
        
        #Show Categories table on start
        self.viewCategories()
        
        self.btnRefresh.clicked.connect(self.refreshButton)
        self.btnInsert.clicked.connect(self.insertButton)
        self.btnUpdate.clicked.connect(self.updateButton)
        self.btnDelete.clicked.connect(self.deleteButton)
        
        self.btnAll.clicked.connect(self.viewAll)
        self.btnCatPha.clicked.connect(self.viewCategoriesPharmacys)
        self.btnCatPro.clicked.connect(self.viewCategoriesProducts)
        self.btnPhaPro.clicked.connect(self.viewPharmacysProducts)
        
        #Showing the app
        self.show()
        
    def viewCategories(self):
        cur = con.cursor()
        cur.execute(f"select * from [dbo].[Categories]")  # Butun gemiler sql fonksiyonuyla secilir
        data = cur.fetchall()                             # Secilen tablo data adli degiskende tutulur
        cur.close()
        
        self.table.clearContents()         # Gecerli tablo sifirlanir
        self.table.setColumnCount(2)       # Tablonun sutun sayisi ayarlanir
        self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
        self.table.setColumnWidth(0,120)    # Bazi sutunlarin uzunluklari ayarlanir.
        self.table.setColumnWidth(1,120)
        self.table.setHorizontalHeaderLabels(['Category_ID','Type'])
        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().hide()
        row = self.table.rowCount()
        
        # Data tablosundaki her eleman for dongusu ile donulur
        for x in data:
            # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QTableWidgetItem(str(x[0])))
            self.table.setItem(row, 1, QTableWidgetItem(x[1]))
            
            # Bir sonraki adim icin satir sayisi bir arttirilir
            row = row + 1
            
    def viewPharmacys(self):
        cur = con.cursor()
        cur.execute(f"select * from [dbo].[PHARMACYS]")  # Butun gemiler sql fonksiyonuyla secilir
        data = cur.fetchall()                             # Secilen tablo data adli degiskende tutulur
        cur.close()
        
        self.table.clearContents()         # Gecerli tablo sifirlanir
        self.table.setColumnCount(5)       # Tablonun sutun sayisi ayarlanir
        self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
        self.table.setColumnWidth(0,120)    # Bazi sutunlarin uzunluklari ayarlanir.
        self.table.setColumnWidth(1,100)
        self.table.setColumnWidth(2,100)
        self.table.setColumnWidth(3,105)
        self.table.setColumnWidth(4,105)
        self.table.setHorizontalHeaderLabels(['Pharmacy_ID','Name','Night_Work','Product_ID','Category_ID'])
        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().hide()
        row = self.table.rowCount()
        
        # Data tablosundaki her eleman for dongusu ile donulur
        for x in data:
            # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QTableWidgetItem(str(x[0])))
            self.table.setItem(row, 1, QTableWidgetItem(x[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(x[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(x[3])))
            self.table.setItem(row, 4, QTableWidgetItem(str(x[4])))
            
            # Bir sonraki adim icin satir sayisi bir arttirilir
            row = row + 1            
 
    def viewProducts(self):
        cur = con.cursor()
        cur.execute(f"select * from [dbo].[PRODUCTS]")  # Butun gemiler sql fonksiyonuyla secilir
        data = cur.fetchall()                             # Secilen tablo data adli degiskende tutulur
        cur.close()
        
        self.table.clearContents()         # Gecerli tablo sifirlanir
        self.table.setColumnCount(4)       # Tablonun sutun sayisi ayarlanir
        self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
        self.table.setColumnWidth(0,100)    # Bazi sutunlarin uzunluklari ayarlanir.
        self.table.setColumnWidth(1,120)
        self.table.setColumnWidth(2,60)
        self.table.setColumnWidth(3,110)
        self.table.setHorizontalHeaderLabels(['Product_ID','Register_Date','Price','Category_ID'])
        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().hide()
        row = self.table.rowCount()
        
        # Data tablosundaki her eleman for dongusu ile donulur
        for x in data:
            # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QTableWidgetItem(str(x[0])))
            self.table.setItem(row, 1, QTableWidgetItem(x[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(x[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(x[3])))
            
            # Bir sonraki adim icin satir sayisi bir arttirilir
            row = row + 1
      
    def refreshButton(self):
        if self.radioCategory.isChecked():
            self.viewCategories()
        elif self.radioPharmacy.isChecked():
            self.viewPharmacys()
        elif self.radioProducts.isChecked():
            self.viewProducts()
        else:
            QMessageBox.about(self, "Error", "Please select the table you want to refresh.")
        
    def insertButton(self):
        if self.radioCategory.isChecked():
            self.addCategory = AddCategory("add",con)
            self.addCategory.show()
        elif self.radioPharmacy.isChecked():
            self.addPharmacy = AddPharmacy("add",con)
            self.addPharmacy.show()
        elif self.radioProducts.isChecked():
            self.addProduct = AddProduct("add",con)
            self.addProduct.show()
        else:
            QMessageBox.about(self, "Error", "Please select a table to insert new item.")
            
    def updateButton(self):
        if self.radioCategory.isChecked():
            self.addCategory = AddCategory("upd",con)
            self.addCategory.show()
        elif self.radioPharmacy.isChecked():
            self.addPharmacy = AddPharmacy("upd",con)
            self.addPharmacy.show()
        elif self.radioProducts.isChecked():
            self.addProduct = AddProduct("upd",con)
            self.addProduct.show()
        else:
            QMessageBox.about(self, "Error", "Please select a table to insert new item.")
            
    def deleteButton(self):
        if self.radioCategory.isChecked():
            self.deleteCategory = DeleteElement("cat", con)
            self.deleteCategory.show()            
        elif self.radioPharmacy.isChecked():
            self.deletePharmacy = DeleteElement("pha", con)
            self.deletePharmacy.show()            
        elif self.radioProducts.isChecked():
            self.deleteProduct = DeleteElement("pro", con)
            self.deleteProduct.show()            
        else:
            QMessageBox.about(self, "Error", "Please select a table to delete item.")
        
    def viewCategoriesProducts(self):
        cur = con.cursor()
        cur.execute('''
                    SELECT 
                    [E-ECZANE].dbo.PRODUCTS.Product_ID,
                    [E-ECZANE].dbo.PRODUCTS.Register_Date,
                    [E-ECZANE].dbo.PRODUCTS.Price,
                    [E-ECZANE].dbo.PRODUCTS.Category_ID,
                    [E-ECZANE].dbo.Categories.Type
                    FROM [E-ECZANE].[dbo].PRODUCTS
                    INNER JOIN [E-ECZANE].[dbo].Categories ON [E-ECZANE].[dbo].PRODUCTS.Category_ID = [E-ECZANE].dbo.Categories.Category_ID
                    ''')  # Butun gemiler sql fonksiyonuyla secilir
        data = cur.fetchall()                             # Secilen tablo data adli degiskende tutulur
        cur.close()
        
        self.table.clearContents()         # Gecerli tablo sifirlanir
        self.table.setColumnCount(5)       # Tablonun sutun sayisi ayarlanir
        self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
        self.table.setColumnWidth(0,100)    # Bazi sutunlarin uzunluklari ayarlanir.
        self.table.setColumnWidth(1,120)
        self.table.setColumnWidth(2,50)
        self.table.setColumnWidth(3,120)
        self.table.setColumnWidth(4,120)
        self.table.setHorizontalHeaderLabels(['Product_ID','Register_Date','Price','Category_ID','Type'])
        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().hide()
        row = self.table.rowCount()
        
        # Data tablosundaki her eleman for dongusu ile donulur
        for x in data:
            # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QTableWidgetItem(str(x[0])))
            self.table.setItem(row, 1, QTableWidgetItem(x[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(x[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(x[3])))
            self.table.setItem(row, 4, QTableWidgetItem(str(x[4])))
            
            # Bir sonraki adim icin satir sayisi bir arttirilir
            row = row + 1
            
    def viewCategoriesPharmacys(self):
        cur = con.cursor()
        cur.execute('''
                    SELECT 
                    [E-ECZANE].[dbo].PHARMACYS.Pharmacy_ID, 
                    [E-ECZANE].[dbo].PHARMACYS.Name, 
                    [E-ECZANE].[dbo].PHARMACYS.Night_Work_Date,
                    [E-ECZANE].[dbo].PHARMACYS.Product_ID,
                    [E-ECZANE].[dbo].PHARMACYS.Category_ID,
                    [E-ECZANE].dbo.Categories.Type
                    FROM [E-ECZANE].[dbo].PHARMACYS
                    INNER JOIN [E-ECZANE].[dbo].Categories ON [E-ECZANE].[dbo].PHARMACYS.Category_ID = [E-ECZANE].dbo.Categories.Category_ID
                    
                    ''')  # Butun gemiler sql fonksiyonuyla secilir
        data = cur.fetchall()                             # Secilen tablo data adli degiskende tutulur
        cur.close()
        
        self.table.clearContents()         # Gecerli tablo sifirlanir
        self.table.setColumnCount(6)       # Tablonun sutun sayisi ayarlanir
        self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
        self.table.setColumnWidth(0,120)    # Bazi sutunlarin uzunluklari ayarlanir.
        self.table.setColumnWidth(1,70)
        self.table.setColumnWidth(2,140)
        self.table.setColumnWidth(3,90)
        self.table.setColumnWidth(4,90)
        self.table.setColumnWidth(5,100)
        self.table.setHorizontalHeaderLabels(['Pharmacy_ID','Name','Night_Work_Date','Product_ID','Category_ID','Type'])
        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().hide()
        row = self.table.rowCount()
        
        # Data tablosundaki her eleman for dongusu ile donulur
        for x in data:
            # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QTableWidgetItem(str(x[0])))
            self.table.setItem(row, 1, QTableWidgetItem(x[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(x[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(x[3])))
            self.table.setItem(row, 4, QTableWidgetItem(str(x[4])))
            self.table.setItem(row, 5, QTableWidgetItem(str(x[5])))
            
            # Bir sonraki adim icin satir sayisi bir arttirilir
            row = row + 1
            
    def viewPharmacysProducts(self):
        cur = con.cursor()
        cur.execute('''                
                    SELECT 
                    [E-ECZANE].[dbo].PHARMACYS.Pharmacy_ID,
                    [E-ECZANE].[dbo].PHARMACYS.Name, 
                    [E-ECZANE].[dbo].PHARMACYS.Night_Work_Date, 
                    [E-ECZANE].[dbo].PHARMACYS.Product_ID, 
                    [E-ECZANE].[dbo].PRODUCTS.Register_Date,
                    [E-ECZANE].[dbo].PRODUCTS.Price,
                    [E-ECZANE].[dbo].PRODUCTS.Category_ID
                    FROM [E-ECZANE].[dbo].PHARMACYS
                    INNER JOIN [E-ECZANE].[dbo].PRODUCTS ON [E-ECZANE].[dbo].PHARMACYS.Product_ID = [E-ECZANE].dbo.PRODUCTS.Product_ID and [E-ECZANE].dbo.PHARMACYS.Category_ID = [E-ECZANE].dbo.PRODUCTS.Category_ID
                    ''')  # Butun gemiler sql fonksiyonuyla secilir
        data = cur.fetchall()                             # Secilen tablo data adli degiskende tutulur
        cur.close()
        
        self.table.clearContents()         # Gecerli tablo sifirlanir
        self.table.setColumnCount(7)       # Tablonun sutun sayisi ayarlanir
        self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
        self.table.setColumnWidth(0,120)    # Bazi sutunlarin uzunluklari ayarlanir.
        self.table.setColumnWidth(1,70) 
        self.table.setColumnWidth(2,140)     
        self.table.setColumnWidth(5,50) 
        self.table.setColumnWidth(6,100) 
        self.table.setHorizontalHeaderLabels(['Pharmacy_ID','Name','Night_Work_Date','Product_ID','Register_Date','Price','Category_ID'])
        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().hide()
        row = self.table.rowCount()
        
        # Data tablosundaki her eleman for dongusu ile donulur
        for x in data:
            # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QTableWidgetItem(str(x[0])))
            self.table.setItem(row, 1, QTableWidgetItem(x[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(x[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(x[3])))
            self.table.setItem(row, 4, QTableWidgetItem(str(x[4])))
            self.table.setItem(row, 5, QTableWidgetItem(str(x[5])))
            self.table.setItem(row, 6, QTableWidgetItem(str(x[6])))
            
            # Bir sonraki adim icin satir sayisi bir arttirilir
            row = row + 1
             
    def viewAll(self):
        cur = con.cursor()
        cur.execute('''
                    SELECT 
                    [E-ECZANE].[dbo].PHARMACYS.Pharmacy_ID,
                    [E-ECZANE].[dbo].PHARMACYS.Name, 
                    [E-ECZANE].[dbo].PHARMACYS.Night_Work_Date, 
                    [E-ECZANE].[dbo].PHARMACYS.Product_ID, 
                    [E-ECZANE].[dbo].PRODUCTS.Register_Date,
                    [E-ECZANE].[dbo].PRODUCTS.Price,
                    [E-ECZANE].[dbo].PRODUCTS.Category_ID,
                    [E-ECZANE].[dbo].Categories.Type
                    FROM [E-ECZANE].[dbo].PHARMACYS
                    INNER JOIN [E-ECZANE].[dbo].PRODUCTS ON [E-ECZANE].[dbo].PHARMACYS.Product_ID = [E-ECZANE].dbo.PRODUCTS.Product_ID and [E-ECZANE].dbo.PHARMACYS.Category_ID = [E-ECZANE].dbo.PRODUCTS.Category_ID
                    INNER JOIN [E-ECZANE].dbo.Categories ON [E-ECZANE].dbo.PHARMACYS.Category_ID = [E-ECZANE].dbo.Categories.Category_ID and [E-ECZANE].dbo.PHARMACYS.Category_ID = [E-ECZANE].dbo.Categories.Category_ID
                    ''')  # Butun gemiler sql fonksiyonuyla secilir
        data = cur.fetchall()                             # Secilen tablo data adli degiskende tutulur
        cur.close()
        
        self.table.clearContents()         # Gecerli tablo sifirlanir
        self.table.setColumnCount(8)       # Tablonun sutun sayisi ayarlanir
        self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
        # self.table.setColumnWidth(0,120)    # Bazi sutunlarin uzunluklari ayarlanir.
        self.table.setHorizontalHeaderLabels(['Pharmacy_ID','Name','Night_Work_Date','Product_ID','Register_Date','Price','Category_ID','Type'])
        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().hide()
        row = self.table.rowCount()
        
        # Data tablosundaki her eleman for dongusu ile donulur
        for x in data:
            # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QTableWidgetItem(str(x[0])))
            self.table.setItem(row, 1, QTableWidgetItem(x[1]))
            self.table.setItem(row, 2, QTableWidgetItem(str(x[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(x[3])))
            self.table.setItem(row, 4, QTableWidgetItem(str(x[4])))
            self.table.setItem(row, 5, QTableWidgetItem(str(x[5])))
            self.table.setItem(row, 6, QTableWidgetItem(str(x[6])))
            self.table.setItem(row, 7, QTableWidgetItem(str(x[7])))
            
            # Bir sonraki adim icin satir sayisi bir arttirilir
            row = row + 1
       
#App initialization
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()