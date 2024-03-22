import hashlib
import json
import os
import unittest
from pathlib import Path

import UC3MTravel.HotelManagementException
from UC3MTravel import HotelManager
from UC3MTravel import HotelReservation
# VAMOS A EMPLEAR FREEZE_TIME PARA CONGELAR AL TIEMPO Y COMPROBAR QUE LOS LOCALIZADORES
# QUE SALEN AL PROBAR LA
# FUNCIÓN SON LOS CORRECTOS
from freezegun import freeze_time


class TestHotelManager(unittest.TestCase):
    # TARJETA CON 16 DÍGITOS QUE NO CUMPLE EL ALGORITMO DE LUHN
    def test_room_reservation_valid1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        tarjeta = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            tarjeta.room_reservation(1234567891011121, "Pepe Navarro", "51132027Z", 655789987,
                                     "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Tarjeta de crédito no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # TARJETA CON UN NÚMERO QUE NO ES UN INT
    def test_room_reservation_valid2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        tarjeta = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            tarjeta.room_reservation("1234567891011121", "Pepe Navarro", "51132027Z", 655789987,
                                     "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Tarjeta de crédito no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # TARJETA CON MÁS DE 16 DÍGITOS
    def test_room_reservation_valid3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        tarjeta = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            tarjeta.room_reservation(1234567891011121556, "Pepe Navarro", "51132027Z", 655789987,
                                     "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Tarjeta de crédito no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # TARJETA CON MENOS DE 16 DÍGITOS
    def test_room_reservation_valid4(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        tarjeta = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            tarjeta.room_reservation(123456789101, "Pepe Navarro", "51132027Z", 655789987,
                                     "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Tarjeta de crédito no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # TARJETA CON 17 DÍGITOS
    def test_room_reservation_valid5(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        tarjeta = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            tarjeta.room_reservation(12345678910111217, "Pepe Navarro", "51132027Z", 655789987,
                                     "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Tarjeta de crédito no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # TARJETA CON 15 DÍGITOS
    def test_room_reservation_valid6(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        tarjeta = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            tarjeta.room_reservation(123456789101112, "Pepe Navarro", "51132027Z", 655789987,
                                     "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Tarjeta de crédito no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    ############
    # PRUEBAS DE ID CARD
    # DNI CON NUEVE DÍGITOS
    def test_room_reservation_valid2_1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dni = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dni.room_reservation(6011111111111117, "Pepe Navarro", "511320279", 655789987,
                                 "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "DNI no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # DNI CON UN CARACTER NO NUMÉRICO EN LOS OCHO PRIMEROS
    def test_room_reservation_valid2_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dni = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dni.room_reservation(6011111111111117, "Pepe Navarro", "51132¿27Z", 655789987,
                                 "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "DNI no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # DNI CON UN ÚLTIMO CARACTER NO ALFABÉTICO
    def test_room_reservation_valid2_3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dni = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dni.room_reservation(6011111111111117, "Pepe Navarro", "51132027¿", 655789987,
                                 "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "DNI no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # DNI CON MÁS DE 8 DÍGITOS
    def test_room_reservation_valid2_4(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dni = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dni.room_reservation(6011111111111117, "Pepe Navarro", "5113202721Z", 655789987,
                                 "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "DNI no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # DNI CON MENOS DE 8 DÍGITOS
    def test_room_reservation_valid2_5(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dni = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dni.room_reservation(6011111111111117, "Pepe Navarro", "511320Z", 655789987, "Single",
                                 "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "DNI no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # DNI CON DOS LETRAS
    def test_room_reservation_valid2_6(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dni = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dni.room_reservation(6011111111111117, "Pepe Navarro", "511320272ZW", 655789987,
                                 "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "DNI no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    #############
    # PRUEBAS DE NOMBRE
    # NOMBRE CON CARACTER NO VÁLIDO
    def test_room_reservation_valid3_1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        nombre = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            nombre.room_reservation(6011111111111117, "Pepe ¿avarro", "11185346D", 655789987,
                                    "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Nombre no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    # NOMBRE SIN ESPACIOS
    def test_room_reservation_valid3_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        nombre = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            nombre.room_reservation(6011111111111117, "PepeNavarro", "11185346D", 655789987,
                                    "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Nombre no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    # EL NOMBRE NO ES UNA CADENA DE CARACTERES
    def test_room_reservation_valid3_3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        nombre = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            nombre.room_reservation(6011111111111117, 1234, "11185346D", 655789987, "Single",
                                    "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Nombre no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    # NOMBRE CON 51 CARACTERES
    def test_room_reservation_valid3_4(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        nombre = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            nombre.room_reservation(6011111111111117, "Juan Alberto Quintana Enrique Segundo de "
                                                      "Alemania y tercero de Malta", "11185346D",
                                    655789987, "Single",
                                    "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Nombre no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    # NOMBRE CON 9 CARACTERES
    def test_room_reservation_valid3_5(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        nombre = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            nombre.room_reservation(6011111111111117, "Juan", "11185346D", 655789987, "Single",
                                    "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Nombre no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    #############
    # PRUEBAS DE TELÉFONO
    # TELÉFONO CON UN TÉRMINO QUE NO ES UN NÚMERO
    def test_room_reservation_valid4_1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        telefono = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            telefono.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", "6557899D7",
                                      "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Número de teléfono no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # TELÉFONO CON 10 DÍGITOS O MÁS
    def test_room_reservation_valid4_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        telefono = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            telefono.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 6557899870,
                                      "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Número de teléfono no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # TELÉFONO CON 8 DÍGITOS O MENOS
    def test_room_reservation_valid4_3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        telefono = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            telefono.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 65578998,
                                      "Single", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Número de teléfono no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    ###############
    # PRUEBAS DE TIPO DE HABITACIÓN
    # HABITACIÓN QUE NO SE CORRESPONDE CON NINGUNO DE LOS TRES TIPOS
    def test_room_reservation_valid5_1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        habitacion = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987,
                                        "HOLA", "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Tipo de habitación no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # HABITACIÓN NO ES UNA CADENA DE CARACTERES
    def test_room_reservation_valid5_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        habitacion = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987,
                                        565678, "01/01/2008", 5)
        self.assertEqual(cm.exception.message, "Tipo de habitación no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # HABITACIÓN ES DE TIPO SINGLE
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid5_3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        habitacion = HotelManager.HotelManager()

        reserva = habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                                     655789987, "Single", "01/01/2100", 5)
        self.assertEqual(reserva, "4dcfe23cc26a2c294312a1ad446001a8")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

    # HABITACIÓN DE TIPO DOUBLE
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid5_4(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        habitacion = HotelManager.HotelManager()

        reserva = habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                                     655789987, "Double", "01/01/2100", 5)
        self.assertEqual(reserva, "bad26e4c2a527e8b85a8c1fe9b9c5b1b")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

    # HABITACIÓN DE TIPO SUIT
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid5_5(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        habitacion = HotelManager.HotelManager()

        reserva = habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                                     655789987, "Suit", "01/01/2100", 5)

        self.assertEqual(reserva, "eb590c3e2d1197f162204d44cb85d53e")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)


    ###############
    # PRUEBAS DEL NÚMERO DE DÍAS DE ESTANCIA
    # NÚMERO DE DÍAS QUE NO ES UN ENTERO

    def test_room_reservation_valid6_1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dias = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dias.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                  "01/01/2008", "J")
        self.assertEqual(cm.exception.message, "Número de días no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # EL NÚMERO DE DÍAS ES 11
    def test_room_reservation_valid6_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dias = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dias.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                  "01/01/2008", 11)
        self.assertEqual(cm.exception.message, "Número de días no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # EL NÚMERO DE DÍAS ES 0
    def test_room_reservation_valid6_3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        dias = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            dias.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                  "01/01/2025", 0)
        self.assertEqual(cm.exception.message, "Número de días no válido")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    ###################
    # PRUEBAS DE DIAS
    # LA CADENA DE CARACTERES TIENE UN CARACTER NO VÁLIDO
    def test_room_reservation_valid7_1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "01/0D/2025", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # HAY OCHO DÍGITOS SIN SEPARADORES
    def test_room_reservation_valid7_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "01012008", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # DD TIENE UN VALOR MENOR A 01
    def test_room_reservation_valid7_3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "00/01/2025", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # DD TIENE UN VALOR MAYOR A 30
    def test_room_reservation_valid7_4(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "31/01/2025", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # MM TIENE UN VALOR MENOR A 01
    def test_room_reservation_valid7_5(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "31/00/2025", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # MM TIENE UN VALOR MAYOR A 12
    def test_room_reservation_valid7_6(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "31/13/2025", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # 3 O MÁS DÍGITOS ANTES DEL PRIMER /
    def test_room_reservation_valid7_7(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "014/01/2025", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # 3 O MÁS DÍGITOS EN MM
    def test_room_reservation_valid7_8(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "30/011/2025", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # 5 O MÁS DÍGITOS EN YYYY
    def test_room_reservation_valid7_9(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()


        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "20/01/20008", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)

    # FECHA ANTERIOR A LA DEL SISTEMA
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid7_10(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        fecha = HotelManager.HotelManager()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "29/01/2008", 5)
        self.assertEqual(cm.exception.message, "Fecha de llegada no válida")

        try:
            with open(archivo, "r") as archivo_org:
                removed = False
        except FileNotFoundError as ex:
            removed = True

        self.assertTrue(removed)


    # EJEMPLO CON TODOS LOS DATOS CORRECTOS
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D",
                                            655789987,
                                           "Single", "01/01/2100", 5)
        self.assertEqual(reserva1, "4dcfe23cc26a2c294312a1ad446001a8")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

        reserva2 = manager.room_reservation(6011111111111117, "Gabriel Rivera", "12345678A",
                                           613589749,
                                           "Double", "01/02/2100", 3)
        self.assertEqual(reserva2, "6089bc9af9218b578973ef93f27a4217")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "12345678A":
                found = True
        self.assertTrue(found)

    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        if os.path.isfile(archivo):
            os.remove(archivo)
        manager = HotelManager.HotelManager()
        reserva1 = manager.room_reservation(6011111111111117, "Gabriel Rivera", "12345678A",
                                           613589749,
                                           "Double", "01/02/2100", 3)
        self.assertEqual(reserva1, "6089bc9af9218b578973ef93f27a4217")

        with open(archivo, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "12345678A":
                found = True
        self.assertTrue(found)

        with open(archivo, "r") as archivo_org:
            hash_original = hashlib.md5(archivo_org.__str__().encode()).hexdigest()

        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION) as\
                cm:
            reserva2 = manager.room_reservation(6011111111111117, "Gabriel Rivera", "12345678A",
                                                613589749,
                                                "Double", "01/02/2100", 3)
        self.assertEqual(cm.exception.message, "Reserva ya introducida en el sistema")

        with open(archivo, "r") as archivo_org:
            hash_final = hashlib.md5(archivo_org.__str__().encode()).hexdigest()

        self.assertEqual(hash_original, hash_final)

if __name__ == '__main__':
    unittest.main()
