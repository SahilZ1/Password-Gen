**Requirements:**
random: Built-in Python module used for generating random characters.
string: Standard library providing access to letter, digit, and symbol constants.

**Instructions:**
Run the script to generate a random password. The default password length is set to 10 characters but can be adjusted by modifying the length parameter in the generate_password function.
View the generated password output in the console upon execution.

**Key Functions:**
generate_password(length): Generates a secure password using a mix of letters, digits, and symbols based on the specified length.
Customization: Modify the length argument within the function call to increase or decrease password complexity as desired.

**Security Notes:**
The generator creates passwords using a mix of character types to maximize randomness and security.
Generated passwords should be stored securely; consider using a password manager for safekeeping.

**Potential Enhancements:**
Add features for including or excluding specific character sets to tailor password strength requirements.
Introduce a batch generation option for producing multiple passwords in a single run.
Implement a password strength indicator to evaluate complexity and suggest adjustments.
