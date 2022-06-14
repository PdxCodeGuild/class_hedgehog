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
    MANOVA (Multivariant ANOVA)
"""


"""
dataset = [
    [
        {

        }

    ], 
    [
        {

        }

    ]
]

"""

dataset = [[], [], []] # List of subject IDs, list of dependent values, list of independent values

def mean(dataset: list):

    pass

def sum_of_squares(dataset: list):

    pass

def variance(dataset: list):

    pass

def standard_deviation(dataset: list):

    pass


######## still not sure how classes work, but I'll just write a skeleton and fix it later
class Subject:
    # Each subject will have an identifier and values for variables. We'll start with 1 dependent variable
    def __init__(self, subject: dict, dependent: dict, independent: dict):
        self.subject_name = subject.key # ID number or name
        self.subject_number = subject.value
        self.dependent_value = dependent.value
        self.independent_value = independent.value #not coded right
        
class Dependent_variable: # Will need variable name, type of variable (discrete, categorical, etc)
    def __init__(self, variable_name, variable_type):
        self.variable_name = variable_name
        self.variable_type = variable_type
    
class Independent_variable:
    def __init__(self, variable_name, variable_type):
        self.variable_name = variable_name
        self.variable_type = variable_type


class Experiment: # Will use this to create an instance of each experiment
    def __init__(self, dataset, dependent_variable, independent_variable):
        self.subject_IDs = []
        self.dependent_values = []
        self.independent_values = []
        self.dependent_name = ''
        self.dependent_type = ''
        self.independent_name = ''
        self.independent_type = ''
    
class Distribution: # We're using a class for this in case we want to reuse just the distribution data later
    # Distribution will calculate mean, sum of squares, variance, and standard deviation
    def __init__(self): # Work in progress
        pass

    def mean(self, dataset):
        n = len(dataset)
        sum = 0
        for num in dataset:
            sum += num
        self.mean = sum / n
        return self.mean

    def sum_of_squares(self):

        pass

    def variance(self):

        pass

    def standard_deviation(self, mean: float, dataset): # Sample standard deviation, not population
        # I'm calculating it all here, but I'll go back and calculate them independently in the other functions
        n = len(dataset)
        s = 0 # standard deviation
        sum = 0 
        for num in dataset:
            sum += ((num - mean) ** 2)
        self.s = (sum / (n-1)) ** (1/2)
        return self.s

class Paired_sample_t_test:
    def __init__(self, independent: str, standard_deviation1: float, standard_deviation2: float):

        pass

class Independent_t_test:

    pass

class Single_sample_t_test:

    pass
