from pylab import *

dates = ['2020-12-01', '2020-12-08', '2020-12-15', '2020-12-22', '2020-12-29', '2021-01-05', '2021-01-12', '2021-01-19',
         '2021-01-26', '2021-02-02', '2021-02-09', '2021-02-16', '2021-02-23', '2021-03-02', '2021-03-09', '2021-03-16',
         '2021-03-23', '2021-03-30']

at_with_buffered_tasks = [['2020-12-01', 42.30665], ['2020-12-08', 45.16666], ['2020-12-15', 41.423405],
                          ['2020-12-22', 34.99277], ['2020-12-29', 18.098403], ['2021-01-05', 47.978231],
                          ['2021-01-12', 41.598067], ['2021-01-19', 55.100433], ['2021-01-26', 58.777383],
                          ['2021-02-02', 61.753567], ['2021-02-09', 60.342313], ['2021-02-16', 80.655469],
                          ['2021-02-23', 76.150404], ['2021-03-02', 74.389254], ['2021-03-09', 127.656969],
                          ['2021-03-16', 80.564094], ['2021-03-23', 76.982526], ['2021-03-30', 87.439149]]

at_without_buffered_tasks = [['2020-12-01', 21.634806], ['2020-12-08', 21.898225], ['2020-12-15', 19.51179],
                             ['2020-12-22', 21.052308], ['2020-12-29', 17.717837], ['2021-01-05', 36.355558],
                             ['2021-01-12', 26.123271], ['2021-01-19', 29.942992], ['2021-01-26', 33.50326],
                             ['2021-02-02', 40.985001], ['2021-02-09', 40.050647], ['2021-02-16', 53.167766],
                             ['2021-02-23', 41.699482], ['2021-03-02', 39.963586], ['2021-03-09', 88.004514],
                             ['2021-03-16', 47.314697], ['2021-03-23', 47.685715], ['2021-03-30', 53.402134]]

x1 = [dates.index(a[0]) for a in at_without_buffered_tasks]
y1 = [a[1] for a in at_without_buffered_tasks]

x2 = [dates.index(a[0]) for a in at_with_buffered_tasks]
y2 = [a[1] for a in at_with_buffered_tasks]

pos = arange(len(dates))
xticks(pos, dates, rotation=45)

plot(x1, y1)
# plot(x2, y2)
show()
