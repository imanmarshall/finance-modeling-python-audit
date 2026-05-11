# AI Logic Audit: DCF Terminal Value Calculation

**Task Profile:** Reviewing an AI-generated Python script for a 5-year Discounted Cash Flow (DCF) model for a US-based entity.

### ❌ Error Identified
The AI model used the **Exit Multiple Method** but applied the EBITDA multiple to the **Year 5 EBITDA** without adjusting for the forward-looking year. In professional US Investment Banking standards, the exit multiple should be applied to the **Terminal Year EBITDA** (Next Twelve Months - NTM) to reflect the value at the end of the projection period.

### 🛠 Correction
**Incorrect AI Logic:**
```python
# AI incorrectly applied multiple to the final projection year
terminal_value = year_5_ebitda * ev_ebitda_multiple
