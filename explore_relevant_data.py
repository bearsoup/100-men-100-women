# -*- coding: utf-8 -*-
"""
Generates basic tables from okc_relevant_data_genbin.csv.
"""
import agate

# create agate table from gender-binary csv data
okc_table = agate.Table.from_csv('okc_relevant_data_genbin.csv')

# group by gender, returns TableSet
by_gender = okc_table.group_by('gender', 'Gender')
# count aggregate by_gender, returns table
by_gender_count = by_gender.aggregate([('Count', agate.Count())])
# compute by_gender percentages
by_gender_count_percent = by_gender_count.compute([
    ('%', agate.Percent('Count'))
])
by_gender_count_percent.print_table()
"""
| Gender |  Count |       % |
| ------ | ------ | ------- |
| Woman  |  9,235 | 31.972… |
| Man    | 19,650 | 68.028… |
"""

# group by orientation, returns TableSet
by_orientation = okc_table.group_by('orientation', 'Orientation')
# count aggregate by_orientation, returns table
by_orientation_count = by_orientation.aggregate([('Count', agate.Count())])
# compute by_orientation percentages
by_orientation_count_percent = by_orientation_count.compute([
    ('%', agate.Percent('Count'))
])
by_orientation_count_percent.print_table()
"""
| Orientation |  Count |       % |
| ----------- | ------ | ------- |
| Straight    | 24,603 | 85.176… |
| Bisexual    |  2,508 |  8.683… |
| Gay         |  1,774 |  6.142… |
"""

# group by gender_orientation, returns TableSet
by_gender_orientation = okc_table.group_by(
    'gender_orientation', 'Gender_orientation'
)
# count aggregate by_gender_orientation, returns table
by_gender_orientation_count = by_gender_orientation.aggregate([
    ('Count', agate.Count())
])
# compute by_gender_orientation percentages
by_gender_orientation_count_percent = by_gender_orientation_count.compute([
    ('%', agate.Percent('Count'))
])
by_gender_orientation_count_percent.print_table()
"""
| Gender_orientation |  Count |       % |
| ------------------ | ------ | ------- |
| Hetero_female      |  6,993 | 24.210… |
| Hetero_male        | 17,610 | 60.966… |
| Bisexual_female    |  1,876 |  6.495… |
| Gay_female         |    366 |  1.267… |
| Gay_male           |  1,408 |  4.875… |
| Bisexual_male      |    632 |  2.188… |
"""

# create TableSet grouped by man_with_100, woman_with_100 columns
by_100_tableset = okc_table.group_by(
    lambda row: (row['man_with_100'], row['woman_with_100']),
    'Man Bad, Woman Bad'
)

# aggregate by_100 TableSet by gender
with_100_by_gender = by_100_tableset.aggregate([
    ('Total', agate.Count()),
    ('Man', agate.Count('gender', 'Man')),
    ('Woman', agate.Count('gender', 'Woman')),
])
with_100_by_gender.print_table()
"""
| Man Bad, Woman Bad |  Total |    Man | Woman |
| ------------------ | ------ | ------ | ----- |
| (False, False)     | 24,575 | 16,653 | 7,922 |
| (True, True)       |  2,925 |  1,959 |   966 |
| (False, True)      |    950 |    713 |   237 |
| (True, False)      |    435 |    325 |   110 |
"""
# compute with_100_by_gender percentages
with_100_by_gender_percent = with_100_by_gender.compute([
    ('Total %', agate.Percent('Total')),
    ('Man %', agate.Percent('Man')),
    ('Woman %', agate.Percent('Woman')),
])
with_100_by_gender_percent.select([
    'Man Bad, Woman Bad', 'Total %', 'Man %', 'Woman %'
]).print_table(max_columns=None)
"""
| Man Bad, Woman Bad | Total % |   Man % | Woman % |
| ------------------ | ------- | ------- | ------- |
| (False, False)     | 85.079… | 84.748… | 85.782… |
| (True, True)       | 10.126… |  9.969… | 10.460… |
| (False, True)      |  3.289… |  3.628… |  2.566… |
| (True, False)      |  1.506… |  1.654… |  1.191… |
"""

# aggregate by_100 TableSet by orientation
with_100_by_orientation = by_100_tableset.aggregate([
    ('Total', agate.Count()),
    ('Gay', agate.Count('orientation', 'Gay')),
    ('Bisexual', agate.Count('orientation', 'Bisexual')),
    ('Hetero', agate.Count('orientation', 'Straight')),
])
with_100_by_orientation.print_table()
"""
| Man Bad, Woman Bad |  Total |   Gay | Bisexual | Hetero |
| ------------------ | ------ | ----- | -------- | ------ |
| (False, False)     | 24,575 | 1,623 |    2,378 | 20,574 |
| (True, True)       |  2,925 |    88 |       78 |  2,759 |
| (False, True)      |    950 |    46 |       37 |    867 |
| (True, False)      |    435 |    17 |       15 |    403 |
"""

with_100_by_orientation_percent = with_100_by_orientation.compute([
     ('Total %', agate.Percent('Total')),
     ('Gay %', agate.Percent('Gay')),
     ('Bisexual %', agate.Percent('Bisexual')),
     ('Hetero %', agate.Percent('Hetero')),
])
with_100_by_orientation_percent.print_table(max_columns=None)
"""
| Man Bad, Woman Bad |  Total |   Gay | Bisexual | Hetero | Total % |   Gay % | Bisexual % | Hetero % |
| ------------------ | ------ | ----- | -------- | ------ | ------- | ------- | ---------- | -------- |
| (False, False)     | 24,575 | 1,623 |    2,378 | 20,574 | 85.079… | 91.488… |    94.817… |  83.624… |
| (True, True)       |  2,925 |    88 |       78 |  2,759 | 10.126… |  4.961… |     3.110… |  11.214… |
| (False, True)      |    950 |    46 |       37 |    867 |  3.289… |  2.593… |     1.475… |   3.524… |
| (True, False)      |    435 |    17 |       15 |    403 |  1.506… |  0.958… |     0.598… |   1.638… |
"""

