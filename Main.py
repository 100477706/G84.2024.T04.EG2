# THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
# IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from UC3MTravel import HOTEL_MANAGER


def Main():
    mng = HOTEL_MANAGER()
    res = mng.ReaddatafromJSOn("test.json")
    str_res = res.__str__()
    print(str_res)
    print("CreditCard: " + res.credit_card)
    print(res.localizer)


if __name__ == "__main__":
    Main()
