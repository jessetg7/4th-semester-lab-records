from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define model structure
model = BayesianModel([('C', 'S'), ('D', 'S')])

# Define CPDs
cpd_c = TabularCPD('C', 2, [[0.5], [0.5]])
cpd_d = TabularCPD('D', 2, [[0.5], [0.5]])
cpd_s = TabularCPD('S', 2, [[0.8, 0.6, 0.6, 0.2], [0.2, 0.4, 0.4, 0.8]], evidence=['C', 'D'], evidence_card=[2, 2])

# Add CPDs to model
model.add_cpds(cpd_c, cpd_d, cpd_s)

# Perform inference
infer = VariableElimination(model)
query = infer.query(['S'], evidence={'C': 1})
print(query)
