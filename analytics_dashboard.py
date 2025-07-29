import pandas as pd
import matplotlib.pyplot as plt

def calculate_yield(df):
    total = len(df)
    passed = len(df[df['result'] == 'PASS'])
    yield_percent = (passed / total) * 100
    print(f"✅ Overall Yield: {yield_percent:.2f}% ({passed}/{total})")

def plot_failure_types(df):
    failures = df[df['result'] == 'FAIL']
    failure_counts = failures['failure_type'].value_counts()
    failure_counts.plot(kind='bar', color='crimson')
    plt.title("Failure Type Distribution")
    plt.xlabel("Failure Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_ttr_histogram(df):
    failures = df[df['result'] == 'FAIL']
    failures = failures.dropna(subset=['ttr_sec'])
    failures['ttr_sec'] = pd.to_numeric(failures['ttr_sec'], errors='coerce')
    failures = failures.dropna(subset=['ttr_sec'])
    plt.hist(failures['ttr_sec'], bins=10, color='steelblue')
    plt.title("TTR Distribution (Failed Units)")
    plt.xlabel("Time to Repair (sec)")
    plt.ylabel("Units")
    plt.tight_layout()
    plt.show()

def main():
    print("📥 Loading data from factory_data.csv...")
    df = pd.read_csv('factory_data.csv')
    df.columns = df.columns.str.lower()  # normalize column names

    print("\n--- 📊 Product Yield ---")
    calculate_yield(df)

    print("\n--- ❌ Failure Types ---")
    plot_failure_types(df)

    print("\n--- ⏱️ TTR Histogram ---")
    plot_ttr_histogram(df)

if __name__ == '__main__':
    main()