from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QFormLayout

class ProductEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        self.label = QLabel('Переменные')
        main_layout.addWidget(self.label)

        # Горизонтальный макет для кнопок
        button_layout = QHBoxLayout()

        self.button_variable_1 = QPushButton('ПЕРЕМЕННАЯ 1', self)
        self.button_variable_1.setStyleSheet("background-color: green; color: black; font-size: 16px;")
        self.button_variable_1.clicked.connect(self.on_button_variable_1_clicked)
        button_layout.addWidget(self.button_variable_1)

        self.button_variable_2 = QPushButton('ПЕРЕМЕННАЯ 2', self)
        self.button_variable_2.setStyleSheet("background-color: yellow; color: black; font-size: 16px;")
        self.button_variable_2.clicked.connect(self.on_button_variable_2_clicked)
        button_layout.addWidget(self.button_variable_2)

        self.button_variable_3 = QPushButton('ПЕРЕМЕННАЯ 3', self)
        self.button_variable_3.setStyleSheet("background-color: red; color: black; font-size: 16px;")
        self.button_variable_3.clicked.connect(self.on_button_variable_3_clicked)
        button_layout.addWidget(self.button_variable_3)

        main_layout.addLayout(button_layout)

        self.label.setMinimumHeight(30)
        self.button_variable_1.setMinimumHeight(40)
        self.button_variable_1.setMinimumWidth(150)
        self.button_variable_2.setMinimumHeight(40)
        self.button_variable_2.setMinimumWidth(150)
        self.button_variable_3.setMinimumHeight(40)
        self.button_variable_3.setMinimumWidth(150)

        fields_1_layout = QHBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Наименование")
        self.name_input.setStyleSheet("background-color: white; color: black; font-size: 16px;")
        fields_1_layout.addWidget(self.name_input)
        self.name_input.setMinimumSize(150, 50)

        main_layout.addLayout(fields_1_layout)

        fields_2_layout = QHBoxLayout()

        self.brend_input = QLineEdit(self)
        self.brend_input.setPlaceholderText("Бренд")
        self.brend_input.setStyleSheet("background-color: white; color: black; font-size: 16px;")
        fields_2_layout.addWidget(self.brend_input)
        self.brend_input.setMinimumSize(150, 50)

        main_layout.addLayout(fields_2_layout)

        fields_3_layout = QHBoxLayout()

        self.color_input = QLineEdit(self)
        self.color_input.setPlaceholderText("Цвет")
        self.color_input.setStyleSheet("background-color: white; color: black; font-size: 16px;")
        fields_3_layout.addWidget(self.color_input)
        self.color_input.setMinimumSize(150, 50)

        main_layout.addLayout(fields_3_layout)

        fields_4_layout = QHBoxLayout()

        self.discription_input = QLineEdit(self)
        self.discription_input.setPlaceholderText("Описание")
        self.discription_input.setStyleSheet("background-color: white; color: black; font-size: 16px;")
        fields_4_layout.addWidget(self.discription_input)
        self.discription_input.setMinimumSize(150, 50)

        main_layout.addLayout(fields_4_layout)

        # Добавление поля и кнопки для создания нового поля
        self.new_field_name_input = QLineEdit(self)
        self.new_field_name_input.setPlaceholderText("Введите название нового поля")
        self.new_field_name_input.setStyleSheet("font-size: 16px;")
        self.new_field_name_input.setMinimumSize(150, 50)
        main_layout.addWidget(self.new_field_name_input)

        self.add_field_button = QPushButton('Добавить поле', self)
        self.add_field_button.clicked.connect(self.addNewField)
        self.add_field_button.setMinimumSize(150, 50)
        main_layout.addWidget(self.add_field_button)

        # Макет для динамически добавляемых полей
        self.dynamic_fields_layout = QFormLayout()
        main_layout.addLayout(self.dynamic_fields_layout)

        # Добавление вертикального растяжения, чтобы все элементы оставались сверху
        main_layout.addStretch()

        # Установка главного макета
        self.setLayout(main_layout)
        self.setWindowTitle('Редактор товара')
        self.setMinimumSize(600, 400)
        self.show()

    def addNewField(self):
        # Получаем название нового поля
        field_name = self.new_field_name_input.text().strip()

        # Проверяем, что название не пустое
        if field_name:
            # Создаем новое поле ввода
            new_field = QLineEdit(self)
            new_field.setPlaceholderText(field_name)
            new_field.setStyleSheet("font-size: 16px;")

            # Добавляем новое поле в макет
            self.dynamic_fields_layout.addRow(new_field)

            # Очищаем поле ввода названия
            self.new_field_name_input.clear()

    def on_button_variable_1_clicked(self):
        print("Переменная 1 выбрана")

    def on_button_variable_2_clicked(self):
        print("Переменная 2 выбрана")

    def on_button_variable_3_clicked(self):
        print("Переменная 3 выбрана")

app = QApplication([])
window = ProductEditor()
app.exec_()
