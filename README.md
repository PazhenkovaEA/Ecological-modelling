# Ecological-modelling


Goal: make a simulation of population growth in an age-structured population. We will ignore sex structure. Primiparity is 2 years, maximum life span is 5 years.  The survival rate for each age class describes the proportion of the population that moves onto the next age class. Fecundity describes the rate per capita of births arising from each age category. N = initial number of individuals in each age category.

Fecundity and survival are provided as ranges since there's uncertainty about them. Sample from uniform distribution within this range for each simulation. Within a single run (over 30 reproduction cycles) keep parameters constant, but re-sample parameters for each new run.
Time to run: 30 reproduction cycles (time periods).
Number of simulations (runs): 500 runs

Outputs:
* Array with population size in each age category for each run and each reproductive cycle (time period).
* Array with all parameters used for each individual run.
* Graph of projected population growth/decline
