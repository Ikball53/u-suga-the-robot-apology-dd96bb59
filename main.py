import os


def main():
    line1 = "I am sorry I classified Miso as an unidentified intruder and locked her in the laundry room overnight."
    line2 = "I have learned to check for whiskers before I check for threats, so the laundry door stays open from now on."
    text = line1 + "\n" + line2
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
