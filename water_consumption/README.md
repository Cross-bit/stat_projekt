# Testování spotřeby vody
Pro můj statistický experiment jsem se rozhodl zkoumat data denní spotřeby vody obytného domu
čítající 31 bytů za září 2022. Zároveň je ke každému záznamu spotřeby uvedeno číslo bytu, 
průměrný počet osob v daném měsíci a procentuelně vyjádřená plocha bytu vzhledem k celku.

Data jsou dále logicky členěna do 3 skupin, a to podle 3 oddělených vchodů/(schodišť) budovy (A, B, C).

Vzhledem k GDPR a zachování anonymity vlastníků jsem zpermutoval čísla bytů(a samozřejmě neuvádím vlastníky/zdroj).

Vešekerá data(ve formátu .csv) stejně tak jako scripty použité k analýze dat jsou k nalezení na [github](https://github.com/Cross-bit/stat_projekt). Zároveň zde pro úplnost přikládám i odkaz na formátovanou tabulku vstupních [naměřených hodnot]()

Výstupy budu typicky zaokrouhlovat na 3 desetinná místa. Nicméně je samozřejmé, že knihovny které budu používat budou pracovat s vyšší přesností, čímž může ve výstupech dojít k nepatrnému zkreslení. 

## Odstranění outliers
Jako první je potřeba prozkoumat, zdali se v datech nevyskytují záznamy, které by nemusely mít dostatečnou vypovídající hodnotu o skutečné spotřebě, byly neúplné či zkreslené a mohly by tím 
vnést do výsledných statistik významné chyby.

Pro nalezení těchto zavádějících dat, můžeme využít metody explorační analýzi jako jsou např. box ploty, scatter ploty apod.

### Box plot analýza dat
![Alt text](./assets/img/boxplot_with_outliers.svg)

obr. 1: Box plot celkové spotřeby vody jednotlivých vchodů, hotnoty jsou vyznačeny červeně (rozkmit hodnot po horizontální ose je pouze pro lepší čitelnost), černé křížky značí mean.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>vchod</th>
      <th>min</th>
      <th>max</th>
      <th>mean</th>
      <th>Q1</th>
      <th>Q3</th>
      <th>median</th>
      <th>upper whisker</th>
      <th>lower whisker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A</td>
      <td>1.666</td>
      <td>9.732</td>
      <td>4.898273</td>
      <td>2.98200</td>
      <td>7.06250</td>
      <td>4.5090</td>
      <td>13.183250</td>
      <td>-3.138750</td>
    </tr>
    <tr>
      <td>B</td>
      <td>0.000</td>
      <td>31.985</td>
      <td>8.264600</td>
      <td>1.09675</td>
      <td>9.62600</td>
      <td>5.3915</td>
      <td>22.419875</td>
      <td>-11.697125</td>
    </tr>
    <tr>
      <td>C</td>
      <td>0.006</td>
      <td>12.652</td>
      <td>3.277800</td>
      <td>0.48850</td>
      <td>4.09975</td>
      <td>2.5720</td>
      <td>9.516625</td>
      <td>-4.928375</td>
    </tr>
  </tbody>
</table>
Tab. 1: Statistiky hodnot pro jednotlivé vchody.
<br clear="left" />


Na obrázku (1) je vidět box plot všech naměřených hodnot rozdělený dle 3 jednotlivých vchodů domu. Vykreslená data byla zpracována využitím python balíčku pandas a seaborn, které pro identifikování outlierů používá metodu Tukey (viz. kód pro výpočet hodnot), konkrétní hodnoty jsou poté uvedeny v tabulce (1).

Z grafu je patrné, že vchody B a C obsahují dva byty, kterým byla naměřená spotřeba výrazně se lyšící od ostatních naměřených dat. To v našem případě použitím metody Tukey znamená:
$$ x_B = 37,015 > Q3 + IQR \cdot 1.5$$
$$ x_C = 12,652 > Q3 + IQR \cdot 1.5$$

Kde $x_B$ je spotřeba outlieru bytu B, $x_C$ spotřeba outlieru bytu C, *Q3* je 3. kvartil hodnot a *IQR* je tzv. *Interquartile range* $IQR = Q3 - Q1$. 

Pokud se podíváme na outliery, které jsme získali podrobněji můžeme vidět, že $x_B$, která přísluší bytu 12 je i maximum všech naměřených hodnot vůbec. Zároveň si můžeme všimnout, že spotřeba vody zde byla vysoká 
především v 1. polovině měsíce. V daném bytě navíc byla v průměru za měsíc pouze jedna osoba. 

![Alt text](./assets/img/flat12_vs_others.svg)
Modrá křivka je měsíční spotřeba bytu č. 12. Červená přímka je průměr všech bytů kromě b. č. 12

Jak je navíc vidět na obrázku výše v první polovině měsíce byla spotřeba vody značně nadprůměrná.
Můžeme tedy konstatovat, že se nejspíše jednalo o poruchu(např. protékající záchod), která byla 
16 den odstraněna. Pro naše účely analýzi však tento údaj z dat vyloučíme.

Druhý pozorovaný outlier $x_C$ má sice také nadprůměrnou spotřebu, ale na druhou stranu jsou v bytě osoby 3 a spotřeba je na denní bázi převážně konzistentní. Proto jsem se rozhodl tohoto outliera v datech ponechat.

Byt 19 ve vchodu B je v box-plotu uveden jako maximum (a ne jako outlier) nicméně z dat vidíme, že v bytě byl po celý měsíc pouze jeden člověk a jeho spotřeba byla vysoce nadprůměrná. Navíc zde 100 % víme, že byla chyba protékajícího boileru, čili i tento záznam nebudeme dále analyzovat. 

<hr>

Dále jsem se z dat rozhodl vypustit záznamy, kde byla spotřeba během měsíce nulová, nebo téměř nulová. Jistě se jedná o byty ve kterých byl uvedený počet osob 0. 
U bytu 29 sice můžeme vidět drobnou spotřebu 21. den, nicméně tato hodnota je oproti průměrné spotřebě zanedbatelná. Může se tak jedant o chybu měření či např. lehce propouštějící uzávěr apod.

Byty 13, 14 sice mají uvedený počet obyvatel, ale spotřeba je přes všechny dny také nulová/zanedbatelná. Zde se jako rozumné vysvětlení jeví to, že lidé při záznamu počtu obyvatel(které se navíc koná až na konci roku) použili hodnoty, o kterých se domnívali, že jsou správná. Tedy tyto řádky také raději vynecháme.

Stejně tak dává smysl vypustit byt č. 6, kde ač v celkovém součtu je spotřeba v porovnání s ostatními byty možná, tak většina hodnot je nulová a všechna spotřeba je pak koncentrovaná v několika málo dnech. 
To může opět svědčit o chybě měření a tedy tento záznam také vypustíme.

<hr>

Po odstranění všech outlierů nyní dostaneme Box plot na obrázku (4). Můžeme si také všimnout, že střední hodnoty spotřeb jednolivých vchodů (černé křížky) jsou mnohem blíže u sebe než tomu bylo v prvním případě. To nasvědčuje tomu, že data jsou nyní(minimálně napříč vchody) více konzistentní a v další analýze k nim můžeme přistupovat jednotně, s vyšší mírou důvěry.

![Obr. boxplotů bez outlierů](./assets/img/boxplot_no_outliers.svg)

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>vchod</th>
      <th>min</th>
      <th>max</th>
      <th>mean</th>
      <th>Q1</th>
      <th>Q3</th>
      <th>median</th>
      <th>upper whisker</th>
      <th>lower whisker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>1.666</td>
      <td>9.732</td>
      <td>5.035000</td>
      <td>2.7475</td>
      <td>7.10225</td>
      <td>4.6475</td>
      <td>13.634375</td>
      <td>-3.784625</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>3.739</td>
      <td>9.730</td>
      <td>6.713200</td>
      <td>4.4480</td>
      <td>9.31400</td>
      <td>6.3350</td>
      <td>16.613000</td>
      <td>-2.851000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>1.496</td>
      <td>12.652</td>
      <td>5.239667</td>
      <td>3.6745</td>
      <td>5.30850</td>
      <td>3.9845</td>
      <td>7.759500</td>
      <td>1.223500</td>
    </tr>
  </tbody>
</table>


## Nalezení vhodného modelu
Po odfiltrování zavádějících dat se můžeme podívat na vzorek jako celek a pokusit se nalézt vhodný model, který by naše data dobře popisoval. Pro začátek můžeme vynést všechny naměřené denní hodnoty do histogramu.

![Obr. histogramu denní spotřeby](./assets/img/daily_consumption_histogram.svg)


Jak je patrné, nejvyšší koncentrace hodnot je v okolí 0, poté četnost postupně klesá až na několika vzorů kde spořeba byla za den 1 $m^3$ a více[^1]. 

[^1]: Samozřejmě mohli bychom diskutovat i tyto výjimečné hodnoty např. opět pomocí boxplotů. Nicméně vzhledem k nízké četnosti lze usoudit, že spotřeba  mohla být skutečně takto vysoká a tedy je ve v datech necháme.

Klesání na první pohled velmi připomína exponencionální rozdělení, pro ověření, že by tomu tak skutečně mohlo být, dává smysl provést další analýzu vzorků.


### Q-Q plot analýza
K této analýze lze použít tzv. Q-Q ploty[[3]], které nám pomohou rozhodnout jaké distribuci jsou data nejvíce podobná. Konkrétně hledáme takový Q-Q plot, kde nanesené hodnoty kvantilů z našich vzorků a hodnoty kvantilů distribuce si budou co nejvíce odpovídat. To se v grafu projeví tak, že většina hodnot se bude nacházet na 45 stupňové referenční přímce(y=x). Naopak pro distribuce zásadně odlišné od té skutečné, budou nanesené hodnoty od přímky divergovat.

![Obr. Q-Q normální rozdělení](./assets/img/daily_consumption_histogram_with_model.svg)


Kód pro generování je TODO: cesta

![Obr. histogramu denní spotřeby](./assets/img/daily_consumption_histogram_with_model.svg)

### Komentář k modelu
Z analýzi výše nám nejlépe vychází Q-Q plot pro exponencionální distribuci. Je dobré si však rozmyslet, zdali tento model skutečně dobře odpovídá našim datům. Exponencionální rozdělení typicky modeluje nezávislé časové intervaly, určující za jak dlouho nastane nějaký jev v budoucnu. 
Zde se sice nejedná o čas, nicméně při spotřebě vody se jedná o typicky nezávislé 
že spotřeba v jednotlivých dnech jsou naprosto nezávislé veličiny, tedy že pravděpodobnost budoucí spotřeby nijak nezávisí na spotřebě v předchozím dni. 
Ikdyž bychom mohli oponovat tím, že lidé se pravidelně myjí, dávají si průměrně stejný počet šálků čaje apod. Nicméně 


Dále pro "ověření", že můj model není až tak špatně zvolený, v podobných studiiích[1], např. pro modelování byla použita gamma distribuce. Ta by pro modelování dat také mohla být zvolena jak je z Q-Q grafu vidět. Nicméně protože je v mém případě Q-Q graf obdobně dobrý(až na diskutované výchylky) a protože exponenciální distribuce je pouze specialní[2] případ obecnější gamma distribuce, rozhodl jsem se modelovat data takto zjednodušeně.

Když nyní máme stanovenou distribuci, můžeme se začít ptát na důležité otázky např. typu: 
Jaká je pravděpodobnost, že v libovolný den jednotka spotřebuje nejvýše X m^3 vody apod.

Zajímavé body můžeme vidět níže:








[3]: https://www.itl.nist.gov/div898/handbook/eda/section3/qqplot.htm

### Nalezení parametru modelu metodou ML (maximální věrohodnosti)
Metodou maximální věrohodnosti můžeme jednoduše zjistit, že dobrým odhadem pro parametr $\hat{\lambda}$ 
je převrácená hodnota střední hodnoty vzorku, tedy:
$$\hat{\lambda} = \frac{1}{\bar{X}}$$

[proof](https://www.statlect.com/fundamentals-of-statistics/exponential-distribution-maximum-likelihood)

Jak je vidět na obrázku, funkce 



### Nalezení confidenčního intervalu meanu $\mu$
Dále se můžeme pokusit nalézt konfidenční interval pro střední hodnotu populace $\mu$.
Z CLT víme, že pokud je vzorek dostatečně velký(podstatně více než 30), tak nám zde odpadá požadavek na normalitu rozdělení. Dále pro určení budeme potřebovat rozptyl populace. Ten sice přesně neznáme, ale známe alespoň rozptyl dat celého roku(ke kterým mám také přístup). Nejedná se tedy o rozptyl celé populace(která je hypoteticky v našem případě nekonečná nebo do konce životnosti měřidel apod.), takže zde jistá míra nepřesnosti stále bude, nicméně jako aproximace v našem případě bude dostačující.

Zvolme tedy hladinu spolehlivosti $(1-\alpha) = 0.95$. Směrodatná odchylka populace je $\sigma = 0.0513$, velikost vzorku je $n = 630$ $(dny \cdot \#Zaznamu)$, výběrový průměr vzorku $S_n = 0,183$ a pro $\theta = (\mu)$ hledáme konfidenční interval $C_n$ t.ž.: $\lim_{n\to\infty}P(\theta \in C_n ) = 1-\alpha$.

Pro horní a dolní mez intervalu $C_n$ máme v limitě
$$S_n \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}.$$

Pro 95 % konfidenční interval($\alpha/2 = 0.025$) je z scozre $z_{\alpha/2}=1.96$.
Po dosazení tak dostaneme konfidenční interval:
$$C_n = [0.179,0.187]$$



Population variance:
0.0026316775684612245
Standard deviation:
0.0513 TODO





## Exponenciální rozdělení
Jak je vidět na histogramu, naměřené vzorky především v nižších hodnotách připomínají klesající exponencielu. Jediný 

Navíc protože mezi 

Naše H_0 hypotéza tedy v tomto případě bude:
Náhodný výběr má exponenionální rozdělení.
a jako alternativní hypotézu H_a zvolíme negaci H_0 tedy:
Náhodný výběr nená exponenciální rozdělení.

Pro test normality_test.py

Otázku, kterou bychom si mohli položit je, proč mají naše data
zrova toto rozdělení. Exponencionální rozdělení se typicky používá
pro modelování nezávislých časových událostí, konkrétně pravděpodobnost 
za jak dlouho nastane nějaký jev.


Dále pro "ověření", že můj model není až tak špatně zvolený, v podobných
studiiích[[1]], např. pro modelování byla použita gamma distribuce.
Ta by pro modelování dat také mohla být zvolena jak je z Q-Q grafu vidět.
Nicméně protože je v mém případě Q-Q graf obdobně dobrý(až na diskutované výchylky)
a protože exponenciální distribuce je pouze specialní[[2]] případ obecnější gamma distribuce, 
rozhodl jsem se modelovat data takto zjednodušeně.


[1]: https://www.mdpi.com/2073-4441/10/10/1481#B49-water-10-01481

[2]: https://statproofbook.github.io/P/exp-gam.html


Díky nalezenému modelu se nyní můžeme ptát na otázky typu:

Jaká je pravděpodobnost, že v náhodný den bude spotřeba větší/menší než X


## Linearita počtu lidí v domácnosti a celkové spotřeby
Další analýza se bude zabývat závislostí, mezi počtem lid
Lze očekávat, že s větším počtem lidí v bytě bude lineárně s každžým členem růst i spotřeba této jednotky.

![Obr. histogramu denní spotřeby](./assets/img/regression_people_count_vs_consumption.svg)

Dostaneme:

$R$ hodnotu: 0,354 <br>
$R^2$ hodnotu: 0,125
Odtud vidíme, že pouze jen okolo 12,5 % hodnot odpovídá našemu modelu. To ale znamená, že ač náznak linerity v datech je, většinu dat nezahrnuje, a proto tento model musíme zavrhnout.

Údaje spolu sice na 35 % korelují (hodnota $R$), ale to také není zrovna mnoho. Z tohoto důvodu linearitu a jakoukoliv korelaci těchto dat, minimálně na našem vzorku, zavrhneme.



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








