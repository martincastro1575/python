def call_cost_claculate(call):
    cost = 0
    if call.is_local():
        cost = calculate_local_cost_of(call)
    elif call.is_national():
        cost = calulate_national_cost_of(call)
    elif call.is_international():
        cost = calulate_international_cost_of(call)
    return cost

 #Elmininando IF
 #********************************************************************************
 # paso 1: Crear una jerarquía polimórfica con una abstracción por cada condición.
 #********************************************************************************
class ConditionSuperClass(object):
    pass

class ConditionLocal(ConditionSuperClass):
    pass

class ConditionNational(ConditionSuperClass):
    pass

class ConditionInterNational(ConditionSuperClass):
    pass


#**********************************************************************
#paso 2: Usando un mismo nombre de mensaje repartir el cuerpo del if en cada abstracción
#**********************************************************************
class ConditionSuperClass(object):
    def m(self):
        raise NotImplementedError("SubClass Responsability")

class ConditionLocal(ConditionSuperClass):
    def m(self):
        #aqui va el codigo para calculate_local_cost_of

class ConditionNational(ConditionSuperClass):
    def m(self):
        #aqui va el codigo para calculate_national_cost_of

class ConditionInterNational(ConditionSuperClass):
    def m(self):
        #aqui va el codigo para calculate_international_cost_of


#**********************************************************************
#paso 3: Nombrar el mensaje del paso anterior.
#**********************************************************************
class ConditionSuperClass(object):
    def calculate(self):
        raise NotImplementedError("SubClass Responsability")
class ConditionLocal(ConditionSuperClass):
    def calculate(self):
        #aqui va el codigo para calcular el costo local

class ConditionNational(ConditionSuperClass):
    def calculate(self):
        #aqui va el codigo para calcular el costo nacional

class ConditionInterNational(ConditionSuperClass):
    def calculate(self):
        #aqui va el codigo para calcular el costo internacional


#**********************************************************************
#paso 4: Nombrar las abstracciones.
#**********************************************************************
class CallCostCalculator(object):
    def calculate(self):
        raise NotImplementedError("SubClass Responsability")
class LocalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo local

class NationalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo nacional

class InterNationalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo internacional


#**********************************************************************
#paso 5: Reemplazar if por envío de mensaje polimórfico
#**********************************************************************
class CallCostCalculator(object):
    def calculate(self):
        raise NotImplementedError("SubClass Responsability")
class LocalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo local

class NationalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo nacional

class InterNationalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo internacional

cost_calculator.calculate()


#**********************************************************************
#paso 6: Buscar objeto polimórfico si es necesario
#**********************************************************************
class CallCostCalculator(object):

    @classmethod
    def to_handle(klass, call):
        #codigo que busca el CostCallCalulator correspondiente

    def calculate(self):
        raise NotImplementedError("SubClass Responsability")
    
class LocalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo local

class NationalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo nacional

class InterNationalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #aqui va el codigo para calcular el costo internacional

cost_calculator = CallCostCalculator.to_handle(call)
cost_calculator.calculate()