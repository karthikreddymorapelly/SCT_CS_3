import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character (!@#$ etc).")

    # Final result
    if strength == 5:
        return "Strong Password ✅"
    elif strength >= 3:
        return "Moderate Password ⚠️\n" + "\n".join(remarks)
    else:
        return "Weak Password ❌\n" + "\n".join(remarks)


# Run program
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print(check_password_strength(pwd))
