from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import depresiasiUI

#membuat pewarisan pada Python, dalam kasus ini class main mewarisi class depresiasiUI
class Main(QMainWindow, depresiasiUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #setupUi merupakan fungsi dari class depresiasiUI yang berfungsi untuk melakukan setup
        #sesuai dengan apa yang telah didefinisikan sebelumnya
        self.setupUi(self)
        #manjalankan fungsi hitungHasil() ketika tombol hitung di klik
        self.hitung.clicked.connect(self.hitungHasil)

    #definisikan fungsi untuk menghitung hasil
    def hitungHasil(self):
        #mengambil nilai input
        input1 = self.lineEdit1.text()
        input2 = self.lineEdit2.text()
        input3 = self.umur.text()
        #menampung nilai input ke dalam variabel dengan tipe data int
        nilai1 = int(input1)
        nilai2 = int(input2)
        nilai3 = int(input3)
        #menghitung dan menampilkan hasil
        hasil = (nilai1-nilai2)/nilai3
        self.lineEdit3.setText(str(hasil))

def main():
    app = QApplication(sys.argv)        #buat instance baru QtApplication
    winForm = Main()                    #inisialisasi variable winForm sebagain class Main
    winForm.show()                      #tampilkan windows form
    sys.exit(app.exec_())               #eksekusi applikasi

if __name__ == '__main__':              #jika file dijalanakan secara langsung, maka jalankan fungsi main()
    main()