def create_pattern(n):
    m = 3 * n
    welcome = "welcome"

    # Calculate the center position for 'welcome'
    center_welcome = m // 2 - len(welcome) // 2

    # Create the pattern
    for i in range(n):
        for j in range(m):
            if j == 0 or j == m - 1:
                print("|", end="")
            elif i == n // 2 and j == center_welcome:
                print(welcome, end="")
                j += len(welcome) - 1
            else:
                print("-", end="")
        print()

# Test the function with n = 7
n = 7
create_pattern(n)
