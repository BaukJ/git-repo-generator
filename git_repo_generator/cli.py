
import click
#import Generator from git_repo_generator.generator
from git_repo_generator.generator import Generator

@click.command()
@click.argument("folder")
@click.option("--commits", "-c", default=100, type=int)
def cli(folder, commits=100):
  print("running")
  gen = Generator()
  gen.create(folder)

