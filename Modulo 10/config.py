def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as err:
        print("No se pudo encontrar el documento config.txt! ", err)
    except IsADirectoryError:
        print("Se encontro config.txt pero es un directorio, no se pudo leerlo")
    except PermissionError as err:
        print("Se encontro config.txt pero no se pudo leerlo ", err)

    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("No se pudo encontrar el documento config.txt! ", err)
        elif err.errno == 13:
            print("Se encontro config.txt pero es un directorio, no se pudo leerlo")

if __name__ == '__main__':
    main()


def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"All arguments must be of type int, but recieved: {argument}")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after '{days_left}' days")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

try:
    print(water_left(5, 100, 2))
except RuntimeError as err:
    print(err)

water_left("3", "200", None)
