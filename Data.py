import sys
import pandas as pd
import numpy as np
from tabulate import tabulate

filename = "employee_salary_dataset.csv"
df = pd.read_csv(filename)

target = "Monthly_Salary"

print("\n" + "-"*40)
print(" Statistik Keseluruhan")
print("-"*40)

s = df[target].dropna()

print(f"- Count   : {int(s.count())}")
print(f"- Median  : {s.median()}")
print(f"- Mode    : {s.mode().iloc[0] if not s.mode().empty else 'N/A'}")
print(f"- Mean    : {s.mean()}")
print(f"- Min     : {s.min()}")
print(f"- Max     : {s.max()}")

print("\n" + "-"*40)
print(" Ringkasan Per Kategori")
print("-"*40)

# Tentukan kolom kategori: gunakan 'Category' jika ada, kalau tidak pakai 'Department',
# kalau tidak ada keduanya gunakan kolom bertipe object pertama (kecuali 'Name').
if "Category" in df.columns:
	cat_col = "Category"
elif "Department" in df.columns:
	cat_col = "Department"
else:
	obj_cols = [c for c in df.select_dtypes(include=["object"]).columns if c != "Name"]
	if not obj_cols:
		print("Tidak ditemukan kolom kategori untuk pengelompokan.")
		sys.exit(1)
	cat_col = obj_cols[0]

# Hitung agregat per kategori. 'mode' tidak bisa langsung dipakai di .agg list,
# jadi kita hitung terpisah.
group = df.groupby(cat_col)
grp_count = group[target].count().rename("count")
grp_median = group[target].median().rename("median")
grp_mean = group[target].mean().rename("mean")
grp_min = group[target].min().rename("min")
grp_max = group[target].max().rename("max")
grp_mode = group[target].apply(lambda s: s.mode().iloc[0] if not s.mode().empty else np.nan).rename("mode")

grp = pd.concat([grp_count, grp_median, grp_mode, grp_mean, grp_min, grp_max], axis=1).reset_index()

print(tabulate(grp, headers='keys', tablefmt='psql', showindex=False))
