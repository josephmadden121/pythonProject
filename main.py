# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Joseph Madden
# 09/07/2022
# The purpose of this program is to provide fiber optic cable installation cost by getting details from customers.

# Get Name, Company and Cable Length Required
name = input('Joseph?\n')
print('Hello', name, '! Welcome to the Fiber Optic Cost Calculator!')
company = input('Please tell us your company name')
length = float(input('Please enter how many feet of Fiber Optic Cable you require:'))

# compute the cost of fiber optic cable
unit_cost = 0.87
cost = (length * unit_cost)

# print receipt for customer
print(name, 'Here are your results:\n')

print('*************** Estimate for', name, 'with', company, '***************')
print('Cable Installation Requested (in feet):', length,)
print('Cable Unit Cost: $0.87')
print('Cable Total Cost: $ %.2f' % cost)
print('*************** THANK YOU FOR YOUR BUSINESS!!! ***************')
