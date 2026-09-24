# UI reference from the working desktop build

Source of truth reviewed from `app/main_window.py` in the supplied working ZIP.

## Main order

Desktop uses a two-column scrollable layout.

### Left column
1. General Information
2. Customer Information
5. Carrier Costs & Pricing
- WWE + Services Management
- CBCFS + Services Management
- FedEx + UPS
- Uber Freight + Local Delivery
- Plataforma Ganadora

### Right column
3. Product Information
- Product
- SKU
- Record ID
- QTY
- Details (Dimensions)
- Dimensions/Repack
- PRICE X CASE
- Revenue
- INSURED VALUE

4. Cubic volume calculator
- # / # Pallet / # Cases / # Level / Height / Weight / Total Weight / Total CS
- add/remove row
- bulk rows
- reset
- GRAND TOTAL
- Calculada / Verificada
- Pallet configuration
- Bundle
- VERIFIED CONFIGURATION

Then the quote product cart.

### Bottom action bar
Data Base, Save Quote, Update Quote, View quotes, Export, + Note, Add product, Limpiar 3-5, Limpiar Todo.

## Responsive rule

On narrow screens the same order is preserved vertically:

General → Customer → Product → Cubic → Carrier Costs/Services → Winner → Cart → Actions.

The web version should reflow this existing workflow rather than introducing a different navigation model.

## Functional rules to preserve

- Carrier calculations and Local Delivery formulas must remain compatible with the desktop version.
- Customer address resolution remains exact.
- Quote edit/delete must use `quote_instance_id`.
- Rule specificity, carrier restrictions, SOLO LTL, UPS threshold, revenue override and validation warning stay intact.
