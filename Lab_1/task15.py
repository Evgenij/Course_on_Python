from functools import wraps

def pre_process(a=0.97):
    def decorator(func):
        @wraps(func)
        def decorator(signal):
            for i in range(1, len(signal)):
                signal[i] = signal[i]-a*signal[i-1]
            func(signal)
        return decorator
    return decorator

@pre_process(a=0.93)
def plot_signal(signal):
    for sample in signal:
        print(sample)

list_souce = [1,2,3]
plot_signal(list_souce)