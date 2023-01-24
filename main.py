import sys
from threading import Thread
from ctypes import Structure, windll, c_uint, sizeof, byref, wintypes, WinDLL
from PyQt6 import QtWidgets
import design
import time


def thread1():
    class ExampleApp(QtWidgets.QMainWindow, design.Ui_Stalin, Thread):
        def __init__(self):
            # Это здесь нужно для доступа к переменным, методам
            # и т.д. в файле design.py
            super().__init__()
            self.setupUi(self)  # Это нужно для инициализации нашего дизайна
            self.btnBrowse.clicked.connect(self.the_button_was_clicked)  # При нажатии кнопки выполняем метод
            # the_button_was_clicked

        def the_button_was_clicked(self):
            global stop
            if self.btnBrowse.text() == "Старт":    # Если текст кнопки "Старт"
                self.btnBrowse.setText("Стоп")      # Меняем текст кнопки
                self.label.show()   # Показываем строку что программа запущена
                stop = False
                if thread2.is_alive():  # Проверяем что поток 1 запущен. Если нет запускаем.
                    stop = False
                else:
                    thread2.start()

            else:   # Если текст кнопки "Стоп"
                self.btnBrowse.setText("Старт")     # Меняем текст кнопки
                self.label.hide()   # Скрываем строку что программа запущена
                stop = True     # Меняем переменную для перехода потока2 в режим ожидания

    def main():
        app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        window = ExampleApp()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно
        app.exec()  # и запускаем приложение

    if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
        main()  # то запускаем функцию main()


def thread2():
    user32 = WinDLL("user32", use_last_error=True)
    kernel32 = WinDLL("kernel32", use_last_error=True)

    class LASTINPUTINFO(Structure):
        _fields_ = [
            ('cbSize', c_uint),
            ('dwTime', c_uint),
        ]

    def get_idle_duration():  # Получаем время простоя
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        user32.GetLastInputInfo(byref(lastInputInfo))
        millis = kernel32.GetTickCount64() - lastInputInfo.dwTime  # Вычесляем количество тиков (разница в тиках между
        # последним вкученем Пк и итоговым числом промежутков времени,
        # после того как было принято последнее событие ввода данных. )
        return millis / 1000.0

    while True:
        time.sleep(1)
        if not stop:    # При получении True переходим в цикл ожидания.
            if windll.User32.GetForegroundWindow() != 0:  # Если компьютер заблокирован переходим в цикл ожидания.
                i = get_idle_duration()
                # print(get_idle_duration())
                if i <= 60:
                    pass    # Используется для отладки
                    # print("Пользователь активен")
                elif i > 60:
                    # print("Пробуждение")
                    cursor = wintypes.POINT()
                    windll.user32.GetCursorPos(byref(cursor))  # Получаем текущую позицию курсора с координатами x,y
                    windll.user32.SetCursorPos(0, 0)  # Смещаем курсор на координаты 0, 0
                    windll.user32.mouse_event(2, 0, 0, 0)  #
                    windll.user32.mouse_event(4, 0, 0, 0)  # Делаем клик мышкой
                    windll.user32.SetCursorPos(cursor.x, cursor.y)  # Возвращаем в исходное положение


thread2 = Thread(target=thread2, daemon=True)  # Создание потока 2. Назначаем демона
# (При закрытии или аварийного завершения потока 1 поток 2 автоматически закроется)
thread1 = Thread(target=thread1)  # Создание потока 1
thread1.start()  # Запуск потока 1
thread1.join()  # Ожидание завершения потока 1
