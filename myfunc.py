import numpy as np

# Function to calculate instantaneous wind turbine capacity
def calculate_wind_turbine_capacity(density, area, wind_speed, cp, efficiency):
    """
    Calculate the Wind Turbine Capacity (P) in MW (instantaneous capacity).
    """
    return 0.5 * density * area * (wind_speed ** 3) * cp * efficiency / 1e6  # Convert W to MW

# Function to calculate Annual Energy Production (AEP)
def calculate_AEP(capacity, capacity_factor):
    """
    Calculate the Annual Energy Production (AEP) in MWh/year.
    """
    hours_per_year = 8760
    return capacity * capacity_factor * hours_per_year

# Function to calculate Total Annual Cost (TAC) in EUR/MWh
def calculate_TAC(CAPEX, OPEX, r, n, capacity):
    """
    Calculate the Total Annual Cost (TAC) in EUR/MWh with discounted OPEX and annualized CAPEX.
    """
    # Capital Recovery Factor (CRF) for CAPEX annualization
    CRF = (r * (1 + r)**n) / ((1 + r)**n - 1)
    
    # Annualized CAPEX in EUR/year per MW capacity
    annualized_CAPEX = CAPEX * CRF
    
    # Discounted OPEX over the project lifetime
    years = np.arange(1, n + 1)
    discount_factors = (1 + r) ** (-years)
    discounted_OPEX = np.sum(OPEX * discount_factors)  # NPV of OPEX per MW capacity
    
    # Total Annual Cost normalized by the turbine capacity
    return (annualized_CAPEX + discounted_OPEX) / capacity

# Function to calculate LCOE
def calculate_LCOE(TAC, AEP):
    """
    Calculate the Levelized Cost of Energy (LCOE) in EUR/MWh.
    """
    return TAC / AEP

def calculate_abc(a,b):
    return a+b 