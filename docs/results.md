# Results

Produced by `python main.py`. Test sets are 20% of each dataset (the most recent days for the weather) and were not used for fitting or model choice.

## House prices: Models

### Test-set errors

| Model | Role | CV r2 | MAE | RMSE | R² |
| --- | --- | --- | --- | --- | --- |
| Linear Regression | Main | 0.784 | 21797.428 | 35827.971 | 0.833 |
| Random Forest | Benchmark beyond the course | 0.824 | 17954.346 | 27833.002 | 0.899 |
| Average | Baseline | -0.002 | 62575.926 | 87619.035 | -0.001 |

![predicted vs actual](../outputs/figures/houses/predicted_vs_actual.png)

## House prices: Weights

![coefficients](../outputs/figures/houses/coefficients.png)

### Linear Regression weights (per standard deviation of each input)

| Input | Weight |
| --- | --- |
| Neighbourhood = StoneBr | 49018.3592 |
| Neighbourhood = NridgHt | 46901.8086 |
| Neighbourhood = NoRidge | 45031.8984 |
| Neighbourhood = Blueste | -36585.5723 |
| Neighbourhood = BrDale | -35493.5837 |
| Neighbourhood = Veenker | 34544.0095 |
| Living area (sq ft) | 26056.9637 |
| Neighbourhood = Crawfor | 23283.7129 |
| Neighbourhood = Blmngtn | -23119.6238 |
| Overall quality (1 to 10) | 21739.2745 |
| Neighbourhood = NPkVill | -20173.2648 |
| Neighbourhood = MeadowV | -15069.7353 |
| Neighbourhood = OldTown | -14823.445 |
| Neighbourhood = Edwards | -14010.5261 |
| Neighbourhood = ClearCr | 13533.6405 |
| Neighbourhood = Mitchel | -11201.2684 |
| Neighbourhood = NWAmes | -11178.8384 |
| Age when sold (years) | -9500.8245 |
| Neighbourhood = SawyerW | -9136.4839 |
| Garage size (cars) | 8998.1916 |
| Neighbourhood = IDOTRR | -8781.0446 |
| Neighbourhood = Gilbert | -8682.4058 |
| Basement area (sq ft) | 7061.4662 |
| Neighbourhood = SWISU | -6259.3562 |
| Lot area (sq ft) | 6183.7876 |
| Neighbourhood = NAmes | -5579.4752 |
| Neighbourhood = Timber | 5193.2373 |
| Neighbourhood = Somerst | 5001.8257 |
| Bedrooms | -3520.0477 |
| Neighbourhood = Sawyer | -2859.387 |
| Neighbourhood = BrkSide | 1268.0496 |
| Neighbourhood = CollgCr | -822.5312 |
| Full bathrooms | -320.3445 |

## House prices: Which inputs matter

![permutation importance](../outputs/figures/houses/permutation_importance.png)

### Permutation importance (drop in R² when the input is shuffled)

|  | Linear Regression | Random Forest |
| --- | --- | --- |
| Living area (sq ft) | 0.2353 | 0.1883 |
| Overall quality (1 to 10) | 0.1788 | 0.5704 |
| Neighbourhood | 0.1143 | 0.0137 |
| Garage size (cars) | 0.035 | 0.0371 |
| Basement area (sq ft) | 0.0304 | 0.0931 |
| Age when sold (years) | 0.0261 | 0.0312 |
| Lot area (sq ft) | 0.0077 | 0.0231 |
| Bedrooms | 0.0045 | 0.006 |
| Full bathrooms | -0.0003 | 0.0076 |

## House prices: Errors

![residuals](../outputs/figures/houses/residuals.png)

### Largest Linear Regression errors on the test set

