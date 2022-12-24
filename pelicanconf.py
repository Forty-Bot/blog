AUTHOR = 'Sean Anderson'
SITENAME = 'pair of pared pears'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

THEME = 'blue-penguin'
THEME_TEMPLATES_OVERRIDES = ('templates',)

PLUGIN_PATHS = ('pelican-plugins',)
PLUGINS = ('asciidoc_reader', 'filetime_from_git')
ASCIIDOC_CMD = 'asciidoctor'

DELETE_OUTPUT_DIRECTORY = True
