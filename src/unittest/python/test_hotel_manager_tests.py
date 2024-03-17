import json
import os
import unittest

import UC3MTravel.HotelManagementException
from UC3MTravel import HotelManager
from UC3MTravel import HotelReservation
# VAMOS A EMPLEAR FREEZE_TIME PARA CONGELAR AL TIEMPO Y COMPROBAR QUE LOS LOCALIZADORES QUE SALEN AL PROBAR LA
# FUNCIÓN SON LOS CORRECTOS
from freezegun import freeze_time

class TestHotelManager(unittest.TestCase):
    # TARJETA CON 16 DÍGITOS QUE NO CUMPLE EL ALGORITMO DE LUHN
    def test_room_reservation_valid1(self):
        tarjeta = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            tarjeta.room_reservation(1234567891011121, "Pepe Navarro", "51132027Z", 655789987, "Single",
                                     "01/01/2008", 5)

    # TARJETA CON UN NÚMERO QUE NO ES UN INT
    def test_room_reservation_valid2(self):
        tarjeta = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            tarjeta.room_reservation("1234567891011121", "Pepe Navarro", "51132027Z", 655789987, "Single", "01/01/2008",
                                     5)

    # TARJETA CON MÁS DE 16 DÍGITOS
    def test_room_reservation_valid3(self):
        tarjeta = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            tarjeta.room_reservation(1234567891011121556, "Pepe Navarro", "51132027Z", 655789987, "Single",
                                     "01/01/2008", 5)

    # TARJETA CON MENOS DE 16 DÍGITOS
    def test_room_reservation_valid4(self):
        tarjeta = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            tarjeta.room_reservation(123456789101, "Pepe Navarro", "51132027Z", 655789987, "Single", "01/01/2008", 5)

    # TARJETA CON 17 DÍGITOS
    def test_room_reservation_valid5(self):
        tarjeta = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            tarjeta.room_reservation(12345678910111217, "Pepe Navarro", "51132027Z", 655789987, "Single", "01/01/2008",
                                     5)

    # TARJETA CON 15 DÍGITOS
    def test_room_reservation_valid6(self):
        tarjeta = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            tarjeta.room_reservation(123456789101112, "Pepe Navarro", "51132027Z", 655789987, "Single", "01/01/2008", 5)

    # DNI CON NUEVE DÍGITOS
    def test_room_reservation_valid2_1(self):
        dni = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dni.room_reservation(6011111111111117, "Pepe Navarro", "511320279", 655789987, "Single", "01/01/2008", 5)

    # DNI CON UN CARACTER NO NUMÉRICO EN LOS OCHO PRIMEROS
    def test_room_reservation_valid2_2(self):
        dni = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dni.room_reservation(6011111111111117, "Pepe Navarro", "51132¿27Z", 655789987, "Single", "01/01/2008", 5)

    # DNI CON UN ÚLTIMO CARACTER NO ALFABÉTICO
    def test_room_reservation_valid2_3(self):
        dni = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dni.room_reservation(6011111111111117, "Pepe Navarro", "51132027¿", 655789987, "Single", "01/01/2008", 5)

    # DNI CON MÁS DE 8 DÍGITOS
    def test_room_reservation_valid2_4(self):
        dni = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dni.room_reservation(6011111111111117, "Pepe Navarro", "5113202721Z", 655789987, "Single", "01/01/2008", 5)

    # DNI CON MENOS DE 8 DÍGITOS
    def test_room_reservation_valid2_5(self):
        dni = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dni.room_reservation(6011111111111117, "Pepe Navarro", "511320Z", 655789987, "Single", "01/01/2008", 5)

    # DNI CON DOS LETRAS
    def test_room_reservation_valid2_6(self):
        dni = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dni.room_reservation(6011111111111117, "Pepe Navarro", "511320272ZW", 655789987, "Single", "01/01/2008", 5)

    # NOMBRE CON CARACTER NO VÁLIDO
    def test_room_reservation_valid3_1(self):
        nombre = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            nombre.room_reservation(6011111111111117, "Pepe ¿avarro", "11185346D", 655789987, "Single", "01/01/2008", 5)

    # NOMBRE SIN ESPACIOS
    def test_room_reservation_valid3_2(self):
        nombre = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            nombre.room_reservation(6011111111111117, "PepeNavarro", "11185346D", 655789987, "Single", "01/01/2008", 5)

    # EL NOMBRE NO ES UNA CADENA DE CARACTERES
    def test_room_reservation_valid3_3(self):
        nombre = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            nombre.room_reservation(6011111111111117, 1234, "11185346D", 655789987, "Single", "01/01/2008", 5)

    # NOMBRE CON 51 CARACTERES
    def test_room_reservation_valid3_4(self):
        nombre = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            nombre.room_reservation(6011111111111117, "Juan Alberto Quintana Enrique Segundo de Alemania y tercero de Malta", "11185346D",
                                    655789987, "Single",
                                    "01/01/2008", 5)

    # NOMBRE CON 9 CARACTERES
    def test_room_reservation_valid3_5(self):
        nombre = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            nombre.room_reservation(6011111111111117, "Juan", "11185346D", 655789987, "Single", "01/01/2008", 5)

    # TELÉFONO CON UN TÉRMINO QUE NO ES UN NÚMERO
    def test_room_reservation_valid4_1(self):
        telefono = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            telefono.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", "6557899D7", "Single",
                                              "01/01/2008", 5)

    # TELÉFONO CON 10 DÍGITOS O MÁS
    def test_room_reservation_valid4_2(self):
        telefono = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            telefono.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 6557899870, "Single",
                                              "01/01/2008", 5)

    # TELÉFONO CON 8 DÍGITOS O MENOS
    def test_room_reservation_valid4_3(self):
        telefono = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            telefono.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 65578998, "Single",
                                              "01/01/2008", 5)

    # HABITACIÓN QUE NO SE CORRESPONDE CON NINGUNO DE LOS TRES TIPOS
    def test_room_reservation_valid5_1(self):
        habitacion = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "HOLA",
                                              "01/01/2008", 5)

    # HABITACIÓN NO ES UNA CADENA DE CARACTERES
    def test_room_reservation_valid5_2(self):
        habitacion = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, 565678,
                                              "01/01/2008", 5)

    # HABITACIÓN ES DE TIPO SINGLE
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid5_3(self):
        os.remove("file_store.json")
        habitacion = HotelManager.HotelManager()
        self.assertEqual(habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Single",
                                              "01/01/2100", 5), HotelReservation.HOTEL_RESERVATION("11185346D",
                                                6011111111111117, "Pepe Navarro", 655789987, "Single", "01/01/2100", 5).localizer)
        with open("file_store.json", "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

    # HABITACIÓN DE TIPO DOUBLE
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid5_4(self):
        os.remove("file_store.json")
        habitacion = HotelManager.HotelManager()
        self.assertEqual(habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Double",
                                              "01/01/2100", 5), HotelReservation.HOTEL_RESERVATION("11185346D",
                                                6011111111111117, "Pepe Navarro", 655789987, "Double", "01/01/2100",
                                                                                                   5).localizer)
        with open("file_store.json", "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)
    # HABITACIÓN DE TIPO SUIT
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid5_5(self):
        os.remove("file_store.json")
        habitacion = HotelManager.HotelManager()
        self.assertEqual(habitacion.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                              "01/01/2100", 5), HotelReservation.HOTEL_RESERVATION("11185346D",
                                                6011111111111117, "Pepe Navarro", 655789987, "Suit", "01/01/2100", 5).localizer)

        with open("file_store.json", "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

    # NÚMERO DE DÍAS QUE NO ES UN ENTERO
    def test_room_reservation_valid6_1(self):
        dias = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dias.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                              "01/01/2008", "J")

    # EL NÚMERO DE DÍAS ES 11
    def test_room_reservation_valid6_2(self):
        dias = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dias.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                              "01/01/2008", 11)

    # EL NÚMERO DE DÍAS ES 0
    def test_room_reservation_valid6_3(self):
        dias = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            dias.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                              "01/01/2008", 0)

    # LA CADENA DE CARACTERES TIENE UN CARACTER NO VÁLIDO
    def test_room_reservation_valid7_1(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                              "01/0D/2008", 5)

    # HAY OCHO DÍGITOS SIN SEPARADORES
    def test_room_reservation_valid7_2(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                              "01012008", 5)

    # DD TIENE UN VALOR MENOR A 01
    def test_room_reservation_valid7_3(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                              "00/01/2008", 5)

    # DD TIENE UN VALOR MAYOR A 30
    def test_room_reservation_valid7_4(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "31/01/2008", 5)

    # MM TIENE UN VALOR MENOR A 01
    def test_room_reservation_valid7_5(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "31/00/2008", 5)

    # MM TIENE UN VALOR MAYOR A 12
    def test_room_reservation_valid7_6(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "31/13/2008", 5)

    # 3 O MÁS DÍGITOS ANTES DEL PRIMER /
    def test_room_reservation_valid7_7(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "014/01/2008", 5)

    # 3 O MÁS DÍGITOS EN MM
    def test_room_reservation_valid7_8(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "30/011/2008", 5)

    # 5 O MÁS DÍGITOS EN YYYY
    def test_room_reservation_valid7_9(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "20/01/20008", 5)

    # FECHA ANTERIOR A LA DEL SISTEMA
    def test_room_reservation_valid7_10(self):
        fecha = HotelManager.HotelManager()
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            fecha.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Suit",
                                   "29/01/2008", 5)

    # RESERVA YA EXISTENTE
    def test_room_reservation_valid8_1(self):
        os.remove("file_store.json")
        manager = HotelManager.HotelManager()
        manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Single",
                                              "01/01/2100", 5)
        with self.assertRaises(UC3MTravel.HotelManagementException.HOTEL_MANAGEMENT_EXCEPTION):
            manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Single",
                                              "01/01/2100", 5)


    # EJEMPLO CON TODOS LOS DATOS CORRECTOS
    @freeze_time("2024-03-16 17:00:00")
    def test_room_reservation_valid(self):
        os.remove("file_store.json")
        manager = HotelManager.HotelManager()
        reserva = manager.room_reservation(6011111111111117, "Pepe Navarro", "11185346D", 655789987, "Single",
                                              "01/01/2100", 5)
        self.assertEqual(reserva, HotelReservation.HOTEL_RESERVATION("11185346D",
                                                6011111111111117, "Pepe Navarro", 655789987, "Single", "01/01/2100", 5).localizer)

        with open("file_store.json", "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item['_HOTEL_RESERVATION__id_card'] == "11185346D":
                found = True
        self.assertTrue(found)

if __name__ == '__main__':
    unittest.main()
