import unittest
import pandas as pd
from my_lambdata.ds_utilities import enlarge, MyDataSplitter

# Run this with the command: python -m test.ds_utilities_test

class TestDsUtilities(unittest.TestCase):

    def test_enlarge(self):
        # first assert will fail
        # self.assertEqual(enlarge(3), 350)
        self.assertEqual(enlarge(3), 300)

    def test_date_divider(self):
        raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
                    'age': [20, 19, 22, 21],
                    'favorite_color': ['blue', 'red', 'yellow', "green"],
                    'grade': [88, 92, 95, 70],
                    'birth_date': ['01-15-1996', '08-05-1997', '04-28-1996', '12-16-1995']}
        df = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
        date_col = 'birth_date'

        current_shape = df.shape[1]
        expected_shape = current_shape + 3

        # Create MyDataSplitter object
        splitter = MyDataSplitter(df)
        converted_df = splitter.date_divider(date_col)

        self.assertEqual(expected_shape, converted_df.shape[1])


if __name__ == '__main__':
    unittest.main()
