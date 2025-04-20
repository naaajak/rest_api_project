# bmi.py
def bmi(waga, wzrost):
    bmi_val = waga / (wzrost ** 2)
    if bmi_val < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi_val < 25:
        return "Waga prawidłowa"
    elif 25 <= bmi_val < 30:
        return "Nadwaga"
    else:
        return "Otyłość"

if __name__ == "__main__":
    print(bmi(70, 1.75))
