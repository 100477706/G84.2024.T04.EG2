import hashlib
import json
import os
import unittest
from pathlib import Path

import UC3MTravel.HotelManagementException
from UC3MTravel import HOTEL_MANAGER
from UC3MTravel import HotelReservation
from freezegun import freeze_time

class TestHotelManager(unittest.TestCase):

# PRUEBAS VALIDAS
    def test_guest_checkout_valid1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
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

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)


    def test_guest_checkout_valid2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
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

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        reserva2 = manager.RoomReservation(6011111111111117, "Gabriel Rivera", "12345678A",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva2, "33af6850960f746f8f9bf0d585c41dfd")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "12345678A":
                found = True
        self.assertTrue(found)

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '33af6850960f746f8f9bf0d585c41dfd',
                                    'IdCard': '12345678A'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        with open(ingreso, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        if data_list.get('Localizer') == "33af6850960f746f8f9bf0d585c41dfd":
            found = True
        self.assertTrue(found)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "f9867bbfcaa85e6d91103ca17a3a8714be7521451bb2afaacce78301ab19c7ba")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "f9867bbfcaa85e6d91103ca17a3a8714be7521451bb2afaacce78301ab19c7ba"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)

##############
# PRUEBAS CON BASE EN EL DIAGRAMA DE FLUJO

# PRUEBA DE CAMINO 1
    def test_guest_checkout_valid3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
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

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)


# PRUEBA DE CAMINO 2
    def test_guest_checkout_valid4(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
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

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)
        my_frezeer.stop()

        datos_checkout = []
        dic_checkout = {}
        dic_checkout.update({'_CHECKOUT__room_key':
                                 'f9867bbfcaa85e6d91103ca17a3a8714be7521451bb2afaacce78301ab19c7ba',
                             '_CHECKOUT__departure_time': '10/02/2024 20:00'})
        datos_checkout.append(dic_checkout)

        with open(checkout, "w", encoding="utf-8", newline="") as file:
            json.dump(datos_checkout, file, indent=2)

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)


