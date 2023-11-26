import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from googletrans import Translator

class TranslationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Translation App")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.input_text = QLineEdit()
        self.output_text = QLabel()
        translate_button = QPushButton("Translate")

        layout.addWidget(self.input_text)
        layout.addWidget(translate_button)
        layout.addWidget(self.output_text)

        translate_button.clicked.connect(self.translate_text)

        self.translator = Translator()

    def translate_text(self):
        text = self.input_text.text()
        if text:
            translation = self.translator.translate(text, src='en', dest='uz')
            self.output_text.setText(translation.text)
        else:
            self.output_text.setText("Please enter text to translate.")

def main():
    app = QApplication(sys.argv)
    window = TranslationApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
