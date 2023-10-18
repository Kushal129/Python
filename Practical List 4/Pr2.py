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
max_p, min_p = df['Production'].max(), df['Production'].min()
print(f"Max Production: {max_p}\nMin Production: {min_p}")

# III. Name of Mines with production of 0
mines_0 = df.loc[df['Production'] == 0, 'Name']
print("Mines with Production of 0:")
print(mines_0)

# IV. Second-highest production
shp = df['Production'].nsmallest(2).iloc[-1]
print(f"Second-Highest Production: {shp}")

# V. Third minimum labor hours
third_mlh = df['Labor Hours'].nsmallest(3).iloc[-1]
print(f"Third Minimum Labor Hours: {third_mlh}")

# VI. Report for 'Labor Hours'
labor_h_r = df['Labor Hours'].describe()
print("Labor Hours Report:")
print(labor_h_r)

# VII. Insert a column filled with NaN values
df['New Column'] = None

# VIII. Sum and average of 'Production' and 'Labor Hours'
p_sum, p_average = df['Production'].sum(), df['Production'].mean()
l_h_sum, l_h_average = df['Labor Hours'].sum(), df['Labor Hours'].mean()

print(f"Production Sum: {p_sum}\nProduction Average: {p_average}")
print(f"Labor Hours Sum: {l_h_sum}\nLabor Hours Average: {l_h_average}")

# IX. Store the updated DataFrame as "result.csv"
df.to_csv("result.csv", index=False)
