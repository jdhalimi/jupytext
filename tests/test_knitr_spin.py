import os
import pytest
import jupytext
from .utils import list_notebooks, skip_if_dict_is_not_ordered

jupytext.file_format_version.FILE_FORMAT_VERSION = {}


@skip_if_dict_is_not_ordered
@pytest.mark.parametrize('r_file', list_notebooks('R'))
def test_jupytext_same_as_knitr_spin(r_file, tmpdir):
    nb = jupytext.readf(r_file)
    rmd_jupytext = jupytext.writes(nb, ext='.Rmd')

    # Rmd file generated with spin(hair='R/spin.R', knit=FALSE)
    rmd_file = r_file.replace('R', 'Rmd')

    with open(rmd_file) as fp:
        rmd_spin = fp.read()

    assert rmd_spin == rmd_jupytext
