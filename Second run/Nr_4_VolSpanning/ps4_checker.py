##########################################################
##                                                      ##
## Voluntary Problem Set                                ##
## 2nd Moment and First Moment Shocks to Equity returns ##
##                                                      ##
##########################################################

# Note: Please round all numeric answers to two decimals


########### Task A ###########

# The joined pandas data frame has x rows and y columns
a_n_rows = 5224
a_n_cols = 419


########### Task B ###########

# Variance explained by PC1 (PC2) of the international return panel
b_pc1_explained_variance = 0.33
b_pc2_explained_variance = 0.04


########### Task C ###########

# Unconditional correlation of the EU and the US first principal component of returns
c_corr = 0.61

# Adj R2, point estimate, t-stat of regressing PC1 of the international return panel onto PC1 of US equity
c_us_adj_r2 = 0.99
c_us_coef = 1.0
c_us_tstat = 985.52

# Adj R2, point estimate, t-stat of regressing PC1 of the international return panel onto PC1 of EU equity
c_eu_adj_r2 = 0.44
c_eu_coef = 0.66
c_eu_tstat = 64.09

# Additional variance explained by EU information
c_add_r2 = 0.01


########### Task D ###########

# Pairwise correlation of the respective variances
d_corr_us_intl = 0.99
d_corr_eu_intl = 0.82
d_corr_us_eu = 0.8

# Which currency area was the epicenter of the Covid pandemic? ['intl'/'EU'/'US']
d_epicenter = 'US'


########### Task E ###########

# By how much do US volatility shocks outweigh ES volatility shocks?
# (Answer as absolute value, i.e. 0.12 for 12%)
e_factor_us_eu = 0.17

# Pairwise correlation of vol shocks
e_corr_intl_us = 0.95
e_corr_intl_eu = 0.56
e_corr_us_eu = 0.53


########### Task F ###########

# Pairwise correlation of return shocks
f_corr_intl_us = 1.00
f_corr_intl_eu = 0.66
f_corr_us_eu = 0.61


########### Task G ###########

# R2 for regressing return shocks on vol shocks
g_r2_intl = 0.02
g_r2_us = 0.02
g_r2_eu = 0.02

# Do return shocks spawn vol shocks? ['yes'/'no']
g_return_vol = 'no'