import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import sklearn.metrics as m

df = pd.read_csv('./supply_demand_minutes_prec_all.csv')
# df = df.reindex(columns=['created_at', 'totalSupply'])
# df.columns = ['ds', 'y']
df['ds'] = pd.to_datetime(df['ds'])
df['ds'] = df['ds'].dt.tz_localize(None)
# print(df.head(n=25))

df.set_index('ds', inplace=True)
df = df.groupby(pd.Grouper(freq='5Min')).agg({'s': 'max', 'd': 'max'}).reset_index()
# print(df.head())
# print(df.dtypes)

train_combined = df[df['ds'] < '2021-08-23']
test_combined = df[df['ds'] >= '2021-08-23']

supply_train = train_combined[['ds', 's']]
supply_train.columns = ['ds', 'y']
demand_train = train_combined[['ds', 'd']]
demand_train.columns = ['ds', 'y']


# print(test_combined.tail(n=20))


def predict(train_data, test_data, ylabel):
    p = Prophet()
    p.fit(train_data)
    future = test_combined[['ds']]
    print(future.describe())
    # future = m.make_future_dataframe(periods=10080, freq='1min', include_history=False)
    forecast = p.predict(future)

    prediction = pd.merge(test_combined, forecast, on='ds', how='inner')
    prediction[prediction['yhat'] < 0] = 0
    prediction = prediction.dropna()

    # modified_x = prediction[['ds']]
    # modified_x = pd.to_datetime(modified_x['ds'])
    # modified_x['ds'] = modified_x['ds'].dt.date
    # modified_x['ds'] = modified_x['ds'].dt.tz_localize(None)

    prediction.to_pickle('supply_prediction')
    print(prediction['ds'])
    print('mean absolute error', m.mean_absolute_error(prediction['s'], prediction['yhat']))
    next_day_prediction = prediction[prediction['ds'] < '2021-08-23']
    np_abs = np.abs(next_day_prediction['s'] - next_day_prediction['yhat'])
    mae = np.mean(np.divide(np_abs, next_day_prediction['s'], out=np.zeros_like(np_abs), where=next_day_prediction['s'] != 0))

    print("self calculate", mae)

    # fig, ax = plt.subplots()
    # ax.plot(prediction['ds'], prediction['s'])
    # ax.plot(prediction, prediction['yhat'])
    # plt.legend(["actual", "forecast"], loc="upper left")
    # plt.ylabel(ylabel)
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    # plt.xticks(rotation=45)
    # plt.show()
    # forecast['yhat'].to_pickle('supply_forecast_pickled')

    # print('mean absolute error', m.mean_absolute_error(test_data, forecast['yhat']))
    # print('mean squared error', m.mean_squared_error(test_data, forecast['yhat']))
    # print('mean absolute percentage error', m.mean_absolute_percentage_error(test_data, forecast['yhat']))

    # plt.savefig('s3.png', dpi=1000)


def plot(x, test_data, prediction, ylabel):
    fig, ax = plt.subplots()
    ax.plot(x, test_data)
    ax.plot(x, prediction)
    plt.legend(["actual", "forecast"], loc="upper left")
    plt.ylabel(ylabel)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.xticks(rotation=45)

    plt.show()


def error():
    print('within error func')
    prediction = pd.read_pickle('supply_prediction')
    # prediction[prediction < 0] = 0

    # test_data = test_data[test_data.isna()]
    # prediction = prediction[test_data.isna()]
    print(np.any(np.isnan(prediction['s'])))
    print(np.any(np.isnan(prediction['yhat'])))
    # test_data = np.nan_to_num(test_data)
    # prediction = np.nan_to_num(prediction)

    # print("self calculate", np.mean(np.abs(test_data-prediction)/test_data))

    # print('mean absolute error', m.mean_absolute_error(prediction['s'], prediction['yhat']))
    # print('mean squared error', m.mean_squared_error(test_data, prediction))
    # plot(test_combined[['ds']], test_data, prediction, 'available suppliesss')


predict(supply_train, test_combined['s'], 'available supply')
# predict(demand_train, test_combined['d'], 'unassigned demand')
# error()
