from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QMainWindow

class appLogic:
    def validate_input(self, input_text):
        valid_destinations = [
            "Ancient Egypt",
            "Woodstock",
            "Renaissance",
            "Jurassic Period"
        ]
        return input_text in valid_destinations
    
    def get_destination_info(self, destination):
        if destination == "Ancient Egypt":
            win = ancientEgyptWindow()
            win.show()
            return win
        elif destination == "Woodstock":
            win = woodstockWindow()
            win.show()
            return win
        elif destination == "Renaissance":
            win = renaissanceWindow()
            win.show()
            return win
        elif destination == "Jurassic Period":
            win = jurassicPeriodWindow()
            win.show()
            return win
        else:
            return "Unknown destination."
        
    def progress_bar(self, destination):
        QProgressBar = QtWidgets.QProgressBar()
        QProgressBar.setGeometry(200, 200, 250, 20)
        if destination == "Ancient Egypt":
            QProgressBar.setValue(25)
            QProgressBar.setStyleSheet("QProgressBar::chunk { background: yellow; }")
        elif destination == "Woodstock":
            QProgressBar.setValue(50)
            QProgressBar.setStyleSheet("QProgressBar::chunk { background: green; }")
        elif destination == "Renaissance":
            QProgressBar.setValue(75)
            QProgressBar.setStyleSheet("QProgressBar::chunk { background: blue; }")
        elif destination == "Jurassic Period":
            QProgressBar.setValue(100)
            QProgressBar.setStyleSheet("QProgressBar::chunk { background: red; }")
        return QProgressBar
        

class ancientEgyptWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ancient Egypt")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        label1 = QLabel("Location Ancient Egypt: Giza", self)
        label1.setGeometry(50, 20, 500, 30)
        label1.setStyleSheet("font-size: 20px; font-weight: bold;")

        label2 = QLabel("You die, and instead of peace, you're dragged into a tomb\n" \
        " to rot next to your boss forever. In the early dynasties, when pharaohs died,\n" \
        " some servants were killed or buried alive to “serve” them in the afterlife.\n" \
        " Imagine being loyal enough to your ruler that your reward is suffocation in a sealed \
        stone room under sand and sun.", self)
        label2.setGeometry(50, 50, 500, 30)

        label3 = QLabel("Description: The Great Pyramids and the Sphinx are here.", self)
        label3.setGeometry(50, 80, 500, 30)

class woodstockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Woodstock")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        label1 = QLabel("Location Woodstock: Bethel, New York", self)
        label1.setGeometry(50, 20, 500, 30)
        label1.setStyleSheet("font-size: 20px; font-weight: bold;")

        label2 = QLabel("You die, and instead of peace, you're dragged into a muddy field\n" \
        " to rot next to your boss forever. The Woodstock festival was a music festival\n" \
        " that took place in August 1969.", self)
        label2.setGeometry(50, 50, 500, 30)
        label3 = QLabel("Description: The site of the famous 1969 music festival.", self)
        label3.setGeometry(50, 80, 500, 30)

class renaissanceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Renaissance")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        label1 = QLabel("Location Renaissance: Florence, Italy", self)
        label1.setGeometry(50, 20, 500, 30)
        label1.setStyleSheet("font-size: 20px; font-weight: bold;")

        label2 = QLabel("You die, and instead of peace, you're dragged into a painting\n" \
        " to rot next to your boss forever. The Renaissance was a period of great cultural\n" \
        " revival and achievement in Europe.", self)
        label2.setGeometry(50, 50, 500, 30)

        label3 = QLabel("Description: A period of great cultural revival and achievement.", self)
        label3.setGeometry(50, 80, 500, 30)

class jurassicPeriodWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jurassic Period")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        label1 = QLabel("Location Jurassic Period: Morrison Formation, USA", self)
        label1.setGeometry(50, 20, 500, 30)
        label1.setStyleSheet("font-size: 20px; font-weight: bold;")

        label2 = QLabel("You die, and instead of peace, you're dragged into a fossil\n" \
        " to rot next to your boss forever. The Jurassic Period is known for its rich\n" \
        " dinosaur fossils.", self)
        label2.setGeometry(50, 50, 500, 30)

        label3 = QLabel("Description: Known for its rich dinosaur fossils.", self)
        label3.setGeometry(50, 80, 500, 30)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("All Py is Good Py")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(50, 330, 500, 20)
        self.progress_bar.setValue(0)  # Initial value

        
        label1 = QLabel("Let's go back in time, doc?", self)
        label1.setGeometry(50, 20, 500, 30)
        label1.setStyleSheet("font-size: 20px; font-weight: bold;")

        label2 = QLabel("Chose a place from the list below:", self)
        label2.setStyleSheet("font-size: 16px; font-weight: bold;")
        label2.setGeometry(50, 50, 500, 30)

        label3 = QLabel("Ancient Egypt: Location Giza", self)
        label3.setStyleSheet("font-weight: bold;")
        label3.setGeometry(50, 80, 500, 30)

        label4 = QLabel("Woodstock: Bethel, New York", self)
        label4.setStyleSheet("font-weight: bold;")
        label4.setGeometry(50, 110, 500, 30)

        label5 = QLabel("Renaissance: Florence, Italy", self)
        label5.setStyleSheet("font-weight: bold;")
        label5.setGeometry(50, 140, 500, 30)

        label6 = QLabel("Jurassic Period: Morrison Formation, USA", self)
        label6.setStyleSheet("font-weight: bold;")
        label6.setGeometry(50, 170, 500, 30)

        self.textInput = QLineEdit(self)
        self.textInput.setGeometry(50, 210, 500, 30)
        self.textInput.setPlaceholderText("Enter your Delorean destination here...")
        self.textInput.setStyleSheet("font-size: 14px;")

        self.return_label = QLabel("", self)
        self.return_label.setGeometry(50, 290, 500, 30)
        self.return_label.setStyleSheet("font-weight: bold;")

        self.button = QPushButton("Submit", self)
        self.button.setGeometry(50, 250, 500, 30)
        self.button.clicked.connect(self.check_destination)

    def check_destination(self):
        destination_answer = self.textInput.text()
        validation = appLogic().validate_input(destination_answer)
        if validation:
            self.return_label.setText("Great choice! Let's go!")
            self.return_label.setStyleSheet("color: green; font-weight: bold;")
            self.destination_window = appLogic().get_destination_info(destination_answer)
            # Update progress bar
            if destination_answer == "Ancient Egypt":
                self.progress_bar.setValue(25)
                self.progress_bar.setStyleSheet("QProgressBar::chunk { background: yellow; }")
            elif destination_answer == "Woodstock":
                self.progress_bar.setValue(50)
                self.progress_bar.setStyleSheet("QProgressBar::chunk { background: green; }")
            elif destination_answer == "Renaissance":
                self.progress_bar.setValue(75)
                self.progress_bar.setStyleSheet("QProgressBar::chunk { background: blue; }")
            elif destination_answer == "Jurassic Period":
                self.progress_bar.setValue(100)
                self.progress_bar.setStyleSheet("QProgressBar::chunk { background: red; }")
        else:
            self.return_label.setText(
                "Invalid destination. Please try again.\nPlease enter Ancient Egypt, Woodstock, Renaissance, or Jurassic Period."
            )
            self.return_label.setStyleSheet("color: red; font-weight: bold;")
            self.progress_bar.setValue(0)
            self.progress_bar.setStyleSheet("")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()  # Keeps the window open