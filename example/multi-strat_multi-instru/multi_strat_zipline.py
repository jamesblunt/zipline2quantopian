
from global_import.zipline_import import *
from multi_strategy.strat_main import *
	
if __name__ == '__main__':
    
    fast_backtest = False
    algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data, capital_base = 10000, fast_backtest=fast_backtest)
    
    instrument = [''.join(w) for w in algo.instrument]

    data = load_from_yahoo(stocks=instrument, indexes={},start=algo.startDate, end=algo.endDate)
    data = data.dropna()
    #
    # End Of Fetch and Load
    #

    results = algo.run(data)

    if not fast_backtest:
        algo_name = 'multi_mom_50%_strat1'
        benchmark_name = 'SPY'
        bench_plot = False
        plot_portfolio(results, algo, algo_name, bench_plot, benchmark_name)
        
        print("\n RISK METRICS \n")
        print(algo.perf_tracker.cumulative_risk_metrics)
        dd = from_trough_to_depth_trough(results, -7)
