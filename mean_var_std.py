import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(numbers).reshape(3, 3)
    
    calculations = {
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().item()],
        'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().item()],
        'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().item()],
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().item()],
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().item()],
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().item()]
    }
    
    return calculations


# Test the function
test_input = [0,1,2,3,4,5,6,7,8]
print(calculate(test_input))
