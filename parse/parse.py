import pandas as pd
COLUMNS = ['State', 'Postal Abbr.', 'FIPS Code']
df = pd.DataFrame(columns=COLUMNS)


def parse(file):
    c = 0
    for line in f:
        line = line.rstrip()
        line = line.split('    ')
        if c > 4:
            list1 = line[:3]
            list2 = line[3:]
            df.loc[len(df)] = list1
            if len(list2) > 0:
                df.loc[len(df)] = list2
        c += 1


f = open('data.txt')
parse(f)
print(df)

