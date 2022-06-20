"""
Let's write a program that calculates and displays statistical data
Goals:
    Calculate the distribution of a dataset
    Display that data

    T-tests
        -Independent t-test
        -Paired t-test
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
import random

#######################################################################################################

""" Functions for mathematical operations """

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
    standard_deviation = variance ** (1/2)
    return standard_deviation

#######################################################################################################

""" API """

subject_data_request = requests.get('https://fakerapi.it/api/v1/persons?_quantity=100')
subject_data_request_unpacked = subject_data_request.json()
# print(subject_data_request_unpacked)
subject_data = subject_data_request_unpacked['data']
# print(subject_data)

#######################################################################################################

""" Data """

dataset = []
for index, data in enumerate(subject_data):
    subject = {}
    subject_ID = index + 1
    gender = data['gender']
    if gender == 'male':
        dependent_value = (random.randint(30 , 60) + random.randint(30 , 60))
    elif gender == 'female':
        dependent_value = (random.randint(24, 54) + random.randint(24, 54))
    subject['ID'] = subject_ID
    subject['gender'] = gender
    subject['dependent value'] = dependent_value
    dataset.append(subject)
# print(dataset)

#######################################################################################################

""" Classes """

class Dataset:
    def __init__(self, dataset: list):
        self.dependent_variable_name = 'weight'
        self.dependent_variable_type = 'ratio'
        self.dependent_variable_data_type = 'continuous'
        self.independent_variable_name = 'gender'
        self.independent_variable_type = 'nominal'
        self.independent_variable_data_type = 'discrete'
        self.subject_IDs = []
        for subject in dataset:
            self.subject_IDs.append(subject.get('ID'))
        self.dependent_values = []
        for subject in dataset:
            self.dependent_values.append(subject.get('dependent value'))
        self.independent_values = []
        for subject in dataset:
            self.independent_values.append(subject.get('gender'))
    
    def print_data(self):
        return f' Subject IDs: {self.subject_IDs} \nDependent Variable Values: {self.dependent_values} \nIndependent Variable Values: {self.independent_values}\n'

    def __str__(self):
        return f'ID: Identification number\nGender: Male = 0, Female = 1\nDependent Variable Name: {self.dependent_variable_name}\nDependent Variable Type: {self.dependent_variable_type}\nDependent Data Type: Continuous\nIndependent Variable Name: Gender\nIndependent Variable Type: Nominal\nIndependent Data Type: Discrete\n'

class Distribution: 
    def __init__(self, dependent_values: list): # Dataset will be a list of dependent variable values
        self.mean = mean(dependent_values)
        self.sum_of_squares = sum_of_squares(self.mean, dependent_values)
        self.variance = variance(self.sum_of_squares, dependent_values)
        self.standard_deviation = standard_deviation(self.variance)
    
    def __str__(self):
        return f'mean: {self.mean} \nsum of squares: {self.sum_of_squares} \nvariance: {self.variance} \nSD: {self.standard_deviation}\n'

    # def visualize():
    #     pass
        
class Independent_t_test:
    def __init__(self, dataset):
        self.sample_1 = []
        self.sample_2 = []
        for subject in dataset:
            if subject.get('gender') == 'male':
                self.sample_1.append(subject.get('dependent value'))
            elif subject.get('gender') == 'female':
                self.sample_2.append(subject.get('dependent value'))
        # print(self.sample_1, self.sample_2)

        self.sample_1_distribution = Distribution(self.sample_1)
        self.sample_1_mean = self.sample_1_distribution.mean
        self.sample_1_sum_of_squares = self.sample_1_distribution.sum_of_squares
        self.sample_1_variance = self.sample_1_distribution.variance
        self.sample_1_standard_deviation = self.sample_1_distribution.standard_deviation

        self.sample_2_distribution = Distribution(self.sample_2)
        self.sample_2_mean = self.sample_2_distribution.mean
        self.sample_2_sum_of_squares = self.sample_2_distribution.sum_of_squares
        self.sample_2_variance = self.sample_2_distribution.variance
        self.sample_2_standard_deviation = self.sample_2_distribution.standard_deviation

        self.t_value = (self.sample_1_mean - self.sample_2_mean)/(((self.sample_1_variance/len(self.sample_1))+(self.sample_2_variance/len(self.sample_2)))**(1/2))

        self.degrees_of_freedom = len(self.sample_1) + len(self.sample_2) - 2

    def __str__(self):
        return f'Sample 1 size: {len(self.sample_1)}\nSample 1 mean: {self.sample_1_mean}\nSample 1 SD: {self.sample_1_standard_deviation}\nSample 2 size: {len(self.sample_2)}\nSample 2 mean: {self.sample_2_mean}\nSample 2 SD: {self.sample_2_standard_deviation}\nt-value: {self.t_value}\nDegrees of Freedom: {self.degrees_of_freedom}'

#########################################################################################################

""" Testing """

test1_data = Dataset(dataset)
test1_independent_t_test = Independent_t_test(dataset)
print(test1_independent_t_test)

#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################

""" ######################################  Works in Progress  ######################################"""

#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
'''
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
    
    
class Single_sample_t_test:
    def __init__(self):
    
        pass
    
    def __str__(self):

        pass

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
    #     self.standard_deviation = self.variance ** (1/2)
    #     return self.standard_deviation

#######################################################################################################
'''