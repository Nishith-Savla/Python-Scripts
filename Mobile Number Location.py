from phonenumbers import geocoder, carrier, parse, NumberParseException


def get_location_and_carrier(number):
    try:
        valid_number = parse(number)
    except NumberParseException:
        print("Valid number not found")
        return None, None

    return geocoder.description_for_number(valid_number, "en"), carrier.name_for_number(valid_number, "en")


if __name__ == '__main__':
    number = input(
        "Enter phonenumber to check location(in format +<country-code>XXXXXXXXXX): ")
    location, carrier = get_location_and_carrier(number)

    if location:
        print(f"Region: {location}")
    else:
        print("Region not found.")

    if carrier:
        print(f"Carrier: {carrier}")
    else:
        print("Carrier not found.")
