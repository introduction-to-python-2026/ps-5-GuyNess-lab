import string_utils as su
import equation_utils as eu

def balance_reaction(reaction):
    # 1. ניתוח התגובה
    # שימוש ב-su כי הייבוא הוא import string_utils as su
    reactants, products = su.parse_chemical_reaction(reaction)
    reactant_atoms = su.count_atoms_in_reaction(reactants)
    product_atoms = su.count_atoms_in_reaction(products)

    # 2. בניית ופתרון המערכת
    # eu.build_equations מחזיר את כל המשוואות ואת הסמלים שצריך לפתור
    equations, coefficients_symbols = eu.build_equations(reactant_atoms, product_atoms)
    
    # eu.my_solve פותר את מערכת המשוואות עבור הסמלים
    # unsimplified_coefficients כולל את כל המקדמים שנפתרו
    unsimplified_coefficients = eu.my_solve(equations, coefficients_symbols)
    
    # הוספת המקדם האחרון שהגדרנו ל-1
    unsimplified_coefficients.append(1) 

    # 3. פישוט המקדמים למספרים שלמים
    final_coefficients = eu.simplify_coefficients(unsimplified_coefficients)

    # 4. עיצוב הפלט הסופי כמחרוזת
    balanced_equation = eu.format_balanced_reaction(reactants, products, final_coefficients)
    
    return balanced_equation

def main():
    reaction = "Fe2O3 + H2 -> Fe + H2O"
    balanced_eq = balance_reaction(reaction)
    print(balanced_eq)

if __name__ == "__main__":
    main()
