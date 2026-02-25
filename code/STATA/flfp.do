global datapath "/Users/ashbelur/Documents/ash belur/BIGPROJECTS/phd/projects/introduction/data/raw/"

global root    "/Users/ashbelur/Documents/ash belur/BIGPROJECTS/phd/projects/"
global project "introduction/"
global output  "output/"

global outputdir "${root}${project}${output}"

clear all

cd "$datapath"

import delimited "${datapath}GOLDIN.csv

save goldin, replace
use goldin

rename v2 flpp
rename v3 gdpp
destring flpp gdpp, replace ignore("%,") force

graph twoway (scatter flpp gdpp, mlabel(v1) mlabsize(2)) (qfit flpp gdpp), xsc(r(6,12)) ysc(r(0,100)) xtitle("ln GDP per capita (USD)") ytitle("Female Labor Force Participation (%)")

generate gdpp2 = gdpp*gdpp

regress flpp gdpp gdpp2

display _b[_cons]
display _b[gdpp]
display _b[gdpp2]

clear all
cd "$datapath"

import delimited GOLDIN2.csv
scalar b_cons = 269.8555 
scalar b1 = -49.55947 
scalar b2 = 2.752815 

quietly rename v3 gdpp
quietly rename v4 CHN
quietly rename v5 IND
quietly rename v6 BRA
quietly rename v7 RUS
quietly rename v8 KOR
quietly rename v9 IDN
quietly rename v10 SGP
quietly rename v11 VNM
quietly rename v12 BGD

generate qfitted = b_cons + b1*gdpp + b2*gdpp*gdpp


graph twoway (line CHN gdpp, lcolor(red)) (line IND gdpp, lcolor(red) lwidth(thin)) (line BRA gdpp, lcolor(green) lwidth(vthin))(line RUS gdpp, lcolor(yellow) lwidth(medthick)) (line KOR gdpp, lcolor(green) lwidth(thin)) (line IDN gdpp, lcolor(yellow) lwidth(medthin)) (line SGP gdpp, lcolor(green) lwidth(medium)) (line VNM gdpp, lcolor(yellow) lwidth(vthin))  (line BGD gdpp, lcolor(red) lwidth(medium)) (scatter qfitted gdpp, lcolor(black) msymbol(smcircle) msize(tiny)), xtitle("ln GDP per capita (USD)") ytitle("Female Labor Force Participation (%)")
