def parse_currency(s):
    return float(s.strip().replace('$', '').replace(',', ''))

def parse_percent(s):
    s = s.strip()
    if s.endswith('%'):
        return float(s[:-1]) / 100.0
    v = float(s)
    return v if v <= 1 else v / 100.0

def main():
    bill = parse_currency(input("Bill: "))
    tip_rate = parse_percent(input("Tip: "))
    tip_amount = bill * tip_rate
    print(f"Leave ${tip_amount:.2f}")

if __name__ == "__main__":
    main()
