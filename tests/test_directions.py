import unittest
import src.directions as directions


class TestDirectionMethods(unittest.TestCase):

    def test_up(self):
        self.assertEqual(
            directions.move_up('key up')
            , 'snake moves up'
            )

    def test_down(self):
        self.assertEqual(
            directions.move_down('key down')
            , 'snake moves down'
            )
    
    def test_left(self):
        self.assertEqual(
            directions.move_left('key left')
            , 'snake moves left'
            )

    def test_right(self):
        self.assertEqual(
            directions.move_right('key right')
            , 'snake moves right'
            )

#--------------------------------------------------------------

    def test_up_wrong(self):
        self.assertEqual(
            directions.move_up('key asd')
            , "wrong key"
            )

    def test_down_wrong(self):
        self.assertEqual(
            directions.move_down('key 23')
            , "wrong key"
            )
    
    def test_left_wrong(self):
        self.assertEqual(
            directions.move_left('key gf')
            , "wrong key"
            )

    def test_right_wrong(self):
        self.assertEqual(
            directions.move_right('key 4t')
            , "wrong key"
            )




if __name__ == '__main__':
    unittest.main()