import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def game():
  game_images = [rock, paper, scissors]

  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")

game_continue = True

while game_continue == True:
  game()
  user_contine = input("Do you like to continue?Type 'y' for yes and 'n' for no. ").lower()
  if user_contine == "y":
    game_continue == True
  elif user_contine == "n":
    game_continue == False
    print("Goodbye!")
  else:
    print("Please type n or y please")'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to load a dataset from a CSV file
def load_dataset():
    while True:
        try:
            file_path = input("Enter the path to the CSV file: ")
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")

# Function to perform data analysis
def analyze_data(data):
    # Data cleaning (remove missing values)
    data = data.dropna()

    # Summary statistics
    summary_stats = data.describe()

    # Data aggregation (example: calculate the mean of a specific column)
    mean_column = data['Column_Name'].mean()

    # Data visualization (example: histogram)
    data['Column_Name'].hist()
    plt.title('Histogram of Column_Name')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

    # Additional analysis operations
    # Example: Count unique values in a categorical column
    unique_values_count = data['Categorical_Column'].nunique()

    # Example: Group data by a categorical column and calculate the mean of another column
    group_mean = data.groupby('Category_Column')['Value_Column'].mean()

    # Additional visualizations
    # Example: Scatter plot of two numerical columns
    plt.scatter(data['Numerical_Column1'], data['Numerical_Column2'])
    plt.title('Scatter Plot')
    plt.xlabel('Numerical_Column1')
    plt.ylabel('Numerical_Column2')
    plt.show()

    # Example: Box plot of a numerical column
    data.boxplot(column='Numerical_Column3')
    plt.title('Box Plot')
    plt.ylabel('Numerical_Column3')
    plt.show()

    return summary_stats, mean_column, unique_values_count, group_mean

# Main program
if __name__ == "__main__":
    # Load the dataset
    dataset = load_dataset()

    # Perform data analysis
    summary_stats, mean_column, unique_values_count, group_mean = analyze_data(dataset)

    # Display summary statistics and results
    print("\nSummary Statistics:")
    print(summary_stats)
    print(f"Mean of Column_Name: {mean_column:.2f}")

    # Display additional analysis results
    print(f"Number of unique values in Categorical_Column: {unique_values_count}")
    print("\nGrouped mean by Category_Column:")
    print(group_mean)

    # You can continue adding more analysis operations and visualizations as needed.