| Living area (sq ft) | Basement area (sq ft) | Lot area (sq ft) | Bedrooms | Full bathrooms | Garage size (cars) | Overall quality (1 to 10) | Age when sold (years) | Neighbourhood | Real | Predicted | Error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4316 | 2444 | 21535 | 4 | 3 | 3 | 10 | 13 | NoRidge | 755000.0 | 471687.8 | 283312.2 |
| 2364 | 2330 | 12919 | 2 | 2 | 3 | 9 | 1 | NridgHt | 611657.0 | 366896.65 | 244760.35 |
| 2868 | 1992 | 16056 | 4 | 3 | 3 | 9 | 1 | StoneBr | 556581.0 | 381114.14 | 175466.86 |
| 2076 | 2076 | 13891 | 2 | 2 | 3 | 10 | 0 | NridgHt | 465000.0 | 365280.05 | 99719.95 |
| 2296 | 1722 | 13478 | 3 | 2 | 3 | 10 | 1 | NridgHt | 451950.0 | 365618.24 | 86331.76 |
| 2028 | 1868 | 11443 | 2 | 2 | 3 | 8 | 1 | Timber | 369900.0 | 284328.92 | 85571.08 |
| 1337 | 1337 | 5395 | 2 | 2 | 2 | 8 | 15 | StoneBr | 180000.0 | 265320.03 | -85320.03 |
| 1954 | 798 | 15660 | 3 | 1 | 2 | 7 | 69 | Crawfor | 311500.0 | 231107.3 | 80392.7 |
| 1973 | 1935 | 14226 | 3 | 2 | 3 | 8 | 1 | NridgHt | 395000.0 | 321602.45 | 73397.55 |
| 2008 | 896 | 7800 | 3 | 3 | 1 | 5 | 58 | Edwards | 225000.0 | 151814.99 | 73185.01 |
| 2042 | 2042 | 12704 | 3 | 2 | 3 | 8 | 1 | NridgHt | 253293.0 | 325872.45 | -72579.45 |
| 2515 | 2035 | 32668 | 4 | 3 | 2 | 6 | 50 | Crawfor | 200624.0 | 273034.79 | -72410.79 |
| 1726 | 1726 | 9416 | 3 | 2 | 3 | 7 | 0 | Somerst | 311872.0 | 245715.68 | 66156.32 |
| 1044 | 540 | 8712 | 2 | 1 | 2 | 5 | 58 | IDOTRR | 55993.0 | 121653.62 | -65660.62 |
| 1902 | 0 | 8930 | 4 | 2 | 2 | 6 | 32 | Sawyer | 112000.0 | 176307.41 | -64307.41 |
| 1644 | 1518 | 12800 | 2 | 2 | 2 | 7 | 20 | SawyerW | 275000.0 | 212134.29 | 62865.71 |
| 1709 | 970 | 2522 | 3 | 2 | 2 | 7 | 2 | Edwards | 137500.0 | 196993.5 | -59493.5 |
| 1739 | 970 | 2645 | 3 | 2 | 2 | 8 | 10 | Somerst | 172500.0 | 230993.72 | -58493.72 |
| 2794 | 1462 | 15138 | 4 | 2 | 3 | 8 | 14 | NoRidge | 403000.0 | 345084.07 | 57915.93 |
| 1317 | 649 | 8500 | 3 | 1 | 1 | 4 | 88 | IDOTRR | 40000.0 | 95121.78 | -55121.78 |

## House prices: Data

### Data quality

| Column | Type | Missing | Distinct values |
| --- | --- | --- | --- |
| GrLivArea | numeric | 0 | 861 |
| TotalBsmtSF | numeric | 0 | 721 |
| LotArea | numeric | 0 | 1073 |
| BedroomAbvGr | numeric | 0 | 8 |
| FullBath | numeric | 0 | 4 |
| GarageCars | numeric | 0 | 5 |
| OverallQual | numeric | 0 | 10 |
| Age | numeric | 0 | 122 |
| Neighborhood | category | 0 | 25 |
| SalePrice | target | 0 | 663 |

![target](../outputs/figures/houses/target.png)

![correlations](../outputs/figures/houses/correlations.png)

## Student grades: Models

### Test-set errors

| Model | Role | CV r2 | MAE | RMSE | R² |
| --- | --- | --- | --- | --- | --- |
| Linear Regression | Main | 0.841 | 0.746 | 1.155 | 0.863 |
| Random Forest | Benchmark beyond the course | 0.846 | 0.731 | 1.209 | 0.85 |
| Average | Baseline | -0.02 | 2.395 | 3.173 | -0.032 |

