class Fraction:
    def __init__(self, numerateur: int, denominateur: int):
        self.total = 0
        self.numerateur = numerateur
        self.denominateur = denominateur

    def __add__(self, frac2: object) -> object:
        """
        Effectue un somme de 2 objets (fractions).
        Une fois fini, on simplifie le résultat si simplifiable.
        Si les 2 denominateurs sont communs, on pourra conserver le même dénominateur au final

        __PRE__:
        - self.num1 doit être de type integer, initialisée ou non None
        - self.den1 doit être de type integer, initialisée ou non None
        - self.num2 doit être de type integer, initialisée ou non None provenant d'un objet
        - self.den2 doit être de type integer, initialisée ou non None provenant d'un objet

        __POST__:
        - self.numerateur ne sera pas réécrit et conservera sa valeur initiale
        - self.denominateur ne sera pas réécrit et conservera sa valeur initiale
        - frac 2 ne sera pas alteré
        - Un objet Fraction sera retourné
        """
        num1, num2 = self.numerateur, frac2.numerateur
        den1, den2 = self.denominateur, frac2.denominateur
        if den1 == den2:
            num = num1 + num2
            den = den1
        else:
            num = (num1 * den2) + (num2 * den1)
            den = den1 * den2

        return Fraction(
            numerateur=num,
            denominateur=den
        ).simplifier_values()

    def __sub__(self, frac2: object) -> object:
        """
        Effectue un soustraction de 2 objets (fractions).
        Une fois fini, on simplifie le résultat si simplifiable.
        Si les 2 denominateurs sont communs, on pourra conserver le même dénominateur au final

        __PRE__:
        - self.num1 doit être de type integer, initialisée ou non None
        - self.den1 doit être de type integer, initialisée ou non None
        - self.num2 doit être de type integer, initialisée ou non None provenant d'un objet
        - self.den2 doit être de type integer, initialisée ou non None provenant d'un objet

        __POST__:
        - self.numerateur ne sera pas réécrit et conservera sa valeur initiale
        - self.denominateur ne sera pas réécrit et conservera sa valeur initiale
        - frac 2 ne sera pas alteré
        - Un objet Fraction sera retourné
        """
        num1, num2 = self.numerateur, frac2.numerateur
        den1, den2 = self.denominateur, frac2.denominateur

        if den1 == den2:
            num = num1 - num2
            den = den1
        else:
            num = (num1 * den2) - (num2 * den1)
            den = den1 * den2

        return Fraction(
            numerateur=num,
            denominateur=den
        ).simplifier_values()

    def __truediv__(self, frac2) -> object:
        """
        Effectue un division de 2 objets (fractions).
        Une fois fini, on simplifie le résultat si simplifiable.

        __PRE__:
        - self.num1 doit être de type integer, initialisée ou non None
        - self.den1 doit être de type integer, initialisée ou non None
        - self.num2 doit être de type integer, initialisée ou non None provenant d'un objet
        - self.den2 doit être de type integer, initialisée ou non None provenant d'un objet

        __POST__:
        - self.numerateur ne sera pas réécrit et conservera sa valeur initiale
        - self.denominateur ne sera pas réécrit et conservera sa valeur initiale
        - frac 2 ne sera pas alteré
        - Un objet Fraction sera retourné
        """
        num1, num2 = self.numerateur, frac2.numerateur
        den1, den2 = self.denominateur, frac2.denominateur
        num = num1 * den2
        den = den1 * num2

        # Retourner un nouvel objet de la classe Fraction avec les valeurs calculées
        return Fraction(num, den).simplifier_values()

    def __mul__(self, frac2) -> object:
        """
        Effectue un multiplication de 2 objets (fractions).
        Une fois fini, on simplifie le résultat si simplifiable.

        __PRE__:
        - self.num1 doit être de type integer, initialisée ou non None
        - self.den1 doit être de type integer, initialisée ou non None
        - self.num2 doit être de type integer, initialisée ou non None provenant d'un objet
        - self.den2 doit être de type integer, initialisée ou non None provenant d'un objet

        __POST__:
        - self.numerateur ne sera pas réécrit et conservera sa valeur initiale
        - self.denominateur ne sera pas réécrit et conservera sa valeur initiale
        - frac 2 ne sera pas alteré
        - Un objet Fraction sera retourné
        """
        num1, num2 = self.numerateur, frac2.numerateur
        den1, den2 = self.denominateur, frac2.denominateur

        num = num1 * num2
        den = den1 * den2

        return Fraction(num, den).simplifier_values()

    def checker_erreur(self) -> dict:
        """
        Méthode de vérification de validité de fractions
        Cette vérification est effectuée à l'initialisation de cet objet

        __PRE:__
        - self.numerateur doit être de type integer, intialisée ou non None
        - self.denominateur doit être de type integer, intialisée ou non None

        __POST:__
        - Aucune valeur n'est modifiée
        - Un dictionnaire non stocké et non permanent est renvoyé
        """
        # Dénominateur à 0
        if self.denominateur == 0:
            return {
                "signal": 1,
                "reason": "DEN_IS_0"
            }

        # Si fraction contient des valeurs qui ne sont pas des chiffres
        if type(self.numerateur) is not int or type(self.denominateur) is not int:
            return {
                "signal": 1,
                "reason": "FRACT_NO_INT"
            }

        # Si tout est OK
        return {
            "signal": 0,
            "reason": "ALL_OK"
        }

    def gcd(self) -> int:
        """
        self.gcd pour grand commun diviseur, fonctionne en complément de la méthode self.simplifier_values.
        La condition pour quitter le while est d'avoir un reste a 0.
        Dès lors que ce reste sera à 0, num et den aura alors son facteur le plus grand

        **Reference**: Théoreme d'Euclide

        __PRE:__
        - self.numerateur doit être de type integer, intialisée ou non None
        - self.denominateur doit être de type integer, intialisée ou non None

        __POST:__
        - Les variables self.denominateur et self.numerateur ne sont pas impactées
        - Seul un integer étant un facteur de division va être résulté, cette valeur n'est pas stockée
        """
        num, den = self.numerateur, self.denominateur
        while den:
            num, den = den, num % den
        return num

    def simplifier_values(self) -> tuple:
        """
        Cette méthode permet de simplifier une fraction à sa plus petite valeur possible.
        Cette méthode est étroitement liée à gcd.

        __PRE:__
        - self.numerateur doit être de type integer, initialisée ou non None
        - self.denominateur doit être de type integer, initialisée ou non None
        - quelque soit la valeur de self.gcd, il y aura ou non simplification

        __POST:__
        - self.numerateur sera réécrit et ne conservera pas sa valeur initiale
        - self.denominateur sera réécrit et ne conservera pas sa valeur initiale
        """
        facteur_commun = self.gcd()
        self.numerateur //= facteur_commun
        self.denominateur //= facteur_commun

        return self.numerateur, self.denominateur

    def __str__(self) -> str:
        """
        Simplement réafficher une fraction simple

        __PRE__:
        - self.numerateur doit être de type integer, initialisée ou non None
        - self.denominateur doit être de type integer, initialisée ou non None

        __POST__:
        - self.numerateur ne sera pas réécrit et conservera sa valeur initiale
        - self.denominateur ne sera pas réécrit et conservera sa valeur initiale
        :return:
        """
        return self.numerateur if self.denominateur == 1 else f"{self.numerateur}/{self.denominateur}"
