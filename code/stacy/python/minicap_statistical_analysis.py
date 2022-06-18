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

#######################################################################################################

""" Import modules """

import requests

#######################################################################################################

''' Functions for mathematical operations '''

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

#######################################################################################################

""" API """

subject_data_request = requests.get('https://fakerapi.it/api/v1/persons?_quantity=2')
subject_data_request_unpacked = subject_data_request.json()
# print(subject_data_request_unpacked)
subject_data = subject_data_request_unpacked['data']
# print(subject_data)

#######################################################################################################

''' Data '''



""" Testing """



#######################################################################################################

""" Unused Classes """

# class Subject:
#     def __init__(self, subject_ID: str, dependent: int, independent: int): 
#         self.ID = subject_ID
#         self.dependent_value = dependent
#         self.independent_value = independent
#     def __str__(self):
#         return f"subject_ID: {self.ID} \ndependent value: {self.dependent_value} \nindependent value: {self.independent_value}\n"

# class Dependent_variable: # Will need variable name, type of variable (nominal, ordinal, interval, ratio), and data type(discrete or continuous)
#     def __init__(self, variable_dict): # Dictionary for name, type, and metadata for variable
#         self.variable_name = variable_dict.get('variable_name')
#         self.variable_type = variable_dict.get('variable_type') # Should be discrete for now, but this sets up other variable types for the future
#     def __str__(self):
#         return f"Variable name: {self.variable_name}, Variable type: {self.variable_type}"

# class Independent_variable: 
#     def __init__(self, variable_dict): 
#         self.variable_name = variable_dict.get('variable_name')
#         self.variable_type = variable_dict.get('variable_type')
#     def __str__(self):
#         return f"Variable name: {self.variable_name}, Variable type: {self.variable_type}"

""" Unused Functions """

    # def find_mean(self, dependent_values):
    #     n = len(dependent_values)
    #     sum = 0
    #     for num in dependent_values:
    #         sum += num
    #     mean = sum / n
    #     return mean

    # def sum_of_squares(self, dependent_values): # mean and list of values
    #     self.sum_of_squares = 0 
    #     for num in dependent_values:
    #         self.sum_of_squares += ((num - self.mean) ** 2)
    #     return self.sum_of_squares

    # def variance(self, dependent_values): # sum of squares and list of values
    #     n = len(dependent_values)
    #     self.variance = self.sum_of_squares/(n-1)
    #     return self.variance

    # def standard_deviation(self): # variance and list of values
    #     self.standard_deviation = self.variance ** 1/2
    #     return self.standard_deviation

#######################################################################################################

""" Classes """

class Dataset:
    def __init__(self, dataset: list):
        self.dependent_variable_name = ''
        self.independent_variable_name = ''
        self.dependent_variable_type = ''
        self.independent_variable_type = ''
        self.subject_IDs = []
        self.dependent_values = []
        self.independent_values = []

    def __str__(self):

        pass

class Distribution: 
    def __init__(self, dependent_values: list): # Dataset will be a list of dependent variable values
        self.mean = mean(dependent_values)
        self.sum_of_squares = sum_of_squares(self.mean, dependent_values)
        self.variance = variance(self.sum_of_squares, dependent_values)
        self.standard_deviation = standard_deviation(self.variance)
    
    def visualize():

        pass
    
    def __str__(self):
        return f'mean: {self.mean} \nsum of squares: {self.sum_of_squares} \nvariance: {self.variance} \nSD: {self.standard_deviation}\n'

class Independent_t_test:
    def __init__(self):
    
        pass

    def __str__(self):

        pass

class Paired_sample_t_test:
    ''' Needs refactor to take in Experiment class info '''
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
    
    
class Single_sample_t_test:
    def __init__(self):
    
        pass
    
    def __str__(self):

        pass

#######################################################################################################


