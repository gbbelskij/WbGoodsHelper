from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QFormLayout, QVBoxLayout, QSpacerItem, QSizePolicy

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

        # Создаем и добавляем статичные поля
        self.createStaticFields(main_layout)

        # Поле и кнопка для создания нового поля
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
        self.dynamic_fields_layout = QVBoxLayout()
        self.dynamic_fields_container = QWidget()
        self.dynamic_fields_container.setLayout(self.dynamic_fields_layout)
        main_layout.addWidget(self.dynamic_fields_container)

        # Добавление вертикального растяжения, чтобы все элементы оставались сверху
        main_layout.addStretch()

        # Установка главного макета
        self.setLayout(main_layout)
        self.setWindowTitle('Редактор товара')
        self.setMinimumSize(600, 400)
        self.show()

    def createStaticFields(self, layout):
        # Создаем и добавляем статичные поля
        self.static_fields = [
            ('Наименование', 'name_input'),
            ('Бренд', 'brend_input'),
            ('Цвет', 'color_input'),
            ('Описание', 'discription_input')
        ]

        for label_text, name in self.static_fields:
            # Создаем горизонтальный макет для метки и поля
            field_layout = QVBoxLayout()
            field_label = QLabel(label_text, self)
            field_label.setStyleSheet("font-size: 16px;")
            field_input = QLineEdit(self)
            field_input.setStyleSheet("background-color: white; color: black; font-size: 16px;")
            field_input.setMinimumSize(150, 50)
            field_layout.addWidget(field_label)
            field_layout.addWidget(field_input)
            layout.addLayout(field_layout)

            # Сохраняем ссылку на поле ввода
            setattr(self, name, field_input)

    def addNewField(self):
        # Получаем название нового поля
        field_name = self.new_field_name_input.text().strip()

        # Проверяем, что название не пустое
        if field_name:
            # Создаем горизонтальный макет для поля и кнопки удаления
            field_layout = QVBoxLayout()

            horizontal_layout = QHBoxLayout()
            # Создаем новое поле ввода

            field_label = QLabel(field_name, self)
            field_label.setStyleSheet("font-size: 16px;")
            field_input = QLineEdit(self)
            field_input.setStyleSheet("background-color: white; color: black; font-size: 16px;")
            field_input.setMinimumSize(150, 50)

            # Создаем кнопку удаления
            delete_button = QPushButton('Удалить', self)
            delete_button.setStyleSheet("background-color: red; color: white; font-size: 14px;")
            delete_button.clicked.connect(lambda _, l=field_layout: self.removeField(l))

            # Добавляем поле и кнопку удаления в макет
            field_layout.addWidget(field_label)
            horizontal_layout.addWidget(field_input)
            horizontal_layout.addWidget(delete_button)

            field_layout.addLayout(horizontal_layout)

            # Добавляем макет в основной макет
            self.dynamic_fields_layout.addLayout(field_layout)

            # Очищаем поле ввода названия
            self.new_field_name_input.clear()

    def removeField(self, layout):
        # Удаляем макет и все виджеты в нем
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                item.layout().deleteLater()
        layout.deleteLater()

    def on_button_variable_1_clicked(self):
        print("Переменная 1 выбрана")

    def on_button_variable_2_clicked(self):
        print("Переменная 2 выбрана")

    def on_button_variable_3_clicked(self):
        print("Переменная 3 выбрана")

app = QApplication([])
window = ProductEditor()
app.exec_()
