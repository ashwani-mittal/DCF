#!/usr/bin/env python
# coding: utf-8

# In[2]:


#DCF Question 1

# first we need to define the rate as the interest rate
interest_rate = float(input("Please enter the Rate of Interest: "))  / 100

# then we define the present value
presentV = float(input("Please enter the Present Value of Annuity: $ "))  

# then we define the time elapased for the annuity
time = int(input("Enter period of time: ")) 

# The formula for ACF will be PV = ACF ( 1 - ( 1 / ( 1 + rate )^t ) ) / rate
# Use the above formula to solve for ACF to define your formula

# below ACF is for annual cash flow
ACF = round((presentV * interest_rate / ( 1 - ( 1 / ( 1 + interest_rate )**time))) , 2)

print(f"The annual cash flow of the annuity is {ACF}" )


# In[8]:


#DCF Question 2

# Lets start by defining Monthly Payment Value (MPV)
mon_pay_val = float(input("Please enter the Monthly Payment Value: $"))    

# now we can define the present value of the contract (PV)
presentV = float(input("Please enter the Present Value of Contract: $"))  

# Monthly Rate (MR) equation can be defined below as:
mon_rate = mon_pay_val / presentV

# The formula for Annual Percentage Rate(APR) is APR =(MPV/PV)*12
# We mentioned above MPV/PV is actually monthly rate (MR)
# Formula for APR now becomes APR = MR * 12

APR = mon_rate * 12

# Now the formula for Effective Annual Return (EAR) which is EAR = ((1 + MR)**12 - 1)
# Now just solve for EAR  

EAR = ( ( 1 + mon_rate ) **12 - 1 )

print("The Effective Annual Percentage Rate is %0.2f percent" % (EAR*100))
print("The Annual Percentage Rate is %0.2f percent" % (APR*100))
print("The Monthly Percentage Rate is %0.2f percent" % (mon_rate*100))


# In[11]:


# DCF Question 3

# lets first define the time elapsed in months 
time = int(input("Please enter period of time (in months): ")) 

# now define Return Value (RV) which will be the times by which the investment shall grow your money(triple)
return_value = float(input("Please enter the times by which the investment shall grow your money: "))  

# now below we define number of quarters in a year (4 quarters)
n = time / 3

# now below we define the rate of return(ROR) in terms of return_value and quarters with this equation
ROR = (return_value**(1/n)) - 1

print("The Rate of Return every quarter will be %0.2f percent" % (ROR*100))


# In[15]:


# DCF Question 4



# lets first define the payment (pmt) received from lottery
pmt = int(input("Please enter the lottery amount received: $ "))

# now define n as the number of payments you will recieve in years
n = int(input("Please enter the number of payments you will receive: "))

# now define percent increase per year as growth
growth = float(input("Please enter the increase in percent growth per year: ")) / 100

# now define discount rate as dis_rate
dis_rate = float(input("Please enter the discount rate given in percent: ")) / 100

# now we can use the formula that is for present value of growing annuity
# to use this first lets break annuity factor into interest and growth factor
int_factor = ((1+dis_rate)**(-n)) #(1/(1+i)**n we made it a reciprocal here
grow_factor = ((1+growth)**n)

# now we can calculate the numerator and denominator of the annuity factor
numerator = 1 - grow_factor*int_factor
denominator = dis_rate-growth

# now we can calculate the annuity factor(annu_factor)
annu_factor = numerator/denominator

#use present value for annuity formula
presentV = pmt*annu_factor

#print output
print(f'The present value of the growing annuity is ${round(presentV)}')


# In[13]:


# DCF Question 5

import math

# Below first you define the dollar value of your final account balance
final_value = float(input("Please enter the final balance amount for your account: $"))   

# presentV (PV) here will be defined as the monthly payments you are making presently
presentV = float(input("Please enter the monthly payment that you're making: $"))  

# interest rate here will be the monthly increase by percent in selling price
interest = float(input("Please enter the monthly rate of Interest(in %): ")) / 100 

# the formula for # of Periods : num_periods= ln[(1+(final_value(interest)/presentV))**−1] ÷ ln(1+interest)
# Solve for NP
 
num_periods = round(math.log(1 + ( final_value * (interest / 12) / presentV)) / math.log( 1 + (interest / 12) ))

print("The number of payments you will have will come out to: %d" % num_periods )


# In[21]:


# DCF Question 6

# lets start by defining time  for fixed-rate mortgage to buy a new home
# make sure to multiple time 30 years and convert it into monthly by multiplying by 12
time = int(input("Please enter the period of time (in years): "))*12 

# now define the dollar value you have available for your monthly payments
mon_payment = float(input("Please enter the monthly payment: $"))  

# now annual percent rate will be defined as the APR given by bank on your mortgage
# when using interest in the present value equation below , you need to divide interest by 12 for monthly interest
annual_pr = float(input("Please enter the APR given by the bank on mortgage (in %): ")) / 100 

#now lets get input for the loan amount
loan = float(input("Please enter the loan amount: $"))

# now below we can define the presentV (PV) formula
presentV = mon_payment * ( 1 - ( 1 / ( 1 + (annual_pr / 12) )**(time) )) / (annual_pr / 12)

