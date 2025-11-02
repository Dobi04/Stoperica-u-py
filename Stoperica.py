import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(700,300,400,100)
        self.setWindowTitle("Stopwatch")
        
        
        self.time = QTime(0, 0, 0 ,0)
        self.timer = QTimer(self)
        self.Time_Label = QLabel("00:00:00.00", self)
        
        self.Start_Button = QPushButton("Start", self)
        self.Stop_Button = QPushButton("Stop", self)
        self.Reset_Button = QPushButton("Reset", self)
        

        vBox = QVBoxLayout()
        
        vBox.addWidget(self.Time_Label)
        vBox.addWidget(self.Start_Button)
        vBox.addWidget(self.Stop_Button)
        vBox.addWidget(self.Reset_Button)
        
        self.setLayout(vBox)
        self.Time_Label.setAlignment(Qt.AlignCenter)

        
        hBox = QHBoxLayout()
        hBox.addWidget(self.Start_Button)
        hBox.addWidget(self.Stop_Button)
        hBox.addWidget(self.Reset_Button)
        
        vBox.addLayout(hBox)
        
        self.setStyleSheet("""
                           QPushButton{
                               font-size: 40px;
                           }
                           QLabel{
                               background-color: #4ce6e0;
                               font-size: 120px;
                               font-weight: Bold;
                           }
                           """)
        self.Start_Button.clicked.connect(self.start)
        self.Stop_Button.clicked.connect(self.stop)
        self.Reset_Button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        
    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.Time_Label.setText("00:00:00.00")
    
    def format_time(self, time):
        text = str(self.time)
        heurs = time.hour()
        minutes = time.minute()
        seconds = time.second()
        millisecond = time.msec() //10
        return f"{heurs:02}:{minutes:02}:{seconds:02}.{millisecond:02}"
    
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.Time_Label.setText(self.format_time(self.time))
    
        
def main():
    app = QApplication(sys.argv)
    window = Stopwatch()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()