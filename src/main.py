from argparse import ArgumentParser

from dotenv import load_dotenv
from pydantic import BaseModel


class Argments(BaseModel):
    test: str

    @classmethod
    def parse_args(cls: BaseModel) -> BaseModel:
        parser = ArgumentParser()
        for k in cls.schema()["properties"]:
            parser.add_argument(f"-{k[0:1]}", f"--{k}")
        return cls.parse_obj(parser.parse_args().__dict__)


def main(args: Argments) -> None:
    return args


if __name__ == "__main__":
    load_dotenv()
    args = Argments.parse_args()
    main(args)
