# French Republican Calendar Converter

I built a Python program that translates dates between our familiar Gregorian calendar and the French Republican calendar, a short-lived but fascinating system adopted by revolutionary France in 1793 and used until Napoleon abolished it in 1806. I chose this because it sits at an intersection of history and arithmetic: the calendar wasn't just a relabeling of months, but a full reimagining of how time should be divided, and turning that reimagining into working code forced me to think carefully about edge cases, leap years, and date arithmetic.

The Republican calendar replaced the seven-day week with a ten-day "décade," renamed months after seasonal themes (Vendémiaire, Thermidor, etc.), and gave every month exactly 30 days. Since 12 months of 30 days only add up to 360, the calendar added five extra days at year-end (Sansculottides), each with its own revolutionary name; leap years got a sixth. My program models all of this.

In republican_calendar.py, main() drives a two-option CLI: convert Gregorian to Republican, or Republican to Gregorian. validate_date_string() parses date strings and raises clear errors on invalid input. gregorian_to_republican() measures days since the calendar's epoch (22 September 1792), walks forward year by year, and determines the Republican year, month, day, and day-name. republican_to_gregorian() reverses the process. Small helpers like get_decade_day_name() and is_republican_leap_year() keep the code modular and testable.

test_french_republican_calendar.py contains pytest tests for key functions, checking both known-good conversions (like 9 Thermidor, Year II, the date of the Thermidorian Reaction) and invalid inputs that should raise ValueError. The program uses only Python's standard library; pytest is listed in requirements.txt for testing.

A design note: the real Republican calendar's leap years were tied to the autumn equinox in Paris, requiring astronomical calculations. Instead, I used a simplified rule (year % 4 == 3), which matches the historically documented leap years during the calendar's actual lifespan and is clearly noted in the code as an approximation.

Running python republican_calendar.py lets you convert any date. For example, 14 July 1989 converts to "Quartidi 24 Messidor, Year 197," and converting back from 9 Thermidor, Year II correctly returns "1794-07-27."

This project taught me to break complex problems into testable pieces, and it gave me a new appreciation for how code can illuminate the past. The full code is available at: github.com/jasminfouss/french_republican_calendar
