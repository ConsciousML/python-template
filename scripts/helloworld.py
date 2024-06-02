"""Dummy script that imports hello from the template_package and runs it"""

from template_package.helloword import helloword


def main() -> None:
    helloword()


if __name__ == "__main__":
    helloword()
