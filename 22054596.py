# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:41:24 2024

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_x(data, mean_salary):
    """
    Calculate the fraction of the population with salaries between mean_salary and 1.25 * mean_salary.

    Parameters:
    - data: pandas DataFrame containing the salary data
    - mean_salary: mean annual salary

    Returns:
    - fraction_X: fraction of the population with salaries between mean_salary and 1.25 * mean_salary
    """
    lower_bound = mean_salary
    upper_bound = 1.25 * mean_salary
    fraction_X = ((data['salary'] >= lower_bound) & (data['salary'] <= upper_bound)).mean()
    return fraction_X

def plot_salary_distribution(data, mean_salary, fraction_X):
    """
    Plot the salary distribution histogram with mean_salary and fraction_X marked.

    Parameters:
    - data: pandas DataFrame containing the salary data
    - mean_salary: mean annual salary
    - fraction_X: fraction of the population with salaries between mean_salary and 1.25 * mean_salary
    """
    plt.hist(data['salary'], bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label=f'Mean Salary: {mean_salary:.2f} €')
    plt.axvline(1.25 * mean_salary, color='green', linestyle='dashed', linewidth=2, label=f'X (1.25*Mean): {fraction_X:.2%}')
    plt.xlabel('Annual Salary (€)')
    plt.ylabel('Probability Density')
    plt.title('Salary Distribution in European Country')
    plt.legend()
    plt.show()

def main():
    # Read the data from the CSV file
    data = pd.read_csv("C:\\Users\\HP\\Downloads\\data6.csv", header=None, names=['salary'])

    # Calculate mean annual salary
    mean_salary = np.mean(data['salary'])

    # Calculate the value X
    fraction_X = calculate_x(data, mean_salary)

    # Plot the salary distribution and mark mean_salary and fraction_X on the graph
    plot_salary_distribution(data, mean_salary, fraction_X)

if __name__ == "__main__":
    main()