# PRUEBA DE CAMINO 4
    def test_guest_checkout_valid5(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
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

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)
        my_frezeer.stop()

        with freeze_time("2030-10-05 10:00:00"):
            with self.assertRaises(
                    UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as cm:
                room_key = "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3"
                salida = manager.GuestCheckout(room_key)
            self.assertEqual(cm.exception.message, "FECHA DE SALIDA NO VÁLIDA")

        try:
            with open(checkout, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)


# PRUEBA DE CAMINO 5
    def test_guest_checkout_valid6(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
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

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            with self.assertRaises(
                    UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as cm:
                room_key = "f9867bbfcaa85e6d91103ca17a3a8714be7521451bb2afaacce78301ab19c7ba"
                salida = manager.GuestCheckout(room_key)
            self.assertEqual(cm.exception.message, "ROOM KEY NO COINCIDE")

        try:
            with open(checkout, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)


# PRUEBA DE CAMINO 6 - NO SE ENTRA EN EL BUCLE
    def test_guest_checkout_valid7(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)
        manager = HOTEL_MANAGER()

        lista_datos = []
        lista_datos.append({})
        try:
            with open(arrival, "w", encoding="utf-8", newline="") as file:
                json.dump(lista_datos, file, indent=2)
        except FileNotFoundError as ex:
            print("Error al buscar el archivo")

        with self.assertRaises(
                UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as cm:
            room_key = "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3"
            salida = manager.GuestCheckout(room_key)
        self.assertEqual(cm.exception.message, "ROOM KEY NO COINCIDE")

        try:
            with open(checkout, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)


# PRUEBA DE CAMINO 7 - SE PASA POR EL BUCLE UNA SOLA VEZ (IGUAL A LA PRIMERA)
    def test_guest_checkout_valid8(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
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

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(arrival, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_STAY__idcard'] == "11185346D":
                found = True
        self.assertTrue(found)
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)


# PRUEBA DE CAMINO 8 - SE PASA POR EL BUCLE DOS VECES
    def test_guest_checkout_valid9(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        reserva2 = manager.RoomReservation(6011111111111117, "Gabriel Rivera", "12345678A",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva2, "494415e484ecd3fb8083c44e58029a6c")

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '7532a04bf679689f4156228d60c542e4',
                                    'IdCard': '11185346D'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '494415e484ecd3fb8083c44e58029a6c',
                                    'IdCard': '12345678A'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "95628f204e582fb643bb0e21c3c88121cb91a52cc64079c39d17c01060d4786c")
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "95628f204e582fb643bb0e21c3c88121cb91a52cc64079c39d17c01060d4786c"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)


# DADO QUE ROOM RESERVATION PUEDE TENER INFINIDAD DE RESERVACIONES Y EL DOCUMENTO DEL HOTEL STAY
# TENDRA LA MISMA EXTENSION QUE DE RESERVACIONES, ENTONCES SUPONDREMOS COMO NUMERO LIMITE DE
# RESERVACIONES EL VALOR DE 5, PARA PODER EFECTUAR LAS PRUEBAS RESTANTES CON RESPECTO AL BUCLE

# PRUEBA DE CAMINO 9 - EL NUMERO MAXIMO DE ITERACIONES -1
    def test_guest_checkout_valid10(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        reserva2 = manager.RoomReservation(6011111111111117, "Gabriel Rivera", "12345678A",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva2, "494415e484ecd3fb8083c44e58029a6c")

        reserva3 = manager.RoomReservation(6011111111111117, "Joaquin Pujol", "10047776B",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva3, "5b6bc6895dda417b90e6922b82d93892")

        reserva4 = manager.RoomReservation(6011111111111117, "Santiago Diaz", "30224780C",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva4, "bead895c037b602608a56a207a9ad467")

        # reserva1
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '7532a04bf679689f4156228d60c542e4',
                                    'IdCard': '11185346D'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        # reserva3
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '5b6bc6895dda417b90e6922b82d93892',
                                    'IdCard': '10047776B'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "bca6706dbd48486220751758bcef57878ba8f1aa9da89e4780ef7da95974960f")

        # reserva4
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': 'bead895c037b602608a56a207a9ad467',
                                    'IdCard': '30224780C'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "8efd33d036edb4e2891c17870fe8c693e540cecead2eddfc765a71ef53d0066b")

        # reserva2
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '494415e484ecd3fb8083c44e58029a6c',
                                    'IdCard': '12345678A'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "95628f204e582fb643bb0e21c3c88121cb91a52cc64079c39d17c01060d4786c")
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "95628f204e582fb643bb0e21c3c88121cb91a52cc64079c39d17c01060d4786c"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)


# PRUEBA DE CAMINO 10 - NUMERO MAXIMO DE ITERACIONES
    def test_guest_checkout_valid11(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        reserva2 = manager.RoomReservation(6011111111111117, "Gabriel Rivera", "12345678A",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva2, "494415e484ecd3fb8083c44e58029a6c")

        reserva3 = manager.RoomReservation(6011111111111117, "Joaquin Pujol", "10047776B",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva3, "5b6bc6895dda417b90e6922b82d93892")

        reserva4 = manager.RoomReservation(6011111111111117, "Santiago Diaz", "30224780C",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva4, "bead895c037b602608a56a207a9ad467")

        reserva5 = manager.RoomReservation(6011111111111117, "Rebeca Fung", "61358974E",
                                            613799789,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva5, "35b635110dff257321ed0d3164f0cf3d")

        # reserva1
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '7532a04bf679689f4156228d60c542e4',
                                    'IdCard': '11185346D'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        # reserva3
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '5b6bc6895dda417b90e6922b82d93892',
                                    'IdCard': '10047776B'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "bca6706dbd48486220751758bcef57878ba8f1aa9da89e4780ef7da95974960f")

        # reserva4
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': 'bead895c037b602608a56a207a9ad467',
                                    'IdCard': '30224780C'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "8efd33d036edb4e2891c17870fe8c693e540cecead2eddfc765a71ef53d0066b")

        # reserva5
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '35b635110dff257321ed0d3164f0cf3d',
                                    'IdCard': '61358974E'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "c7e03ac8e0d7cfdd81db98f20e08f412f9ffb3b38245991bba412082d61cdcbd")

        # reserva2
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '494415e484ecd3fb8083c44e58029a6c',
                                    'IdCard': '12345678A'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "95628f204e582fb643bb0e21c3c88121cb91a52cc64079c39d17c01060d4786c")
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "95628f204e582fb643bb0e21c3c88121cb91a52cc64079c39d17c01060d4786c"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)

    # PRUEBA DE CAMINO 11 - NUMERO MAXIMO DE ITERACIONES +1
    def test_guest_checkout_valid12(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        reserva2 = manager.RoomReservation(6011111111111117, "Gabriel Rivera", "12345678A",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva2, "494415e484ecd3fb8083c44e58029a6c")

        reserva3 = manager.RoomReservation(6011111111111117, "Joaquin Pujol", "10047776B",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva3, "5b6bc6895dda417b90e6922b82d93892")

        reserva4 = manager.RoomReservation(6011111111111117, "Santiago Diaz", "30224780C",
                                            613589749,
                                            "Double", "16/03/2024", 5)
        self.assertEqual(reserva4, "bead895c037b602608a56a207a9ad467")

        reserva5 = manager.RoomReservation(6011111111111117, "Rebeca Fung", "61358974E",
                                            613799789,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva5, "35b635110dff257321ed0d3164f0cf3d")

        reserva6 = manager.RoomReservation(6011111111111117, "Victor Franco", "87654321F",
                                            643799789,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva6, "ad575662e7ccc013facae0bb9f611a97")

        # reserva1
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '7532a04bf679689f4156228d60c542e4',
                                    'IdCard': '11185346D'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        # reserva3
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '5b6bc6895dda417b90e6922b82d93892',
                                    'IdCard': '10047776B'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "bca6706dbd48486220751758bcef57878ba8f1aa9da89e4780ef7da95974960f")

        # reserva4
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': 'bead895c037b602608a56a207a9ad467',
                                    'IdCard': '30224780C'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "8efd33d036edb4e2891c17870fe8c693e540cecead2eddfc765a71ef53d0066b")

        # reserva5
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '35b635110dff257321ed0d3164f0cf3d',
                                    'IdCard': '61358974E'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "c7e03ac8e0d7cfdd81db98f20e08f412f9ffb3b38245991bba412082d61cdcbd")

        # reserva2
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '494415e484ecd3fb8083c44e58029a6c',
                                    'IdCard': '12345678A'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "95628f204e582fb643bb0e21c3c88121cb91a52cc64079c39d17c01060d4786c")

        # reserva6
        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': 'ad575662e7ccc013facae0bb9f611a97',
                                    'IdCard': '87654321F'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "7691fcb5182d005b7da3b17758589c798a19943bb106a99cb3269d2dd521f72c")
        my_frezeer.stop()

        with freeze_time("2024-03-21 10:00:00"):
            room_key = "95628f204e582fb643bb0e21c3c88121cb91a52cc64079c39d17c01060d4786c"
            salida = manager.GuestCheckout(room_key)
            self.assertEqual(salida, True)

