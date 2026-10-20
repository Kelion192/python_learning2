filename = "sample.txt"

with open (filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = 0

for line in lines:
    word_count += len(line.split())

print(f"Lines: {line_count}")
print(f"Words: {word_count}")