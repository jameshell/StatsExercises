import numpy as np
from scipy import stats as st
import sys

#Methods
def CalculateVariance(arr1):
    OPERATION = 'Variance'
    try:
        npyArray = np.asarray(arr1)
        return np.var(npyArray)
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None

def CalculateMean(arr1):
    OPERATION = 'Mean'
    try:
        result = np.mean(arr1)
        return result
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None

def CalculateMedian(arr1):
    OPERATION = 'Median'
    try:
        result = np.median(arr1)
        return result
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None

def CalculateMode(arr1):
    OPERATION = 'Mode'
    try:
        npyArray = np.asarray(arr1)
        return st.mode(npyArray)
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None

def CalculateStandardDeviation(arr1):
    OPERATION = 'Standard Deviation'
    try:
        npyArray = np.asarray(arr1)
        return np.std(npyArray)
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None

def CalculateRange(arr1):
    OPERATION = 'Range'
    try:
        npyArray = np.asarray(arr1)
        return np.ptp(npyArray, axis=1)
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None

def CalculateCoefficientOfVariation(arr1):
    OPERATION = 'Coefficient of Variation'
    try:
        cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
        return cv(arr1)
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None