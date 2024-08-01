from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QInputDialog
from PyQt5.QtCore import Qt


class ClickableLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("border: 2px solid black; border-radius: 10px; padding: 5px; background-color: lightgray;")
        self.setAlignment(Qt.AlignCenter)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        # Обработка события клика
        print(f"Clicked on: {self.text()}")
        super().mousePressEvent(event)

class ProductEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.photo_links = []  # Список для хранения ссылок на фотографии
        self.initUI()
        self.colors = ["green", "yellow", "red", "lightblue", "purple"]
        self.color_now = 0

    def initUI(self):
        main_layout = QHBoxLayout()

        # Левая часть - меню для выбора фотографий
        self.photo_menu_layout = QVBoxLayout()
        self.addPhotoButton()
        self.add_photo_button = QPushButton('Добавить фото', self)
        self.add_photo_button.setStyleSheet("background-color: #28A745; color: white; font-size: 20px;")
        self.add_photo_button.clicked.connect(self.addPhotoButton)
        self.photo_menu_layout.addWidget(self.add_photo_button)
        main_layout.addLayout(self.photo_menu_layout, 1)

        # Правая часть - основное содержимое
        right_layout = QVBoxLayout()

        self.button_plus_variable = QPushButton('+', self)
        self.button_plus_variable.setStyleSheet("background-color: #0066FF; color: white; font-size: 20px;")
        self.button_plus_variable.clicked.connect(self.on_button_plus_variable_clicked)
        self.button_plus_variable.setMaximumWidth(100)
        right_layout.addWidget(self.button_plus_variable)

        # Горизонтальный макет для кнопок
        self.button_layout = QHBoxLayout()
        right_layout.addLayout(self.button_layout)

        # Создаем и добавляем статичные поля
        self.createStaticFields(right_layout)

        # Поле и кнопка для создания нового поля
        self.new_field_name_input = QLineEdit(self)
        self.new_field_name_input.setPlaceholderText("Введите название нового поля")
        self.new_field_name_input.setStyleSheet("font-size: 21px;")
        self.new_field_name_input.setMinimumSize(150, 50)
        right_layout.addWidget(self.new_field_name_input)

        self.add_field_button = QPushButton('Добавить поле', self)
        self.add_field_button.clicked.connect(self.addNewField)
        self.add_field_button.setMinimumSize(150, 50)
        right_layout.addWidget(self.add_field_button)

        # Макет для динамически добавляемых полей
        self.dynamic_fields_layout = QVBoxLayout()
        self.dynamic_fields_container = QWidget()
        self.dynamic_fields_container.setLayout(self.dynamic_fields_layout)
        right_layout.addWidget(self.dynamic_fields_container)

        # Добавление вертикального растяжения, чтобы все элементы оставались сверху
        right_layout.addStretch()

        # Установка правого макета как основной части
        main_layout.addLayout(right_layout, 2)

        # Установка главного макета
        self.setLayout(main_layout)
        self.setWindowTitle('Редактор товара')
        self.setMinimumSize(600, 400)
        self.show()

    def createStaticFields(self, layout):
        # Создаем и добавляем статичные поля

        # Поле "Наименование"
        field_layout = QVBoxLayout()
        dynamic_layout = QHBoxLayout()
        field_label = QLabel("Наименование", self)
        field_label.setStyleSheet("font-size: 21px;")
        self.name_input = QLineEdit(self)
        self.name_input.setStyleSheet("background-color: white; color: black; font-size: 21px;")
        self.name_input.setMinimumSize(150, 50)
        self.name_input.textChanged.connect(lambda text, l=dynamic_layout: self.updateWords(l, self.name_input))
        field_layout.addWidget(field_label)
        field_layout.addWidget(self.name_input)
        field_layout.addLayout(dynamic_layout)
        layout.addLayout(field_layout)

        # Поле "Бренд"
        field_layout = QVBoxLayout()
        dynamic_layout = QHBoxLayout()
        field_label = QLabel("Бренд", self)
        field_label.setStyleSheet("font-size: 21px;")
        self.brend_input = QLineEdit(self)
        self.brend_input.setStyleSheet("background-color: white; color: black; font-size: 21px;")
        self.brend_input.setMinimumSize(150, 50)
        self.brend_input.textChanged.connect(lambda text, l=dynamic_layout: self.updateWords(l, self.brend_input))
        field_layout.addWidget(field_label)
        field_layout.addWidget(self.brend_input)
        field_layout.addLayout(dynamic_layout)
        layout.addLayout(field_layout)

        # Поле "Цвет"
        field_layout = QVBoxLayout()
        dynamic_layout = QHBoxLayout()
        field_label = QLabel("Цвет", self)
        field_label.setStyleSheet("font-size: 21px;")
        self.color_input = QLineEdit(self)
        self.color_input.setStyleSheet("background-color: white; color: black; font-size: 21px;")
        self.color_input.setMinimumSize(150, 50)
        self.color_input.textChanged.connect(lambda text, l=dynamic_layout: self.updateWords(l, self.color_input))
        field_layout.addWidget(field_label)
        field_layout.addWidget(self.color_input)
        field_layout.addLayout(dynamic_layout)
        layout.addLayout(field_layout)

        # Поле "Описание"
        field_layout = QVBoxLayout()
        dynamic_layout = QHBoxLayout()
        field_label = QLabel("Описание", self)
        field_label.setStyleSheet("font-size: 21px;")
        self.discription_input = QLineEdit(self)
        self.discription_input.setStyleSheet("background-color: white; color: black; font-size: 21px;")
        self.discription_input.setMinimumSize(150, 50)
        self.discription_input.textChanged.connect(lambda text, l=dynamic_layout: self.updateWords(l, self.discription_input))
        field_layout.addWidget(field_label)
        field_layout.addWidget(self.discription_input)
        field_layout.addLayout(dynamic_layout)
        layout.addLayout(field_layout)

    def add_variable_button(self, text, color):
        button = QPushButton(text, self)
        button.setStyleSheet(f"background-color: {color}; color: black; font-size: 21px;")
        button.setMinimumHeight(40)
        button.setMinimumWidth(150)
        button.clicked.connect(lambda: self.on_variable_button_clicked(text))
        self.button_layout.addWidget(button)

    def addNewField(self):
        # Получаем название нового поля
        field_name = self.new_field_name_input.text().strip()

        # Проверяем, что название не пустое
        if field_name:
            # Создаем горизонтальный макет для поля и кнопки удаления
            field_layout = QVBoxLayout()

            horizontal_layout = QHBoxLayout()

            dynamic_layout = QHBoxLayout()
            # Создаем новое поле ввода

            field_label = QLabel(field_name, self)
            field_label.setStyleSheet("font-size: 21px;")
            field_input = QLineEdit(self)
            field_input.setStyleSheet("background-color: white; color: black; font-size: 21px;")
            field_input.setMinimumSize(150, 50)
            field_input.textChanged.connect(lambda text, l=dynamic_layout: self.updateWords(l, field_input))

            # Создаем кнопку удаления
            delete_button = QPushButton('Удалить', self)
            delete_button.setStyleSheet("background-color: red; color: white; font-size: 14px;")
            delete_button.clicked.connect(lambda _, l=field_layout: self.removeField(l))

            # Добавляем поле и кнопку удаления в макет
            field_layout.addWidget(field_label)
            horizontal_layout.addWidget(field_input)
            horizontal_layout.addWidget(delete_button)

            field_layout.addLayout(horizontal_layout)
            field_layout.addLayout(dynamic_layout)

            # Добавляем макет в основной макет
            self.dynamic_fields_layout.addLayout(field_layout)

            # Очищаем поле ввода названия
            self.new_field_name_input.clear()

    def updateWords(self, layout, input_field):
        # Очищаем текущие кликабельные лейблы
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Получаем слова из текстового поля
        words = input_field.text().split()

        # Создаем кликабельные лейблы для каждого слова
        for word in words:
            clickable_label = ClickableLabel(word, self)
            layout.addWidget(clickable_label)

    def on_word_clicked(self, word):
        print(f'Слово "{word}" было кликнуто')

    def removeField(self, layout):
        # Удаляем макет и все виджеты в нем
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                # Рекурсивно удаляем вложенные макеты
                self.removeField(item.layout())
        layout.deleteLater()

    def on_variable_button_clicked(self, text):
        print(f"{text} выбрана")

    def on_button_plus_variable_clicked(self):
        self.add_variable_button(f'ПЕРЕМЕННАЯ {self.color_now + 1}', self.colors[self.color_now % 5])
        self.color_now += 1

    def addPhotoButton(self):
        # Создаем новую кнопку с плюсом
        new_button = QPushButton('+', self)
        new_button.setStyleSheet("background-color: #FF6600; color: white; font-size: 20px;")
        new_button.clicked.connect(self.addPhotoLink)
        new_button.setMaximumWidth(100)
        self.photo_menu_layout.insertWidget(self.photo_menu_layout.count() - 1, new_button)  # Добавляем над кнопкой "Добавить фото"

    def addPhotoLink(self):
        # Открываем диалоговое окно для ввода ссылок на фотографии
        links, ok = QInputDialog.getMultiLineText(self, 'Добавить ссылки на фотографии', 'Введите ссылки через enter:')
        if ok:
            # Разделяем введенные строки на отдельные ссылки
            new_links = links.split('\n')
            # Добавляем ссылки в список
            self.photo_links.extend([link.strip() for link in new_links if link.strip()])
            print(f"Ссылки на фотографии: {self.photo_links}")

app = QApplication([])
window = ProductEditor()
window.show()
app.exec_()
