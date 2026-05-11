"""
US Financial Modeling & Valuation Toolkit
Focus: US GAAP Compliance and Investment Banking Standards
"""

def calculate_wacc(equity_val: float, debt_val: float, 
                   cost_of_equity: float, pre_tax_cost_of_debt: float, 
                   tax_rate: float = 0.21) -> float:
    """
    Calculates the Weighted Average Cost of Capital (WACC).
    Default tax_rate reflects the US Federal Corporate Tax rate.
    """
    total_val = equity_val + debt_val
    w_e = equity_val / total_val
    w_d = debt_val / total_val
    
    # After-tax cost of debt logic
    at_cost_of_debt = pre_tax_cost_of_debt * (1 - tax_rate)
    
    wacc = (w_e * cost_of_equity) + (w_d * at_cost_of_debt)
    return wacc

def calculate_ufcf(ebit: float, tax_rate: float, 
                   depreciation: float, capex: float, 
                   change_in_nwc: float) -> float:
    """
    Calculates Unlevered Free Cash Flow (UFCF).
    Formula: EBIT * (1 - T) + D&A - CapEx - ΔNWC
    """
    nopat = ebit * (1 - tax_rate)
    ufcf = nopat + depreciation - capex - change_in_nwc
    return ufcf

if __name__ == "__main__":
    # Example: Valuation for a US mid-cap firm
    print("--- Financial Model Logic Test ---")
    
    # 1. Calculate WACC
    current_wacc = calculate_wacc(
        equity_val=1000000, 
        debt_val=500000, 
        cost_of_equity=0.09, 
        pre_tax_cost_of_debt=0.05
    )
    print(f"Calculated WACC: {current_wacc:.2%}")
    
    # 2. Calculate UFCF
    fcf = calculate_ufcf(500000, 0.21, 50000, 75000, 10000)
    print(f"Calculated Unlevered FCF: ${fcf:,.2f}")
def calculate_roe(net_income: float, average_equity: float) -> float:
    """Calculates Return on Equity (ROE) per US GAAP standards."""
    return net_income / average_equity
