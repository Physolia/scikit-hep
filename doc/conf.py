# -*- coding: utf-8 -*-

# Add the directory above this one, containing the skhep module, to the Python PATH variable.
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'nbsphinx',
]

# generate autosummary even if no references
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Scikit-HEP'
copyright = u'2016-2019, The Scikit-HEP Administrators'
author = u'The Scikit-HEP Administrators'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import skhep
version = skhep.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'templates', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_sidebars = {
    '**': [
        #'about.html',
        'navigation.html',
        'relations.html',
        #'searchbox.html',
        'donate.html',
    ]
}
html_theme_options = {
    #'github_user': 'scikit-hep',
    #'github_repo': 'scikit-hep',
    #'github_type': 'star',
    #'github_banner': True,
    'logo': 'images/logo.svg',
    #'fixed_sidebar': True,
    'show_powered_by': False,
    'link': '#7092C0',
    'font_family': 'Source Sans Pro',
    'head_font_family': 'Source Serif Pro',
    'code_font_family': 'Consolas',
    'code_font_size': '0.8em'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = 'Scikit-HEP'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Scikit-HEP'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/logo.svg'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Scikit-HEPdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Scikit-HEP.tex', u'Scikit-HEP Documentation',
     u'The Scikit-HEP Administrators', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Scikit-HEP', u'Scikit-HEP Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Scikit-HEP', u'Scikit-HEP Documentation',
     author, 'Scikit-HEP', 'One line description of project.',
     'Miscellaneous'),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'https://docs.python.org/': None
}
