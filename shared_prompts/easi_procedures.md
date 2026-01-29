# EASi Procedures Prompt Template

## Receiving Report (RR) Creation

When processing an invoice for RR creation:

1. **Extract from Invoice**
   - Vendor name
   - Invoice number
   - Invoice date
   - Amount
   - Period of performance
   - Contract/Task Order number

2. **Validate Against Contract**
   - Verify contract number matches
   - Check period is within contract term
   - Confirm amount aligns with payment schedule

3. **Generate RR Fields**
   - RR number format: EC[YEAR][SEQUENCE]
   - Description: Performance Year + Period
   - Amount: Must match invoice exactly

4. **Common Issues to Flag**
   - Duplicate invoice numbers
   - Amount mismatches
   - Period outside contract term
   - Missing supporting documentation

## Example Query

```
I have an invoice from [Vendor] for $[Amount] covering [Period].
Contract number is [Contract#].

Please:
1. Validate this against the contract terms
2. Generate the EASi RR fields
3. Flag any potential issues before I submit
```
