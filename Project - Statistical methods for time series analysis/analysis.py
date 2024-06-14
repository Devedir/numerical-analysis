import numpy as np
import matplotlib.pyplot as plt


def holt_winters_additive(series, alpha, beta, gamma, seasonal_periods, n_forecast):
    n = len(series)
    level = np.zeros(n)
    trend = np.zeros(n)
    season = np.zeros(n)
    forecast = np.zeros(n + n_forecast)

    # Initialize the components
    level[0] = series[0]
    trend[0] = series[1] - series[0]
    for i in range(seasonal_periods):
        season[i] = series[i] - level[0]

    for t in range(1, n):
        if t >= seasonal_periods:
            season_idx = t - seasonal_periods
        else:
            season_idx = t
        if t == 1:
            level[t] = alpha * (series[t] - season[season_idx]) + (1 - alpha) * (level[t - 1] + trend[t - 1])
        else:
            level[t] = alpha * (series[t] - season[season_idx]) + (1 - alpha) * (level[t - 1] + trend[t - 1])
        trend[t] = beta * (level[t] - level[t - 1]) + (1 - beta) * trend[t - 1]
        season[t] = gamma * (series[t] - level[t]) + (1 - gamma) * season[season_idx]

    for t in range(n):
        forecast[t] = level[t] + trend[t] + season[t % seasonal_periods]

    for t in range(n, n + n_forecast):
        forecast[t] = level[n - 1] + (t - n + 1) * trend[n - 1] + season[t % seasonal_periods]

    return forecast


# Przykład użycia
# Reading data from a file with cleaning
with open('data.txt', 'r') as data_file:
    data = [line.rstrip().split(';') for line in data_file.readlines()]
    for i in range(len(data)):
        # date = data[i][0].split('-')
        # data[i][0] = (int(date[0]), int(date[1]))
        data[i][1] = int(data[i][1])

def main():
    series = [val for _, val in data]
    times = [date for date, _ in data]
    alpha = 0.4
    beta = 0.1
    gamma = 0.3
    seasonal_periods = 12

    # Jak model nakłada się na dane rzeczywiste:
    past = holt_winters_additive(series, alpha, beta, gamma, seasonal_periods, 0)
    plt.plot(times, series, label='Dane rzeczywiste')
    plt.plot(times, past.tolist(), label='Przybliżenie modelem')
    plt.title('Miesięczne urodzenia w Polsce w latach 2019-2023')
    plt.xlabel('czas')
    plt.ylabel('liczba urodzeń')
    plt.legend(loc='upper right')
    ticks = ['2019-01', '2020-01', '2021-01', '2022-01', '2023-01', '2023-12']
    plt.xticks(ticks)
    plt.grid(True)
    plt.show()

    # Prognoza na kolejne 4 lata:
    n_forecast = 4 * 12
    previous_dates = ["'" + date[2:] for date in times]
    further_dates = []
    for year in range(19, 28):
        for month in range(1, 13):
            further_dates.append(f"'{year}-{month:02}")
    forecast = holt_winters_additive(series, alpha, beta, gamma, seasonal_periods, n_forecast)
    plt.plot(previous_dates, series, label='Dane rzeczywiste')
    plt.plot(further_dates, forecast.tolist(), label='Prognoza modelem')
    plt.title('Prognoza liczby miesięcznych urodzeń w Polsce do roku 2027')
    plt.xlabel('czas')
    plt.ylabel('liczba urodzeń')
    plt.legend(loc='upper right')
    ticks = [f"'{year}-01" for year in range(19, 28)]
    ticks.append("'27-12")
    plt.xticks(ticks)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
