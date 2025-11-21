
def split_by_capitals(formula):
    if not formula:
        return []

    split_formula = []
    start = 0

    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end

    # אחרי הלולאה נוסיף את החלק האחרון
    split_formula.append(formula[start:])
    return split_formula


def split_at_number(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]
            numeric_part = int(formula[i:])
            return prefix, numeric_part
    return formula, 1



def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count
    return atom_counts

        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary
