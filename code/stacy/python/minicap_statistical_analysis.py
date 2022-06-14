"""
Let's write a program that calculates and displays statistical data
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
    MANOVA (Multivariant ANOVA)
"""

dataset = [[], [], []] # List of subject IDs, list of dependent values, list of independent values

def mean(dataset):
    n = len(dataset)
    sum = 0
    for num in dataset:
        sum += num
    mean = sum / n
    return mean

def sum_of_squares(mean: float, dataset: list): # mean and list of values
    sum = 0 
    for num in dataset:
        sum += ((num - mean) ** 2)
    return sum

def variance(sum_of_squares: float, dataset: list): # sum of squares and list of values
    n = len(dataset)
    variance = sum_of_squares/(n-1)
    return variance

def standard_deviation(variance: float): # variance and list of values
    standard_deviation = variance ** 1/2
    return standard_deviation

######## still not sure how classes work, but I'll just write a skeleton and fix it later
class Subject:
    # Each subject will have an identifier and values for variables. We'll start with 1 dependent variable
    def __init__(self, subject: dict, dependent: int, independent: int): # subject dict will be {'name': 'x', 'ID': y}
        self.subject_name = subject.get('name') # ID number or name
        self.subject_number = subject.get('ID')
        self.dependent_value = dependent
        self.independent_value = independent
        
class Dependent_variable: # Will need variable name, type of variable (discrete, categorical, etc)
    def __init__(self, variable_name, variable_type):
        self.variable_name = variable_name
        self.variable_type = variable_type
    
class Independent_variable:
    def __init__(self, variable_name, variable_type):
        self.variable_name = variable_name
        self.variable_type = variable_type

class Experimental_data: # Will use this to create an instance of each experiment
    def __init__(self, dataset, dependent_variable, independent_variable):
        self.subject_IDs = []
        self.dependent_values = []
        self.independent_values = []
        self.dependent_name = ''
        self.dependent_type = '' # let's start with discrete variables to make it easier to calculate
        self.independent_name = ''
        self.independent_type = ''
    
class Distribution: # We're using a class for this in case we want to reuse just the distribution data later
    # Distribution will calculate mean, sum of squares, variance, and standard deviation
    def __init__(self, dataset: list): # Work in progress
        self.mean = mean(dataset)
        self.sum_of_squares = sum_of_squares(self.mean, dataset)
        self.variance = variance(self.variance, dataset)
        self.standard_deviation = standard_deviation(self.variance)

class Paired_sample_t_test:
    def __init__(self, subject, dependent, independent, dataset):
        self.sample_size = ''
        self.dependent = ''
        self.independent = ''
        self.standard_deviation1 = ''
        self.standard_deviation2 = ''
        self.effect_size = ''
        self.statistical_significance = ''

    def effect_size(self):

        pass

    def statistical_significance(self):

        pass

    def visualize_distribution(self):

        pass
    def __str__(self):

        pass
    
class Independent_t_test:

    pass

class Single_sample_t_test:

    pass
