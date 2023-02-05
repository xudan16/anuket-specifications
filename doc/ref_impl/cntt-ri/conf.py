project = 'Anuket Reference Implementation based on RA1 specifications (RI1)'
html_title = "Anuket Reference Implementation based on RA1 specifications (RI1)"
copyright = '2021, Anuket. Licensed under CC BY 4.0'
author = 'Anuket Project of Linux Foundation Networking'
exclude_patterns = [
    '.tox',
    'README.rst'
]
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]
linkcheck_ignore = [
    'http://127.0.0.1',
    'https://trex-tgn.cisco.com'
]
intersphinx_mapping = {
    'cntt': ('https://cntt.readthedocs.io/en/latest/', None),
    'ref_model': ('https://cntt.readthedocs.io/projects/rm/en/latest/', None),
    'ref_arch_openstack': ('https://cntt.readthedocs.io/projects/ra1/en/latest/', None)
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
numfig = True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Listing %s', 'section': 'Section %s'}
html_static_path = ['_static']
templates_path = ['_templates']
html_css_files = [
    'custom.css',
]

html_show_sourcelink = False
html_theme_options = {
    'nav_title': '',
     # Set the color and the accent color
    'color_primary': 'blue-grey,',
    'color_accent': 'white',
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 0,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
    'base_url': "https://docs.anuket.io/",
    'repo_url': 'https://gerrit.opnfv.org/',
    'repo_name': '',
    'repo_type': 'github',
}

# Inverse png
html_logo = '_static/anuket-logo.png'
html_favicon = '_static/favicon.ico'
