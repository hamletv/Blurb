import os, click
from app import app

@app.cli.group()
def translate():    # parent command, base for sub-commands below
    """Translation and localization commands"""
    pass

@translate.command()
def update():
    """Update all languages"""
    if os.system('pybabel extract -F babel.cfg -k _l -o translated_messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i translated_messages.pot -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('translated_messages.pot')

@translate.command()
def compile():
    """Compile all languages"""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')

@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language"""
    if os.system('pybabel extract -F babel.cfg -k _l -o translated_messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel init -i translated_messages.pot -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('translated_messages.pot')
