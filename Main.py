import numpy as np
import StatsUtilities as utils

def main():
    # Put all the data in this array.
    arr = [4,3,2,3,5,3,2,2,4,4]
    print(f"Mean: {utils.CalculateMean(arr)}")
    print(f"Median: {utils.CalculateMedian(arr)}")
    print(f"Mode: {utils.CalculateMode(arr)}")
    print(f"Range: {utils.CalculateRange(arr)}")
    print(f"Variance: {utils.CalculateVariance(arr)}")
    print(f"Standard Deviation: {utils.CalculateStandardDeviation(arr)}")
    print(f"Coefficient of Variation: {utils.CalculateCoefficientOfVariation(arr)}")

if __name__ == "__main__":
    main()
