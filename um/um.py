import re



def main():
    print(count(input("Text: ")))


def count(s):
    finds = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(finds)


if __name__ == "__main__":
    main()
