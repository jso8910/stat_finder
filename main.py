import sys
from situational_woba.gen_weights import main as gen_weights
from situational_woba.calc_swOBA import main as calc_swOBA
from table2ascii import table2ascii  # type: ignore


def prep_stats(start_year: int, end_year: int):
    gen_weights(start_year, end_year, False)


def print_stats(pid: str, start_year: int, end_year: int):
    swoba = calc_swOBA(start_year, end_year, False, pid)
    print(table2ascii(
        header=["swOBA"],
        body=[
            [
                f"{round(swoba, 3):.3f}"
            ]
        ]
    )
    )


def main():
    end_year = int(
        input("Enter the latest year you want considered, <= 2021, >= 1915: "))
    start_year = int(
        input(f"Enter the earliest year you want considered, <= {end_year}, >= 1915: "))
    pid = input(
        f"Enter a valid retrosheet player ID of a player who has played between {end_year} and {start_year}: ")
    if end_year < start_year:
        print("The earliest year must be less than or equal to the latest year.")
        sys.exit(1)
    elif start_year < 1915:
        print("The earliest year must be greater than or equal to 1915.")
        sys.exit(1)
    elif end_year > 2021:
        print("The latest year must be less than or equal to 2021.")
        sys.exit(1)
    is_gen_weights = input(
        "Generate weights and do all needed preparations? (Y/n): ")
    if is_gen_weights.lower() == "n":
        pass
    else:
        prep_stats(start_year, end_year)

    print_stats(pid, start_year, end_year)


if __name__ == '__main__':
    main()
