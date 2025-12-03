s = input("Sisesta failinimi (näiteks failinimi.ext): ").strip()
if '.' not in s or s.endswith('.') or (s.startswith('.') and s.count('.') == 1):
    print("Puudub laiend")
else:
    print(s.rsplit('.', 1)[1])

