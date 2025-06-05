import random

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def analyze_number(n):
    print("🔍 Number Analysis:")
    print(f"  🔢 Number: {n}")
    print("  ⚖️ Type:", "Even" if n % 2 == 0 else "Odd")
    print("  🔹 Prime:", "Yes" if is_prime(n) else "No")
    print("  ✅ Whole Number" if isinstance(n, int) and n >= 0 else "  ❌ Not Whole")
    print("  🏅 Perfect Number:", "Yes" if is_perfect(n) else "No")
    print(f"  🧮 Binary: {bin(n)}")
    print(f"  🧮 Octal: {oct(n)}")
    print(f"  🧮 Hex: {hex(n)}")
    print()

def give_hint(secret, guess):
    diff = abs(secret - guess)
    if diff == 0:
        return "🎯 Correct!"
    elif diff <= 3:
        return "🔥 Very hot!"
    elif diff <= 10:
        return "🌡️ Warm"
    elif diff <= 20:
        return "🧊 Cold"
    else:
        return "❄️ Freezing cold"

def play_game():
    print("🎮 Welcome to the Infinite Number Guessing Game!")
    print("Try to guess the secret number, no limits on attempts or range!")
    
    # Let's define a *very* large range:
    low, high = 1, 10**9
    secret = random.randint(low, high)

    attempt = 0
    while True:
        attempt += 1
        while True:
            user_input = input(f"Attempt {attempt}: Enter a number between {low} and {high}: ").strip()
            if not user_input.isdigit():
                print("❌ Please enter a valid number.")
                continue
            guess = int(user_input)
            if guess < low or guess > high:
                print(f"⚠️ Stay within range ({low}–{high})")
                continue
            break

        analyze_number(guess)
        hint = give_hint(secret, guess)
        print(hint)

        if guess == secret:
            print(f"🎉 You guessed it in {attempt} attempt(s)!")
            analyze_number(secret)
            break

if __name__ == "__main__":
    play_game()
