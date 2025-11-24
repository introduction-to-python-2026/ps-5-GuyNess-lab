from string_utils import (
    parse_chemical_reaction,
    count_atoms_in_reaction
)

from equation_utils import (
    build_equations,
    my_solve,
    simplify_coefficients,
    format_balanced_reaction
)

def balance_reaction(reaction):
    reactants, products = parse_chemical_reaction(reaction)
    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    equations, coefficient_symbols = build_equations(reactant_atoms, product_atoms)
    
    unsimplified_coefficients = my_solve(equations, coefficient_symbols) + [1]
    
    final_coefficients = simplify_coefficients(unsimplified_coefficients)

    balanced_equation = format_balanced_reaction(
        reactants, products, final_coefficients
    )
    
    return balanced_equation

def main():
    reaction = "Fe2O3 + H2 -> Fe + H2O"
    balanced_eq = balance_reaction(reaction)
    print(balanced_eq)

if __name__ == "__main__":
    main()
