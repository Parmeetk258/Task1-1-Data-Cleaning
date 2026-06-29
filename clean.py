import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["duration"] = df["duration"].fillna("Unknown")

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Save cleaned dataset
df.to_csv("netflix_titles_cleaned.csv", index=False)

# Display missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved as netflix_titles_cleaned.csv")