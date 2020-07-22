#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# probnum documentation build configuration file, created by
# sphinx-quickstart on Fri Nov  2 15:54:04 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath("../../../probnum/src"))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "1.6.1"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinx_automodapi.automodapi",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "nbsphinx",
    "m2r",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Remove possible duplicate methods when using 'automodapi'
# autodoc_default_flags = ['no-members']
numpydoc_show_class_members = True

# Settings for automodapi
automodapi_toctreedirnm = "automod"
automodapi_writereprocessed = False
automodsumm_inherited_members = True

# The suffix(es) of source filenames.
# You can specify multiple suffixes as a list of strings:
source_suffix = [".rst", ".md", ".ipynb"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "probnum"
copyright = str(datetime.utcnow().year)
author = "Jonathan Wenger"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The full version, including alpha/beta/rc tags.
release = "0.0.1"
# The short X.Y version.
version = ".".join(release.split(".")[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = "img/pn_logo_wide.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the
# documentation.
html_theme_options = {"style_nav_header_background": "#fcfcfc"}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "img/favicons/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "img"]


def setup(app):
    app.add_stylesheet("probnum-style.css")  # also can be a full URL
    # app.add_stylesheet("ANOTHER.css")


# Custom sidebar templates, maps document names to template names.
html_sidebars = {}
# html_sidebars = {'modules': ['localtoc.html'],
#                  'automod/**': ['localtoc.html', 'relations.html']}

# Inheritance graphs generated by graphviz
graphviz_output_format = "svg"
inheritance_graph_attrs = dict(size='""')

# -- Jupyter notebooks (nbsphinx) ------------------------------

# Work-around until https://github.com/sphinx-doc/sphinx/issues/4229 is solved:
html_scaled_image_link = False

# Don't add .txt suffix to source files:
html_sourcelink_suffix = ""

# Allow errors in the build process
nbsphinx_allow_errors = True

# Whether to execute notebooks before conversion or not.
# Possible values: 'always', 'never', 'auto' (default).
nbsphinx_execute = "always"

# List of arguments to be passed to the kernel that executes the notebooks:
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",  # e.g. for matplotlib plots
    "--InlineBackend.rc={'figure.dpi': 96}",
]

# Use a different kernel than stored in the notebook metadata
# Install the kernel (in the current virtualenv) via 'ipython kernel install --user --name=probnum_kernel'
nbsphinx_kernel_name = "probnum_kernel"

# Width of input/output prompts (HTML only). Any CSS length can be specified.
# nbsphinx_prompt_width = 1000px


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "probnumdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "probnum.tex", "probnum's Documentation", [author], "manual"),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "probnum", "probnum's Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "probnum",
        "probnum's Documentation",
        author,
        "probnum",
        "Probabilistic Numerics in Python.",
        "Miscellaneous",
    ),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"https://docs.python.org/": None}
