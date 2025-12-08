import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Customer Retention Data - 2024 Quarterly
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Retention_Rate': [71.96, 70.03, 72.28, 74.84]
}

df = pd.DataFrame(data)

# Calculate key metrics
average_retention = df['Retention_Rate'].mean()
industry_target = 85
gap_to_target = industry_target - average_retention
improvement_needed = (gap_to_target / average_retention) * 100

# Print summary statistics
print("=" * 60)
print("CUSTOMER RETENTION ANALYSIS - 2024")
print("=" * 60)
print(f"\nQuarterly Retention Rates:")
for _, row in df.iterrows():
    print(f"  {row['Quarter']}: {row['Retention_Rate']:.2f}%")
print(f"\nAverage Retention Rate: {average_retention:.2f}%")
print(f"Industry Target: {industry_target}%")
print(f"Gap to Target: {gap_to_target:.2f} percentage points")
print(f"Improvement Needed: {improvement_needed:.2f}%")
print("=" * 60)

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('E-commerce Customer Retention Analysis 2024', fontsize=16, fontweight='bold')

# 1. Quarterly Trend Line Chart
ax1 = axes[0, 0]
ax1.plot(df['Quarter'], df['Retention_Rate'], marker='o', linewidth=2, 
         markersize=10, color='#2E86AB', label='Actual Retention Rate')
ax1.axhline(y=industry_target, color='#A23B72', linestyle='--', 
            linewidth=2, label=f'Industry Target ({industry_target}%)')
ax1.axhline(y=average_retention, color='#F18F01', linestyle=':', 
            linewidth=2, label=f'2024 Average ({average_retention:.2f}%)')
ax1.fill_between(range(len(df)), df['Retention_Rate'], industry_target, 
                  alpha=0.2, color='red', label='Gap to Target')
ax1.set_xlabel('Quarter', fontsize=11, fontweight='bold')
ax1.set_ylabel('Retention Rate (%)', fontsize=11, fontweight='bold')
ax1.set_title('Quarterly Retention Rate Trend', fontsize=12, fontweight='bold')
ax1.legend(loc='lower right')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(65, 90)

# 2. Bar Chart with Benchmark
ax2 = axes[0, 1]
bars = ax2.bar(df['Quarter'], df['Retention_Rate'], color=['#E63946', '#F77F00', '#FCBF49', '#06A77D'], 
               edgecolor='black', linewidth=1.5)
ax2.axhline(y=industry_target, color='#A23B72', linestyle='--', 
            linewidth=2, label=f'Target: {industry_target}%')
ax2.set_xlabel('Quarter', fontsize=11, fontweight='bold')
ax2.set_ylabel('Retention Rate (%)', fontsize=11, fontweight='bold')
ax2.set_title('Retention Rate by Quarter vs Target', fontsize=12, fontweight='bold')
ax2.legend()
ax2.set_ylim(65, 90)
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')

# 3. Gap Analysis
ax3 = axes[1, 0]
gaps = [industry_target - rate for rate in df['Retention_Rate']]
colors = ['#E63946' if gap > 12 else '#F77F00' if gap > 10 else '#06A77D' for gap in gaps]
bars = ax3.bar(df['Quarter'], gaps, color=colors, edgecolor='black', linewidth=1.5)
ax3.set_xlabel('Quarter', fontsize=11, fontweight='bold')
ax3.set_ylabel('Gap to Industry Target (pp)', fontsize=11, fontweight='bold')
ax3.set_title('Gap to Industry Target by Quarter', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3, axis='y')
# Add value labels
for bar in bars:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}pp', ha='center', va='bottom', fontweight='bold')

# 4. Performance Summary Dashboard
ax4 = axes[1, 1]
ax4.axis('off')
summary_text = f"""
KEY METRICS SUMMARY

Current Performance:
  • 2024 Average: {average_retention:.2f}%
  • Best Quarter: Q4 ({df['Retention_Rate'].max():.2f}%)
  • Worst Quarter: Q2 ({df['Retention_Rate'].min():.2f}%)
  • Trend: Improving (+{df['Retention_Rate'].iloc[-1] - df['Retention_Rate'].iloc[0]:.2f}pp from Q1 to Q4)

Target vs Actual:
  • Industry Target: {industry_target}%
  • Gap to Close: {gap_to_target:.2f} percentage points
  • Improvement Required: {improvement_needed:.1f}%

Quarterly Performance:
  • Q1 2024: 71.96% (Gap: 13.04pp)
  • Q2 2024: 70.03% (Gap: 14.97pp)
  • Q3 2024: 72.28% (Gap: 12.72pp)
  • Q4 2024: 74.84% (Gap: 10.16pp)

Status: 🔴 BELOW TARGET
Action Required: IMMEDIATE
"""
ax4.text(0.1, 0.95, summary_text, transform=ax4.transAxes, 
         fontsize=10, verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.savefig('retention_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'retention_analysis.png'")

# Additional Analysis: Quarter-over-Quarter Growth
print("\n" + "=" * 60)
print("QUARTER-OVER-QUARTER ANALYSIS")
print("=" * 60)
for i in range(1, len(df)):
    qoq_change = df['Retention_Rate'].iloc[i] - df['Retention_Rate'].iloc[i-1]
    print(f"{df['Quarter'].iloc[i]} vs {df['Quarter'].iloc[i-1]}: {qoq_change:+.2f}pp ({qoq_change/df['Retention_Rate'].iloc[i-1]*100:+.2f}%)")

# Statistical insights
print("\n" + "=" * 60)
print("STATISTICAL INSIGHTS")
print("=" * 60)
print(f"Standard Deviation: {df['Retention_Rate'].std():.2f}%")
print(f"Coefficient of Variation: {(df['Retention_Rate'].std()/df['Retention_Rate'].mean()*100):.2f}%")
print(f"Range: {df['Retention_Rate'].max() - df['Retention_Rate'].min():.2f}pp")

plt.show()
