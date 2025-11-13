"""
Export module for generating tax-ready reports
Creates Excel files with organized transaction data
"""

import pandas as pd
from io import BytesIO
from datetime import datetime
from typing import Optional
from config import BUSINESS_TYPE, PERSONAL_TYPE


class TaxExporter:
    """Export categorized transactions to Excel for tax filing"""

    def export_to_excel(self, df: pd.DataFrame, year: Optional[int] = None) -> BytesIO:
        """
        Export categorized transactions to Excel

        Args:
            df: Categorized DataFrame
            year: Tax year (optional, for filename)

        Returns:
            BytesIO object containing Excel file
        """
        output = BytesIO()

        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Sheet 1: All Transactions
            self._write_all_transactions(df, writer)

            # Sheet 2: Business Expenses Summary
            self._write_business_summary(df, writer)

            # Sheet 3: Business Expenses Detail
            self._write_business_detail(df, writer)

            # Sheet 4: Personal Expenses Summary
            self._write_personal_summary(df, writer)

            # Sheet 5: Personal Expenses Detail
            self._write_personal_detail(df, writer)

            # Sheet 6: Monthly Summary
            self._write_monthly_summary(df, writer)

        output.seek(0)
        return output

    def _write_all_transactions(self, df: pd.DataFrame, writer: pd.ExcelWriter):
        """Write all transactions to Excel"""
        export_df = df.copy()

        # Format columns
        if 'date' in export_df.columns:
            export_df['date'] = pd.to_datetime(export_df['date']).dt.strftime('%Y-%m-%d')

        # Select and order columns
        columns = ['date', 'description', 'amount', 'category', 'type']
        columns = [col for col in columns if col in export_df.columns]

        export_df = export_df[columns]
        export_df = export_df.sort_values('date')

        export_df.to_excel(writer, sheet_name='All Transactions', index=False)

    def _write_business_summary(self, df: pd.DataFrame, writer: pd.ExcelWriter):
        """Write business expenses summary"""
        business_df = df[df['type'] == BUSINESS_TYPE].copy()

        if business_df.empty:
            pd.DataFrame({'Message': ['No business expenses found']}).to_excel(
                writer, sheet_name='Business Summary', index=False
            )
            return

        # Only expenses (negative amounts)
        business_df = business_df[business_df['amount'] < 0].copy()
        business_df['amount'] = business_df['amount'].abs()

        # Group by category
        summary = business_df.groupby('category').agg({
            'amount': ['sum', 'count']
        }).reset_index()

        summary.columns = ['Category', 'Total Amount', 'Transaction Count']
        summary = summary.sort_values('Total Amount', ascending=False)

        # Add total row
        total_row = pd.DataFrame({
            'Category': ['TOTAL'],
            'Total Amount': [summary['Total Amount'].sum()],
            'Transaction Count': [summary['Transaction Count'].sum()]
        })

        summary = pd.concat([summary, total_row], ignore_index=True)

        summary.to_excel(writer, sheet_name='Business Summary', index=False)

    def _write_business_detail(self, df: pd.DataFrame, writer: pd.ExcelWriter):
        """Write detailed business expenses"""
        business_df = df[df['type'] == BUSINESS_TYPE].copy()

        if business_df.empty:
            pd.DataFrame({'Message': ['No business expenses found']}).to_excel(
                writer, sheet_name='Business Detail', index=False
            )
            return

        # Only expenses
        business_df = business_df[business_df['amount'] < 0].copy()
        business_df['amount'] = business_df['amount'].abs()

        # Format date
        if 'date' in business_df.columns:
            business_df['date'] = pd.to_datetime(business_df['date']).dt.strftime('%Y-%m-%d')

        # Select columns
        columns = ['date', 'description', 'category', 'amount']
        columns = [col for col in columns if col in business_df.columns]

        business_df = business_df[columns]
        business_df = business_df.sort_values(['category', 'date'])

        business_df.to_excel(writer, sheet_name='Business Detail', index=False)

    def _write_personal_summary(self, df: pd.DataFrame, writer: pd.ExcelWriter):
        """Write personal expenses summary"""
        personal_df = df[df['type'] == PERSONAL_TYPE].copy()

        if personal_df.empty:
            pd.DataFrame({'Message': ['No personal expenses found']}).to_excel(
                writer, sheet_name='Personal Summary', index=False
            )
            return

        # Only expenses
        personal_df = personal_df[personal_df['amount'] < 0].copy()
        personal_df['amount'] = personal_df['amount'].abs()

        # Group by category
        summary = personal_df.groupby('category').agg({
            'amount': ['sum', 'count']
        }).reset_index()

        summary.columns = ['Category', 'Total Amount', 'Transaction Count']
        summary = summary.sort_values('Total Amount', ascending=False)

        # Add total row
        total_row = pd.DataFrame({
            'Category': ['TOTAL'],
            'Total Amount': [summary['Total Amount'].sum()],
            'Transaction Count': [summary['Transaction Count'].sum()]
        })

        summary = pd.concat([summary, total_row], ignore_index=True)

        summary.to_excel(writer, sheet_name='Personal Summary', index=False)

    def _write_personal_detail(self, df: pd.DataFrame, writer: pd.ExcelWriter):
        """Write detailed personal expenses"""
        personal_df = df[df['type'] == PERSONAL_TYPE].copy()

        if personal_df.empty:
            pd.DataFrame({'Message': ['No personal expenses found']}).to_excel(
                writer, sheet_name='Personal Detail', index=False
            )
            return

        # Only expenses
        personal_df = personal_df[personal_df['amount'] < 0].copy()
        personal_df['amount'] = personal_df['amount'].abs()

        # Format date
        if 'date' in personal_df.columns:
            personal_df['date'] = pd.to_datetime(personal_df['date']).dt.strftime('%Y-%m-%d')

        # Select columns
        columns = ['date', 'description', 'category', 'amount']
        columns = [col for col in columns if col in personal_df.columns]

        personal_df = personal_df[columns]
        personal_df = personal_df.sort_values(['category', 'date'])

        personal_df.to_excel(writer, sheet_name='Personal Detail', index=False)

    def _write_monthly_summary(self, df: pd.DataFrame, writer: pd.ExcelWriter):
        """Write monthly breakdown of expenses"""
        if df.empty or 'date' not in df.columns:
            pd.DataFrame({'Message': ['No data for monthly summary']}).to_excel(
                writer, sheet_name='Monthly Summary', index=False
            )
            return

        # Only expenses
        expenses_df = df[df['amount'] < 0].copy()
        expenses_df['amount'] = expenses_df['amount'].abs()

        # Add month column
        expenses_df['month'] = pd.to_datetime(expenses_df['date']).dt.to_period('M')

        # Group by month and type
        monthly = expenses_df.groupby(['month', 'type'])['amount'].sum().reset_index()
        monthly = monthly.pivot(index='month', columns='type', values='amount').fillna(0)

        # Add total column
        monthly['Total'] = monthly.sum(axis=1)

        # Format month as string
        monthly.index = monthly.index.astype(str)

        monthly.to_excel(writer, sheet_name='Monthly Summary')

    def generate_tax_summary_text(self, df: pd.DataFrame, year: Optional[int] = None) -> str:
        """
        Generate a text summary of business expenses for quick reference

        Args:
            df: Categorized DataFrame
            year: Tax year

        Returns:
            Formatted text summary
        """
        business_df = df[df['type'] == BUSINESS_TYPE].copy()
        business_df = business_df[business_df['amount'] < 0].copy()

        if business_df.empty:
            return "No business expenses found."

        year_text = f" for {year}" if year else ""
        summary = f"Real Estate Business Expense Summary{year_text}\n"
        summary += "=" * 50 + "\n\n"

        # Group by category
        by_category = business_df.groupby('category')['amount'].sum().abs().sort_values(ascending=False)

        for category, amount in by_category.items():
            summary += f"{category:.<40} ${amount:>12,.2f}\n"

        summary += "-" * 50 + "\n"
        summary += f"{'TOTAL BUSINESS EXPENSES':.<40} ${by_category.sum():>12,.2f}\n"

        return summary