# now lets define the balloon paymant (BP) in terms of loan amount and PV
bp = loan - presentV

print("The balloon payment at the end of the is going to be  %0.2f" % bp)


# In[5]:


# DCF Question 7

# below first lets define the number of days for the 30-year mortgage
num_days = int(input("Please enter the mortgage period (in years): ")) * 365

# below now lets define presentV which here is going to be the loan amount
presentV= int(input("Please enter the total loan amount: $")) * (80/100)

# below now lets define the monthly payment on this loan amount
mon_pay = int(input("Please enter your monthly payment: $"))

# lets now add up the total payments below 
total_pay = mon_pay * (360) # 30 years times 12 givees you 360 months

# now lets divide total payments by amount that you owe: your presentV to get daily returns
daily_returns = total_pay/presentV

# now lets multiple get your annual returns by multiplying mon_returns by 12
annual_returns = daily_returns*365

# Now lets calculate the Annual Percent Rate (APR)
APR = (annual_returns/num_days)*100

# Now lets calculate the Effective Annual Return (EAR)
EAR = (1+((APR/12)*12))-1

print(f'The EAR is {round(EAR, 2)}%')

print(f'The APR is going to come out to be: {round(APR,2)}%')


# In[25]:


# DCF Question 8

# in order to tackel this questions, first we need to split this into two annuities
# 10 years will be associated and ran for one annuity and after that we have to discount it back 6 more years to present day
# our second annuity will be a seix year annuity leading back to present day

# now we will than consider the first time as time1 as the beginning of the period which is six years from present 
# second, we will consider time0 as the present day
# time2 is going to be the end of the annuity period


# below now lets take number of time period for the n_time2_time1 as the difference between final year and time1
n_time2_time1 = int(input("Please enter the period (in years) for the 10% discount rate: "))*12
# above we are multiplying n_time2_time1 by 12 gives you period in months for 10% discount rate (120 months)

# below now lets take the discount rate between time2 and time1 by dividing 10/100 and again that value by 12
int_time2_time1 = float(input("Please enter the interest rate compounded monthly (in%) for the later 10 years: ")) / (100 * 12)
# above you are dividing int_time2_time1 by 100 first do convert 10 into .10 and by 12 to find the monthly compounded interest rate

# below now lets define the payment that you are receiving 16 years later by the annuity
pmt_annuity = int(input("Please enter the annuity payment: $"))

# below now we need to compute present value of remaining annuity at time time1
presentV_time1 = pmt_annuity*((1-((1+int_time2_time1)**(-n_time2_time1)))/int_time2_time1)

# now we compute the present value of this cash flow at time time0 
# (time0= first 6 years from present)

# below n_time1_time0 is going to be the difference between time1 and time0
n_time1_time0 = int(input("Please enter the period(in years) for the 13% discount rate: "))*12
# above we are multiplying n_time1_time0 by 12 gives you period in months for 13% discount rate (72 months)

# below now lets take the discount rate between time1 and time0 by dividing 13/100 and again that value by 12
int_time1_time0 = float(input("Please enter the interest rate compounded monthly (in%) for the first 6 years: ")) / (100 *12)

# below now discount the cash flow back to present day
presentV_time1_time0 = presentV_time1/((1+int_time1_time0)**n_time1_time0)

# below now we calculate the initial annuity present value
presentV_time0 = pmt_annuity*((1-((1+int_time1_time0)**(-n_time1_time0)))/int_time1_time0)

# below now sum the two cash flows to get the full present value (PV)
PV = presentV_time0 + presentV_time1_time0
print(f'The present value of the annuity is ${round(PV,2)}')


# In[23]:


# DCF Question 9

# first we need to define the rate as the interest rate 
# (this is given in APR so we need to divide the apr by 12 for the interest rate in monthly terms)
apr = float(input("Please enter the annual percent rate: "))  / 100

interest_rate = apr/12

# then we define the present value
presentV = float(input("Please enter the Present Value of the car from Muscle Motors: $ "))  

# then we define the time elapased for the annuity
time = int(input("Enter period of time (in months): ")) 

# The formula for ACF will be PV = ACF ( 1 - ( 1 / ( 1 + rate )^t ) ) / rate
# Use the above formula to solve for ACF to define your formula

# below MCF is for monthly cash flow which is also the same as your monthly payments in this problem
MCF = round((presentV * interest_rate / ( 1 - ( 1 / ( 1 + interest_rate )**time))) , 2)

print(f"The monthly payment for the car is: $ {MCF}" )


# In[27]:


# DCF Question 10

# First import the library needed for calculation
import math

# here present value is the one year loan amount you are looking at
presentV = int(input("Please enter the one year loan amount of interest: $"))

# below now we need to substract the upfront payment of 3 points 
# in order to calculate the net payable amount

presentV_net = presentV*(1-.03) # 3 points which is 3 percent you pay up front

# now we define the interest quoted to us
int_rate = float(input("Please enter the interest rate quoted (in%): ")) / 100

# now below we need to compute the interest payment on the loan at given 10%

int_payment = int_rate * presentV

# below now we compute the interest rate on the net outstanding loan

net_int = int_payment/presentV_net

# now we print the output of the actual interest rate being paid
print(f'The actual interest rate that is being paid {round(net_int*100,2)}%')

