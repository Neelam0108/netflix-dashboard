# 🎬 Netflix Data Analytics Dashboard

> Exploratory data analysis and interactive dashboard built on Netflix content data using Python, NumPy, and Power BI.

**Author:** Neelam Choudhary  
**Email:** neelamchoudharync999@gmail.com  
**LinkedIn:** [linkedin.com/in/neelam-choudhary](https://linkedin.com/in/neelam-choudhary)  
**GitHub:** [github.com/Neelam0108](https://github.com/Neelam0108)

---

## 📌 Project Overview

This project dives into a Netflix dataset to answer real business questions:
- Which genres attract the most viewers?
- How has Netflix's content library grown over the years?
- Which countries produce the most content?
- Is there a relationship between user rating and views?

The insights were visualised in both **Matplotlib** (Python) and an interactive **Power BI dashboard**.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| NumPy | Statistical computations |
| Pandas | Data manipulation & cleaning |
| Matplotlib | Static chart generation |
| Jupyter Notebook | Interactive development |
| Power BI | Interactive business dashboard |
| MS Excel | Initial data review |
| GitHub | Version control & project hosting |

---

## 📁 Project Structure

```
netflix-dashboard/
│
├── netflix_analysis.py          # Main Python analysis script
├── notebooks/
│   └── Netflix_Analysis.ipynb   # Step-by-step Jupyter notebook
├── data/
│   └── genre_summary.csv        # Exported summary (auto-generated)
├── screenshots/
│   └── netflix_dashboard.png    # Dashboard chart output
├── docs/
│   └── Netflix_Project_Report.pdf  # Full project report
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Neelam0108/netflix-dashboard.git
cd netflix-dashboard
```

**2. Install dependencies**
```bash
pip install numpy pandas matplotlib jupyter
```

**3. Run the analysis**
```bash
python netflix_analysis.py
```

**4. Open the notebook (optional)**
```bash
jupyter notebook notebooks/Netflix_Analysis.ipynb
```

---

## 📊 Key Findings

- **Drama & Action** genres drive the highest average viewership
- **60% Movies / 40% TV Shows** in the content mix
- Netflix content growth peaked between **2018 and 2022**
- **USA and India** are the top two content-producing countries
- User rating has a **weak positive correlation** with views

---

## 📸 Dashboard Preview

![Netflix Dashboard](screenshots/netflix_dashboard.png)

---

## 🔗 Power BI Dashboard

The interactive Power BI report was built using the exported `data/genre_summary.csv`.  
It includes slicers for **Year**, **Genre**, and **Country** for dynamic filtering.

---

## 📄 License

This project is for educational and portfolio purposes only.  
Dataset used is either publicly available or synthetically generated for demonstration.

---

*Made with ❤️ by Neelam Choudhary — B.Tech ECE, UIT RGPV Bhopal*
