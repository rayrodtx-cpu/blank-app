"""
Transaction categorization module
Automatically categorizes transactions based on keywords and patterns
"""

import pandas as pd
from typing import Dict, Tuple, Optional
from config import BUSINESS_CATEGORIES, PERSONAL_CATEGORIES, ALL_CATEGORIES, BUSINESS_TYPE, PERSONAL_TYPE


class TransactionCategorizer:
    """Categorizes bank transactions based on description matching"""

    def __init__(self):
        self.business_keywords = self._build_keyword_map(BUSINESS_CATEGORIES)
        self.personal_keywords = self._build_keyword_map(PERSONAL_CATEGORIES)

    def _build_keyword_map(self, categories: Dict[str, list]) -> Dict[str, str]:
        """
        Build a mapping of keywords to categories

        Args:
            categories: Dictionary of category names to keyword lists

        Returns:
            Dictionary mapping keywords to category names
        """
        keyword_map = {}
        for category, keywords in categories.items():
            for keyword in keywords:
                keyword_map[keyword.lower()] = category
        return keyword_map

    def categorize_transaction(self, description: str, amount: float = 0) -> Tuple[str, str]:
        """
        Categorize a single transaction

        Args:
            description: Transaction description
            amount: Transaction amount (negative for expenses, positive for income)

        Returns:
            Tuple of (category, type) where type is BUSINESS_TYPE or PERSONAL_TYPE
        """
        if pd.isna(description):
            return "Uncategorized", PERSONAL_TYPE

        description_lower = str(description).lower()

        # Try to match business categories first (since user is focused on real estate)
        category = self._match_keywords(description_lower, self.business_keywords)
        if category:
            return category, BUSINESS_TYPE

        # Try personal categories
        category = self._match_keywords(description_lower, self.personal_keywords)
        if category:
            return category, PERSONAL_TYPE

        # Default: if negative amount (expense), might be business; if positive (income), personal
        # But let user review these
        if amount < 0:
            return "Other Business Expense", BUSINESS_TYPE
        else:
            return "Uncategorized", PERSONAL_TYPE

    def _match_keywords(self, description: str, keyword_map: Dict[str, str]) -> Optional[str]:
        """
        Match description against keywords

        Args:
            description: Transaction description (lowercase)
            keyword_map: Mapping of keywords to categories

        Returns:
            Category name if matched, None otherwise
        """
        # Try exact phrase matching first
        for keyword, category in keyword_map.items():
            if keyword in description:
                return category

        return None

    def categorize_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Categorize all transactions in a dataframe

        Args:
            df: DataFrame with 'description' and 'amount' columns

        Returns:
            DataFrame with added 'category' and 'type' columns
        """
        results = df.apply(
            lambda row: self.categorize_transaction(
                row.get('description', ''),
                row.get('amount', 0)
            ),
            axis=1
        )

        df['category'] = [r[0] for r in results]
        df['type'] = [r[1] for r in results]

        return df

    def get_category_summary(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Generate summary by category

        Args:
            df: Categorized DataFrame

        Returns:
            Summary DataFrame with totals by category
        """
        if df.empty:
            return pd.DataFrame(columns=['Category', 'Type', 'Count', 'Total'])

        summary = df.groupby(['category', 'type']).agg({
            'amount': ['count', 'sum']
        }).reset_index()

        summary.columns = ['Category', 'Type', 'Count', 'Total']
        summary['Total'] = summary['Total'].apply(lambda x: abs(x))  # Show as positive for easier reading

        # Sort by total descending
        summary = summary.sort_values('Total', ascending=False)

        return summary

    def get_business_summary(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Get summary of business expenses

        Args:
            df: Categorized DataFrame

        Returns:
            Dictionary with business expense totals
        """
        business_df = df[df['type'] == BUSINESS_TYPE]

        if business_df.empty:
            return {
                'total_expenses': 0,
                'transaction_count': 0,
                'by_category': {}
            }

        # Calculate totals (expenses are negative, so we negate them)
        total = abs(business_df[business_df['amount'] < 0]['amount'].sum())

        # By category
        by_category = business_df[business_df['amount'] < 0].groupby('category')['amount'].sum()
        by_category = by_category.apply(abs).to_dict()

        return {
            'total_expenses': total,
            'transaction_count': len(business_df),
            'by_category': by_category
        }

    def get_personal_summary(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Get summary of personal expenses

        Args:
            df: Categorized DataFrame

        Returns:
            Dictionary with personal expense totals
        """
        personal_df = df[df['type'] == PERSONAL_TYPE]

        if personal_df.empty:
            return {
                'total_expenses': 0,
                'transaction_count': 0,
                'by_category': {}
            }

        # Calculate totals (expenses are negative, so we negate them)
        total = abs(personal_df[personal_df['amount'] < 0]['amount'].sum())

        # By category
        by_category = personal_df[personal_df['amount'] < 0].groupby('category')['amount'].sum()
        by_category = by_category.apply(abs).to_dict()

        return {
            'total_expenses': total,
            'transaction_count': len(personal_df),
            'by_category': by_category
        }

    def update_transaction_category(self, df: pd.DataFrame, index: int,
                                   category: str, trans_type: str) -> pd.DataFrame:
        """
        Update category and type for a specific transaction

        Args:
            df: DataFrame
            index: Row index
            category: New category
            trans_type: New type (BUSINESS_TYPE or PERSONAL_TYPE)

        Returns:
            Updated DataFrame
        """
        if index in df.index:
            df.at[index, 'category'] = category
            df.at[index, 'type'] = trans_type

        return df
