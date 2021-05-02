# BI
Objectives

Find out if Meo Map campaign increases the total orders of each user in Aug (compared to Jul) and Jan(compared to Dec)

Assumptions
Meo Map is the only campaign that targets customer frequency.
Correlation between Meo Map users and non-Meo Map users order change shows the effect of Meo Map on users’ frequency.

Methodology
Choose dataset for Jul-Aug and Dec-Jan
Separate data into 2 groups: Meo Map group (who use MM coupons in Aug and Jan, and look at these users’ behaviour in Jul and Dec) and non-Meo Map group (users who not use MM in Aug and Jan), count users’ orders monthly and take order increment from Jul to Aug and from Dec to Jan
Problem: non-Meo Map users are on the lower tier in order number so we can’t compare the change in behaviour of high-frequency MM users and low-frequency non-MM users
To prevent bias, we choose subset of high-order non-MM customers (have the order quantity comparable to Meo Map users in the same time period) to compare with Meo Map’s
=> Find mean of order change of 2 periods by cities
Use Excel Solver to find subset of same number of people for nonMM and MM users from 2 cities: Hanoi and HCM with mean close to MM Users (using mean of MM Users in Aug and Jan)
Only look at these users in our previous dataset
We will do 2 tailed t-test (with significant level of 0.05) on Meo Map and non-Meo Map group order change since the subset we chose are 95% confidence interval (set of 6000 and 9400 orders for first period and second period)
