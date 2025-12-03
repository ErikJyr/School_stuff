tekst = input("Enter text: ") 
def count_vowels(s):
    vowels = set("aeiouõäöü")
    return sum(1 for ch in s if ch in vowels)

if __name__ == "__main__":
    print(count_vowels(tekst))