import matplotlib.pyplot as plt

def simulate_population_growth_for_loop(initial_pop, growth_rate, generations):
    """
    Simulates population growth using a for loop
    """
    population = [initial_pop]
    for _ in range(1, generations + 1):
        new_pop = population[-1] * (1 + growth_rate)
        population.append(new_pop)
    return population

def simulate_population_growth_while_loop(initial_pop, growth_rate, max_pop):
    """
    Simulates population growth using a while loop until reaching max population
    """
    population = [initial_pop]
    while population[-1] < max_pop:
        new_pop = population[-1] * (1 + growth_rate)
        population.append(new_pop)
    return population

def plot_population_growth(pop_data, title, xlabel, ylabel):
    """
    Creates a line plot of population growth over time
    """
    plt.figure(figsize=(10, 6))
    plt.plot(pop_data, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Parameters
initial_population = 100
growth_rate = 0.1  # 10% growth per generation
generations = 20
max_population = 1000

# Simulate using for loop
print("Simulating with for loop (fixed generations)...")
for_loop_pop = simulate_population_growth_for_loop(initial_population, growth_rate, generations)
plot_population_growth(for_loop_pop, 
                      "Exponential Population Growth (For Loop)", 
                      "Generations", 
                      "Population Size")

# Simulate using while loop
print("\nSimulating with while loop (until reaching max population)...")
while_loop_pop = simulate_population_growth_while_loop(initial_population, growth_rate, max_population)
plot_population_growth(while_loop_pop, 
                      "Exponential Population Growth (While Loop)", 
                      "Generations", 
                      "Population Size")

# Print some statistics
print(f"\nFor loop simulation reached {for_loop_pop[-1]:.0f} after {generations} generations")
print(f"While loop simulation reached {max_population} after {len(while_loop_pop)-1} generations")