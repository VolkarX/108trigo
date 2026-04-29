# 108trigo

**⚠️ IMPORTANT : Ceci est un projet Epitech. Il est strictement interdit de le copier, de le réutiliser ou de s'en inspirer pour votre propre rendu sous peine de sanctions pour triche (moulinette anti-cheat).**

## Description

`108trigo` est un programme en Python qui permet de calculer des fonctions trigonométriques et exponentielles sur des matrices carrées. Le programme utilise le développement en séries de Taylor pour approximer le résultat de ces opérations sur les matrices.

Les fonctions supportées sont :
- `EXP` : Exponentielle de la matrice
- `COS` : Cosinus de la matrice
- `SIN` : Sinus de la matrice
- `COSH` : Cosinus hyperbolique de la matrice
- `SINH` : Sinus hyperbolique de la matrice

## Compilation

Le projet utilise un `Makefile` pour générer l'exécutable. 
Pour le compiler, exécutez la commande suivante à la racine du projet :

```bash
make
```

Pour nettoyer les fichiers temporaires et l'exécutable :
```bash
make fclean
```

## Utilisation

```text
USAGE
    ./108trigo fun a0 a1 a2 ...

DESCRIPTION
    fun   fonction à appliquer parmis "EXP", "COS", "SIN", "COSH" et "SINH"
    a0 a1 a2 ...  coefficients de la matrice, donnés ligne par ligne
```

### Remarques importantes :
- Le nombre total de coefficients fournis doit obligatoirement correspondre à la taille d'une **matrice carrée** (ex: 4 coefficients pour 2x2, 9 coefficients pour 3x3, etc.).
- En cas de matrice non carrée, d'argument invalide, ou de fonction non reconnue, le programme s'arrête avec le code d'erreur `84` (norme Epitech).
- Les coefficients de sortie sont affichés avec une précision à deux décimales (ex: `1.00`).

## Exemple 

```bash
$ ./108trigo EXP 1 2 3 4
```
Ce calcul appliquera l'exponentielle de matrice sur la matrice 2x2 :
[ 1  2 ]
[ 3  4 ]