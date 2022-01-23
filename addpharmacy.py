from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore

class AddPharmacy (QMainWindow):

    def __init__(self, type_,con):
        super().__init__()
        
        uic.loadUi('python/addpharmacy.ui',self)
        
        if type_ == "add":
            self.txtPharmacyID.setDisabled(True)
        
        
        self.btnSave.clicked.connect(lambda: self.addPharmacy(con, type_))
        self.btnCancel.clicked.connect(self.close)              
        

    def addPharmacy(self, con, type_):
        cur = con.cursor()
        if(type_ == "add"):
            cur.execute(
                '''
                py
                ''',
                (self.txtName.text(), self.dateNight.date().toPyDate(), self.txtProductID.text(), self.txtCategoryID.text(),));
        elif(type_ == "upd"):
            cur.execute(
                '''
                UPDATE [dbo].[PHARMACYS] 
                SET Name = ? , Night_Work_Date = ? , Product_ID = ? , Category_ID = ? 
                WHERE Pharmacy_ID = ?
                ''',
                (self.txtName.text(), self.dateNight.date().toPyDate(), self.txtProductID.text(), self.txtCategoryID.text(), self.txtPharmacyID.text()));
        else:
            QMessageBox.about(self, "Hata", "Yanlış işlem")
        con.commit()
        cur.close()
        self.close()