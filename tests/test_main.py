import unittest
import rolling_measures

class TestMain(unittest.TestCase):    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_StdDev(self):
        stddev = rolling_measures.StdDev()
        stddev.add(0)
        stddev.add(10)
        self.assertEqual(stddev.get(), 5.0)

        stddev = rolling_measures.StdDev()
        stddev.add(0)
        stddev.add(0)
        stddev.add(0)
        stddev.add(4)
        self.assertEqual(stddev.getSqr(), 3)

    def test_Avg(self):
        avg = rolling_measures.Avg()
        avg.add(0)
        avg.add(10)
        self.assertEqual(avg.get(), 5.0)

        avg = rolling_measures.Avg()
        avg.add(0)
        avg.add(0)
        avg.add(0)
        avg.add(4)
        self.assertEqual(avg.get(), 1)

    def test_Sum(self):
        sum = rolling_measures.Sum()
        sum.add(0)
        sum.add(10)
        self.assertEqual(sum.get(), 10)

        sum = rolling_measures.Sum()
        sum.add(0)
        sum.add(0)
        sum.add(0)
        sum.add(4)
        self.assertEqual(sum.get(), 4)

    def test_Count(self):
        count = rolling_measures.Count()
        count.add(0)
        count.add(10)
        self.assertEqual(count.get(), 2)

        count = rolling_measures.Count()
        count.add(0)
        count.add(0)
        count.add(0)
        count.add(4)
        self.assertEqual(count.get(), 4)

    def test_Stats(self):    
        stat = rolling_measures.Stats({
                "latitude": rolling_measures.Stat("latitude", rolling_measures.Avg),
                "longitude": rolling_measures.Stat("longitude", rolling_measures.Avg),
                "sigma": rolling_measures.StatSum(rolling_measures.Stat("latitude", rolling_measures.StdDev),
                                                  rolling_measures.Stat("longitude", rolling_measures.StdDev))})
        stat.add({'latitude': 1.0, 'longitude': 1.0})
        stat.add({'latitude': 3.0, 'longitude': 3.0})

        self.assertEqual(stat.get()['latitude'], 2.0)
        self.assertEqual(stat.get()['longitude'], 2.0)
        self.assertAlmostEqual(stat.get()['sigma'], 1.41421356237)
