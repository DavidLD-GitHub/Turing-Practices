import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^<iframe.*https?://(?:www\.)?youtube.com/embed/(\w){11}", s, re.IGNORECASE)
    if matches:
        return "https://youtu.be/" + matches.group()[-11:]
    else:
        return None





if __name__ == "__main__":
    main()
