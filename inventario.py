import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


###____BASE DE CONOCIMIENTOS____###
# Definir la estructura de la red bayesiana
model = BayesianNetwork([('EventoEspecial', 'DemandaAlta'), 
                         ('DemandaAlta', 'InventarioBajo'), 
                         ('TiempoEntregaLargo', 'InventarioBajo'),
                         ('InventarioBajo', 'ReponerInventario')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_E = TabularCPD(variable='EventoEspecial', variable_card=2, values=[[0.8], [0.2]])
cpd_D = TabularCPD(variable='DemandaAlta', variable_card=2, 
                   values=[[0.8, 0.3], [0.2, 0.7]], evidence=['EventoEspecial'], evidence_card=[2])
cpd_T = TabularCPD(variable='TiempoEntregaLargo', variable_card=2, values=[[0.5], [0.5]])
cpd_I = TabularCPD(variable='InventarioBajo', variable_card=2, 
                   values=[[0.9, 0.6, 0.4, 0.1], [0.1, 0.4, 0.6, 0.9]], 
                   evidence=['DemandaAlta', 'TiempoEntregaLargo'], evidence_card=[2, 2])
cpd_R = TabularCPD(variable='ReponerInventario', variable_card=2, 
                   values=[[0.95, 0.2], [0.05, 0.8]], evidence=['InventarioBajo'], evidence_card=[2])

# Agregar las CPDs al modelo
model.add_cpds(cpd_E, cpd_D, cpd_T, cpd_I, cpd_R)

# Validar el modelo
model.check_model()

####__MOTOR DE INFERENCIA__####
# Inferencia
infer = VariableElimination(model)

# Función para convertir entrada de usuario a valores binarios DATOS DE ENTRADA
def input_to_binary(input_value):
    if input_value.lower() in ['si', 'yes', 'y', '1']:
        return 1
    else:
        return 0

########___ DATOS DE ENTRADA___#######
# Entrada de usuario
evento_especial = input("¿Hay un evento especial? (Si/No): ")
tiempo_entrega_largo = input("¿El tiempo de entrega es largo? (Si/No): ")

# Convertir entradas a valores binarios DATOS DE ENTRADA
evento_especial_bin = input_to_binary(evento_especial)
tiempo_entrega_largo_bin = input_to_binary(tiempo_entrega_largo)

# Ejemplo de consulta MOTOR DE INFERENCIA
query = infer.query(variables=['ReponerInventario'], 
                    evidence={'EventoEspecial': evento_especial_bin, 'TiempoEntregaLargo': tiempo_entrega_largo_bin})


###____DATOS DE SALIDA____###
# Mostrar resultados con etiquetas claras y formato de tabla
result = query.values
print("+----------------------+--------------------------+")
print("| ReponerInventario    |   phi(ReponerInventario) |")
print("+======================+==========================+")
print(f"| No Reponer           |                   {result[0]:.4f} |")
print("+----------------------+--------------------------+")
print(f"| Sí Reponer           |                   {result[1]:.4f} |")
print("+----------------------+--------------------------+")
