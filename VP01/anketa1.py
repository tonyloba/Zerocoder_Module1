# Function to determine the age category
def run_anketa1() -> None:

    def determine_age_category(age):
        if age < 13:
            return "Kid"
        elif 13 <= age < 60:
            return "Adult"
        else:
            return "Elder"

    # Ask for user's name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Determine the age category
    age_category = determine_age_category(age)

    # Print the response
    print(f"Hello {name}, you are an {age_category}.")


if __name__ == "__main__":
    run_anketa1()
