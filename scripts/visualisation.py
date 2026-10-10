import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


df = pd.read_csv('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Visualization\\data\\medical_data_cleaned.csv')

print("=" * 70)
print("HEALTHCARE DATA VISUALIZATION")
print("=" * 70)
print(f"Total patients: {len(df)}")
print(f"Columns: {list(df.columns)}")
print()

#  CHART 1: DISEASE DISTRIBUTION 
print("Creating Chart 1: Disease Distribution...")
plt.figure(figsize=(12, 6))
disease_counts = df['Medical_Condition'].value_counts()
plt.barh(disease_counts.index, disease_counts.values, color='steelblue')
plt.xlabel('Number of Patients')
plt.ylabel('Medical Condition')
plt.title('Disease Distribution in Healthcare Data')
plt.tight_layout()
plt.savefig('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Visualization\\data\\1_disease_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 1_disease_distribution.png\n")

#  CHART 2: AGE DISTRIBUTION 
print("Creating Chart 2: Age Distribution...")
plt.figure(figsize=(10, 6))
age_order = ['0-17', '18-34', '35-49', '50-64', '65+']
age_counts = df['Age_Group'].value_counts().reindex(age_order)
plt.bar(age_counts.index, age_counts.values, color='coral')
plt.xlabel('Age Group')
plt.ylabel('Number of Patients')
plt.title('Patient Age Distribution')
plt.tight_layout()
plt.savefig('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Visualization\\data\\2_age_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 2_age_distribution.png\n")

#  CHART 3: GENDER RATIO 
print("Creating Chart 3: Gender Distribution...")
plt.figure(figsize=(8, 6))
gender_counts = df['Gender'].value_counts()
colors = ['#ff9999', '#66b3ff']
plt.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Gender Distribution')
plt.tight_layout()
plt.savefig('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Visualization\\data\\3_gender_ratio.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 3_gender_ratio.png\n")

#  CHART 4: TREATMENT/MEDICATION USAGE 
print("Creating Chart 4: Treatment Usage...")
plt.figure(figsize=(12, 6))
treatment_counts = df['Treatment'].value_counts().head(10)  # Top 10 treatments
plt.barh(treatment_counts.index, treatment_counts.values, color='mediumseagreen')
plt.xlabel('Number of Patients')
plt.ylabel('Treatment Type')
plt.title('Top 10 Treatments Used')
plt.tight_layout()
plt.savefig('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Visualization\\data\\4_treatment_usage.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 4_treatment_usage.png\n")

#  CHART 5: OUTCOME DISTRIBUTION 
print("Creating Chart 5: Treatment Outcomes...")
plt.figure(figsize=(10, 6))
outcome_counts = df['Outcome'].value_counts()
colors_outcome = ['#90EE90', '#FFB6C6', '#FFD700']
plt.bar(outcome_counts.index, outcome_counts.values, color=colors_outcome)
plt.xlabel('Outcome')
plt.ylabel('Number of Patients')
plt.title('Patient Treatment Outcomes')
plt.tight_layout()
plt.savefig('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Visualization\\data\\5_outcome_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 5_outcome_distribution.png\n")

#  CHART 6: DISEASE BY AGE GROUP 
print("Creating Chart 6: Disease by Age Group...")
plt.figure(figsize=(14, 8))
disease_age = pd.crosstab(df['Age_Group'], df['Medical_Condition'])
disease_age = disease_age.reindex(['0-17', '18-34', '35-49', '50-64', '65+'])
disease_age.plot(kind='bar', figsize=(14, 6), colormap='Set2')
plt.xlabel('Age Group')
plt.ylabel('Number of Patients')
plt.title('Disease Distribution by Age Group')
plt.legend(title='Medical Condition', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('C:\\Users\\Divya\\Documents\\GitHub\\Healthcare-Data-Visualization\\data\\6_disease_by_age.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Saved: 6_disease_by_age.png\n")

# ===== SUMMARY STATISTICS =====
print("=" * 70)
print("SUMMARY STATISTICS")
print("=" * 70)
print(f"\nDisease Distribution:")
print(df['Medical_Condition'].value_counts())
print(f"\nAge Group Distribution:")
print(df['Age_Group'].value_counts().sort_index())
print(f"\nGender Distribution:")
print(df['Gender'].value_counts())
print(f"\nOutcome Distribution:")
print(df['Outcome'].value_counts())
print(f"\nAverage Age: {df['Age'].mean():.1f} years")
print(f"Age Range: {df['Age'].min()} - {df['Age'].max()} years")

print("\n" + "=" * 70)
print("✓ ALL CHARTS CREATED SUCCESSFULLY!")
print("=" * 70)
print("\nCharts saved in: data/ folder")
print("1. disease_distribution.png")
print("2. age_distribution.png")
print("3. gender_ratio.png")
print("4. treatment_usage.png")
print("5. outcome_distribution.png")
print("6. disease_by_age.png")