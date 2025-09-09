"""Test code for TIL Python programming jupyter notebook Lab 4 - Data Import Export"""
import pytest
import os.path
from testbook import testbook

@pytest.fixture(scope='module')
def tb():
    with testbook('lab4_2025.ipynb', execute=True) as tb:
        yield tb

# Q1
def test_int_read_1_1(tb):
    assert tb.ref('int_read')(os.path.join('data', 'addition.txt')) == [2, 3, 5, 10, 20], 'integers not read correctly'

def test_int_read_1_2(tb):
    assert tb.ref('int_sum')([2, 3, 5, 10, 20]) == 40, 'sum of integers not correct'

def test_int_read_1_3():
    assert os.path.isfile(os.path.join('data', 'addition2.txt')), 'addition2.txt does not exist inside data folder'

def test_int_read_1_4(tb):
    assert tb.ref('int_read')(os.path.join('data', 'addition2.txt')) == [2, 3, 5, 10, 20, 40], 'extra integers not written correctly'

# Q2
def test_pandas_2_1(tb):
    df = tb.ref('df')
    assert df.shape[0] == 584, 'Netflix dataframe does not have the right amount of movies'
    assert df.loc[2, 'Premiere'] == 'December 26, 2019', 'Incorrect data point in dataframe'
    assert abs(df.loc[333, 'IMDB Score'] - 6.5) < 1e-6, 'Incorrect data point in dataframe'
    assert df.loc[579, 'Title'] == 'Taylor Swift: Reputation Stadium Tour', 'Incorrect data point in dataframe'

def test_pandas_2_4(tb):
    movie100 = tb.ref('movie100')
    assert len(movie100) == 2, 'Incorrect number of columns '
    assert movie100['Title'] == 'Game Over, Man!'
    assert movie100['Genre'] == 'Action/Comedy'

def test_pandas_2_5(tb):
    df2 = tb.ref('df2')
    assert abs(df2.loc['Searching for Sheela', 'IMDB Score'] - 4.1) < 1e-6
    assert df2.loc['Whipped', 'Premiere'] == 'September 18, 2020'
    assert df2.loc['All Because of You', 'Language'] == 'Malay'

def test_pandas_2_6(tb):
    assert tb.ref('number_of_movies')(tb.ref('df')) == 584

def test_pandas_2_7(tb):
    assert set(tb.ref('get_columns')(tb.ref('df'))) == {'Premiere', 'Runtime', 'IMDB Score', 'Genre', 'Language', 'Title'}

def test_pandas_2_8(tb):
    assert abs(tb.ref('highest_score')(tb.ref('df')) - 9.0) < 1e-6

def test_pandas_2_9(tb):
    assert tb.ref('best_scoring_movie')(tb.ref('df')) == 'David Attenborough: A Life on Our Planet'

def test_pandas_2_10(tb):
    assert abs(tb.ref('lowest_score')(tb.ref('df')) - 2.5) < 1e-6

def test_pandas_2_11(tb):
    assert tb.ref('worst_scoring_movie')(tb.ref('df')) == 'Enter the Anime'

def test_pandas_2_12(tb):
    df_english = tb.ref('above_average_english')(tb.ref('df'))
    assert df_english.shape[0] == 210
    assert df_english.iloc[2, df_english.columns.get_loc('Premiere')] == 'March 30, 2018'
    assert df_english.iloc[206, df_english.columns.get_loc('Title')] == 'Ben Platt: Live from Radio City Music Hall'

def test_pandas_2_14(tb):
    assert tb.ref('number_of_languages')(tb.ref('df')) == 38

def test_pandas_2_15():
    assert os.path.isfile(os.path.join('data', 'action_movies.csv')), 'action_movies.csv does not exist inside data folder'

def test_pandas_2_16_a(tb):
    genre_count = tb.ref('genre_count')
    df = tb.ref('df')
    assert genre_count(df, 'Aftershow / Interview') == 36
    assert genre_count(df, 'Biographical/Comedy') == 6
    assert genre_count(df, 'Mystery') == 12
    assert genre_count(df, 'Biopic') == 54
    assert genre_count(df, 'Action') == 42
    assert genre_count(df, 'Comedy') == 294

def test_pandas_2_16_b(tb):
    genre_count = tb.ref('genre_score')
    df = tb.ref('df')
    assert abs(genre_count(df, 'Concert Film') - (7.6 + 1.0 / 30.0)) < 1e-6
    assert abs(genre_count(df, 'Animation/Superhero') - 4.9) < 1e-6
    assert abs(genre_count(df, 'Drama-Comedy') - 7.2) < 1e-6
    assert abs(genre_count(df, 'One-man show') - (7.1 + 1.0 / 30.0)) < 1e-6
    assert abs(genre_count(df, 'Science fiction/Drama') - (4.5+ 1.0 / 30.0)) < 1e-6
    assert abs(genre_count(df, 'Christmas comedy') - 6.0) < 1e-6

def test_pandas_2_17(tb):
    assert tb.ref('best_genre')(tb.ref('df')) == 'Animation/Christmas/Comedy/Adventure'