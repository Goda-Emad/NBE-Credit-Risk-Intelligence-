"""
Download Dataset Script
Downloads German Credit Dataset from UCI Repository
"""

import os
import urllib.request
import pandas as pd
from pathlib import Path
from datetime import datetime

# Dataset URLs
UCI_BASE = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german"

URLS = {
    "german.data":         f"{UCI_BASE}/german.data",
    "german.data-numeric": f"{UCI_BASE}/german.data-numeric",
    "german.doc":          f"{UCI_BASE}/german.doc"
}

COLUMN_NAMES = [
    "Status_Account", "Duration", "Credit_History", "Purpose",
    "Credit_Amount", "Savings", "Employment", "Installment_Rate",
    "Personal_Status", "Other_Debtors", "Residence_Since", "Property",
    "Age", "Other_Plans", "Housing", "Existing_Credits", "Job",
    "Num_Dependents", "Telephone", "Foreign_Worker", "Risk"
]


def download_file(url: str, output_path: str) -> bool:
    """Download a single file"""
    try:
        print(f"  Downloading: {url}")
        urllib.request.urlretrieve(url, output_path)
        size = os.path.getsize(output_path) / 1024
        print(f"  ✅ Saved: {output_path} ({size:.1f} KB)")
        return True
    except Exception as e:
        print(f"  ❌ Failed: {e}")
        return False


def convert_to_csv(data_file: str, output_file: str) -> bool:
    """Convert .data file to CSV with column names"""
    try:
        df = pd.read_csv(data_file, sep=r"\s+",
                         header=None, names=COLUMN_NAMES)

        # Map target: 1=Bad → 0, 2=Good → 1
        df["Risk"] = df["Risk"].map({1: 0, 2: 1})

        df.to_csv(output_file, index=False)
        print(f"  ✅ CSV created: {output_file} ({df.shape})")
        return True
    except Exception as e:
        print(f"  ❌ Conversion failed: {e}")
        return False


def validate_data(csv_file: str) -> dict:
    """Validate downloaded data"""
    df = pd.read_csv(csv_file)

    results = {
        "rows":           len(df),
        "columns":        len(df.columns),
        "missing_values": df.isnull().sum().sum(),
        "duplicates":     df.duplicated().sum(),
        "good_risk":      (df["Risk"] == 1).sum(),
        "bad_risk":       (df["Risk"] == 0).sum(),
        "is_valid":       len(df) == 1000
    }

    print(f"\n  📊 Validation Results:")
    for k, v in results.items():
        status = "✅" if k != "is_valid" else ("✅" if v else "❌")
        print(f"  {status} {k}: {v}")

    return results


def main():
    print("="*60)
    print("📥 NBE Credit Risk - Data Download Script")
    print("="*60)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Create directories
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n📂 Output directory: {raw_dir}/")

    # Download files
    print("\n⬇️  Downloading files...")
    success_count = 0
    for filename, url in URLS.items():
        output_path = raw_dir / filename
        if download_file(url, str(output_path)):
            success_count += 1

    print(f"\n  Downloaded: {success_count}/{len(URLS)} files")

    # Convert to CSV
    print("\n🔄 Converting to CSV...")
    data_file  = raw_dir / "german.data"
    csv_file   = raw_dir / "german_credit_original.csv"

    if data_file.exists():
        convert_to_csv(str(data_file), str(csv_file))
    else:
        print("  ❌ german.data not found!")
        return False

    # Validate
    print("\n🔍 Validating data...")
    if csv_file.exists():
        validate_data(str(csv_file))

    print("\n" + "="*60)
    print("✅ Download complete!")
    print(f"   Data saved to: {csv_file}")
    print("   Next step: python scripts/train_pipeline.py")
    print("="*60)
    return True


if __name__ == "__main__":
    main()
