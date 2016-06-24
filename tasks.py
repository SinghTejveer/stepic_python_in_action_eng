import sys

from invoke import task

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
