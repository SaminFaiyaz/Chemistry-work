import re

# A simplified periodic table with atomic masses
ATOMIC_MASSES = {
    'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81, 'C': 12.011,
    'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180, 'Na': 22.990,
    'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974, 'S': 32.06,
    'Cl': 35.45, 'K': 39.098, 'Ca': 40.078, 'Fe': 55.845, 'Cu': 63.546,
    'Zn': 65.38, 'Ag': 107.87, 'Au': 196.97
}

def calculate_percentage():
    print("=== Molecule Percentage Calculator ===")
    formula = input("Enter a chemical formula (e.g., H2O, C6H12O6): ").strip()
    
    # Regular expression to match Element and Number
    matches = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
    
    if not matches:
        print("Error: Invalid formula structure.")
        return

    total_mass = 0
    elements_in_formula = {}

    # Parse formula and calculate total mass
    for element, count_str in matches:
        if element not in ATOMIC_MASSES:
            print(f"Error: Element '{element}' not found in our database.")
            return
            
        count = int(count_str) if count_str else 1
        elements_in_formula[element] = elements_in_formula.get(element, 0) + count
        total_mass += ATOMIC_MASSES[element] * count

    # Print results
    print(f"\n--- Results for {formula} ---")
    print(f"Total Molecular Mass: {total_mass:.2f} g/mol")
    
    for element, count in elements_in_formula.items():
        element_mass = ATOMIC_MASSES[element] * count
        percentage = (element_mass / total_mass) * 100
        print(f"{element}: {percentage:.2f}%")

if __name__ == "__main__":
    calculate_percentage()
