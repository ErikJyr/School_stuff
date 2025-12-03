s = input("Sisesta string: ")
s = s.strip()
n = len(s)
if n < 7 or n % 2 == 0:
    print("String ei vasta tingimustele (peab olema vähemalt 7 märki ja paaritu pikkusega).")
else:
    chars = list(s)
    mid = n // 2
    kolm = ''.join(chars[mid-1:mid+2])
    print("Kolm keskmist sümbolit:", kolm)