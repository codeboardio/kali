from Root import application
import unittest
class test4(unittest.TestCase):
	def test_one(self):
		self.assertEqual(application.foo(),1)
if __name__ == '__main__':
	unittest.main()