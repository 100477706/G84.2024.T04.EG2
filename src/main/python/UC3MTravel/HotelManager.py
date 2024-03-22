import json
from pathlib import Path

from .HotelManagementException import HOTEL_MANAGEMENT_EXCEPTION
from .HotelReservation import HOTEL_RESERVATION
from datetime import datetime


class HotelManager:
    def __init__(self):
        pass

    def room_reservation(self, credit_card, name_and_surname, id_card, phone_number, room_type,
                         arrival_date: str, num_days):

        if self.validatecreditcard(credit_card) == False:
            raise HOTEL_MANAGEMENT_EXCEPTION("Tarjeta de crédito no válida")
        if len(id_card) != 9 or id_card[8].isalpha() == False:
            raise HOTEL_MANAGEMENT_EXCEPTION("DNI no válido")
        for i in range(8):
            if id_card[i].isnumeric() == False:
                raise HOTEL_MANAGEMENT_EXCEPTION("DNI no válido")
        #NOMBRE
        if isinstance(name_and_surname, str) == False:
            raise HOTEL_MANAGEMENT_EXCEPTION("Nombre no válido")
        if 10 > len(name_and_surname) or len(name_and_surname)> 50:
            raise HOTEL_MANAGEMENT_EXCEPTION("Nombre no válido")
        espacio = False
        for i in name_and_surname:
            if i.isalpha() == False and i.isspace() == False:
                raise HOTEL_MANAGEMENT_EXCEPTION("Nombre no válido")
            if i.isspace():
                espacio = True
        if espacio == False:
            raise HOTEL_MANAGEMENT_EXCEPTION("Nombre no válido")
        #TELÉFONO
        if isinstance(phone_number, int) == False:
            raise HOTEL_MANAGEMENT_EXCEPTION("Número de teléfono no válido")
        if len(str(phone_number)) != 9:
            raise HOTEL_MANAGEMENT_EXCEPTION("Número de teléfono no válido")
        #HABITACIÓN
        if isinstance(room_type, str) == False:
            raise HOTEL_MANAGEMENT_EXCEPTION("Tipo de habitación no válido")
        if room_type.lower() != "single" and room_type.lower() != "double" and \
                room_type.lower() != "suit":
            raise HOTEL_MANAGEMENT_EXCEPTION("Tipo de habitación no válido")
        #NÚMERO DE DÍAS
        if isinstance(num_days, int) == False:
            raise HOTEL_MANAGEMENT_EXCEPTION("Número de días no válido")
        if num_days < 1 or num_days > 10:
            raise HOTEL_MANAGEMENT_EXCEPTION("Número de días no válido")
        #FECHA
        if len(arrival_date) != 10:
            raise HOTEL_MANAGEMENT_EXCEPTION("Fecha de llegada no válida")
        for i in range(len(arrival_date)):
            if (i < 2 or 2 < i < 5 or 5 < i < 10) and arrival_date[i].isnumeric() == False:
                raise HOTEL_MANAGEMENT_EXCEPTION("Fecha de llegada no válida")
            if (i == 2 or i == 5) and arrival_date[i] != "/":
                raise HOTEL_MANAGEMENT_EXCEPTION("Fecha de llegada no válida")
        if int(arrival_date[0]) == 0 and int(arrival_date[1]) == 0:
            raise HOTEL_MANAGEMENT_EXCEPTION("Fecha de llegada no válida")
        if int(arrival_date[0]) > 3 or (int(arrival_date[0]) == 3 and int(arrival_date[1]) > 0):
            raise HOTEL_MANAGEMENT_EXCEPTION('Fecha de llegada no válida')
        if (int(arrival_date[3]) == 0 and int(arrival_date[4]) == 0) or \
                (int(arrival_date[3]) > 1 or (int(
                arrival_date[3]) == 1 and int(arrival_date[4]) > 2)):
            raise HOTEL_MANAGEMENT_EXCEPTION("Fecha de llegada no válida")
        if int(arrival_date[6] + arrival_date[7] + arrival_date[8] +
               arrival_date[9]) < datetime.now().year:
            raise HOTEL_MANAGEMENT_EXCEPTION("Fecha de llegada no válida")
        if int(arrival_date[6] + arrival_date[7] + arrival_date[8] +
               arrival_date[9]) == datetime.now().year and int(
                arrival_date[3] + arrival_date[4]) < datetime.now().month:
            raise HOTEL_MANAGEMENT_EXCEPTION("Fecha de llegada no válida")
        if int(arrival_date[6] + arrival_date[7] + arrival_date[8] +
               arrival_date[9]) == datetime.now().year and int(
                arrival_date[3] + arrival_date[4]) == datetime.now().month and \
                int(arrival_date[0] + arrival_date[1])\
                < datetime.now().day:
            raise HOTEL_MANAGEMENT_EXCEPTION("Fecha de llegada no válida")

        #LOCALIZADOR
        reserva = HOTEL_RESERVATION(id_card, credit_card, name_and_surname, phone_number,
                                    room_type, arrival_date, num_days)

        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH +"file_store.json"
        try:
            with open(archivo, "r", encoding= "utf-8", newline="") as file:
                lista_datos = json.load(file)
        except FileNotFoundError as ex:
            lista_datos = []
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("ERROR JSON")
        try:
            # Compruebo si ya hay en el archivo una reserva de la misma persona el mismo día
            for item in lista_datos:
                if item['_HOTEL_RESERVATION__id_card'] == id_card and \
                        item['_HOTEL_RESERVATION__arrival'] == \
                        arrival_date:
                    print("reserva ya hecha")
                    raise HOTEL_MANAGEMENT_EXCEPTION("Reserva ya introducida en el sistema")
            lista_datos.append(reserva.__dict__)
            with open(archivo, "w", encoding="utf-8", newline="") as file:
                json.dump(lista_datos, file, indent=2)
            print("Reserva realizada")
        except FileNotFoundError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("archivo o ruta incorrecta")
        return reserva.localizer


    def validatecreditcard(self, x):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        # Comprobamos si la tarjeta tiene 16 dígitos
        if len(str(x)) != 16:
            return False

        # Convertimos el número a lista y obtenemos el supuesto valor del último dígito según Luhn
        num_lista = []
        for a in range(len(str(x))-1):
            num_lista.append(str(x)[a])

        # Guardamos la suma del algoritmo de Luhn en la variable suma
        suma = 0
        # Cada dígito par lo duplicamos y sumamos cada dígito del resultado a suma
        # Cada dígito impar lo sumamos directamente a suma
        for a in range(len(num_lista)):
            if a % 2 != 0:
                suma += int(num_lista[a])
            else:
                num_actual = int(num_lista[a])
                num_actual *= 2
                if num_actual >= 10:
                    suma += int(str(num_actual)[0]) + int(str(num_actual)[1])
                else:
                    suma += num_actual
        # Calculamos el resultado del último dígito
        ultimo_digito = (suma * 9) % 10
        # Comprobamos si el último dígito es el que debería ser según Luhn
        if str(ultimo_digito) == str(x)[len(str(x)) - 1]:
            return True
        else:
            return False


    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise ("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HOTEL_MANAGEMENT_EXCEPTION("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HOTEL_RESERVATION(id_card="12345678Z", credit_card_numb=c,
                                    name_and_surname="John Doe",
                                    phone_number=p, room_type="single",
                                    arrival_date = "27/02/2025", num_days=3)
        except KeyError as e:
            raise HOTEL_MANAGEMENT_EXCEPTION("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HOTEL_MANAGEMENT_EXCEPTION("Invalid credit card number")

        # Close the file
        return req