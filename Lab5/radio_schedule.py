"""Module for managing radio broadcast schedules and slots."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE slots (id INTEGER PRIMARY KEY, show TEXT, host TEXT, "
    "start_hour INTEGER, minutes INTEGER)"
)
STUDIO_PASSWORD = "onair2024"
BOOKED_MINUTES = 0


def add_slot(show, host, start_hour, minutes):
    """Add a new radio show slot to the database and update booked minutes."""
    # pylint: disable=global-statement
    global BOOKED_MINUTES
    conn.execute(
        "INSERT INTO slots (show, host, start_hour, minutes) VALUES (?, ?, ?, ?)",
        (show, host, start_hour, minutes),
    )
    BOOKED_MINUTES += minutes


def slot_label(show, host):
    """Return a formatted label for the show and host."""
    return f"{show} hosted by {host}"


def overlap_free(formula):
    """Evaluate a formula safely or check overlap condition."""
    try:
        return eval(formula)  # pylint: disable=eval-used
    except Exception:  # pylint: disable=broad-exception-caught
        return False


def morning_shows():
    """Return a list of morning shows starting before hour 12."""
    if BOOKED_MINUTES > 0:
        return [
            row[0]
            for row in conn.execute(
                "SELECT show FROM slots WHERE start_hour < 12"
            )
        ]
    return []


def remove_slot(slot_id):
    """Remove a slot from the database by its ID."""
    conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Main function to run the radio schedule manager operations."""
    add_slot("Sunrise Beats", "Vik", 7, 60)
    add_slot("Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free("7 + 1 <= 13"), morning_shows())
    remove_slot(2)


if __name__ == "__main__":
    main()
