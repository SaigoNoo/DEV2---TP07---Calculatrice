from math_custom import Fraction
from os import system
from platform import system as os
from rich.console import Console
from rich.panel import Panel


def commande(string: str) -> str:
    return input(f"\n -> {string} > ")


def fract_to_tuple(frac_ent: str) -> tuple:
    """
    Méthode qui convertit une fraction stringifiée en tuple.
    En effet, lors de la déclaration de la fraction dans le main, on recoit des strings, et donc,
    les num et den ne sont pas des integer et aucune operation n'est alors possible.
    C'est donc à ca que sert cette méthode, formater une fraction en tuple tout en changant le type des chiffres en int.
    On en profite aussi pour convertir les entiers comme 5 en fraction (5, 1) pour avoir un format standard.
    """
    if "/" in frac_ent:
        num = int(frac_ent.split("/")[0].strip())
        den = int(frac_ent.split("/")[1].strip())
        return num, den
    else:
        return int(frac_ent.strip()), 1


def clear():
    if os() in ['Darwin', 'Linux']:
        system("clear")
    else:
        system("cls")


if __name__ == "__main__":
    clear()
    first_help = True
    while True:
        if first_help:
            print(
                "+------------------------------------------------------------------------------------+\n"
                "|  Bienvenue dans le mode interactif de la calculette. Tapez !h pour plus d'aide...  |\n"
                "+------------------------------------------------------------------------------------+\n"
            )
            first_help = False
        command = commande(string=f"Entre une commande:")
        if command == "!h" or command == "":
            print("\n+------------------------------------------------------+\n"
                  "|                        Aide                          |\n"
                  "+------------------------------------------------------+\n"
                  "|  !h                ->   Mode aide                    |\n"
                  "|  !q                ->   Quitter le mode calculette   |\n"
                  "|  !c                ->   Faire un calcul simple       |\n"
                  "+------------------------------------------------------+\n"
                  )
            continue
        elif command == "!q":
            print("Merci d'avoir utilisé cette super calculatrice du tonnerre !")
            break
        elif command == "!n":
            print("Hop là, la mémoire à été reset à 0")
        elif command == "!c":
            # Premiere Fraction
            fraction = fract_to_tuple(
                frac_ent=commande(string=f"Entrez votre première fraction")
            )

            fraction_une = Fraction(
                numerateur=fraction[0],
                denominateur=fraction[1]
            )

            # Check de la fraction
            if fraction_une.checker_erreur(is_frac_2=False)["signal"] == 1:
                print(f"Erreur: {fraction_une.checker_erreur(is_frac_2=False)['reason']}")
                continue

            # Seconde Fraction
            fraction = fract_to_tuple(
                frac_ent=commande(string=f"Entrez votre seconde fraction")
            )

            fraction_deux = Fraction(
                numerateur=fraction[0],
                denominateur=fraction[1]
            )

            # Check de la fraction
            if fraction_deux.checker_erreur(is_frac_2=True)["signal"] == 1:
                print(f"Erreur: {fraction_deux.checker_erreur(is_frac_2=True)['reason']}")
                continue

            # Operateur
            operateur = commande(
                string=f"Quelle opération voulez-vous effectuer [+ - * /]"
            ).strip()

            result = 0

            # Faire une opération entre ces 2 fractions
            if operateur == '+':
                result = fraction_une + fraction_deux
                operateur = "Somme"

            elif operateur == '-':
                result = fraction_une - fraction_deux
                operateur = "Soustraction"

            elif operateur == '/':
                result = fraction_une / fraction_deux
                operateur = "Division"

            elif operateur == '*':
                result = fraction_une * fraction_deux
                operateur = "Multiplication"

            print("")
            response = Panel.fit(
                f"Fraction 1: {fraction_une}\n"
                f"Fraction 2: {fraction_deux}\n"
                f"Operateur: {operateur}\n"
                f"Réponse finale: {result.__str__()}",
                title=f"Résultat", width=1000)
            Console(record=True).print(response)

        else:
            print(f"ERREUR: {command} n'est pas une instruction connue...")
