import pandas as pd

def main():
    df = pd.read_excel('data.xlsx')
    # Process data
    df.to_csv('data.csv', index=False)

if __name__ == '__main__':
    main()