![predicted vs actual](../outputs/figures/students/predicted_vs_actual.png)

## Student grades: Weights

![coefficients](../outputs/figures/students/coefficients.png)

### Linear Regression weights (per standard deviation of each input)

| Input | Weight |
| --- | --- |
| Second-term grade (0 to 20) | 2.5113 |
| First-term grade (0 to 20) | 0.4844 |
| Absences | 0.1178 |
| Weekly study time (band) | 0.0927 |
| Past class failures | -0.0908 |

## Student grades: Which inputs matter

![permutation importance](../outputs/figures/students/permutation_importance.png)

### Permutation importance (drop in R² when the input is shuffled)

|  | Linear Regression | Random Forest |
| --- | --- | --- |
| Second-term grade (0 to 20) | 1.3463 | 1.6203 |
| First-term grade (0 to 20) | 0.0283 | -0.0001 |
| Absences | 0.0028 | 0.0497 |
| Past class failures | 0.0024 | 0.012 |
| Weekly study time (band) | 0.0005 | -0.0004 |

## Student grades: Errors

![residuals](../outputs/figures/students/residuals.png)

### Largest Linear Regression errors on the test set

| First-term grade (0 to 20) | Second-term grade (0 to 20) | Weekly study time (band) | Absences | Past class failures | Real | Predicted | Error |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | 9 | 1 | 0 | 2 | 0 | 9.13 | -9.13 |
| 8 | 5 | 2 | 8 | 1 | 8 | 5.57 | 2.43 |
| 6 | 9 | 2 | 0 | 0 | 11 | 8.65 | 2.35 |
| 11 | 12 | 2 | 2 | 0 | 14 | 12.22 | 1.78 |
| 8 | 8 | 2 | 4 | 0 | 10 | 8.24 | 1.76 |
| 14 | 15 | 1 | 2 | 0 | 17 | 15.27 | 1.73 |
| 14 | 13 | 1 | 8 | 0 | 12 | 13.68 | -1.68 |
| 15 | 15 | 3 | 2 | 0 | 14 | 15.68 | -1.68 |
| 11 | 12 | 3 | 2 | 0 | 14 | 12.34 | 1.66 |
| 17 | 18 | 3 | 0 | 0 | 17 | 18.61 | -1.61 |
| 7 | 9 | 2 | 2 | 3 | 10 | 8.42 | 1.58 |
| 18 | 18 | 1 | 0 | 0 | 17 | 18.56 | -1.56 |
| 12 | 11 | 2 | 0 | 0 | 13 | 11.48 | 1.52 |
| 11 | 11 | 3 | 0 | 0 | 10 | 11.42 | -1.42 |
| 9 | 9 | 1 | 0 | 3 | 10 | 8.62 | 1.38 |
| 12 | 13 | 2 | 6 | 0 | 12 | 13.38 | -1.38 |
| 7 | 7 | 2 | 0 | 3 | 8 | 6.62 | 1.38 |
| 12 | 13 | 2 | 2 | 0 | 12 | 13.28 | -1.28 |
| 10 | 11 | 3 | 2 | 0 | 10 | 11.28 | -1.28 |
| 9 | 11 | 2 | 11 | 0 | 10 | 11.22 | -1.22 |

## Student grades: Data

### Data quality

| Column | Type | Missing | Distinct values |
| --- | --- | --- | --- |
| G1 | numeric | 0 | 17 |
| G2 | numeric | 0 | 16 |
| studytime | numeric | 0 | 4 |
| absences | numeric | 0 | 24 |
| failures | numeric | 0 | 4 |
| G3 | target | 0 | 17 |

![target](../outputs/figures/students/target.png)

![correlations](../outputs/figures/students/correlations.png)

## Tomorrow's temperature: Models

### Test-set errors

