# Data Notes

## Source

This project uses the Los Angeles Open Data Portal dataset:

**Traffic Collision Data from 2010 to Present**  
https://data.lacity.org/Public-Safety/Traffic-Collision-Data-from-2010-to-Present/d5tf-ez2w/about_data

The raw dataset is not included in this repository because it is large. Users should download the dataset directly from the official source.

## Download Option

You can download the full CSV using the Socrata API endpoint:

```text
https://data.lacity.org/api/views/d5tf-ez2w/rows.csv?accessType=DOWNLOAD
```

Or use:

```bash
python scripts/download_data.py
```

The download script saves the raw file to:

```text
data/raw/traffic_collision_data.csv
```

The `data/raw/` and `data/processed/` folders are ignored by Git to avoid uploading large files.

## Project Dataset Summary

According to the project report:

- Raw dataset used in the project: 621,677 records
- Records removed during cleaning: 169,031 records
- Final cleaned dataset for analysis: 452,646 records
- Final labeled dataset used for modeling, excluding Unknown severity: 360,687 records

## Cleaning Notes

The project cleaning workflow included:

- Removing invalid coordinates
- Removing records with coordinates outside the Los Angeles boundary used in the project
- Handling missing victim age, sex, descent, and MO Code fields
- Removing duplicate records
- Creating severity labels from MO Codes
- Creating temporal features such as Hour, DayOfWeek, Month, TimePeriod, and IsWeekend
- Creating demographic grouping variables
- Creating collision-type indicator variables from MO Codes
- Creating a spatial risk score using historical fatality rate by LAPD division
