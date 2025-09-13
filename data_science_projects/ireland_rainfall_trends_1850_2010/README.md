# Rainfall Trend Analysis in Ireland (1850–2010)

This project analyses long-term rainfall records from 25 stations across Ireland, focusing on seasonal trends and extreme events. Using Python, Pandas, GeoPandas, and open datasets, it reproduces historical patterns and highlights hydrological anomalies relevant to climate research.

## Notebooks

- `01_data_exploration.ipynb`: Raw data inspection, structure checks, and preparation for analysis.
- `02_avg_rainfall_analysis.ipynb`: Calculation of monthly, seasonal, and annual averages, with spatial comparison across stations. 
- `03_statistical_analysis.ipynb`: Correlation analysis between stations, reference series construction, and variability assessment using z-scores. 
- `04_extremes_detection.ipynb`: Identification of wettest and driest years/seasons per station.


## Tools Used
- Python (pandas, numpy, matplotlib, seaborn, geopandas, and contextily.)
- Dataset derived from published sources: https://edepositireland.ie/handle/2262/76134
- Related article: https://mural.maynoothuniversity.ie/id/eprint/8729/

## Outputs
- Summary tables of rainfall extremes.
- Reproducible seasonal trend visualisations.
- Heat map of total rainfall throughout the years.

## Author
Harish Sharma (Maynooth University)
