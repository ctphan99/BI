# BI
Objectives
Check if users who receive offer order more high AOV than Control group in each aov range, which value is the most efficient and effective to offer in each aov range and propose promo scheme for high aov ranges
Assumptions
The law of diminishing returns apply to the orders as our coupon value increase
Methodology
Choose dataset from February onward
Group users into 13 groups of 3 AOV (min 120, 150, 200) for different coupon values
Separate data into 2 cities: Ho Chi Minh and Ha Noi, and 3 AOVs for each city
Problem: The orders return will increase as the coupon value increases, but the increment will slow down at a certain amount (in other words, the return will not be worth the cost increment), that point will present the most beneficial value that will maximize the order increase and minimize the cost.
=> In each AOV, we calculate the CPO and orders number for 4 different coupon-received groups  and the Control group 
We want to see if higher-valued coupon increase the order as fast as the lower-value coupon so here we will compare coupon to coupon
For each higher value coupon, compare to the order increase and CPO increase of the lower value one 
The highest order increment will present the best performance coupon value which bring back max order per coupon increment
For CPO increment, we will look at the range for CPO increment and orders increment to get the most effective AOV range for the minimum CPO and maximize the order return

Second Analysis:
We want to see the coupon effect in general so we will look at the cost and order number of each coupon and compare them to the Control group (use Control Group as default)
Problem: Minimizing cost and maximizing orders number have equal importance, but there is no default way to sort 2 values with opposite direction (cost_ ↑ and order_ ↓) at the same time
=>We will convert 2 values range to the same 1 common range and combine them, this will be our sort standard value for the coupons
The highest sort standard value is the recommended discount amount for each AOV group
