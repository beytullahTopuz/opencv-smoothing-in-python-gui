'''
    1180505035 beytullah topuz
    sayısal görüntü işleme hafta 6 ödev
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
import imutils


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 550, 281, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 701, 521))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btn_gaussian = QtWidgets.QPushButton(self.widget1)
        self.btn_gaussian.setObjectName("btn_gaussian")
        self.verticalLayout.addWidget(self.btn_gaussian)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.btn_median = QtWidgets.QPushButton(self.widget1)
        self.btn_median.setObjectName("btn_median")
        self.verticalLayout_2.addWidget(self.btn_median)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.btn_bilateral = QtWidgets.QPushButton(self.widget1)
        self.btn_bilateral.setObjectName("btn_bilateral")
        self.verticalLayout_3.addWidget(self.btn_bilateral)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.btn_averaging = QtWidgets.QPushButton(self.widget1)
        self.btn_averaging.setObjectName("btn_averaging")
        self.verticalLayout_4.addWidget(self.btn_averaging)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.btn_resim_yukle = QtWidgets.QPushButton(self.widget1)
        self.btn_resim_yukle.setObjectName("btn_resim_yukle")
        self.verticalLayout_5.addWidget(self.btn_resim_yukle)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # click events
        self.btn_gaussian.clicked.connect(self.gaussianbutton)
        self.btn_median.clicked.connect(self.medianBlurButton)
        self.btn_bilateral.clicked.connect(self.bilateralFiltreButton)
        self.btn_averaging.clicked.connect(self.averagingBlurButton)
        self.btn_resim_yukle.clicked.connect(self.loadImage)

    def gaussianbutton(self):
        print("gaussian")
        try:
            gaussianBlur = cv2.GaussianBlur(self.image, (5, 5), 16)

            gImage = imutils.resize(gaussianBlur, width=259)
            frame = cv2.cvtColor(gImage, cv2.COLOR_BGR2RGB)
            gImage = QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(gImage))
        except:
            print("dosya , resim yok")

    def bilateralFiltreButton(self):
        print("iki taraflı filtreleme")
        try:
            bilateralF = cv2.bilateralFilter(self.image, 11, 110, 100)

            bImage = imutils.resize(bilateralF, width=259)
            frame = cv2.cvtColor(bImage, cv2.COLOR_BGR2RGB)
            bImage = QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.label_3.setPixmap(QtGui.QPixmap.fromImage(bImage))
        except:
            print("dosya , resim yok")

    def averagingBlurButton(self):
        # label_4 kullanilacak
        print("averaging")
        try:
            blur = cv2.blur(self.image, (5, 5))
            image = imutils.resize(blur, width=259)
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            image = QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.label_4.setPixmap(QtGui.QPixmap.fromImage(image))
        except:
            print("dosya , resim yok")

    def medianBlurButton(self):
        print("median")
        try:
            medianBlur = cv2.medianBlur(self.image, 5)

            image = imutils.resize(medianBlur, width=259)
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
        except:
            print("dosya , resim yok")

    def loadImage(self):
        try:
            self.filename = QFileDialog.getOpenFileName(
                filter="Image (*.*)")[0]
            self.image = cv2.imread(self.filename)
            self.setPhoto(self.image)
        except:
            print("file resim seçimi yapmadiniz")

    def setPhoto(self, image):
        # bütün label arayüzüşerine orijinal fotoğrafı yükleme işlemi
        self.tmp = image
        image = imutils.resize(image, width=343)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
        self.label_3.setPixmap(QtGui.QPixmap.fromImage(image))
        self.label_4.setPixmap(QtGui.QPixmap.fromImage(image))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "1180505035 sayisal goruntu isleme odev"))
        self.label_5.setText(_translate(
            "MainWindow", "Kernel Boyutunu giriniz : "))
        self.label.setText(_translate("MainWindow", ""))
        self.btn_gaussian.setText(_translate(
            "MainWindow", "GAUSIIAN YUMUSATMA"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.btn_median.setText(_translate("MainWindow", "MEDIAN YUMUSATMA"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.btn_bilateral.setText(_translate(
            "MainWindow", "IKI TARAFLI (BILATERAL) YUMUSATMA"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.btn_averaging.setText(_translate(
            "MainWindow", "AGIRLIKLI ORTALAMA (AVERAGING) YUMUSATMASI"))
        self.btn_resim_yukle.setText(_translate("MainWindow", "RESIM YUKLE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
