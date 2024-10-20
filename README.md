
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

### 1. **Pattern 1: Pyramid of Stars**

This function prints a pyramid of stars with centered alignment and spaces on each side. The pyramid grows in size as the input number increases.

Example for `num = 5`:
```
         *         
       * * *       
     * * * * *     
   * * * * * * *   
 * * * * * * * * * 
```

### 2. **Pattern 2: Inverted Pyramid of Stars**

Prints an inverted pyramid of stars with spaces on each side. The pattern reduces in size as the rows increase.

Example for `num8 = 5`:
```
 * * * * * * * * * 
   * * * * * * *   
     * * * * *     
       * * *       
         *         
```

### 3. **Pattern 3: Diamond-Shaped Star Pattern**

Combines both the pyramid and inverted pyramid from Patterns 1 and 2 to print a diamond-shaped star pattern.

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

### 4. **Pattern 4: Mirrored Half-Diamond**

Prints a mirrored half-diamond pattern using stars.

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

### 5. **Pattern 5: Binary Number Pattern**

Prints a binary number pattern that alternates between 0 and 1 for each row, starting with a different number on even and odd rows.

Example for `num11 = 5`:
```
0 
1 0 
0 1 0 
1 0 1 0 
```

### 6. **Pattern 6: Number Pyramid with Mirror**

Prints a number pyramid pattern with spaces between the numbers and mirrors the numbers on both sides.

Example for `num12 = 5`:
```
1       1 
1 2     2 1 
1 2 3   3 2 1 
1 2 3 4 4 3 2 1 
```

### 7. **Pattern 7: Incremental Numbers**

Prints incremental numbers row by row.

Example for `num13 = 5`:
```
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
```

### 8. **Pattern 8: Increasing Characters (A, B, C...)**

Prints a triangle of increasing characters (A, B, C...) row by row.

Example for `num14 = 5`:
```
A 
A B 
A B C 
A B C D 
```

### 9. **Pattern 9: Decreasing Characters**

Prints a triangle of decreasing characters starting from A.

Example for `num15 = 5`:
```
A B C D 
A B C 
A B 
A 
```

### 10. **Pattern 10: Incrementing Characters after 'A'**

Prints a triangle of increasing characters but starts with ASCII values after 'A'.

Example for `num16 = 5`:
```
A 
B B 
C C C 
D D D D 
```

### 11. **Pattern 11: Centered Alphabet Triangle**

Prints a triangle of increasing alphabet characters, centered with spaces.

Example for `num17 = 5`:
```
        A
       A B
      A B C
     A B C D
    A B C D E
```


## License

This project is licensed under the MIT License.

---

Enjoy creating and printing unique patterns! 🎨

