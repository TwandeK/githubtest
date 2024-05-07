import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_simulations = 10000
discount_rates = np.random.uniform(0.05, 0.10, num_simulations)  # Discount rate range: 5% to 10%
investment_costs = np.random.uniform(100000, 500000, num_simulations)  # Investment cost range: $100,000 to $500,000
profits = np.random.uniform(50000, 200000, num_simulations)  # Profit range: $50,000 to $200,000
years = 5  # Number of years for the project

# Calculate NPV for each simulation
npvs = []
for i in range(num_simulations):
    cash_flows = [-investment_costs[i]]
    print(f'cashflows: {cash_flows}')
    for year in range(1, years + 1):
        cash_flow_year = profits[i] / ((1 + discount_rates[i]) ** year)
        print(f'cash_flow_year: {cash_flow_year}')
        cash_flows.append(cash_flow_year)
        print(f'cash_flows: {cash_flows}')
    npv = np.sum(cash_flows)
    npvs.append(npv)

# Plot histogram of NPVs
plt.hist(npvs, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Net Present Value (NPV)')
plt.ylabel('Frequency')
plt.title('Monte Carlo Analysis of NPV')
plt.grid(True)
plt.show()

# Calculate statistics
mean_npv = np.mean(npvs)
std_npv = np.std(npvs)
min_npv = np.min(npvs)
max_npv = np.max(npvs)

print("Mean NPV: $", mean_npv)
print("Standard Deviation of NPV: $", std_npv)
print("Minimum NPV: $", min_npv)
print("Maximum NPV: $", max_npv)