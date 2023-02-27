def make_periodic_table():
    # Define a dictionary to store the atomic weights of each element
    periodic_table = {
        'H': 1.008,
        'He': 4.003,
        'Li': 6.941,
        'Be': 9.012,
        'B': 10.81,
        'C': 12.01,
        'N': 14.01,
        'O': 16.00,
        'F': 19.00,
        'Ne': 20.18,
        'Na': 22.99,
        'Mg': 24.31,
        'Al': 26.98,
        'Si': 28.09,
        'P': 30.97,
        'S': 32.06,
        'Cl': 35.45,
        'K': 39.10,
        'Ca': 40.08,
        'Sc': 44.96,
        'Ti': 47.87,
        'V': 50.94,
        'Cr': 52.00,
        'Mn': 54.94,
        'Fe': 55.85,
        'Ni': 58.69,
        'Co': 58.93,
        'Cu': 63.55,
        'Zn': 65.38,
        'Ga': 69.72,
        'Ge': 72.63,
        'As': 74.92,
        'Se': 78.96,
        'Br': 79.90,
        'Kr': 83.80,
        'Rb': 85.47,
        'Sr': 87.62,
        'Y': 88.91,
        'Zr': 91.22,
        'Nb': 92.91,
        'Mo': 95.94,
        'Tc': 98.00,
        'Ru': 101.07,
        'Rh': 102.91,
        'Pd': 106.42,
        'Ag': 107.87,
        'Cd': 112.41,
        'In': 114.82,
        'Sn': 118.71,
        'Sb': 121.76,
        'I': 126.90,
        'Te': 127.60,
        'Xe': 131.29,
        'Cs': 132.91,
        'Ba': 137.33,
        'La': 138.91,
        'Ce': 140.12,
        'Pr': 140.91,
        'Nd': 144.24,
        'Pm': 145.00,
        'Sm': 150.36,
        'Eu': 151.96,
        'Gd': 157.25,
        'Tb': 158.93,
        'Dy': 162.50,
        'Ho': 164.93,
        'Er': 167.26,
        'Tm': 168.93,
        'Yb': 173.05,
        'Lu': 174.97,
        'Hf': 178.49,
        'Ta': 180.95,
        'W': 183.84,
        'Os': 190.23,
        'Ir': 192.22,
        'Pt': 195.08,
        'Au': 196.97,
        'Hg': 200.59,
        'Tl': 204.38,
        'Pb': 207.2,
        'Bi': 208.98,
        'Th': 232.04,
        'Pa': 231.04,
        'U': 238.03,
        'Np': 237.05,
        'Pu': 244.06,
        'Am': 243.06,
        'Cm': 247.07,
        'Bk': 247.07,
        'Cf': 251.08,
        'Es': 252.08,
        'Fm': 257.10,
        'Md': 258.10,
        'No': 259.10,
        'Lr': 262.11,
        'Rf': 267.13,
        'Db': 270.15,
        'Sg': 271.15,
        'Bh': 270.13,
        'Hs': 277.16,
        'Mt': 276.15,
        'Ds': 281.17,
        'Rg': 280.17,
        'Cn': 285.18,
        'Nh': 284.18,
        'Fl': 289.19,
        'Mc': 288.19,
        'Lv': 293.20,
        'Ts': 294.21,
        'Og': 294.21,
}

    return periodic_table

def compute_molar_mass(periodic_table, element_amounts):
# Compute the total molar mass
    total_mass = 0.0
    for element, amount in element_amounts.items():
        if element in periodic_table:
            total_mass += periodic_table[element] * amount
        else:
            print(f"Error: {element} is not a valid element.")
    
            return None
    # Compute the number of moles in the sample
    num_moles = total_mass / sum(element_amounts.values())
    return total_mass, num_moles

def main():
    periodic_table = make_periodic_table()
    # Get input from the user
    element_amounts = {}
    while True:
            element = input("Enter an element symbol (or 'done' to finish): ")
            if element == "done":
                break
    
    amount = float(input(f"Enter the amount of {element}: "))
    element_amounts[element] = amount

# Compute the molar mass and number of moles
    result = compute_molar_mass(periodic_table, element_amounts)
    if result is not None:
        total_mass, num_moles = result
    print(f"The total molar mass is {total_mass:.2f} g/mol.")
    print(f"The number of moles in the sample is {num_moles:.2f} mol.")
main()