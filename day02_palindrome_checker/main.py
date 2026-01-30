def main():
    print("Enter a word and I will check if it is a palindrome!")

    word = input().lower()

    is_palindrome = check_palindrome(word)

    if is_palindrome:
        print("Your word is a palindrome")
    else:
         print("No palindrome")

def check_palindrome(word: str) -> bool:
    i = 0
    j = len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1

    return True

if __name__ == "__main__":
    main()