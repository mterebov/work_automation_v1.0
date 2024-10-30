import unittest
import MAIN


class TestMAIN(unittest.TestCase):

    def SetUp(self):
        self.file_data = []
        self.date_range = "01.09.2024 - 30.09.2024"
        self.summarry = 'Итого: 6.5 (5200.0)'
        self.year = True
        self.tasks = [['Резервное копирование баз 1С', '04.09.2024', '2 часа\n'],
                 ['Удаление помеченных на удаление объектов в Опт ГК и очистка неиспользуемых регистров сведений - еженедельно', '11.09.2024', '1 час\n'],
                 ['Обновление карты сайта', '11.09.2024', '0.5 часа\n'],
                 ['Обслуживание ИМ - анализ и удаление логов, оптимизация базы данных, проверка антивирусом, бэкап базы и скриптов', '11.09.2024', '2 часа\n'],
                 ['Тестирование и исправление базы Опт ГК - еженедельное', '18.09.2024', '1 час']]

    def summarry_test(self):
        self.test_sum = MAIN.summary(self.tasks)
        self.assertEqual(self.test_sum, self.summarry)
