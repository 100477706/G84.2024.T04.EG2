import unittest


class TestHotelManager(unittest.TestCase):
    def test_room_resrvation_valid(self):
        my_reservation = HotelManager()
        value = my_reservation.room_reservation()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
