# PATTERNS

# Pattern Printing with Python

This repository contains various pattern printing programs written in Python. These functions print different patterns using loops, stars (`*`), numbers, and characters. Each function is designed to take a numerical input and output a unique pattern to the console. Below is a detailed description of each function and the pattern it generates.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Pattern Descriptions](#pattern-descriptions)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pattern-printing.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pattern-printing
   ```

3. Ensure you have Python installed. You can check this by running:
   ```bash
   python --version
   ```

4. Run any of the Python scripts using:
   ```bash
   python script_name.py
   ```

---

## Usage

Each pattern function takes a single integer input (typically representing the number of rows or the size of the pattern) and prints the respective pattern to the console.

To use any function:
1. Import the function into your script or run the function directly by passing the desired number of rows or size.
2. Example:
   ```python
   pattern7(5)
   ```

---

## Pattern Descriptions

### 1. `pattern7(num)`
This function prints a **pyramid of stars** with centered alignment and spaces on each side. The pyramid grows in size as the input number increases.

Example for `num = 5`:
```
         *         
       * * *       
     * * * * *     
   * * * * * * *   
 * * * * * * * * * 
```

### 2. `pattern8(num8)`
Prints an **inverted pyramid of stars** with spaces on each side. The pattern reduces in size as the rows increase.

Example for `num8 = 5`:
```
 * * * * * * * * * 
   * * * * * * *   
     * * * * *     
       * * *       
         *         
```

### 3. `pattern9(num)`
Combines both `pattern7` and `pattern8` to print a **diamond-shaped star pattern**.

Example for `num = 5`:
```
         *         
       * * *       
     * * * * *     
   * * * * * * *   
 * * * * * * * * * 
   * * * * * * *   
     * * * * *     
       * * *       
         *         
```

### 4. `pattern10(num10)`
Prints a **mirrored half-diamond** pattern using stars.

Example for `num10 = 5`:
```
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
```

### 5. `pattern11(num11)`
Prints a **binary number pattern** that alternates between 0 and 1 for each row, starting with a different number on even and odd rows.

Example for `num11 = 5`:
```

0 
1 0 
0 1 0 
1 0 1 0 
```

### 6. `pattern12(num12)`
Prints a **number pyramid pattern** with spaces between the numbers, and mirrors the numbers on both sides.

Example for `num12 = 5`:
```
1       1 
1 2     2 1 
1 2 3   3 2 1 
1 2 3 4 4 3 2 1 
```

### 7. `pattern13(num13)`
Prints **incremental numbers** row by row.

Example for `num13 = 5`:
```
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
```

### 8. `pattern14(num14)`
Prints a **triangle of increasing characters** (A, B, C, ...) row by row.

Example for `num14 = 5`:
```
A 
A B 
A B C 
A B C D 
```

### 9. `pattern15(num15)`
Prints a **triangle of decreasing characters** starting from A.

Example for `num15 = 5`:
```
A B C D 
A B C 
A B 
A 
```

### 10. `pattern16(num16)`
Prints a **triangle of increasing characters** but starts the pattern with ASCII values after 'A'.

Example for `num16 = 5`:
```

A 
B B 
C C C 
D D D D 
```

### 11. `pattern17(num17)`
Prints a **triangle of increasing alphabet characters**, centered with spaces.

Example for `num17 = 5`:
```
        A
       A B
      A B C
     A B C D
    A B C D E
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes. Whether it's adding more patterns, optimizing code, or enhancing documentation, your efforts are appreciated!

1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/yourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/yourFeature`).
5. Open a pull request.

---

Enjoy creating and printing unique patterns! 🎨
