import pandas as pd
from sqlalchemy import create_engine

dataset = pd.read_csv("C:\\Users\\Auguxto\\Desktop\\Projeto Analise 2\\bi-vendas-etl\\data\\raw\\Startups2021.csv", sep=",")

engine = create_engine(
    "postgresql://postgres:senha@localhost:5432/unicorns"
)

# remover duplicados
dataset = dataset.drop_duplicates()

# tratar datas
dataset["Date Joined"] = pd.to_datetime(dataset["Date Joined"], errors="coerce")

# tratar nulos
dataset["City"] = dataset["City"].fillna("Unknown")
dataset["Select Investors"] = dataset["Select Investors"].fillna("Unknown")

# limpar valuation
dataset["Valuation ($B)"] = (
    dataset["Valuation ($B)"]
    .replace(r"[$B]", "", regex=True)
    .astype(float)
)

dim_company = (
    dataset[["Company", "Country", "City", "Industry"]]
    .drop_duplicates()
    .rename(columns={
        "Company": "company",
        "Country": "country",
        "City": "city",
        "Industry": "industry"
    })
)
fact_unicorn = (
    dataset[["Company", "Valuation ($B)", "Date Joined"]]
    .rename(columns={
        "Company": "company",
        "Valuation ($B)": "valuation_b",
        "Date Joined": "date_joined"
    })
)

dim_company.to_sql("dim_company", engine, if_exists="replace", index=False)
fact_unicorn.to_sql("fact_unicorn", engine, if_exists="replace", index=False)