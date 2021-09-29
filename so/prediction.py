import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import sklearn.metrics as m


def get_train_and_test_for_week(df):
    test_start_day = pd.to_datetime('2021-08-23')
    train_combined = df[df['ds'] < test_start_day]

    test_data = dict()
    test_data['week_' + str(test_start_day.date())] = df[df['ds'] >= test_start_day]

    for i in range(7):
        start_index = test_start_day + pd.offsets.Day(i)
        end_index = test_start_day + pd.offsets.Day(i + 1)
        test_day_i_data = df[(df['ds'] >= start_index) & (df['ds'] < end_index)]
        test_data[str(start_index.date())] = test_day_i_data

    train_data = train_combined[['ds', 's']]
    train_data.columns = ['ds', 'y']
    return train_data, test_data


def predict(data: list):
    train_data, test_data = data[0]
    p = Prophet()
    p.fit(train_data)
    errors = dict()

    for k, t in test_data.items():
        forecast = p.predict(t)
        merged = pd.merge(t, forecast, on='ds', how='inner')
        y = merged['s']
        yhat = merged['yhat']
        yhat[yhat < 0] = 0
        diff = y - yhat
        diff_abs = diff.abs()
        max_abs = merged[['s', 'yhat']].abs().max(axis=1)
        mae = (diff_abs / (1 + max_abs)).mean()
        # mae = np.mean(np.divide(diff_abs, y, out=np.zeros_like(diff_abs), where=y != 0))
        errors[k] = mae

        fig, ax = plt.subplots()
        ax.plot(merged['ds'], merged['s'])
        ax.plot(merged['ds'], merged['yhat'])
        plt.legend(["actual", "forecast"], loc="upper left")
        # plt.ylabel(ylabel)
        # ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        plt.xticks(rotation=45)
        plt.savefig(k + '_10min_max.png', dpi=1000)
        # plt.show()

    print(errors)


if __name__ == '__main__':
    df = pd.read_csv('./supply_demand_minutes_prec_all.csv')

    # set data-type of ds column correctly
    df['ds'] = pd.to_datetime(df['ds'])
    df['ds'] = df['ds'].dt.tz_localize(None)

    # aggregate the data at 5 minutes buckets
    df.set_index('ds', inplace=True)
    df = df.groupby(pd.Grouper(freq='5Min')).agg({'s': 'max', 'd': 'max'}).reset_index()
    df = df.dropna()

    train_data, test_data = get_train_and_test_for_week(df)
    predict([(train_data, test_data)])
