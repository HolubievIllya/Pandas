import pandas as pd



# 1. In the cell below, create a DataFrame fruits that looks like this: 
fruits = pd.DataFrame({"Apples": [30], "Bananas": [21]})
# Check your answer
q1.check()
fruits

# 2. Create a dataframe fruit_sales that matches the diagram below:
fruit_sales = pd.DataFrame({"Apples": [35, 41],
                            "Bananas": [21, 34]},
                           index=["2017 Sales", "2018 Sales"])
# Check your answer
q2.check()
fruit_sales

# 3. Create a variable ingredients with a Series that looks like:
ingredients = pd.Series(["4 cups", "1 cup", "2 large", "1 can"],
                       index=["Flour", "Milk", "Eggs", "Spam"],
                       name="Dinner")
# Check your answer
q3.check()
ingredients

# 4. Read the following csv dataset of wine reviews into a DataFrame called reviews: The filepath to the csv file is ../input/wine-reviews/winemag-data_first150k.csv.
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)
# Check your answer
q4.check()
reviews

# 5. Run the cell below to create and display a DataFrame called animals:
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals
# In the cell below, write code to save this DataFrame to disk as a csv file with the name cows_and_goats.csv.
# Your code goes here
animals.to_csv("cows_and_goats.csv")
# Check your answer
q5.check()
