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

    # EJEMPLO CON TODOS LOS CASOS CORRECTOS
    @freeze_time("2024-03-16 17:00:00")
    def test_guest_arrival_valid1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"
        ingreso = JSON_FILES_PATH + "store_reservation.json"
        arrival = JSON_FILES_PATH + "store_arrival.json"
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

        habitacion = manager.guest_arrival(ingreso)

        with open(ingreso, "r", encoding='utf-8', newline="") as file:
            data_list = json.load(file)
        found = False
        if data_list.get('Localizer') == "7532a04bf679689f4156228d60c542e4":
            found = True
        self.assertTrue(found)


if __name__ == '__main__':
    unittest.main()