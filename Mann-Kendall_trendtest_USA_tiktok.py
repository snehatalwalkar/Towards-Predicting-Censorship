# 30 day correlations between G trends during censorship week for keywords tiktok.com and tiktok. sc_com is for south carolina tiktok.com. sc is for tiktok.
#<Dec 1-15 2022>
import pymannkendall as mk

#tiktok.com 
sc_com = [0,	0,	77,	48,	30,	0,	0,	36,	35,	0,	100,	0]

md_com = [76,	100,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]

ut_com = [100,	91,	0,	0,	85,	0,	0,	0,	0,	0,	0,	0]

ga_com = [0,	93,	100,	59,	0,	0,	0,	0,	0,	0,	0,	97]



#tiktok.

sc =	[73,	57,	76,	84,	83,	67,	64,	100,	86,	90,	83,	70]

md =	[65,	79,	100,	89,	67,	88,	80,	75,	80,	98,	88,	82]

ut =	[67,	57,	100,	88,	66,	64,	80,	87,	52,	94,	85,	50]

ga =	[89,	77,	71,	87,	80,	75,	79,	80,	87,	95,	100,	84]



 
# perform Mann-Kendall Trend Test
print('M-KT for tiktok.com on 4 US states from Dec 1-15, 2022')
print('\nSC:',mk.original_test(sc_com))
print('\nMD:',mk.original_test(md_com))
print('\nUT:',mk.original_test(ut_com))
print('\nGA:',mk.original_test(ga_com))

print('\n\nM-KT for keyword "tiktok" on 4 US states from Dec 1-15, 2022')
print('\n\n SC:',mk.original_test(sc))
print('\nMD:',mk.original_test(md))
print('\nUT:',mk.original_test(ut))
print('\nGA:',mk.original_test(ga))


#Ref:https://www.geeksforgeeks.org/how-to-perform-a-mann-kendall-trend-test-in-python/
#
#Reference output:
#Mann_Kendall_Test(trend=’no trend’, h=False, p=0.3672323880406272, z=-0.9016696346674322, Tau=-0.24444444444444444, 
#s=-11.0, var_s=123.0, slope=-0.2857142857142857, intercept=54.285714285714285)
#
#The output interpretation can be done in the following different ways:
#
#trend: This tells the trend-increasing, decreasing, or no trend.
#h: True if the trend is present. False if no trend is present.
#p: The p-value of the test.
#z: The normalized test statistic.
#Tau: Kendall Tau.
#s: Mann-Kendal’s score
#var_s: Variance S
#slope: Theil-Sen estimator/slope
#intercept: Intercept of Kendall-Theil Robust Line
