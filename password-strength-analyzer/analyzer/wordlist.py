def generate_wordlist(data):
    base_words = []

    for value in data.values():
        if value and value.strip():
            base_words.append(value.strip())

    wordlist = set()

    for word in base_words:
        wordlist.add(word)
        wordlist.add(word.lower())
        wordlist.add(word.upper())
        wordlist.add(word.capitalize())
        wordlist.add(word[::-1])

        # Common patterns
        wordlist.add(word + "123")
        wordlist.add(word + "!")
        wordlist.add(word + "@")
        wordlist.add(word + "2024")

        # Simple leetspeak
        leet = (
            word.replace("a", "@")
                .replace("e", "3")
                .replace("i", "1")
                .replace("o", "0")
        )
        wordlist.add(leet)

    return sorted(wordlist)
