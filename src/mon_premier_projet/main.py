from mon_premier_projet.module1 import hello_module1
from mon_premier_projet.module2 import add
from mon_premier_projet.module2 import sub
from mon_premier_projet.utilitaires.maths import multiply
from mon_premier_projet.utilitaires.texte import to_upper_case, to_lower_case
from mon_premier_projet.utilitaires.convert import convert_to_yens, convert_to_dollars



def main():
    print(hello_module1())
    print("2+3 = ", add(2, 3))
    print("2x3 = ", multiply(2, 3))
    print(to_upper_case("texte majuscule"))
    print(to_lower_case("TEXTE MINUSCULE"))
    print("2-3 = ", sub(2, 3))
    print("3€ = ", convert_to_dollars(3),"$")
    print("3€ = ", convert_to_yens(3),"¥")

if __name__ == "__main__":
    main()