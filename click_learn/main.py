import click

# @click.command()
# def main():
#     click.echo("hello click")


@click.command()
@click.option("-n", "--num", help="input a num")
def main(num):
    click.echo(f"{num =}")


# python3 main.py --help
# Usage: main.py [OPTIONS]

# Options:
#   -n, --num TEXT  input a num
#   --help          Show this message and exit.
if __name__ == "__main__":
    main()
