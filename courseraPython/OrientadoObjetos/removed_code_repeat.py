def customers_with_name_startswith(letter):
    #selecciona clientes con nombre que empiezan con la letra letter
    selected_customers = []
    for customer in customers:
        if customer.name.startswith(letter):
            selected_customers.append(customer)
    return selected_customers

def overdraw_accounts():
    #selecciona las cuentas que tiene giro al descubierto
    selected_accounts = []
    for account in accounts:
        if account.is_overdraw():
            selected_accounts.append(account)
    return selected_accounts

#Luego de remover el codigo repetido, nos queda el siguiente codigo:
def select(objects, condition):
    #Selecciona los objetos que cumplen una condicion
    selected = []
    for an_object in objects:
        if condition(an_object):
            selected.append(an_object)
    return selected

select(customers, lambda customer: customer.name.startswith(letter))
select(account, lambda account: account.is_overdraw())