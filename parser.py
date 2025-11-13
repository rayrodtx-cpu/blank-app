"""
Bank statement parser module
Handles CSV and PDF file parsing and converts to standardized format
"""

import pandas as pd
import io
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import re
from config import CSV_COLUMN_MAPPINGS, DATE_FORMATS


class BankStatementParser:
    """Parser for bank statements in various formats"""

    def __init__(self):
        self.df = None

    def parse_csv(self, file_content: bytes, encoding: str = 'utf-8') -> pd.DataFrame:
        """
        Parse CSV bank statement

        Args:
            file_content: Raw file bytes
            encoding: File encoding (default utf-8)

        Returns:
            DataFrame with standardized columns
        """
        try:
            # Try reading with different encodings if utf-8 fails
            encodings = [encoding, 'utf-8', 'latin-1', 'iso-8859-1']
            df = None

            for enc in encodings:
                try:
                    df = pd.read_csv(io.BytesIO(file_content), encoding=enc)
                    break
                except UnicodeDecodeError:
                    continue

            if df is None:
                raise ValueError("Could not decode CSV file with supported encodings")

            # Standardize column names
            df = self._standardize_columns(df)

            # Parse dates
            df = self._parse_dates(df)

            # Handle amounts (combine debit/credit if needed)
            df = self._parse_amounts(df)

            # Clean up
            df = self._clean_dataframe(df)

            self.df = df
            return df

        except Exception as e:
            raise ValueError(f"Error parsing CSV: {str(e)}")

    def parse_pdf(self, file_content: bytes) -> pd.DataFrame:
        """
        Parse PDF bank statement using tabula

        Args:
            file_content: Raw PDF file bytes

        Returns:
            DataFrame with standardized columns
        """
        try:
            import tabula

            # Read PDF tables
            tables = tabula.read_pdf(
                io.BytesIO(file_content),
                pages='all',
                multiple_tables=True,
                pandas_options={'header': 0}
            )

            if not tables:
                raise ValueError("No tables found in PDF")

            # Combine all tables
            df = pd.concat(tables, ignore_index=True)

            # Standardize columns
            df = self._standardize_columns(df)

            # Parse dates
            df = self._parse_dates(df)

            # Handle amounts
            df = self._parse_amounts(df)

            # Clean up
            df = self._clean_dataframe(df)

            self.df = df
            return df

        except ImportError:
            raise ValueError("PDF parsing requires 'tabula-py' package. Install with: pip install tabula-py")
        except Exception as e:
            raise ValueError(f"Error parsing PDF: {str(e)}")

    def _standardize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Map various bank column names to standard names"""

        # Create mapping for this specific dataframe
        column_map = {}
        df_columns_lower = {col: col.lower().strip() for col in df.columns}

        for standard_name, possible_names in CSV_COLUMN_MAPPINGS.items():
            for col in df.columns:
                col_lower = df_columns_lower[col]
                if any(name.lower() in col_lower for name in possible_names):
                    column_map[col] = standard_name
                    break

        # Apply mapping
        df = df.rename(columns=column_map)

        # Ensure we have minimum required columns
        required = ['date', 'description']
        missing = [col for col in required if col not in df.columns]

        if missing:
            raise ValueError(f"Could not find required columns: {missing}. Available: {list(df.columns)}")

        return df

    def _parse_dates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Parse date column into datetime"""

        if 'date' not in df.columns:
            return df

        # Try different date formats
        for date_format in DATE_FORMATS:
            try:
                df['date'] = pd.to_datetime(df['date'], format=date_format)
                break
            except (ValueError, TypeError):
                continue

        # If none worked, try pandas default parser
        if df['date'].dtype == 'object':
            try:
                df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
            except Exception:
                pass

        return df

    def _parse_amounts(self, df: pd.DataFrame) -> pd.DataFrame:
        """Parse and combine amount columns"""

        # Handle case where debits and credits are separate columns
        if 'amount' in df.columns:
            df['amount'] = self._clean_amount(df['amount'])
        elif 'debit' in df.columns or 'credit' in df.columns:
            # Create amount column from debit/credit
            if 'debit' not in df.columns:
                df['debit'] = 0
            if 'credit' not in df.columns:
                df['credit'] = 0

            df['debit'] = self._clean_amount(df['debit'])
            df['credit'] = self._clean_amount(df['credit'])

            # Negative for debits (expenses), positive for credits (income)
            df['amount'] = df['credit'] - df['debit']
        else:
            # No amount column found, create empty one
            df['amount'] = 0.0

        return df

    def _clean_amount(self, series: pd.Series) -> pd.Series:
        """Clean amount column - remove currency symbols, commas, etc."""

        if series.dtype in ['float64', 'int64']:
            return series

        # Convert to string and clean
        series = series.astype(str)
        series = series.str.replace('$', '', regex=False)
        series = series.str.replace(',', '', regex=False)
        series = series.str.replace('(', '-', regex=False)  # Parentheses for negative
        series = series.str.replace(')', '', regex=False)
        series = series.str.strip()

        # Convert to float
        series = pd.to_numeric(series, errors='coerce')
        series = series.fillna(0.0)

        return series

    def _clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean up the dataframe"""

        # Remove rows where description is empty
        if 'description' in df.columns:
            df = df[df['description'].notna()]
            df = df[df['description'].astype(str).str.strip() != '']

        # Remove rows where date is invalid
        if 'date' in df.columns:
            df = df[df['date'].notna()]

        # Remove rows where amount is 0 (optional - you might want to keep these)
        # df = df[df['amount'] != 0]

        # Reset index
        df = df.reset_index(drop=True)

        # Add year column for filtering
        if 'date' in df.columns and pd.api.types.is_datetime64_any_dtype(df['date']):
            df['year'] = df['date'].dt.year

        return df

    def get_years(self) -> List[int]:
        """Get list of years in the dataset"""
        if self.df is None or 'year' not in self.df.columns:
            return []
        return sorted(self.df['year'].unique().tolist(), reverse=True)

    def filter_by_year(self, year: int) -> pd.DataFrame:
        """Filter transactions by year"""
        if self.df is None:
            return pd.DataFrame()
        return self.df[self.df['year'] == year].copy()