# PRUEBA DE CAMINO 12
    def test_guest_checkout_valid13(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with open(archivo, "r", encoding="utf-8", newline="") as archivo_ing:
            datos = json.load(archivo_ing)

            dic_ingreso = {}
            for persona in datos:
                dic_ingreso.update({'Localizer': '7532a04bf679689f4156228d60c542e4',
                                    'IdCard': '11185346D'})

        with open(ingreso, "w", encoding="utf-8", newline="") as file:
            json.dump(dic_ingreso, file, indent=2)

        habitacion = manager.GuestArrival(ingreso)
        self.assertEqual(habitacion,
                         "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3")

        with freeze_time("2024-03-21 10:00:00"):
            with self.assertRaises(
                    UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as cm:
                room_key = "27z8949ax8561e3m7bd588dd370e154fede607c3a6cdc1h342444ik8473701j3"
                salida = manager.GuestCheckout(room_key)
            self.assertEqual(cm.exception.message, "FORMATO DE ROOM_KEY INCORRECTO")

        try:
            with open(checkout, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)


# PRUEBA DE CAMINO 14
    def test_guest_checkout_valid14(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_stay.json"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        if os.path.isfile(ingreso):
            os.remove(ingreso)
        if os.path.isfile(arrival):
            os.remove(arrival)
        if os.path.isfile(checkout):
            os.remove(checkout)

        my_frezeer = freeze_time("2024-03-16 17:00:00")
        my_frezeer.start()
        manager = HOTEL_MANAGER()
        reserva1 = manager.RoomReservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                            "Single", "16/03/2024", 5)
        self.assertEqual(reserva1, "7532a04bf679689f4156228d60c542e4")

        with freeze_time("2024-03-21 10:00:00"):
            with self.assertRaises(
                    UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as cm:
                room_key = "27d8949aa8561e3e7bd588dd370e154fede607c3a6cdc1b342444af8473701a3"
                salida = manager.GuestCheckout(room_key)
            self.assertEqual(cm.exception.message, "ARCHIVO O RUTA INCORRECTO")

        try:
            with open(checkout, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True
        self.assertTrue(removed)