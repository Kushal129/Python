import pandas as pd

# # Create a DataFrame with sample data and save it to "Production.csv"
# data = {
#     "Name": ["Kushal", "Malay", "Jay", "Vishal", "Lalu", "Meet", "Sayam", "Kushal", "Henvi", "Dawro"],
#     "Production": [100, 200, 0, 300, 150, 0, 250, 400, 500, 0],
#     "Labor Hours": [120, 220, 100, 300, 180, 90, 250, 400, 500, 80],
# }
# df = pd.DataFrame(data)
# df.to_csv("Production.csv", index=False)

# I. Read and print the data
df = pd.read_csv("Production.csv")
print(df)

# II. Max and min values of 'Production'
max_production, min_production = df['Production'].max(), df['Production'].min()
print(f"Max Production: {max_production}\nMin Production: {min_production}")

# III. Name of Mines with production of 0
mines_with_zero_production = df.loc[df['Production'] == 0, 'Name']
print("Mines with Production of 0:")
print(mines_with_zero_production)

# IV. Second-highest production
second_highest_production = df['Production'].nsmallest(2).iloc[-1]
print(f"Second-Highest Production: {second_highest_production}")

# V. Third minimum labor hours
third_min_labor_hours = df['Labor Hours'].nsmallest(3).iloc[-1]
print(f"Third Minimum Labor Hours: {third_min_labor_hours}")

# VI. Report for 'Labor Hours'
labor_hours_report = df['Labor Hours'].describe()
print("Labor Hours Report:")
print(labor_hours_report)

# VII. Insert a column filled with NaN values
df['New Column'] = None

# VIII. Sum and average of 'Production' and 'Labor Hours'
production_sum, production_average = df['Production'].sum(), df['Production'].mean()
labor_hours_sum, labor_hours_average = df['Labor Hours'].sum(), df['Labor Hours'].mean()
print(f"Production Sum: {production_sum}\nProduction Average: {production_average}")
print(f"Labor Hours Sum: {labor_hours_sum}\nLabor Hours Average: {labor_hours_average}")

# IX. Store the updated DataFrame as "result.csv"
df.to_csv("result.csv", index=False)
