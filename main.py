def main():
    username = input("What is your name? ")
    greeting = "Welcome {}!".format(username)
    print(greeting)

if __name__ == '__main__':
    main()