| Model | Role | CV r2 | MAE | RMSE | R² |
| --- | --- | --- | --- | --- | --- |
| Linear Regression | Main | 0.903 | 1.339 | 1.744 | 0.9 |
| Random Forest | Benchmark beyond the course | 0.897 | 1.365 | 1.774 | 0.896 |
| Average | Baseline | -0.015 | 4.564 | 5.592 | -0.029 |
| Same as today | Baseline | nan | 1.489 | 1.963 | 0.873 |

![predicted vs actual](../outputs/figures/weather/predicted_vs_actual.png)

## Tomorrow's temperature: Weights

![coefficients](../outputs/figures/weather/coefficients.png)

### Linear Regression weights (per standard deviation of each input)

| Input | Weight |
| --- | --- |
| Highest temperature today (°C) | 2.7232 |
| Mean temperature today (°C) | 1.7222 |
| Month = 7 | 1.5741 |
| Month = 1 | -1.2645 |
| Month = 8 | 1.2389 |
| Month = 6 | 1.1222 |
| Month = 2 | -1.1073 |
| Month = 3 | -0.9594 |
| Month = 12 | -0.8635 |
| Month = 9 | 0.7287 |
| Month = 11 | -0.7146 |
| Month = 5 | 0.4879 |
| Month = 4 | -0.4232 |
| Pressure change since yesterday (hPa) | 0.304 |
| Mean cloud cover (%) | 0.2596 |
| Lowest temperature today (°C) | 0.197 |
| Mean humidity (%) | 0.1956 |
| Month = 10 | 0.1806 |
| Mean sea-level pressure (hPa) | 0.1474 |
| Rain and snow (mm) | -0.0774 |
| Sunshine energy (MJ/m²) | -0.0532 |
| Strongest wind (km/h) | 0.026 |

## Tomorrow's temperature: Which inputs matter

![permutation importance](../outputs/figures/weather/permutation_importance.png)

### Permutation importance (drop in R² when the input is shuffled)

|  | Linear Regression | Random Forest |
| --- | --- | --- |
| Highest temperature today (°C) | 0.4904 | 0.1312 |
| Mean temperature today (°C) | 0.1882 | 1.146 |
| Month | 0.0606 | 0.0024 |
| Pressure change since yesterday (hPa) | 0.0065 | 0.0064 |
| Mean cloud cover (%) | 0.0054 | 0.0033 |
| Mean humidity (%) | 0.0021 | -0.0008 |
| Lowest temperature today (°C) | 0.0018 | 0.0056 |
| Mean sea-level pressure (hPa) | 0.0016 | 0.0047 |
| Strongest wind (km/h) | 0.0003 | 0.0022 |
| Rain and snow (mm) | 0.0003 | 0.001 |
| Sunshine energy (MJ/m²) | 0.0002 | 0.0019 |

## Tomorrow's temperature: Errors

![residuals](../outputs/figures/weather/residuals.png)

### Largest Linear Regression errors on the test set

