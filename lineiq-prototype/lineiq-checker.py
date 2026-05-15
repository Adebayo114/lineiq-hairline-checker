brand = "LineIQ"

print("Welcome to ", brand, "Checker!")
print("Hairline Symmetry Checker")

# Get client name and hairline style
Client_name = input("Please enter your name:")
print("Hello", Client_name, "!")
style = input("Enter Hairline Style (Straight, Receding, Widow's Peak):")

# Get temple measurements from user
left_input = input("Enter left temple number:")
right_input = input("Enter right temple number:")

print("Client", Client_name)
print("style:", style)

# Validate input and calculate difference
if left_input.isdigit() and right_input.isdigit():
    left_temple = int(left_input)
    right_temple = int(right_input)

    difference = abs(left_temple - right_temple)

    if difference == 0:
        print("✅ Hairline looks perfectly balanced!")
    elif left_temple > right_temple:
        print("⬅️ Left side is higher")
        print("👉 Reduce the LEFT side slightly")
        print("⚠️ Adjust carefully to avoid pushback")

    elif right_temple > left_temple:
        print("➡️ Right side is higher")
        print("👉 Reduce the RIGHT side slightly")
        print("⚠️ Adjust carefully to avoid pushback")

else:
    print("❌ Invalid input. Please enter numeric values for temples.")