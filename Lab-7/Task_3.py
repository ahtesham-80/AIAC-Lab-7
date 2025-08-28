# 1. Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# 2. Writing to multiple files
f1 = open("data1.txt", "w")
f2 = open("data2.txt", "w")

f1.write("First file content\n")
f2.write("Second file content\n")

print("Files written successfully")

f1.close()
f2.close()

# 3. Reading from one file and writing processed content to another
# First, create the input file if it doesn't exist
with open("input.txt", "w") as f:
    f.write("hello world\n")
    f.write("python programming\n")
    f.write("file handling\n")

try:
    with open("input.txt", "r") as input_file:
        data = input_file.readlines()
    
    with open("output.txt", "w") as output:
        for line in data:
            output.write(line.upper())
    
    print("Processing done")
except FileNotFoundError:
    print("Input file not found")

# 4. Reading numbers, squaring them, and saving results
# First, create the numbers file if it doesn't exist
with open("numbers.txt", "w") as f:
    f.write("1\n")
    f.write("2\n")
    f.write("3\n")
    f.write("4\n")
    f.write("5\n")

try:
    with open("numbers.txt", "r") as f:
        nums = f.readlines()

    squares = []
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))

    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")

    print("Squares written")
except FileNotFoundError:
    print("Numbers file not found")
