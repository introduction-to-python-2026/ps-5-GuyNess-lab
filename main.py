import string_utils as su
import equation_utils as eu

def balance_reaction(reaction):
    """
    Balances a chemical reaction equation using linear algebra.
    Example: 'Fe2O3 + H2 -> Fe + H2O'
    """
    # 1. ניתוח התגובה
    reactants, products = su.parse_chemical_reaction(reaction)
    reactant_atoms = su.count_atoms_in_reaction(reactants)
    product_atoms = su.count_atoms_in_reaction(products)

    # 2. בניית ופתרון המערכת
    equations, coefficients_symbols = eu.build_equations(reactant_atoms, product_atoms)
    
    # 3. מציאת מקדמים (הוספת [1] למקדם האחרון)
    # eu.my_solve אמור להחזיר רשימת פתרונות (שברים/עשרוניים)
    unsimplified_coefficients = eu.my_solve(equations, coefficients_symbols) + [1]
    
    # 4. פישוט המקדמים למספרים שלמים
    # eu.simplify_coefficients אמור להמיר את השברים למספרים שלמים
    final_coefficients = eu.simplify_coefficients(unsimplified_coefficients)

    # 5. עיצוב הפלט הסופי כמחרוזת
    # eu.format_balanced_reaction אמור לחבר את המקדמים והמולקולות
    balanced_equation = eu.format_balanced_reaction(reactants, products, final_coefficients)
    
    return balanced_equation

# קוד הרצה מקומי לבדיקה (אם צריך)
def main():
    reaction = "Fe2O3 + H2 -> Fe + H2O"
    balanced_eq = balance_reaction(reaction)
    print(balanced_eq)

if __name__ == "__main__":
    main()
