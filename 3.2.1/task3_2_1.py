import pandas as pd

pd.set_option("expand_frame_repr", False)

file_name = "5.csv"
df = pd.read_csv(file_name)

df["years"] = df["published_at"].apply(lambda date: int(".".join(date[:4].split("-"))))  # apply что-то вроде map
years = list(df["years"].unique())  # unique берет отдельную колонку в виде списка уникальных значений

for year in years:
    data = df[df["years"] == year]
    data.iloc[:, :6].to_csv(f"created_csv_files\\part_{year}.csv", index=False)

