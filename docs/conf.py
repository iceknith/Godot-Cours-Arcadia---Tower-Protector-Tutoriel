# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sphinx
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Basic Sphinx Example Project"
copyright = "2022, Read the Docs core team"
author = "Read the Docs core team"


# -- General configuration ---------------------------------------------------
# -- General configuration
sys.path.append(os.path.abspath("_extensions"))
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    'gdscript',
    'godot_descriptions',

]

# For math LaTeX
# mathjax_config = {
#     'tex': {
#         'packages': [
#             {'name': 'color', 'options': 'table'},
#         ],
#     }
# }
latex_elements = {
    'preamble': r'''
        \usepackage{amsmath}
        \usepackage{amssymb}
    ''',
}



intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    # 'https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css',
    'custom.css',
]
html_logo = "img/arcadiadocslogov2scaled3.png"

html_context = {
   "default_mode": "dark"
}

# Theme options
html_theme_options = {
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
    # Hide the documentation version name/number under the logo
    "display_version": False,
}


# # For highlinting GDScript for real bro
sys.path.insert(0, os.path.abspath('_extensions'))
highlight_language = 'gdscript'

from gdscript import GDScriptLexer
from sphinx.highlighting import lexers

lexers['gdscript'] = GDScriptLexer()


# For hiding unfinished pages
# exclude_patterns += [
#     'creation-monde.rst',
#     'creation-tour.rst',
#     'creation-ennemis.rst'
# ]