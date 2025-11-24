import string_utils as su
import equation_utils as eu


def balance_reaction(reaction):
    # 1. ניתוח התגובה (Parsing)
    reactants, products = su.parse_chemical_reaction(reaction)
    reactant_atoms = su.count_atoms_in_reaction(reactants)
    product_atoms = su.count_atoms_in_reaction(products)

    # 2. בניית משוואה ופתרון (Building and Solving)
    # eu.build_equations מחזיר את כל המשוואות ואת הסמלים שצריך לפתור
    equations, coefficients_symbols = eu.build_equations(reactant_atoms, product_atoms)
    
    # eu.my_solve פותר את המערכת. מוסיפים [1] עבור המקדם האחרון
    unsimplified_coefficients = eu.my_solve(equations, coefficients_symbols) + [1]
    
    # 3. פישוט המקדמים למספרים שלמים (השלמה חיונית)
    # eu.simplify_coefficients אמורה להמיר את השברים למספרים שלמים
    final_coefficients = eu.simplify_coefficients(unsimplified_coefficients)

    # 4. עיצוב הפלט הסופי כמחרוזת (השלמה חיונית)
    # eu.format_balanced_reaction מחברת את המקדמים השלמים עם המולקולות
    balanced_equation = eu.format_balanced_reaction(reactants, products, final_coefficients)
    
    # מחזירים את המשוואה המאוזנת כמחרוזת
    return balanced_equation
