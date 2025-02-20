import pandas as pd

# Creating a sample construction dataset
data = {
    "project": ["Building A", "Bridge B", "Mall C", "Highway D", "School E"],
    "type": ["Residential", "Infrastructure", "Commercial", "Infrastructure", "Institutional"],
    "estimated_cost": [500000, 1200000, 800000, 3000000, 600000],
    "actual_cost": [520000, 1300000, 780000, 3100000, 590000],
    "estimated_duration_months": [12, 24, 18, 36, 14],
    "actual_duration_months": [13, 26, 17, 38, 15],
    "location": ["SP", "RJ", "MG", "BA", "RS"]
}

df = pd.DataFrame(data)

# Save the dataset as a CSV file
df.to_csv("construction_projects.csv", index=False)

print("Dataset saved successfully!")
