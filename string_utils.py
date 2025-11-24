def split_before_uppercases(formula):
    """Splits a chemical formula (string) into a list of elements based on uppercase letters."""
    start = 0
    end = 1
    elements_lst = []
    
    if not formula:
        return elements_lst

    while end < len(formula):
        if formula[end].isupper():
            elements_lst.append(formula[start:end])
            start = end
        end+=1
     
    elements_lst.append(formula[start:])
    
    return elements_lst


def split_at_digit(formula):
    """Splits an element string into a tuple of (element name, count)."""
    for char_index, char in enumerate(formula):
        if char.isdigit():
            # חשוב: אם יש ספירה, חותכים משם עד הסוף
            return formula[:char_index], int(formula[char_index:])
    # אם אין ספרות, הספירה היא 1
    return formula, 1


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts. 
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    atoms_count_dict = {}
    
    # שימוש בפונקציות שהוגדרו לעיל
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        
        # עדכון המילון (כפי שנדרש בשלב 2 במשימה)
        atoms_count_dict[atom_name] = atoms_count_dict.get(atom_name, 0) + atom_count    
        
    return atoms_count_dict

# הפונקציות הבאות (parse_chemical_reaction, count_atoms_in_reaction) שייכות בדרך כלל ל-equation_utils.py,
# אך השארתי אותן כאן אם אתה ממקם אותן ב-string_utils.py.
def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists. 
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries. 
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
