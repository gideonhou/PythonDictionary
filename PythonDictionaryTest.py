from PythonDictionary import PyDictObject
import unittest

class testPythonDictionary(unittest.TestCase):
    # set up
    def setUp(self):
        self.dictionary0 = PyDictObject();
        self.dictionary1 = PyDictObject(32);
        self.dictionary2 = PyDictObject('dummy input');

    def tearDown(self):
        return;

    # tests the resize function, put, get, remove
    def test_put(self):
        for el in xrange(0, 4):
            self.assertEqual(self.dictionary0.put(el, el), el);
            self.assertEqual(self.dictionary1.put(el, el), el);

        self.assertEqual(self.dictionary0.slots, 8);
        self.assertEqual(self.dictionary1.slots, 32);
        self.assertEqual(self.dictionary2.slots, 8);

        # repeat the same insertions. Make sure that duplicate keys are not inserted
        for el in xrange(0, 4):
            self.assertEqual(self.dictionary0.put(el, el), None);
            self.assertEqual(self.dictionary1.put(el, el), None);

        self.assertEqual(self.dictionary0.slots, 8);
        self.assertEqual(self.dictionary1.slots, 32);

        # now insert enough entries to make the dictionary resize
        for el in xrange(4, 9):
            self.assertEqual(self.dictionary0.put(el, el), el);

        self.assertEqual(self.dictionary0.slots, 16);

        # remove entries
        for el in xrange(0, 9):
            self.assertEqual(self.dictionary0.remove(el), el);
            self.assertEqual(self.dictionary0.remove(el), None);
        
        return;
    
if __name__ == "__main__":
    unittest.main() # run all tests
