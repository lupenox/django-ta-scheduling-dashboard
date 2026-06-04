import unittest


class MyTestCase(unittest.TestCase):
    class TestGetContactInfo(unittest.TestCase):
        # Pre
        def test_00(self):
            # Cant take a null
            pass

        def test_01(self):
            # Must be an Instructor_ID
            pass

        def test_02(self):
            # Instructor_ID must be in the system
            pass

        # Pos
        def test_03(self):
            # Must return info
            pass

    class TestUpdateContactInfo(unittest.TestCase):
        # Pre
        def test_10(self):
            # Cant take a null
            pass

        def test_11(self):
            # Must be an Instructor_ID
            pass

        def test_12(self):
            # Instructor_ID must be in the system
            pass

        # Pos
        def test_13(self):
            # Return True on sucsess
            pass

        def test_14(self):
            # Return False on fail
            pass


if __name__ == '__main__':
    unittest.main()
