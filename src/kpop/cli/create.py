import string

import click

from .. import Population, MultiPopulation

SYMBOL_TABLE = string.ascii_letters


@click.command()
@click.argument('file')
@click.option('--size', '-I', type=int, prompt='size', help='population size')
@click.option('--num-loci', '-J', type=int, prompt='num loci',
              help='number of loci')
@click.option('--clusters', '-K', type=int, default=1,
              help='number of sub populations')
@click.option('--label', '-l', default='random', help='population label')
def create(file, size=100, num_loci=100, clusters=1, id='random'):
    """
    Random synthetic populations.
    """

    pops = []
    for i in range(clusters):
        symbol = SYMBOL_TABLE[i]
        label_x = id if clusters == 1 else '%s-%s' % (id, symbol)
        pop = Population.random(size, num_loci, id=label_x)
        pops.append(pop)

    pop_total = MultiPopulation(pops)
    pop_total.io.save(file, format='auto')
