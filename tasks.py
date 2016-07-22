import os
import sys

import itertools
from invoke import task
from jinja2 import Environment, FileSystemLoader

from utils.utils import get_files, refactor

PATH = os.path.dirname(os.path.abspath(__file__))
ENV = Environment(loader=FileSystemLoader(os.path.join(PATH, 'templates')))


def render_template(template, context):
    """Render jinja2 template"""
    return ENV.get_template(template).render(context)


@task
def check_venv(ctx):
    # http://stackoverflow.com/a/1883251/2787185
    # Is virtual environment active?
    pyenv = os.environ.get('PYENV_VIRTUAL_ENV', False)
    if not hasattr(sys, 'real_prefix') and not pyenv:
        print('Activate a virtual environment before!')
        sys.exit()


@task(check_venv)
def tests(ctx):
    ctx.run('python -m pytest --doctest-modules')


@task(check_venv)
def syntax(ctx):
    ctx.run('python -m pylint solutions utils tests')


@task
def new(ctx, number):
    filename = 's' + number
    solution_path = os.path.join('solutions', filename + '.py')
    test_path = os.path.join('tests', 'solutions', 'test_' + filename + '.py')

    solution_template = render_template(
        'solution.jinja2', {}) + '\n'
    test_template = render_template(
        'test.jinja2', {'filename': filename}) + '\n'

    if not os.path.isfile(solution_path):
        with open(solution_path, 'w') as solution:
            solution.write(solution_template)
            print('Solution file created')
    if not os.path.isfile(test_path):
        with open(test_path, 'w') as test:
            test.write(test_template)
            print('Test file created')


@task
def rename(ctx):
    proceed = input('Are you sure? (yes/no): ')
    if not proceed.lower() == 'yes':
        print('Aborted...')
        return

    solution_path = os.path.join('solutions')
    test_path = os.path.join('tests', 'solutions')

    print('Reading...')
    solution_files = get_files(solution_path)
    print('   %d solutions' % len(solution_files))
    test_files = get_files(test_path)
    print('   %d tests' % len(test_files))

    print('Refactoring...')
    print('   solutions:', end=' ')
    skipped_solutions = refactor(solution_path, solution_files)
    print('DONE')

    print('   tests:', end=' ')
    skipped_tests = refactor(test_path, test_files)
    print('DONE')

    print('Skipped files...')
    for skipped_file in itertools.chain(skipped_solutions, skipped_tests):
        print('   %s' % skipped_file)
