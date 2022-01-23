from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox

class DeleteElement (QMainWindow):

    def __init__(self, type_,con):
        super().__init__()
        
        loadUi("python/deleteElement.ui",self)
        
        # arguman olarak gonderilen tip degeri butonun baglandigi fonksiyona gonderilir
        self.type = type_
        self.btnDelete.clicked.connect(lambda: self.deleteSelectedId(con,type_))
        self.btnCancel.clicked.connect(self.close)              # Iptal butonu
        
        
    def deleteSelectedId(self,con,type_):
        
        #IF the type is Category
        if type_ == "cat":
            # Checking if the ID given by user is used in other tables
            cur = con.cursor()      
            cur.execute("select * from [dbo].[PHARMACYS] where Category_ID = ( ? )", [self.txtId.text()])
            data = cur.fetchall()
            if len(data) == 0:
                cur.execute("select * from [dbo].[PRODUCTS] where Category_ID = ( ? )", [self.txtId.text()])
                data = cur.fetchall()
                if len(data) == 0:
                    # If the deletion won't effect other tables, such as Pharmacys or Products, we execute our SQL query.
                    cur.execute("delete from [dbo].[Categories] where Category_ID = ( ? )", [self.txtId.text()])
                else:
                    QMessageBox.about(self, "Error", "The category you are trying to delete is used by other entities.")
            else:
                QMessageBox.about(self, "Error", "The category you are trying to delete is used by other entities.")
            cur.close()
            
        #IF the type is Pharmacy
        elif type_ == "pha":
            cur = con.cursor()
            cur.execute("delete from [dbo].[Pharmacys] where Pharmacy_ID = ( ? )", [self.txtId.text()])
            cur.close()
            
        #IF the type is Product
        elif type_ == "pro":
            cur = con.cursor()            
            # Checking if the ID given by user is used in other tables
            cur.execute("select * from [dbo].[PHARMACYS] where Product_ID = ( ? )", [self.txtId.text()])
            data = cur.fetchall()
            if len(data) == 0:
                cur.execute("delete from [dbo].[Products] where Product_ID = ( ? )", [self.txtId.text()])
            else:
                QMessageBox.about(self, "Error", "The category you are trying to delete is used by other entities.")
            cur.close()
        
        self.close()