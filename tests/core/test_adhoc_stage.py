"""Testing basic pipeline stages."""

import pandas as pd

from pdpipe.core import (
    AdHocStage
)


def _test_df():
    return pd.DataFrame(
        data=[[1, 'a'], [2, 'b']],
        index=[1, 2],
        columns=['num', 'char']
    )


def test_adhoc_stage():
    """Testing ad hoc stages."""
    test_stage = AdHocStage(
        op=lambda df: df.drop(['num'], axis=1),
        prec=lambda df: 'num' in df.columns
    )
    df = _test_df()
    res_df = test_stage.apply(df, verbose=True)
    assert 'num' not in res_df.columns
    assert 'char' in res_df.columns


def test_adhoc_stage_no_prec():
    """Testing ad hoc stages."""
    test_stage = AdHocStage(
        op=lambda df: df.drop(['num'], axis=1),
        prec=None
    )
    df = _test_df()
    res_df = test_stage.apply(df, verbose=True)
    assert 'num' not in res_df.columns
    assert 'char' in res_df.columns
