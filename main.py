from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.uix.scrollview import ScrollView
from api.search import perform_search

Window.clearcolor = (0, 0, 0, 1)  # Черный фон

class ParserPanelApp(MDApp):
    def build(self):
        self.title = "Parser Panel"
        self.icon = "assets/zoom.png"
        screen = Screen()

        # Заголовок
        title_label = MDLabel(
            text="Parser Panel",
            halign="center",
            theme_text_color="Custom",
            text_color=(0, 0, 1, 1),
            font_style="H4",
            bold=True
        )

        # Поисковая строка
        self.search_input = MDTextField(
            hint_text="Введите поисковый запрос",
            size_hint=(0.8, None),
            height=50,
            pos_hint={"center_x": 0.5}
        )

        # Кнопка "Поиск"
        search_button = MDRaisedButton(
            text="Поиск",
            size_hint=(None, None),
            size=(200, 50),
            md_bg_color=(0, 0, 1, 1),
            pos_hint={"center_x": 0.5},
            on_press=self.perform_search
        )

        # Меню с типами поиска
        search_menu = MDBoxLayout(orientation="vertical", spacing=10)
        scroll = ScrollView(size_hint=(1, None), height=400)

        # Добавляем типы поиска
        panels = [
            ("Стандартный поиск", "Поиск с выдачей ссылок."),
            ("Подробный поиск", "Ссылки с извлечённым текстом."),
            ("Поиск по времени", "Результаты за последнюю неделю."),
            ("Поиск по сайту", "Только с указанного сайта.")
        ]
        for panel_title, panel_text in panels:
            search_menu.add_widget(
                MDExpansionPanel(
                    icon="assets/zoom.png",
                    content=MDLabel(text=panel_text, halign="center"),
                    panel_cls=MDExpansionPanelOneLine(text=panel_title)
                )
            )
        scroll.add_widget(search_menu)

        # Основной макет
        layout = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            padding=20
        )
        layout.add_widget(title_label)
        layout.add_widget(self.search_input)
        layout.add_widget(search_button)
        layout.add_widget(scroll)

        screen.add_widget(layout)
        return screen

    def perform_search(self, instance):
        query = self.search_input.text
        results = perform_search(query)
        print(results)  # Вывод результата

ParserPanelApp().run()
