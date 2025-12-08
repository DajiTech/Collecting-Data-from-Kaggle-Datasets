"""Charts.py

Membuat berbagai chart/grafik dari dataset gaji karyawan.

Grafik yang dihasilkan:
1. Histogram - Distribusi gaji bulanan
2. Box Plot - Gaji per departemen
3. Bar Chart - Rata-rata gaji per departemen
4. Scatter Plot - Pengalaman vs Gaji
5. Pie Chart - Distribusi karyawan per departemen
6. Line Chart - Distribusi gaji per pendidikan
7. Count Plot - Jumlah karyawan per kota

Semua grafik disimpan ke folder 'Graph' dalam format PNG."""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Atur style dan font
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Buat folder Graph jika belum ada
graph_dir = "Graph"
os.makedirs(graph_dir, exist_ok=True)

# Baca dataset
filename = "employee_salary_dataset.csv"
if not os.path.exists(filename):
    print(f"File tidak ditemukan: {filename}")
    sys.exit(1)

df = pd.read_csv(filename)

print("Membuat grafik dari data karyawan...")
print(f"Dataset: {len(df)} baris, {len(df.columns)} kolom")
print(f"Folder output: {os.path.abspath(graph_dir)}\n")

# 1. Histogram - Distribusi Gaji Bulanan
print("1. Membuat Histogram - Distribusi Gaji Bulanan...")
plt.figure(figsize=(10, 6))
plt.hist(df['Monthly_Salary'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Monthly Salary ($)')
plt.ylabel('Frequency')
plt.title('Distribusi Gaji Bulanan Karyawan')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(graph_dir, '01_histogram_salary.png'), dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Disimpan: 01_histogram_salary.png")

# 2. Box Plot - Gaji per Departemen
print("2. Membuat Box Plot - Gaji per Departemen...")
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Department', y='Monthly_Salary', palette='Set2')
plt.xlabel('Department')
plt.ylabel('Monthly Salary ($)')
plt.title('Distribusi Gaji per Departemen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(graph_dir, '02_boxplot_salary_by_department.png'), dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Disimpan: 02_boxplot_salary_by_department.png")

# 3. Bar Chart - Rata-rata Gaji per Departemen
print("3. Membuat Bar Chart - Rata-rata Gaji per Departemen...")
plt.figure(figsize=(10, 6))
avg_salary = df.groupby('Department')['Monthly_Salary'].mean().sort_values(ascending=False)
avg_salary.plot(kind='bar', color='steelblue', edgecolor='black')
plt.xlabel('Department')
plt.ylabel('Average Monthly Salary ($)')
plt.title('Rata-rata Gaji per Departemen')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(graph_dir, '03_bar_avg_salary_by_department.png'), dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Disimpan: 03_bar_avg_salary_by_department.png")

# 4. Scatter Plot - Pengalaman vs Gaji
print("4. Membuat Scatter Plot - Pengalaman vs Gaji...")
plt.figure(figsize=(10, 6))
plt.scatter(df['Experience_Years'], df['Monthly_Salary'], alpha=0.6, s=100, color='green', edgecolors='black')
plt.xlabel('Years of Experience')
plt.ylabel('Monthly Salary ($)')
plt.title('Hubungan Pengalaman dengan Gaji')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(graph_dir, '04_scatter_experience_vs_salary.png'), dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Disimpan: 04_scatter_experience_vs_salary.png")

# 5. Pie Chart - Distribusi Karyawan per Departemen
print("5. Membuat Pie Chart - Distribusi Karyawan per Departemen...")
plt.figure(figsize=(10, 8))
dept_count = df['Department'].value_counts()
colors = plt.cm.Set3(np.linspace(0, 1, len(dept_count)))
plt.pie(dept_count.values, labels=dept_count.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Distribusi Karyawan per Departemen')
plt.tight_layout()
plt.savefig(os.path.join(graph_dir, '05_pie_distribution_by_department.png'), dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Disimpan: 05_pie_distribution_by_department.png")

# 6. Bar Chart - Rata-rata Gaji per Pendidikan
print("6. Membuat Bar Chart - Rata-rata Gaji per Pendidikan...")
plt.figure(figsize=(10, 6))
avg_salary_edu = df.groupby('Education_Level')['Monthly_Salary'].mean().sort_values(ascending=False)
avg_salary_edu.plot(kind='barh', color='coral', edgecolor='black')
plt.xlabel('Average Monthly Salary ($)')
plt.ylabel('Education Level')
plt.title('Rata-rata Gaji per Tingkat Pendidikan')
plt.tight_layout()
plt.savefig(os.path.join(graph_dir, '06_bar_avg_salary_by_education.png'), dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Disimpan: 06_bar_avg_salary_by_education.png")

# 7. Count Plot - Jumlah Karyawan per Kota
print("7. Membuat Count Plot - Jumlah Karyawan per Kota...")
plt.figure(figsize=(12, 6))
city_count = df['City'].value_counts()
city_count.plot(kind='bar', color='mediumpurple', edgecolor='black')
plt.xlabel('City')
plt.ylabel('Number of Employees')
plt.title('Jumlah Karyawan per Kota')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(graph_dir, '07_count_employees_by_city.png'), dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Disimpan: 07_count_employees_by_city.png")


print("\n" + "="*60)
print(f"✓ Semua grafik berhasil dibuat dan disimpan ke folder '{graph_dir}'")
print("="*60)
print(f"\nFile yang dihasilkan:")
for i, file in enumerate(sorted(os.listdir(graph_dir)), 1):
    file_path = os.path.join(graph_dir, file)
    file_size = os.path.getsize(file_path) / 1024  # KB
    print(f"  {i}. {file:<45} ({file_size:.1f} KB)")
