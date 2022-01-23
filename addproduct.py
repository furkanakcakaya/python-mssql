from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore

class AddProduct (QMainWindow):

    def __init__(self, type_,con):
        super().__init__()
        
        uic.loadUi('python/addproduct.ui',self)
        
        if type_ == "add":
            self.txtProductID.setDisabled(True)
        
        
        self.btnSave.clicked.connect(lambda: self.addProduct(con, type_))
        self.btnCancel.clicked.connect(self.close)              
        
        

    def addProduct(self, con, type_):
        cur = con.cursor()
        if(type_ == "add"):
            cur.execute(
                '''
                INSERT INTO [dbo].PRODUCTS (Register_Date, Price,Category_ID)
                VALUES ( ? , ? , ? )
                ''',
                ( self.dateRegister.date().toPyDate(), self.txtPrice.text(), self.txtCategoryID.text(),));
        elif(type_ == "upd"):
            cur.execute(
                '''
                UPDATE [dbo].[PRODUCTS] 
                SET Register_Date = ? , Price = ? , Category_ID = ? 
                WHERE Product_ID = ?
                ''',
                (self.dateRegister.date().toPyDate(), self.txtPrice.text(), self.txtCategoryID.text(), self.txtProductID.text()));
        else:
            QMessageBox.about(self, "Hata", "Yanlış işlem")
        con.commit()
        cur.close()
        self.close()