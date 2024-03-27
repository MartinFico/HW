def main():
    file_name = "text.txt"  # Název vašeho souboru
    try:
        with open(file_name, "r", encoding="utf-8") as file:
        original_text = file.read()
        print("Původní text:")
        print(original_text)