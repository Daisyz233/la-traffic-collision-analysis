# Data Dictionary

This file summarizes the main raw and engineered fields used in the project. Exact column names may differ depending on the downloaded LA Open Data export.

## Raw Fields Used

| Field | Description |
|---|---|
| DR Number | Unique report identifier for the collision record. |
| Date Occurred | Date of the reported collision. |
| Time Occurred | Time of the reported collision. |
| Area ID / Area Name | LAPD reporting division. |
| Location | Collision location, usually represented by latitude and longitude. |
| Victim Age | Age of victim. |
| Victim Sex | Reported sex of victim. |
| Victim Descent | Reported descent category of victim. |
| MO Codes | Modus operandi codes used to identify collision conditions and severity categories. |

## Engineered Features

| Feature | Description |
|---|---|
| Hour | Hour extracted from collision time. |
| DayOfWeek | Day of week extracted from collision date. |
| IsWeekend | Binary indicator for weekend collisions. |
| Month | Month extracted from collision date. |
| TimePeriod | Grouped time period, such as late night, morning, afternoon, or evening. |
| AgeGroup | Grouped victim age category. |
| spatial_risk_score | Area-level fatality risk score based on historical fatal rate by LAPD division. |
| VehVsPed | Indicator for vehicle-versus-pedestrian collision. |
| VehVsBike | Indicator for vehicle-versus-bike collision. |
| VehVsVeh | Indicator for vehicle-versus-vehicle collision. |
| VehVsMC | Indicator for vehicle-versus-motorcycle collision. |
| HitRun | Indicator for hit-and-run related collision. |
| AtIntersect | Indicator for intersection-related collision. |
| StreetRacing | Indicator for street-racing related collision. |
| DUI | Indicator for DUI-related collision. |

## Severity Target

Severity was encoded into five classes based on MO Codes, using the priority order below when multiple severity codes appeared in one record.

| MO Code | Severity Class |
|---|---|
| 3027 | Fatal |
| 3024 | Severe Injury |
| 3025 | Visible Injury |
| 3026 | Complaint of Pain |
| 3028 | Non-Injury |