| Mean temperature today (°C) | Highest temperature today (°C) | Lowest temperature today (°C) | Mean humidity (%) | Rain and snow (mm) | Strongest wind (km/h) | Mean sea-level pressure (hPa) | Pressure change since yesterday (hPa) | Mean cloud cover (%) | Sunshine energy (MJ/m²) | Month | Real | Predicted | Error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1 | 8.7 | -3.7 | 92 | 10.4 | 30.6 | 1016.5 | -5.9 | 100 | 0.55 | 12 | 11.8 | 4.57 | 7.23 |
| 8.7 | 14.9 | 1.2 | 86 | 11.6 | 32.2 | 1003.7 | -4.2 | 100 | 0.54 | 11 | 15.9 | 9.45 | 6.45 |
| 2.6 | 5.2 | -1.0 | 73 | 0.0 | 26.9 | 1023.2 | 1.2 | 93 | 3.15 | 1 | 9.2 | 3.03 | 6.17 |
| 29.1 | 38.0 | 19.9 | 40 | 0.9 | 22.5 | 1012.0 | -7.2 | 31 | 26.74 | 7 | 21.2 | 27.29 | -6.09 |
| 6.6 | 9.6 | 2.0 | 90 | 7.1 | 34.5 | 1006.4 | 7.3 | 79 | 1.63 | 2 | 12.6 | 6.65 | 5.95 |
| 16.8 | 20.6 | 9.5 | 81 | 13.3 | 38.3 | 1001.9 | -9.8 | 77 | 6.26 | 10 | 9.6 | 15.0 | -5.4 |
| 7.0 | 9.2 | 3.3 | 93 | 2.0 | 12.4 | 1003.9 | -3.0 | 99 | 1.74 | 11 | 12.2 | 6.82 | 5.38 |
| 2.7 | 7.9 | -3.6 | 77 | 1.1 | 16.7 | 1009.7 | 12.7 | 87 | 8.69 | 3 | 10.1 | 4.76 | 5.34 |
| 1.4 | 2.5 | 0.2 | 96 | 13.2 | 23.3 | 991.7 | -8.4 | 100 | 1.86 | 3 | 6.4 | 1.17 | 5.23 |
| 6.2 | 10.3 | 3.4 | 89 | 1.3 | 14.6 | 1019.8 | 5.9 | 55 | 5.54 | 11 | 12.3 | 7.16 | 5.14 |
| 7.2 | 9.2 | 4.1 | 78 | 1.9 | 25.8 | 1018.8 | -6.4 | 100 | 3.79 | 3 | 11.5 | 6.43 | 5.07 |
| 22.7 | 29.4 | 14.8 | 49 | 0.0 | 15.1 | 1024.9 | 0.0 | 63 | 25.82 | 7 | 27.4 | 22.37 | 5.03 |
| 6.3 | 9.6 | 3.2 | 80 | 0.0 | 11.6 | 1026.3 | -1.7 | 60 | 4.5 | 11 | 11.5 | 6.48 | 5.02 |
| 1.1 | 5.3 | -2.4 | 92 | 0.0 | 11.2 | 1032.5 | 13.5 | 40 | 5.37 | 1 | -1.9 | 3.07 | -4.97 |
| 5.7 | 7.9 | 3.2 | 68 | 0.4 | 33.9 | 1023.4 | -6.5 | 59 | 6.78 | 1 | 9.4 | 4.5 | 4.9 |
| 6.2 | 9.7 | 2.5 | 88 | 0.8 | 19.4 | 1024.3 | 1.6 | 91 | 2.07 | 12 | 11.8 | 6.98 | 4.82 |
| 3.0 | 6.3 | 0.8 | 77 | 1.5 | 18.7 | 1007.9 | 5.8 | 63 | 5.06 | 11 | 8.7 | 3.96 | 4.74 |
| 4.2 | 11.3 | 0.8 | 91 | 9.5 | 20.4 | 998.5 | -11.0 | 98 | 0.67 | 11 | 1.4 | 6.13 | -4.73 |
| 8.5 | 10.9 | 5.2 | 91 | 0.0 | 19.8 | 1023.6 | -7.3 | 96 | 1.51 | 12 | 12.7 | 8.02 | 4.68 |
| 6.5 | 10.0 | 1.7 | 68 | 0.1 | 25.3 | 1021.5 | -3.3 | 44 | 3.24 | 11 | 1.5 | 6.15 | -4.65 |

## Tomorrow's temperature: Data

### Data quality

| Column | Type | Missing | Distinct values |
| --- | --- | --- | --- |
| temp_mean | numeric | 0 | 289 |
| temp_max | numeric | 0 | 329 |
| temp_min | numeric | 0 | 260 |
| humidity | numeric | 0 | 58 |
| precipitation | numeric | 0 | 204 |
| wind_max | numeric | 0 | 414 |
| pressure | numeric | 0 | 569 |
| pressure_change | numeric | 0 | 383 |
| cloud_cover | numeric | 0 | 101 |
| radiation | numeric | 0 | 2222 |
| month | category | 0 | 12 |
| temp_tomorrow | target | 0 | 289 |

![target](../outputs/figures/weather/target.png)

![correlations](../outputs/figures/weather/correlations.png)
