import StatsUtilities as utils
import numpy as np

arrDummy1 = np.array([[-4,3], [-4,6]])
arrDummy2 = np.array([[2,5], [5,3]])

def test_Addition():
    solution = np.array([[-2,8], [1,9]])
    assert np.array_equal(utils.Addition(arrDummy1, arrDummy2), solution)

def test_Substraction():
    solution = np.array([[-6,-2], [-9,3]])
    assert np.array_equal(utils.Substraction(arrDummy1, arrDummy2), solution)