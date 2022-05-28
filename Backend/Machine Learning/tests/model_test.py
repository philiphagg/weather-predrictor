import sys
sys.path.insert(0, "library")

from model import Model
import unittest


class ModelTest(unittest.TestCase):
    def test_load_model(self):
        """Test if the model can be loaded"""
        model = Model()
        model.load_model(r'saved_model/weather_model')

        self.assertIsNotNone(model.model)

    def test_load_old_data(self):
        """Test if the old data can be loaded"""
        model = Model()
        model.load_old_data()

        self.assertIsNotNone(model.df)

    def test_get_prediction(self):
        """Test if the prediction can be made"""
        model = Model()
        model.load_model(r'saved_model/weather_model')
        model.load_old_data()
        prediction = model.get_prediction(period=1)
        
        self.assertIsInstance(prediction[0], float)
        self.assertIsInstance(prediction[1], float)
        self.assertIsInstance(prediction[2], float)


if __name__ == '__main__':
    unittest.main()
