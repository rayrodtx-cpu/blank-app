# 📊 Bank Statement Categorizer for Real Estate Tax Filing

A Streamlit web application that helps real estate investors separate business expenses from personal expenses for tax filing. Upload your bank statements and let the app automatically categorize transactions, then export organized data for your accountant or tax preparer.

## Features

- **Multi-File Upload**: Upload multiple CSV or PDF bank statements at once
- **Smart Categorization**: Automatically categorizes transactions based on keywords and merchant names
- **Real Estate Focus**: Pre-configured categories for common rental property expenses:
  - Mortgage Interest
  - Property Taxes
  - Repairs & Maintenance
  - Utilities
  - Insurance
  - Property Management
  - Legal & Professional Fees
  - HOA Fees
  - Advertising
  - Cleaning & Landscaping
  - And more...
- **Business/Personal Separation**: Clearly separates business from personal expenses
- **Manual Review**: Interactive interface to review and adjust categorizations
- **Multi-Year Support**: Filter and export data by tax year
- **Excel Export**: Generates comprehensive Excel reports with multiple worksheets:
  - All Transactions
  - Business Summary
  - Business Detail
  - Personal Summary
  - Personal Detail
  - Monthly Summary

## Installation

### Prerequisites

- Python 3.8 or higher
- For PDF support: Java Runtime Environment (JRE) must be installed

### Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd blank-app
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) For PDF parsing, ensure Java is installed:
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install default-jre

   # On macOS
   brew install java

   # On Windows
   # Download and install from https://www.java.com
   ```

## Usage

### Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

2. Open your browser to the URL shown (typically `http://localhost:8501`)

### How to Use

1. **Export Bank Statements**
   - Log into your bank account online
   - Download statements as CSV files (preferred) or PDF
   - Tip: Most banks allow you to export custom date ranges

2. **Upload Files**
   - Click "Browse files" in the sidebar
   - Select one or more bank statement files
   - Click "Process Files"

3. **Review Transactions**
   - The app will automatically categorize all transactions
   - Review the categorizations in the "All Transactions" tab
   - Check business and personal expense summaries

4. **Adjust Categories**
   - Expand "Manually Adjust Categories" to recategorize transactions
   - Select a transaction, choose the correct category and type
   - Click "Update Category"

5. **Filter by Year**
   - Use the sidebar to filter by specific tax year
   - Helpful for preparing annual tax returns

6. **Export for Tax Filing**
   - Click "Generate Excel Report" in the sidebar
   - Download the Excel file with all categorized data
   - Share with your accountant or use for tax preparation

## Project Structure

```
blank-app/
├── streamlit_app.py    # Main application UI
├── config.py           # Category definitions and keywords
├── parser.py           # Bank statement parsing logic
├── categorizer.py      # Transaction categorization engine
├── exporter.py         # Excel export functionality
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Supported Bank Formats

The app is designed to work with most bank CSV exports. It automatically detects and maps common column names:

- **Date**: date, transaction date, posted date, trans date
- **Description**: description, memo, transaction description, payee
- **Amount**: amount, debit, withdrawal, payment, credit, deposit

If your bank uses different column names, you can modify the `CSV_COLUMN_MAPPINGS` in `config.py`.

## Customization

### Adding Custom Categories

Edit `config.py` to add or modify categories:

```python
BUSINESS_CATEGORIES = {
    "Your Custom Category": [
        "keyword1", "keyword2", "merchant name"
    ],
    # ... other categories
}
```

### Adjusting Keywords

Add keywords to improve automatic categorization:

```python
"Repairs & Maintenance": [
    "repair", "handyman", "plumbing",
    "your local handyman", "favorite hardware store"
]
```

## Tips for Tax Filing

1. **Review Everything**: Always review auto-categorizations before exporting
2. **Save Your Data**: Keep the exported Excel files for your records
3. **Consistent Categories**: Use consistent category names across years
4. **Documentation**: Keep receipts for large business expenses
5. **Consult a Professional**: This tool helps organize data, but consult a tax professional for advice

## Troubleshooting

### PDF Files Not Parsing

- Ensure Java is installed: `java -version`
- Try converting PDF to CSV using your bank's export options
- Some PDF formats (scanned images) may not work well

### Incorrect Categorization

- Use the manual adjustment feature to fix individual transactions
- Add keywords to `config.py` to improve future categorizations
- Consider whether the transaction is truly business or personal

### Missing Transactions

- Check that all bank statement files were uploaded
- Verify date ranges in your exports cover the full tax year
- Look for duplicate removal (transactions appearing in multiple statements)

## Privacy & Security

- All processing happens locally in your browser
- No data is sent to external servers
- Bank statements are not stored permanently
- Clear your browser cache/session to remove uploaded data

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review the Streamlit documentation at https://docs.streamlit.io/
3. Open an issue in the repository

## Disclaimer

This tool is designed to help organize financial data for tax preparation. It does not provide tax advice. Always consult with a qualified tax professional or accountant for tax-related decisions.
