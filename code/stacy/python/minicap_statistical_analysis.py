"""
Let's write a program that calculates and displays 
Goals:
    Calculate the distribution of a dataset
    Display that data

    T-tests
        -Paired t-test
        -Independent t-test
        -One sample t-test

Stretch Goals:
    Chi-square test
    ANOVA
    Z-test
"""
######## still not sure how classes work, but I'll just write a skeleton and fix it later
class Subject:
    # Each subject will have an identifier and values for variables. We'll start with 1 dependent variable
    def __init__(self, subject: str, dependent: int):
        self.subject = subject
        self.dependent = dependent
        
class Distribution: 
    # Distribution will calculate mean, sum of squares, variance, and standard deviation
    def __init__(self, independent: str, dataset: list): # Not sure if independent goes here since it's not a test
        self.independent = independent
        self.dataset = dataset

    def mean(dataset):
        n = len(dataset)
        sum = 0
        for num in dataset:
            sum += num
        mean = sum / n
        return mean

    def sum_of_squares():

        pass

    def variance():

        pass

    def standard_deviation(mean: float, dataset): # Sample standard deviation, not population
        # I'm calculating it all here, but I'll go back and calculate them independently in the other functions
        n = len(dataset)
        s = 0 # standard deviation
        sum = 0 
        for num in dataset:
            sum += ((num - mean) ** 2)
        s = (sum / (n-1)) ** (1/2)
        return s

class Paired_sample_t_test:
    def __init__(self, independent: str, standard_deviation1: float, standard_deviation2: float):

        pass
