import json
from pathlib import Path

from .HotelManagementException import HOTEL_MANAGEMENT_EXCEPTION
from .HotelReservation import HOTEL_RESERVATION
from datetime import datetime
from .HotelStay import HOTEL_STAY


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
        if 10 > len(name_and_surname) or len(name_and_surname) > 50:
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
        archivo = JSON_FILES_PATH + "file_store.json"

        try:
            with open(archivo, "r", encoding="utf-8", newline="") as file:
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
                    raise HOTEL_MANAGEMENT_EXCEPTION("Reserva ya introducida en el sistema")

            lista_datos.append(reserva.__dict__)

            with open(archivo, "w", encoding="utf-8", newline="") as file:
                json.dump(lista_datos, file, indent=2)
            print("Reserva realizada")
        except FileNotFoundError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("Archivo o ruta incorrecta")

        return reserva.localizer



############
#SEGUNDA FUNCIÓN
    def guest_arrival(self, input_file):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "file_store.json"

        try:
            with open(archivo, "r", encoding="utf-8", newline="") as file1:
                datos_reserva = json.load(file1)
        except FileNotFoundError as ex:
            datos_reserva = []
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file2:
                datos_input = json.load(file2)
        except FileNotFoundError as ex:
            datos_input = []
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")


        try:
            with open(input_file, "rb") as file:
                element = file.read(1)
                count = 0

                while element:
                    # SE VERIFICA QUE EL PRIMER BYTE SEA UNA '{'
                    if count == 0:
                        if element != b'{':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA QUE EL SEGUNDO, QUINCAGÉSIMO TERCER Y SEPTUAGÉSIMO SÉPTIMO BYTE
                    # SEA UN '\n'
                    if (count == 1) or (count == 52) or (count == 76):
                        if element != b'\n':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA QUE EL TERCER, CUARTO, DÉCIMO SÉPTIMO, QUINCAGÉSIMO CUARTO,
                    # QUINCAGÉSIMO QUINTO Y SEXAGÉSIMO QUINTO BYTE SON UN ESPACIO EN BLANCO
                    if ((count == 2) or (count == 3) or (count == 16) or (count == 53) or
                            (count == 54) or (count == 64)):
                        if element != b' ':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA QUE EL QUINTO, DÉCIMO QUINTO, DÉCIMO OCTAVO, QUINCAGÉSIMO
                    # PRIMERO, QUINCAGÉSIMO SEXTO, SEXAGÉSIMO TERCERO, SEXAGÉSIMO SEXTO Y
                    # SEPTUAGÉSIMO SEXTO BYTE SON UNAS COMILLAS
                    if ((count == 4) or (count == 14) or (count == 17) or (count == 50) or
                            (count == 55) or (count == 62) or (count == 65) or (count == 75)):
                        if element != b'"':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")
                        else:
                            if count == 4:
                                # SABEMOS QUE DESPUÉS DEL CUARTO BYTE VIENE "LOCALIZER",
                                # POR LO QUE LA LEEMOS COMO UN SOLO BYTE
                                element = file.read(9)
                                count = count + 9

                            if count == 17:
                                # SABEMOS QUE DESPUÉS DEL DÉCIMO SÉPTIMO BYTE VIENE EL VALOR,
                                # HEXADECIMAL DE LOCALIZER, POR LO QUE LA LEEMOS COMO UN SOLO BYTE
                                element = file.read(32)
                                count = count + 32

                            if count == 55:
                                # SABEMOS QUE DESPUÉS DEL QUINCAGÉSIMO SEXTO BYTE VIENE "IDCARD",
                                # POR LO QUE LA LEEMOS COMO UN SOLO BYTE
                                element = file.read(6)
                                count = count + 6

                            if count == 65:
                                # SABEMOS QUE DESPUÉS DEL SEXAGÉSIMO SEXTO BYTE VIENE EL VALOR DE
                                # IDCARD,
                                # POR LO QUE LA LEEMOS COMO UN SOLO BYTE (NO CONTAMOS LA LETRA)
                                element = file.read(8)
                                count = count + 8


                    # SE VERIFICA QUE EL DÉCIMO SEXTO Y EL SEXAGÉSIMO CUARTO BYTE SON UNOS DOS
                    # PUNTOS ':'
                    if (count == 15) or (count == 63):
                        if element != b':':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA QUE EL QUINCAGÉSIMO TERCER BYTE ES UNA COMA:'
                    if count == 51:
                        if element != b',':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA QUE EL LOCALIZER ESTÁ DONDE DEBE Y SI ESTÁ BIEN ESCRITO
                    if count == 13:
                        if element != b'Localizer':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA QUE EL IDCARD ESTÁ DONDE DEBE Y SI ESTÁ BIEN ESCRITO
                    if count == 61:
                        if element != b'IdCard':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA QUE EL ÚLTIMO BYTE SEA UNA '}'
                    if count == 77:
                        if element != b'}':
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA LA ESTRUCTURA DEL VALOR DE IDCARD'
                    if count == 73:
                        comprobacion = int(element)
                        dni = ''.join(map(str, element))
                        if len(dni) < 8:
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")
                        for i in range(8):
                            if dni[i].isnumeric() == False:
                                raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    if count == 74:
                        caracter = element.decode('utf-8')
                        if isinstance(caracter, str) == False:
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    # SE VERIFICA LA ESTRUCTURA DEL LOCALIZER SEA CORRECTA'
                    if count == 49:
                        caracter = element.decode('utf-8')
                        if self.es_hexadecimal(caracter) == False:
                            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

                    count = count + 1
                    element = file.read(1)

        except FileNotFoundError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("Archivo o ruta incorrecta")
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")
        except ValueError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

        # CON ESTO SE PRUEBA QUE EL LOCALIZER DEL JSON FILE INPUT COINCIDA CON EL GENERADO EN LA RF1
        try:
            lista_reserva = []

            localizer = datos_input.get('Localizer')
            id_card = datos_input.get('IdCard')
            for items in datos_reserva:
                lista_reserva.append(items['_HOTEL_RESERVATION__localizer'])
                lista_reserva.append(items['_HOTEL_RESERVATION__id_card'])
                lista_reserva.append(items['_HOTEL_RESERVATION__num_days'])
                lista_reserva.append(items['_HOTEL_RESERVATION__room_type'])
                lista_reserva.append(items['_HOTEL_RESERVATION__arrival'])

            #Inicializamos las variables que usaremos
            # Si localizer y id_card coincide con lo que tenemos en el input, entonces colocamos
            # valores a num_days, room_type y a arrival
            num_days = int
            room_type = str
            dato_reserva_arrival = str

            if len(lista_reserva) > 0:
                comprobacion = False
                for j in range(len(lista_reserva)):
                    if lista_reserva[j] == localizer:
                        if lista_reserva[j+1] == id_card:
                            comprobacion = True
                            num_days = lista_reserva[j+2]
                            room_type = lista_reserva[j+3]
                            dato_reserva_arrival = lista_reserva[j+4]
                    j += 4

                if comprobacion == False:
                    raise HOTEL_MANAGEMENT_EXCEPTION("El IdCard o el Localizer no coincide")

        except FileNotFoundError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("Archivo o ruta incorrecta")
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")


        ingreso = HOTEL_STAY(id_card, localizer, num_days, room_type)
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        arrival = JSON_FILES_PATH + "store_stay.json"

        try:
            with open(arrival, "r", encoding="utf-8", newline="") as file:
                lista_datos = json.load(file)
        except FileNotFoundError as ex:
            lista_datos = []
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

        try:
            # Compruebo si ya hay en el archivo ya hay una room_key de la misma persona
            for item in lista_datos:
                if item['_HOTEL_RESERVATION__id_card'] == id_card and \
                        item['_HOTEL_RESERVATION__localizer'] == \
                        localizer:
                    raise HOTEL_MANAGEMENT_EXCEPTION("Room Key ya existente")

            lista_datos.append(ingreso.__dict__)

            # Antes de escribir sobre el documento, verificamos que la fecha de llegada de
            # HotelStay se corresponda con la fecha registrada en HotelReservation
            dato_stay_arrival = str

            for dato1 in lista_datos:
                dato_stay_arrival = dato1['_HOTEL_STAY__arrival']

            #Comparamos el dato del día de llegada de la reserva con el dato extraído en el área
            # de comprobación del localizer y del id_card
            if dato_stay_arrival[:10] != dato_reserva_arrival:
                raise HOTEL_MANAGEMENT_EXCEPTION("La fecha de llegada no coincide con la del "
                                                 "fichero de reserva")


            with open(arrival, "w", encoding="utf-8", newline="") as file:
                json.dump(lista_datos, file, indent=2)
            print("Room Key generada")
        except FileNotFoundError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("Archivo o ruta incorrecta")

        return ingreso.room_key



    ######
    # TERCERA FUNCIÓN
    def guest_checkout(self, room_key):
        #Esta función debe devolver TRUE si la hora de salida es igual a la programada y si la clave es válida.
        #Primero compruebo que se encuentra store_arrival
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        archivo = JSON_FILES_PATH + "store_stay.json"

        try:
            with open(archivo, "r", encoding="utf-8", newline="") as archivo1:
                datos_llegada = json.load(archivo1)
        except FileNotFoundError as ex:
            datos_llegada = []
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

        #ahora compruebo que room_key es hexadecimal
        if self.es_hexadecimal(room_key) == False:
            raise HOTEL_MANAGEMENT_EXCEPTION("FORMATO DE ROOM_KEY INCORRECTO")
        #Formato correcto, ahora vamos a ver si la room_key es correcta. Para ello, usaremos el mismo método
        #que el usado en la función 2
        try:
            aux = ""
            for element in datos_llegada:
                aux = element["_HOTEL_STAY__room_key"]
            if aux != room_key:
                raise HOTEL_MANAGEMENT_EXCEPTION("ROOM KEY NO COINCIDE")
        except FileNotFoundError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("ARCHIVO O RUTA INCORRECTO")
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")
        #room_key está en el almacén. Ahora vamos a comprobar que la fecha de hoy se corresponde
        #con la fecha de salida registrada en el almacén
        try:
            justnow = datetime.utcnow()
            current_datetime = justnow.strftime('%d/%m/%Y %H:%M')
            departure_date = ""
            for dato in datos_llegada:
                departure_date = dato["_HOTEL_STAY__departure"]
            if current_datetime[:10] != departure_date[:10]:
                raise HOTEL_MANAGEMENT_EXCEPTION("FECHA DE SALIDA NO VÁLIDA")
        except FileNotFoundError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("ARCHIVO O RUTA INCORRECTO")
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")
        #Ahora solo queda generar el almacén para guardar la hora de salida y la room key
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G84.2024.T04.EG2/src/JsonFiles/"
        checkout = JSON_FILES_PATH + "guest_checkout.json"
        try:
            with open(checkout, "r", encoding="utf-8", newline="") as salida:
                datos_checkout = json.load(salida)
        except FileNotFoundError as ex:
            datos_checkout = []
        except json.JSONDecodeError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("JsonDecodeError")

        try:
            datos_checkout.append(current_datetime)
            datos_checkout.append(room_key)
            with open(checkout, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_checkout, file, indent=2)
            print("checkout generado")
        except FileNotFoundError as ex:
            raise HOTEL_MANAGEMENT_EXCEPTION("Archivo o ruta incorrecta")

        return True



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


    def ReaddatafromJSOn(self, fi):

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

    def es_hexadecimal(self, cadena):
        return all(caracter.isdigit() or caracter.lower() in 'abcdef' for caracter in cadena)