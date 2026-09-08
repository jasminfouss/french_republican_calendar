import sys
from datetime import date, timedelta
REPUBLICAN_MONTHS = [
    "Vendémiaire", "Brumaire", "Frimaire",
    "Nivôse", "Pluviôse", "Ventôse",
    "Germinal", "Floréal", "Prairial",
    "Messidor", "Thermidor", "Fructidor",
]
DECADE_DAY_NAMES = [
    "Primidi", "Duodi", "Tridi", "Quartidi", "Quintidi",
    "Sextidi", "Septidi", "Octidi", "Nonidi", "Décadi",
]
SANSCULOTTIDES_NAMES = [
    "Jour de la Vertu", "Jour du Génie", "Jour du Travail",
    "Jour de l'Opinion", "Jour des Récompenses", "Jour de la Révolution",
]
EPOCH = date(1792, 9, 22)
def is_republican_leap_year(year):
    """Return True if the given Republican year has 366 days.
    Uses a simplified 4-year rule: a year is a leap year if
    year % 4 == 3 (so Years III, VII, XI, ... are leap years).
    """
    if year < 1:
        raise ValueError("Republican year must be a positive integer")
    return year % 4 == 3
def validate_date_string(date_str):
    """Parse a 'YYYY-MM-DD' string into a datetime.date object."""
    try:
        year, month, day = (int(part) for part in date_str.strip().split("-"))
        return date(year, month, day)
    except (ValueError, AttributeError):
        raise ValueError("Date must be in YYYY-MM-DD format")
def get_decade_day_name(day_of_month):
    """Return the name of a day within its 10-day 'décade' week."""
    if not 1 <= day_of_month <= 30:
        raise ValueError("day_of_month must be between 1 and 30")
    return DECADE_DAY_NAMES[(day_of_month - 1) % 10]
def gregorian_to_republican(greg_date):
    """Convert a Gregorian date to a Republican date.
    Returns a tuple: (year, month_name, day, day_name)
    """
    if greg_date < EPOCH:
        raise ValueError("Date is before the Republican calendar epoch (1792-09-22)")
    days_elapsed = (greg_date - EPOCH).days
    year = 1
    while True:
        year_length = 366 if is_republican_leap_year(year) else 365
        if days_elapsed < year_length:
            break
        days_elapsed -= year_length
        year += 1
    if days_elapsed >= 360:
        day_index = days_elapsed - 360
        month_name = "Sansculottides"
        day = day_index + 1
        day_name = SANSCULOTTIDES_NAMES[day_index]
    else:
        month_index = days_elapsed // 30
        day = (days_elapsed % 30) + 1
        month_name = REPUBLICAN_MONTHS[month_index]
        day_name = get_decade_day_name(day)
    return year, month_name, day, day_name
def republican_to_gregorian(year, month_name, day):
    """Convert a Republican (year, month_name, day) back to a Gregorian date."""
    if year < 1:
        raise ValueError("year must be >= 1")
    days_before_year = 0
    for y in range(1, year):
        days_before_year += 366 if is_republican_leap_year(y) else 365
    if month_name == "Sansculottides":
        if not 1 <= day <= 6:
            raise ValueError("Sansculottides day must be between 1 and 6")
        days_into_year = 360 + (day - 1)
    else:
        if month_name not in REPUBLICAN_MONTHS:
            raise ValueError(f"Unknown Republican month: {month_name}")
        if not 1 <= day <= 30:
            raise ValueError("day must be between 1 and 30")
        month_index = REPUBLICAN_MONTHS.index(month_name)
        days_into_year = month_index * 30 + (day - 1)

    return EPOCH + timedelta(days=days_before_year + days_into_year)
def main():
    print("=== French Republican Calendar Converter ===")
    print("1) Gregorian -> Republican")
    print("2) Republican -> Gregorian")
    choice = input("Choose an option (1 or 2): ").strip()
    if choice == "1":
        date_str = input("Enter a Gregorian date (YYYY-MM-DD): ")
        try:
            greg_date = validate_date_string(date_str)
            year, month_name, day, day_name = gregorian_to_republican(greg_date)
            print(f"\nRepublican date: {day_name} {day} {month_name}, Year {year}")
        except ValueError as e:
            sys.exit(f"Error: {e}")
    elif choice == "2":
        try:
            year = int(input("Republican year (e.g. 1): "))
            month_name = input(
                f"Republican month ({', '.join(REPUBLICAN_MONTHS)}, or 'Sansculottides'): "
            ).strip()
            day = int(input("Day (1-30, or 1-6 for Sansculottides): "))
            greg_date = republican_to_gregorian(year, month_name, day)
            print(f"\nGregorian date: {greg_date.isoformat()}")
        except ValueError as e:
            sys.exit(f"Error: {e}")
    else:
        sys.exit("Invalid choice. Please run again and choose 1 or 2.")
if __name__ == "__main__":
    main()
