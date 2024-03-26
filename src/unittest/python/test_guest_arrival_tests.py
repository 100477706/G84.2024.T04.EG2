import hashlib
import json
import os
import unittest
from pathlib import Path

import UC3MTravel.HotelManagementException
from UC3MTravel import HotelManager
from UC3MTravel import HotelReservation
from freezegun import freeze_time


class TestGuestArrival(unittest.TestCase):

# PRUEBA CON TODOS LOS CASOS CORRECTOS
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': persona['_HOTEL_RESERVATION__localizer'],
                                    'IdCard': persona['_HOTEL_RESERVATION__id_card']})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        with open(ingreso, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        if data_list.get('Localizer') == "7532a04bf679689f4156228d60c542e4":
            found = True
        self.assertTrue(found)

        habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)


# PRUEBA CON TODOS LOS CASOS CORRECTOS E INTRODUCIENDO MANUALMENTE EL STORE_RESERVATION
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '7532a04bf679689f4156228d60c542e4',
                                    'IdCard': '11185346D'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        with open(ingreso, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        if data_list.get('Localizer') == "7532a04bf679689f4156228d60c542e4":
            found = True
        self.assertTrue(found)

        habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)


##############
# COMPROBACIÓN DE EXCEPCIONES
# PRUEBA DE BORRADO DEL NODO 2 Y POR ENDE DEL 5
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo2_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 2 Y POR ENDE DEL NODO 5
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid4(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo2_duplicacion.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 3
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid5(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo3_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 3
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid6(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo3_duplicacion.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 4 Y POR ENDE DEL 9
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid7(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo4_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 4 Y POR ENDE DEL 9
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid8(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo4_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 5,
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid9(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo5_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 6
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid9(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo6_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 6
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid10(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo6_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 7 Y POR ENDE, DEL NODO 13
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid11(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo7_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 7 Y POR ENDE, DEL NODO 13
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid12(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo7_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 8
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid13(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo8_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 8
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid14(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo8_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 9
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid15(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo9_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 10
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid16(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo10_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 10
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid17(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo10_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 11 Y POR ENDE, DEL NODO 20
# TAMBIÉN SE APLICA PARA EL NODO NO TERMINAL 15 Y PARA SU TERMIANAL 27
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid18(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo11_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 11 Y POR ENDE, DEL NODO 20
# TAMBIÉN SE APLICA PARA EL NODO NO TERMINAL 15 Y PARA SU TERMIANAL 27
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid19(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo11_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 12
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid20(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo12_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 12
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid21(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo12_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 13
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid22(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo13_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 14
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid23(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo14_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 14
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid24(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo14_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 16
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid25(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo16_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 16
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid26(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo16_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 17 Y POR ENDE, DEL NODO 31
# TAMBIÉN APLICA PARA LOS NODOS 19, 21, 23, 24, 26, 28 y 30,
# Y SUS NODOS TERMINALES 33, 34, 36, 37, 39, 40 y 42, RESPECTIVAMENTE
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid27(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo17_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 17 Y POR ENDE, DEL NODO 31
# TAMBIÉN APLICA PARA LOS NODOS 19, 21, 23, 24, 26, 28 y 30,
# Y SUS NODOS TERMINALES 33, 34, 36, 37, 39, 40 y 42, RESPECTIVAMENTE
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid28(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo17_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 18 Y POR ENDE, DEL NODO 32
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid29(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo18_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 18 Y POR ENDE, DEL NODO 32
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid30(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        ingreso = JSON_TEST_RF2 + "nodo18_duplicado.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 20 Y LA CUAL APLICA TAMBIÉN PARA EL NODO 27
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid31(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo20_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE ELIMINADO DEL NODO 22 Y POR ENDE, DEL NODO 35
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid32(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo22_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 22 Y POR ENDE, DEL NODO 35
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid33(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo22_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 25 Y POR ENDE, DEL NODO 39
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid34(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo25_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 25 Y POR ENDE, DEL NODO 39
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid35(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo25_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE BORRADO DEL NODO 29 Y POR ENDE, DEL NODO 41
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid36(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo29_borrado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE DUPLICADO DEL NODO 29 Y POR ENDE, DEL NODO 41
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid37(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo29_duplicado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 31
# TAMBIÉN APLICA PARA LOS TERMINALES 33, 34, 36, 37, 39, 40 y 42
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid38(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo31_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 32
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid39(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo32_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 35
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid40(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo35_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 38
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid41(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo38_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA DE MODIFICADO DEL NODO 41
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid42(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        JSON_TEST_RF2 = str(Path.home()) + \
                        "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/TestJsonRf2/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_TEST_RF2 + "nodo41_modificado.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(arrival):
            os.remove(arrival)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "JsonDecodeError")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA QUE VERIFICA QUE LOS EL DÍA DE LLEGADA NO SE CORRESPONDE CON EL DE LA RESERVA
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid43(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)

        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "29/07/2030", 5)
        self.assertEqual(reserva1, "64f108ad0e214fd504d2520c93347e18")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': persona['_HOTEL_RESERVATION__localizer'],
                                    'IdCard': persona['_HOTEL_RESERVATION__id_card']})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        with open(ingreso, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        if data_list.get('Localizer') == "64f108ad0e214fd504d2520c93347e18":
            found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message,
                         "La fecha de llegada no coincide con la del fichero de reserva")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA QUE VERIFICA SI EL LOCALIZER DEL FICHERO JSON DE ENTRADA COINCIDE CON EL DEL FICHERO DE
# RESERVAS

    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid44(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)

        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '64f108ad0e214fd504d2520c93347e18',
                                    'IdCard': '11185346D'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        with open(ingreso, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        if data_list.get('Localizer') == "64f108ad0e214fd504d2520c93347e18":
            found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "El Localizador no coincide")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)

# PRUEBA QUE VERIFICA SI EL ID_CARD DEL FICHERO JSON DE ENTRADA COINCIDE CON EL DE RESERVAS
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid45(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)

        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '7532a04bf679689f4156228d60c542e4',
                                    'IdCard': '12345678A'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        with open(ingreso, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        if data_list.get('Localizer') == "7532a04bf679689f4156228d60c542e4":
            found = True
        self.assertTrue(found)

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as \
                cm:
            habitacion = manager.guest_arrival(ingreso)
        self.assertEqual(cm.exception.message, "El IdCard no coincide")

        try:
            with open(arrival, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)


if __name__ == '__main__':
    unittest.main()