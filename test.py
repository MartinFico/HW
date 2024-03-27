def main():
    file_name = "text.txt"  # Název vašeho souboru
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            original_text = file.read()
            print("Původní text:")
            print(original_text)

            old_word = input("Zadejte slovo, které chcete nahradit: ")
            new_word = input("Zadejte slovo, kterým chcete nahradit: ")

            replaced_text = original_text.replace(old_word, new_word)
            print("\nText s nahrazeným slovem:")
            print(replaced_text)

            if not old_word.isdigit():  # Pokud se nejedná o číslo, spočítáme slova
                word_count = len(replaced_text.split())
                print("\nPočet slov v textu (po nahrazení):", word_count)

    except FileNotFoundError:
        print(f"Soubor {file_name} nebyl nalezen.")


if __name__ == "__main__":
    main()