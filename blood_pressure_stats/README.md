# Testování


# Testování normálního rozdělení
Jako první test jsem se rozhodl zjistit, zdali mé vzorky odovídají normálnímu rozdělení.
Na přednášce(ve skriptech) byl okrajově zmíněn tzv. KS test (Kolmogorov Smirnov test), který
lze k tomuto ověření použít. Nicméně vzhledem k tomu, že data mají pouze velikost 50 
rozhodl jsem se použít tzv. Shapiro-Wilkenův. 

Navíc protože mezi 

Naše H_0 hypotéza tedy v tomto případě bude:
Náhodný výběr má normální rozdělení.
a jako alternativní hypotézu H_a zvolíme negaci H_0 tedy:
Náhodný výběr není normálně rozdělený.



Pro test normality_test.py

# Personův Chi square test(test dobré shody)

V tomto testu rozdělíme data systolického tlaku do 5 kategorií, a to:
- normal: SYS < 120 **AND** DIA < 80
- elevated  120 <= SYS < 130 **AND** DIA < 80
- hypertension stage 1: 130 <= SYS < 140  **OR** 80 DIA < 90
- hypertension stage 2: 140 <= SYS  **OR** 90 <= DIA
- hypertension stage 3: 180 < SYS  **AND/OR** 120 < DIA

[Zdroj](https://www.health.harvard.edu/heart-health/reading-the-new-blood-pressure-guidelines)

Jako výchozí frekvence populace budeme uvažovat:
- normal: 46.2
- elevated: 17.7
- hypertension stage 1: 19.1
- hypertension stage 2: 12.7
- - hypertension stage 3: 4.4

4.4 46.2 17.7 19.1 12.7

V testu budeme předpokládat, že 
https://www.ahajournals.org/doi/abs/10.1161/HYPERTENSIONAHA.123.20900

[Zdroj](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8040133/)








