# CSC334-bd Final Project

## Data
The CogWear database comprises two datasets: a pilot study and a survey gamification experiment. The pilot dataset involves physiological data from 11 volunteers recorded by three wearable devices during cognitively demanding tasks and baseline conditions. The aim was to assess the experimental setup's efficacy and the signals captured by the wearables, particularly in detecting cognitive workload using consumer-grade smartwatches.

The survey gamification experiment dataset includes physiological data from 13 volunteers across two sessions. Participants engaged in cognitively demanding tasks, followed by rest, and then completed mobile surveys related to work and wellbeing, some gamified and others not. Volunteers were split into two groups, each experiencing different survey types in each session with a two-week break between. This dataset investigates the impact of gamification on the cognitive burden of survey completion.

The background highlights the potential of biosignals captured by wearables for real-time cognitive load detection and context-aware interventions. The study aims to compare the utility of different wearable devices for estimating cognitive load and explores the impact of gamification on survey-related cognitive workload. 

Citations:
Grzeszczyk, M. K., Blanco, R., Adamczyk, P., Kus, M., Marek, S., Pręcikowski, R., and Lisowska, A. (2023) 'CogWear: Can we detect cognitive effort with consumer-grade wearables?' (version 1.0.0), PhysioNet. Available at: https://doi.org/10.13026/5f6t-b637.

Grzeszczyk, M.K., Adamczyk, P., Marek, S., Pręcikowski, R., Kuś, M., Lelujko, M.P., Blanco, R., Trzciński, T., Sitek, A., Malawski, M. and Lisowska, A., 2023. Can gamification reduce the burden of self-reporting in mHealth applications? A feasibility study using machine learning from smartwatch data to estimate cognitive load. In AMIA Annual Symposium Proceedings (Vol. 2023, p. 389). American Medical Informatics Association.

Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P.C., Mark, R., Mietus, J.E., Moody, G.B., Peng, C.K. and Stanley, H.E., 2000. PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.

## Analysis
I first copied and organized the Empatica Blood Volume Pulse, Electrodermal Activity, and Body Surface Temperature CSV files into 6 folders, 3 for the baseline data and 3 for the cognitive load data. There are 3 python files to run: empatica_bvp_overall_analysis.py, empatica_eda_overall_analysis.py, and empatica_temp_overall_analysis.py.

The first thing I did was initialize lists to store the results and the data for visualization. Whilst originally scanning the data, I noticed that there were many outliers and used the interquartile range method to clean up the data. I then iterated through each patient's data to find the baseline means, task (cognitive load) means, T-statistics, and P-values for each individual patient/volunteer. The data was then visualized in a box plot and in a histogram. Finally, the average t-statistic and average p-value of all the data analyzed in the script was calculated in order to make conclusions.

## Results
### Blood Volume Pulse
Most of the results for the 11 patients resembled the results for patient 4 as pictured below:
<img src= "https://i.imgur.com/IhpITUg.png" alt = "Patient 4 BVP results">

The values were as follows:
```
Patient 4:
Mean of baseline data: 0.10443718852036434
Mean of task data: 0.5434258564641161
T-statistic: -1.2311530757185805
P-value: 0.21828657626092648
```

However, there were a couple patients that showed the opposite.

The average T-statistic for all patients was 0.6315543991724609 and the average P-value was 0.20489608346851743. Based on the small T-statistic and large P-value (larger than the commonly used significance level of 0.05), I concluded that there is no significant difference between blood volume pulse levels in a person doing cognitively demanding tasks and baseline conditions.

### Electrodermal Activity
In contrast to blood volume pulse, there was visually a difference in the box plot and histograms of the electrodermal activity.
<img src= "https://i.imgur.com/hjz6rLg.png" alt = "Patient 3 EDA results">

The values were as follows:
```
Patient 3:
Mean of baseline data: 0.37378410422960723
Mean of task data: 0.36233919187817254
T-statistic: 47.99532962157368
P-value: 4.334774627e-315
```

Similar to blood volume pulse, there were a few patients that showed the opposite trend where their EDA went up whilst doing the cognitively demanding task.

The average T-statistic for all patients was 37.80978896087567 and the average P-value was 0.01719791500915723. Based on the large T-statistic and small P-value (smaller than the commonly used significance level of 0.05), I concluded that there is a significant difference between electrodermal activity in a person doing cognitively demanding tasks and baseline conditions.

### Body Surface Temperature
Similar to electrodermal activity, there was visually a difference in the box plot and histograms of the body surface temperatures. 
<img src= "https://i.imgur.com/erha2Ea.png" alt = "Patient 3 EDA results">

The values were as follows:
```
Patient 0:
Mean of baseline data: 33.85395031055901
Mean of task data: 34.68105175292154
T-statistic: -93.56728505228374
P-value: 0.0
```

The average T-statistic for all patients was -51.0085788159212 and the average P-value was 0.06423469699265905. While the P-value is larger than the commonly used significance level of 0.05, the difference is very minor so I concluded that there is a significant difference between body surface temperature in a person doing cognitively demanding tasks and baseline conditions.
