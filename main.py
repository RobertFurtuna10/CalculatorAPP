from calculators.calculator_simplu import Calculator

def main():
    valoare_initiala = 0

    valoare_initiala_input = input("Introduceți valoarea inițială sau apăsați Enter pentru valoarea implicită (0): ")
    if valoare_initiala_input:
        valoare_initiala = float(valoare_initiala_input)

    calc = Calculator(valoare_initiala)
    calc.start()

if __name__ == "__main__":
    main()