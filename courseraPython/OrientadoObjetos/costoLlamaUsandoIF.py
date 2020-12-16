def call_cost_claculate(call):
    cost = 0
    if call.is_local():
        cost = calculate_local_cost_of(call)
    elif call.is_national():
        cost = calulate_national_cost_of(call)
    elif call.is_international():
        cost = calulate_international_cost_of(call)
    return cost