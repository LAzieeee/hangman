def hangman():
    Guess_empty = []
    word = str(input("Enter your word: "))
    word_lower = word.lower()
    for g in range(len(word)):
        Guess_empty.append('_')
    for n in Guess_empty:
        print(n, end="")
    print()
    GuessList = []

    for i in range(len(word_lower) * 2):
        GuessLetterOrWOrd = str(input("Guess the letter or word: ").lower())
        count_letter = GuessList.count(GuessLetterOrWOrd)
        if GuessLetterOrWOrd in GuessList:
            if GuessLetterOrWOrd == '':
                print("Type something")
            else:
                print(f"{GuessLetterOrWOrd} already used")
        
        else:
            if len(GuessLetterOrWOrd) > 1:
                if GuessLetterOrWOrd == word_lower:
                    print("Correct!")
                    break
                else:
                    print("Wrong!")
            else:
                if GuessLetterOrWOrd in word_lower:
                    # print(GuessLetter)
                    for i in range(len(word_lower)):
                        if GuessLetterOrWOrd == word_lower[i]:
                            Guess_empty[i] = GuessLetterOrWOrd
                        else:
                            pass
                    count = Guess_empty.count('_')
                    if count >= 0:
                        for i in Guess_empty:
                            print(i, end="")
                    if count == 0:
                        print()
                        print("This word has solve")
                        break
                    print()
                else:
                    print(f"Not have {GuessLetterOrWOrd} in this word!")
        GuessList.append(GuessLetterOrWOrd)
        print(f"Next time don't type {GuessList} bcuz it already used")
hangman()