# aggregate by_100 TableSet by gender_orientation
with_100_by_gender_orientation = by_100_tableset.aggregate([
    ('Total', agate.Count()),
    ('Gay Man', agate.Count('gender_orientation', 'Gay_male')),
    ('Bisexual Man', agate.Count('gender_orientation', 'Bisexual_male')),
    ('Hetero Man', agate.Count('gender_orientation', 'Hetero_male')),
    ('Gay Woman', agate.Count('gender_orientation', 'Gay_female')),
    ('Bisexual Woman', agate.Count('gender_orientation', 'Bisexual_female')),
    ('Hetero Woman', agate.Count('gender_orientation', 'Hetero_female')),
])
with_100_by_gender_orientation.print_table(max_columns=None)
"""
| Man Bad, Woman Bad |  Total | Gay Man | Bisexual Man | Hetero Man | Gay Woman | Bisexual Woman | Hetero Woman |
| ------------------ | ------ | ------- | ------------ | ---------- | --------- | -------------- | ------------ |
| (False, False)     | 24,575 |   1,292 |          593 |     14,768 |       331 |          1,785 |        5,806 |
| (True, True)       |  2,925 |      71 |           21 |      1,867 |        17 |             57 |          892 |
| (False, True)      |    950 |      32 |           12 |        669 |        14 |             25 |          198 |
| (True, False)      |    435 |      13 |            6 |        306 |         4 |              9 |           97 |
"""
# compute with_100_by_gender_orientation percentages
with_100_by_gender_orientation_percent = with_100_by_gender_orientation.compute([
    ('Total %', agate.Percent('Total')),
    ('Gay Man %', agate.Percent('Gay Man')),
    ('Bisexual Man %', agate.Percent('Bisexual Man')),
    ('Hetero Man %', agate.Percent('Hetero Man')),
    ('Gay Woman %', agate.Percent('Gay Woman')),
    ('Bisexual Woman %', agate.Percent('Bisexual Woman')),
    ('Hetero Woman %', agate.Percent('Hetero Woman')),
])
with_100_by_gender_orientation_percent.select([
    'Man Bad, Woman Bad',
    'Total %',
    'Gay Man %',
    'Bisexual Man %',
    'Hetero Man %',
    'Gay Woman %',
    'Bisexual Woman %',
    'Hetero Woman %',
]).print_table(max_columns=None)
"""
| Man Bad, Woman Bad | Total % | Gay Man % | Bisexual Man % | Hetero Man % | Gay Woman % | Bisexual Woman % | Hetero Woman % |
| ------------------ | ------- | --------- | -------------- | ------------ | ----------- | ---------------- | -------------- |
| (False, False)     | 85.079… |   91.761… |        93.829… |      83.861… |     90.437… |          95.149… |        83.026… |
| (True, True)       | 10.126… |    5.043… |         3.323… |      10.602… |      4.645… |           3.038… |        12.756… |
| (False, True)      |  3.289… |    2.273… |         1.899… |       3.799… |      3.825… |           1.333… |         2.831… |
| (True, False)      |  1.506… |    0.923… |         0.949… |       1.738… |      1.093… |           0.480… |         1.387… |
"""

# PERCENTAGE PIVOTS
# percentage
okc_table.pivot(['man_with_100', 'woman_with_100'], computation=agate.Percent('Count')).print_table()
"""
| man_with_100 | woman_with_100 | Percent |
| ------------ | -------------- | ------- |
|        False |          False | 85.079… |
|        False |           True |  3.289… |
|         True |           True | 10.126… |
|         True |          False |  1.506… |
"""
# percentage by gender
okc_table.pivot(
    ['man_with_100', 'woman_with_100'],
    'gender',
    aggregation=agate.Count('gender'),
    computation=agate.Percent('Count')
    ).print_table()
"""
| man_with_100 | woman_with_100 |   Woman |     Man |
| ------------ | -------------- | ------- | ------- |
|        False |          False | 27.426… | 57.653… |
|        False |           True |  0.820… |  2.468… |
|         True |           True |  3.344… |  6.782… |
|         True |          False |  0.381… |  1.125… |
"""
okc_table.pivot(
    ['man_with_100', 'woman_with_100'],
    'gender_orientation',
    aggregation=agate.Count('gender_orientation'),
    computation=agate.Percent('Count')
     ).print_table(max_columns=None)
"""
| man_with_100 | woman_with_100 | Hetero_female | Hetero_male | Bisexual_female | Gay_female | Gay_male | Bisexual_male |
| ------------ | -------------- | ------------- | ----------- | --------------- | ---------- | -------- | ------------- |
|        False |          False |       20.100… |     51.127… |          6.180… |     1.146… |   4.473… |        2.053… |
|        False |           True |        0.685… |      2.316… |          0.087… |     0.048… |   0.111… |        0.042… |
|         True |           True |        3.088… |      6.464… |          0.197… |     0.059… |   0.246… |        0.073… |
|         True |          False |        0.336… |      1.059… |          0.031… |     0.014… |   0.045… |        0.021… |
"""
