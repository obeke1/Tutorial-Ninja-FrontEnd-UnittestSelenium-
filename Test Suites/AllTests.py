import unittest

from tests.test_cart import test_Cart
from tests.test_title import testTitle

#Get all tests from test_Cart
tc = unittest.TestLoader().loadTestsFromTestCase(test_Cart)
tt = unittest.TestLoader().loadTestsFromTestCase(testTitle)

#Creating tests suites
sanityTestSuite=unittest.TestSuite([tt])
functionTestSuite=unittest.TestSuite([tc])
mastertestSuite=unittest.TestSuite([tc,tt])

#Run Tests suites
#unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)
#unittest.TextTestRunner(verbosity=2).run(functionTestSuite)
unittest.TextTestRunner(verbosity=2).run(mastertestSuite)

