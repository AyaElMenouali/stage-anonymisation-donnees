import pandas as pd
import numpy as np
from faker import Faker
import sklearn
import matplotlib

print("✅ Environnement opérationnel")
print(f"pandas version: {pd.__version__}")
print(f"scikit-learn version: {sklearn.__version__}")

fake = Faker()
print(f"Exemple Faker : {fake.name()}, {fake.email()}")