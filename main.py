from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QInputDialog, QTextEdit, QSizePolicy, QScrollArea, QFrame
from PyQt5.QtCore import Qt


class ClickableTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(False)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def setHtml(self, html):
        super().setHtml(html)
        self.setReadOnly(False)

    def mousePressEvent(self, event):
        cursor = self.cursorForPosition(event.pos())
        cursor.select(cursor.WordUnderCursor)
        clicked_word = cursor.selectedText()
        if clicked_word:
            print("Clicked word:", clicked_word)
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

        # Создаем контейнер для динамических полей и прокручиваемую область
        self.dynamic_fields_layout = QVBoxLayout()
        self.dynamic_fields_container = QWidget()
        self.dynamic_fields_container.setLayout(self.dynamic_fields_layout)
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.dynamic_fields_container)
        scroll_area.setWidgetResizable(True)
        scroll_area.setMinimumHeight(400)
        right_layout.addWidget(scroll_area)

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
        # Поле "Наименование"
        self.add_field_with_button("Наименование", layout)

        # Поле "Бренд"
        self.add_field_with_button("Бренд", layout)

        # Поле "Цвет"
        self.add_field_with_button("Цвет", layout)

        # Поле "Описание"
        self.add_field_with_button("Описание", layout)

    def add_field_with_button(self, label_text, layout):
        field_layout = QVBoxLayout()
        dynamic_layout = QHBoxLayout()

        field_label = QLabel(label_text, self)
        field_label.setStyleSheet("font-size: 21px;")

        text_input = ClickableTextEdit()
        text_input.setStyleSheet("background-color: white; color: black; font-size: 21px;")
        text_input.setMinimumSize(150, 50)
        text_input.setMaximumHeight(70)

        convert_button = QPushButton("Сделать слова кликабельными")
        # Используем lambda для передачи параметра
        convert_button.clicked.connect(lambda: self.convert_text(text_input))

        field_layout.addWidget(field_label)
        dynamic_layout.addWidget(text_input)
        dynamic_layout.addWidget(convert_button)
        field_layout.addLayout(dynamic_layout)
        layout.addLayout(field_layout)

    def convert_text(self, text_input):
        text = text_input.toPlainText()
        words = text.split()
        html_content = " ".join([f'<a href="#">{word}</a>' for word in words])
        text_input.setHtml(html_content)

    def add_variable_button(self, text, color):
        button = QPushButton(text, self)
        button.setStyleSheet(f"background-color: {color}; color: black; font-size: 21px;")
        button.setMinimumHeight(40)
        button.setMinimumWidth(150)
        button.clicked.connect(lambda: self.on_variable_button_clicked(text))
        self.button_layout.addWidget(button)

    def addNewField(self):
        field_name = self.new_field_name_input.text().strip()
        if field_name:
            field_layout = QVBoxLayout()
            dynamic_layout = QHBoxLayout()

            field_label = QLabel(field_name, self)
            field_label.setStyleSheet("font-size: 21px;")
            field_input = ClickableTextEdit()
            field_input.setStyleSheet("background-color: white; color: black; font-size: 21px;")
            field_input.setMinimumSize(150, 50)
            field_input.setMaximumHeight(50)

            convert_button = QPushButton("Сделать слова кликабельными")
            convert_button.clicked.connect(lambda: self.convert_text(field_input))

            delete_button = QPushButton('Удалить', self)
            delete_button.setStyleSheet("background-color: red; color: white; font-size: 14px;")
            delete_button.clicked.connect(lambda _, l=field_layout: self.removeField(l))

            field_layout.addWidget(field_label)
            dynamic_layout.addWidget(field_input)
            dynamic_layout.addWidget(convert_button)
            dynamic_layout.addWidget(delete_button)
            field_layout.addLayout(dynamic_layout)

            self.dynamic_fields_layout.addLayout(field_layout)
            self.new_field_name_input.clear()

    def convert_text(self, text_input):
        text = text_input.toPlainText()
        words = text.split()
        html_content = " ".join([f'<a href="#">{word}</a>' for word in words])
        text_input.setHtml(html_content)

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
