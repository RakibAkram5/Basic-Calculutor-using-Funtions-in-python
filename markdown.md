# **Basic Python Calculator**
## Step 1 :
###  Define Basic Arithmetic Functions
Each arithmetic operation has its own function<br>
1.Addition: add(a, b) returns the sum of a and b.<br>
2.Subtraction: subtract(a, b) returns the difference of a and b.<br>
3.Multiplication: multiply(a, b) returns the product of a and b.<br>
4.Division: divide(a, b) divides a by b and checks if b is zero to avoid division by zero.<br>
5.Exponentiation: exponent(a, b) raises a to the power of b.<br>
6.Modulus: modulus(a, b) returns the remainder of dividing a by b with error handling for division by zero.<br>
## Step 2 :
## getNumber(prompt)
Prompts the user for input, checks if the input is a valid number using a try-except block, and continues prompting until a valid number is entered.<br>
## Step 3: 
### Main Calculator Function
calculator():
Displays a welcome message.
Presents a menu of operations to the user:
Addition, Subtraction, Multiplication, Division, Exponentiation, Modulus, Exit.<br>
Continuously prompts the user for their choice until they choose to exit.<br>
If the choice is between 1 and 6, the program asks for two numbers (num1 and num2).<br>
Based on the user’s choice, the appropriate arithmetic function is called and the result is printed.<br>
If the user enters an invalid choice, the program informs them and asks again.<br>
## Step 4:
###  Running the Program
if __name__ == "__main__"::<br>
This condition ensures that the calculator() function only runs if the script is executed directly (not imported as a module).<br>
This structure makes it easy for the user to perform multiple calculations in one run of the program, handling errors like invalid input and division/modulus by zero gracefully.<br>





