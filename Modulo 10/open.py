def main():
    try:
        open("/path/mars.jpg")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")

if __name__ == "__main__":
    main()
