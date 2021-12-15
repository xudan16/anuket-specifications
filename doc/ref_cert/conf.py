project = 'Anuket Reference Conformance'
copyright = '2021, Anuket'
author = 'Anuket'
exclude_patterns = [
    '.tox',
    'build',
    'RC1',
    'RC2',
    'README.rst'
]
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]
html_theme = "sphinx_rtd_theme"
linkcheck_ignore = [
    'http://127.0.0.1',
    'https://www.sdxcentral.com'
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2
