# ===============================================
## 1. תיקון ופירוט ייבוא 📥
# ===============================================

# ייבוא כל הפונקציות הנדרשות מ-string_utils.py (כפי שנדרש בשלב 3)
from string_utils import (
    parse_chemical_reaction,
    count_atoms_in_reaction
)

# ייבוא כל הפונקציות הנדרשות מ-equation_utils.py
from equation_utils import (
    build_equations,
    my_solve,
    format_balanced_reaction, # פונקציה חסרה שאני מניח שצריך להוסיף או לכתוב
    simplify_coefficients # פונקציה חסרה שאני מניח שצריך להוסיף או לכתוב
)

# ===============================================
## 2. תיקון פונקציית balance_reaction ⚙️
# ===============================================

def balance_reaction(reaction: str) -> str:
    """
    Balances a chemical reaction equation.
    Example: "Fe2O3 + H2 -> Fe + H2O" → "1Fe2O3 + 3H2 → 2Fe + 3H2O"
    """

    # 1. ניתוח התגובה (Parsing)
    reactants, products = parse_chemical_reaction(reaction)
    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    # 2. בניית ופתרון המשוואות (Building and Solving)
    # אני משתמש בשמות הפונקציות שלך, למרות שהן עשויות להיות חסרות:
    equations, coefficient_symbols = build_equations(reactant_atoms, product_atoms)
    
    # הפתרון של sympy מחזיר את n-1 המקדמים הראשונים.
    # מוסיפים את המקדם האחרון (שמוגדר כ-1 לצורך הפתרון המטריציאלי)
    unsimplified_coefficients = my_solve(equations, coefficient_symbols) + [1]
    
    # 3. פישוט המקדמים למספרים שלמים (Simplification)
    # נדרשת פונקציה שתמצא את המכנה המשותף הקטן ביותר (LCM) כדי להפוך את השברים לשלמים.
    # אני מניח שקיימת פונקציה כזו ב-equation_utils:
    final_coefficients = simplify_coefficients(unsimplified_coefficients)

    # 4. עיצוב הפלט הסופי (Formatting)
    # נדרשת פונקציה שתחבר את המקדמים השלמים בחזרה לנוסחה.
    # אני מניח שקיימת פונקציה כזו ב-equation_utils:
    balanced_equation = format_balanced_reaction(
        reactants, products, final_coefficients
    )
    return balanced_equation
    reaction = "Fe2O3 + H2 -> Fe + H2O"
    print(f"Original reaction: {reaction}")
    # balanced_eq = balance_reaction(reaction)
    # print(f"Balanced equation: {balanced_eq}")
    # התוצאה הצפויה: 1Fe2O3 + 3H2 → 2Fe + 3H2O (או 1Fe2O3 + 3H2 -> 2Fe + 3H2O)

# if __name__ == "__main__":
#     main()
