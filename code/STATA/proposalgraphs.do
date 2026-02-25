global root    "/Users/ashbelur/Documents/ash belur/BIGPROJECTS/phd/projects/"
global project "introduction/"
global output  "output/"

global datapath "${root}${project}data/raw/"
global outputdir "${root}${project}${output}"


clear
cd "$datapath"

clear all

// import delimited gdppercapita.csv
// drop seriesname
// drop seriescode
// drop countryname
// drop countrycode

import delimited GDPP.csv
gen year = _n + 1960

rename chn_gdpp china
rename ind_gdpp india
rename bgd_gdpp bangladesh
rename bra_gdpp brazil
rename sgp_gdpp singapore
rename vnm_gdpp vietnam
rename kor_gdpp korea
rename rus_gdpp russia
rename idn_gdpp indonesia
rename usa_gdpp usa

destring indonesia, replace ignore("n") force
destring russia,    replace ignore("n") force

scalar baseyear = 15
scalar base_singapore = singapore[baseyear]
scalar base_korea = korea[baseyear]
scalar base_china = china[baseyear]
scalar base_india = india[baseyear]
scalar base_bangladesh = bangladesh[baseyear]
scalar base_brazil = brazil[baseyear]
scalar base_russia = russia[30]
scalar base_indonesia = indonesia[baseyear]
scalar base_usa = usa[baseyear]

gen singapore_n  = 100* singapore / base_singapore
gen korea_n      = 100 * korea / base_korea
gen china_n      = 100 * china / base_china
gen india_n      = 100 * india / base_india
gen bangladesh_n = 100 * bangladesh / base_bangladesh
gen brazil_n     = 100 * brazil / base_brazil
gen usa_n        = 100 * usa / base_usa

gen indonesia_n = 100 * indonesia / base_indonesia
gen russia_n    = 100 * russia / base_russia

label var singapore_n  "SGP"
label var korea_n      "KOR"
label var indonesia_n  "IDN"
label var bangladesh_n "BGD"
label var india_n      "IND"
label var brazil_n     "BRA"
label var china_n      "CHN"
label var usa_n        "USA"
line usa_n china_n korea_n singapore_n indonesia_n bangladesh_n india_n  brazil_n year, lcolor(black black black black black black black black black ) lpattern(solid dash solid dash solid dash solid dash) lwidth(vthin vthin vthin thin thin thick thick vthin vthin) xlabel(1965 1975 1985 1995 2005 2015 2025) ylabel(100 200 400 800 1600 3200 6400 12800) yscale(log) xtitle("Year") ytitle("GDP per capita (USD) (1975=100)")
graph export "${outputdir}/figures/gdp_percapita.jpg", replace

exit

xpose, clear varname


rename v2 korea_orig
rename v3 india_orig
rename v4 singapore_orig
rename v5 vietnam_orig
rename v6 indonesia_orig
rename v7 brazil_orig
rename v8 pakistan_orig
rename v9 russia_orig

local outcomes china korea india singapore vietnam indonesia brazil pakistan russia
local row = 1
// Need to Add proper covariates
foreach var in `outcomes' {
	gen `var' = 100 * `var'_orig / `var'_orig[9]
}

list
line china korea india singapore vietnam indonesia brazil pakistan russia year, xtitle("Year") ytitle("GDP per capita (1984=100)") lcolor(red blue orange black black black black black black) lwidth(medthin medthin medthick vthin medthin vthin vthin vthin vthin)
graph export "${outputdir}/figures/gdp_percapita.jpg", replace

exit




