
gb = "1.34GB"
mb = "12.22MB"
kb = "492.2KB"

numbers = [gb, mb, kb]

for num in numbers:
    if num.endswith("GB"):
        rint = float(num[:-2]) * 1024 * 1024
    elif num.endswith("MB"):
        rint = float(num[:-2]) * 1024
    elif num.endswith("B"):
        rint = float(num[:-2])
    print(rint)