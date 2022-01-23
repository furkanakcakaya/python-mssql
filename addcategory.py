from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore

class AddCategory (QMainWindow):

    def __init__(self, type_,con):
        super().__init__()
        
        uic.loadUi('python/addcategory.ui',self)
        
        if type_ == "add":
            self.txtCategoryID.setDisabled(True)
        
        
        self.btnSave.clicked.connect(lambda: self.addCategory(con, type_))
        self.btnCancel.clicked.connect(self.close)              
        
        

    def addCategory(self, con, type_):
        cur = con.cursor()
        if(type_ == "add"):
            cur.execute(
                "INSERT INTO [dbo].[Categories] (Type)"
                "VALUES ( ? )",
                (self.txtType.text(),));
        elif(type_ == "upd"):
            cur.execute(
                "UPDATE [dbo].[Categories] SET Type = ? WHERE Category_ID = ( ? )",
                (self.txtType.text(),self.txtCategoryID.text(),));
        else:
            QMessageBox.about(self, "Hata", "Yanlış işlem")
        con.commit()
        cur.close()
        self.close()