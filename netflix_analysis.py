# ============================================================
# Netflix Data Analytics Dashboard
# Author: Neelam Choudhary
# Email: neelamchoudharync999@gmail.com
# GitHub: github.com/Neelam0108
# Description: Exploratory Data Analysis on Netflix Dataset
#              to uncover content trends, genre popularity,
#              and audience behavior patterns.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# ── Color palette (Netflix-inspired) ──────────────────────────
RED    = '#E50914'
DARK   = '#141414'
GRAY   = '#564d4d'
LIGHT  = '#f5f5f1'
ACCENT = '#b81d24'

print("=" * 55)
print("   Netflix Data Analytics — by Neelam Choudhary")
print("=" * 55)

# ──────────────────────────────────────────────────────────────
# STEP 1: Generate a realistic sample dataset
# (Replace this block with: df = pd.read_csv('data/netflix_titles.csv'))
# ──────────────────────────────────────────────────────────────
np.random.seed(42)
n = 500

genres    = ['Drama', 'Comedy', 'Documentary', 'Action', 'Thriller',
             'Romance', 'Sci-Fi', 'Horror', 'Animation', 'Crime']
countries = ['United States', 'India', 'United Kingdom', 'Canada',
             'France', 'Japan', 'South Korea', 'Germany']
ratings   = ['TV-MA', 'TV-14', 'TV-PG', 'PG-13', 'R', 'G', 'NR']
types     = ['Movie', 'TV Show']

df = pd.DataFrame({
    'show_id'     : [f's{i}' for i in range(1, n+1)],
    'type'        : np.random.choice(types, n, p=[0.60, 0.40]),
    'title'       : [f'Title_{i}' for i in range(1, n+1)],
    'country'     : np.random.choice(countries, n,
                        p=[0.35,0.20,0.10,0.08,0.08,0.07,0.07,0.05]),
    'release_year': np.random.randint(2010, 2024, n),
    'rating'      : np.random.choice(ratings, n,
                        p=[0.30,0.25,0.15,0.12,0.10,0.05,0.03]),
    'genre'       : np.random.choice(genres, n),
    'duration_min': np.random.randint(60, 180, n),
    'views_million': np.round(np.random.exponential(5, n), 2),
    'user_rating' : np.round(np.random.uniform(2.5, 5.0, n), 1),
})

print(f"\n✔  Dataset loaded: {df.shape[0]} titles × {df.shape[1]} columns")
print(f"   Date range  : {df['release_year'].min()} – {df['release_year'].max()}")
print(f"   Countries   : {df['country'].nunique()}")

# ──────────────────────────────────────────────────────────────
# STEP 2: Cleaning & basic stats
# ──────────────────────────────────────────────────────────────
df.dropna(inplace=True)
print(f"\n📊  Basic Statistics:")
print(f"   Avg views     : {df['views_million'].mean():.2f}M")
print(f"   Avg user rating: {df['user_rating'].mean():.2f} / 5.0")
print(f"   Most common genre: {df['genre'].value_counts().idxmax()}")

# ──────────────────────────────────────────────────────────────
# STEP 3: NumPy analysis
# ──────────────────────────────────────────────────────────────
views = df['views_million'].values
print(f"\n🔢  NumPy Analysis:")
print(f"   Mean  : {np.mean(views):.2f}M")
print(f"   Median: {np.median(views):.2f}M")
print(f"   Std   : {np.std(views):.2f}M")
print(f"   90th %ile: {np.percentile(views, 90):.2f}M")

# Correlation
corr = np.corrcoef(df['user_rating'].values, df['views_million'].values)[0,1]
print(f"   Correlation (rating ↔ views): {corr:.3f}")

# ──────────────────────────────────────────────────────────────
# STEP 4: Visualisations — 4-panel dashboard figure
# ──────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10),
                          facecolor=DARK)
fig.suptitle('Netflix Content Analytics Dashboard',
             fontsize=20, color=RED, fontweight='bold', y=0.98)

for ax in axes.flat:
    ax.set_facecolor('#1a1a1a')
    ax.tick_params(colors=LIGHT)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRAY)

# — Chart 1: Genre popularity (views) —
ax1 = axes[0, 0]
genre_views = df.groupby('genre')['views_million'].mean().sort_values(ascending=True)
bars = ax1.barh(genre_views.index, genre_views.values,
                color=[RED if v == genre_views.max() else ACCENT for v in genre_views.values])
ax1.set_title('Avg Views by Genre (Millions)', color=LIGHT, fontsize=12)
ax1.set_xlabel('Avg Views (M)', color=LIGHT)
ax1.tick_params(colors=LIGHT)

# — Chart 2: Content type distribution —
ax2 = axes[0, 1]
type_counts = df['type'].value_counts()
wedge_props = dict(width=0.5, edgecolor=DARK, linewidth=3)
ax2.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%',
        colors=[RED, '#555'], wedgeprops=wedge_props,
        textprops={'color': LIGHT})
ax2.set_title('Movies vs TV Shows', color=LIGHT, fontsize=12)

# — Chart 3: Content added by year —
ax3 = axes[1, 0]
year_counts = df['release_year'].value_counts().sort_index()
ax3.plot(year_counts.index, year_counts.values,
         color=RED, linewidth=2.5, marker='o', markersize=4)
ax3.fill_between(year_counts.index, year_counts.values,
                 alpha=0.2, color=RED)
ax3.set_title('Titles Released per Year', color=LIGHT, fontsize=12)
ax3.set_xlabel('Year', color=LIGHT)
ax3.set_ylabel('Number of Titles', color=LIGHT)

# — Chart 4: Top 5 countries —
ax4 = axes[1, 1]
top_countries = df['country'].value_counts().head(5)
colors_bar = [RED, ACCENT, '#8B0000', '#666', '#444']
ax4.bar(top_countries.index, top_countries.values,
        color=colors_bar, edgecolor=DARK)
ax4.set_title('Top 5 Content-Producing Countries', color=LIGHT, fontsize=12)
ax4.set_xlabel('Country', color=LIGHT)
ax4.set_ylabel('Number of Titles', color=LIGHT)
ax4.tick_params(axis='x', rotation=20)

plt.tight_layout()
plt.savefig('screenshots/netflix_dashboard.png', dpi=150,
            bbox_inches='tight', facecolor=DARK)
plt.close()
print("\n✅  Dashboard chart saved → screenshots/netflix_dashboard.png")

# ──────────────────────────────────────────────────────────────
# STEP 5: Export summary CSV
# ──────────────────────────────────────────────────────────────
summary = df.groupby('genre').agg(
    total_titles   = ('show_id', 'count'),
    avg_views_M    = ('views_million', lambda x: round(x.mean(), 2)),
    avg_user_rating= ('user_rating', lambda x: round(x.mean(), 2))
).reset_index().sort_values('avg_views_M', ascending=False)

summary.to_csv('data/genre_summary.csv', index=False)
print("✅  Genre summary exported → data/genre_summary.csv")
print("\n🎉  Analysis complete! Open Power BI and load data/genre_summary.csv")
print("    for interactive dashboard building.\n")
