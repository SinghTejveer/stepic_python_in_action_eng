import os
import sys

from invoke import task
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
ENV = Environment(loader=FileSystemLoader(os.path.join(PATH, 'templates')))


def render_template(template, context):
    """Render jinja2 template"""
    return ENV.get_template(template).render(context)


@task
def check_venv(ctx):
    # http://stackoverflow.com/a/1883251/2787185
    # Is virtual environment active?
    if not hasattr(sys, 'real_prefix'):
        print('Activate a virtual environment before!')
        sys.exit()


@task(check_venv)
def tests(ctx):
    ctx.run('python -m pytest')


@task(check_venv)
def syntax(ctx):
    ctx.run('python -m pylint solutions tests')


@task
def new(ctx, number):
    filename = 's' + number
    solution_path = os.path.join('solutions', filename + '.py')
    test_path = os.path.join('tests', 'test_' + filename + '.py')

    solution_template = render_template('solution.jinja2', {})
    test_template = render_template('test.jinja2', {'filename': filename})

    if not os.path.isfile(solution_path):
        with open(solution_path, 'w') as solution:
            solution.write(solution_template)
            print('Solution file created')
    if not os.path.isfile(test_path):
        with open(test_path, 'w') as test:
            test.write(test_template)
            print('Test file created')
