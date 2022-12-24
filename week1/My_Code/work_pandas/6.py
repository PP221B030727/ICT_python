import pandas as pd


#From a dictionary
#Create the dataset you want to analyze
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'numbers': [3, 7, 2]
}
my_df = pd.DataFrame(mydataset)
print(my_df)