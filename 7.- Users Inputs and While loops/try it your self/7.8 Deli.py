sandwich_orders = ['pastrami', 'jam and cheese', 'tuna', 'capresa']
finished_sandwiches = []

while sandwich_orders:
    sandwich_current = sandwich_orders.pop()
    print(f"\nI made your {sandwich_current} sandwich")

    finished_sandwiches.append(sandwich_current)

print("\n---Order's sandwiches---\n")
for finished_sandwiche in finished_sandwiches:
    print(f"\t{finished_sandwiche} sandwich")

