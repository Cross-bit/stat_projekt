# Testování spotřeby vody
Pro můj statistický experiment jsem se rozhodl zkoumat data denníc spotřeby vody pro obytný dům 
s 31 byty. Data jsou ze září 2022.
Vzhledem k GDPR a zachování anonymity vlastníků jsem zpermutoval čísla bytů (a samozřejmě neuvádím vlastníky/přímo zdroj).

Vešekerá data(ve formátu .csv) stejně tak jako scripty použité k analýze dat jsou k nalezení na [github](https://github.com/Cross-bit/stat_projekt). Zároveň zde pro úplnost přikládám i odkaz na formátovanou tabulku vstupních [naměřených]()


## Odstranění outliers
V prvné řadě je nutné potřeba se podívat na celkko

To může mít vliv v následujících experimentech, kde budeme zkoumat vztahy mezi různými kategoriemi, ale o tom později.


## Exponenciální rozdělení
Jak je vidět na histogramu, naměřené vzorky především v nižších hodnotách připomínají klesající exponencielu. Jediný 

Navíc protože mezi 

Naše H_0 hypotéza tedy v tomto případě bude:
Náhodný výběr má exponenionální rozdělení.
a jako alternativní hypotézu H_a zvolíme negaci H_0 tedy:
Náhodný výběr nená exponenciální rozdělení.

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








