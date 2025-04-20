# decision.py
def decyzja(wiek, dochod):
    if wiek > 25 and dochod > 5000:
        return "Kredyt przyznany"
    else:
        return "Kredyt odrzucony"

if __name__ == "__main__":
    print(decyzja(30, 6000))
