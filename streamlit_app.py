"""
Bank Statement Categorizer for Real Estate Tax Filing
Helps separate business and personal expenses from bank statements
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from parser import BankStatementParser
from categorizer import TransactionCategorizer
from exporter import TaxExporter
from config import ALL_CATEGORIES, BUSINESS_TYPE, PERSONAL_TYPE, BUSINESS_CATEGORIES, PERSONAL_CATEGORIES

# Page configuration
st.set_page_config(
    page_title="Bank Statement Categorizer",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if 'transactions' not in st.session_state:
    st.session_state.transactions = None
if 'categorized' not in st.session_state:
    st.session_state.categorized = False
if 'parser' not in st.session_state:
    st.session_state.parser = BankStatementParser()
if 'categorizer' not in st.session_state:
    st.session_state.categorizer = TransactionCategorizer()


def main():
    st.title("📊 Real Estate Tax Expense Categorizer")
    st.markdown("""
    Upload your bank statements (CSV or PDF) to automatically categorize transactions
    into business and personal expenses for tax filing.
    """)

    # Sidebar for file upload and settings
    with st.sidebar:
        st.header("📁 Upload Bank Statements")

        uploaded_files = st.file_uploader(
            "Choose CSV or PDF files",
            type=['csv', 'pdf'],
            accept_multiple_files=True,
            help="Upload one or more bank statement files"
        )

        if uploaded_files:
            if st.button("Process Files", type="primary"):
                process_files(uploaded_files)

        st.divider()

        # Year filter
        if st.session_state.transactions is not None and not st.session_state.transactions.empty:
            st.header("📅 Filter by Year")
            years = st.session_state.parser.get_years()

            if len(years) > 0:
                selected_year = st.selectbox(
                    "Select Tax Year",
                    options=['All Years'] + years,
                    index=0
                )

                if selected_year != 'All Years':
                    st.session_state.filtered_year = selected_year
                else:
                    st.session_state.filtered_year = None

            st.divider()

            # Export section
            st.header("📥 Export for Tax Filing")

            year_for_export = st.session_state.get('filtered_year', None)

            if st.button("Generate Excel Report", type="primary"):
                generate_export(year_for_export)

    # Main content area
    if st.session_state.transactions is None:
        show_welcome_screen()
    else:
        show_transaction_interface()


def show_welcome_screen():
    """Display welcome screen with instructions"""
    st.info("👈 Upload your bank statement files using the sidebar to get started!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Supported File Formats")
        st.markdown("""
        - **CSV**: Most common format from banks
        - **PDF**: Bank statement PDFs (experimental)
        """)

        st.subheader("📋 How It Works")
        st.markdown("""
        1. Upload your bank statement files
        2. Review auto-categorized transactions
        3. Adjust categories as needed
        4. Export organized data for tax filing
        """)

    with col2:
        st.subheader("🏢 Business Categories (Real Estate)")
        business_cats = list(BUSINESS_CATEGORIES.keys())
        for cat in business_cats[:8]:  # Show first 8
            st.markdown(f"- {cat}")
        if len(business_cats) > 8:
            st.markdown(f"- ... and {len(business_cats) - 8} more")

        st.subheader("🏠 Personal Categories")
        personal_cats = list(PERSONAL_CATEGORIES.keys())
        for cat in personal_cats[:5]:  # Show first 5
            st.markdown(f"- {cat}")
        if len(personal_cats) > 5:
            st.markdown(f"- ... and {len(personal_cats) - 5} more")


def process_files(uploaded_files):
    """Process uploaded bank statement files"""
    all_transactions = []

    with st.spinner("Processing files..."):
        progress_bar = st.progress(0)

        for idx, file in enumerate(uploaded_files):
            try:
                # Read file content
                file_content = file.read()

                # Parse based on file type
                if file.name.endswith('.csv'):
                    df = st.session_state.parser.parse_csv(file_content)
                elif file.name.endswith('.pdf'):
                    df = st.session_state.parser.parse_pdf(file_content)
                else:
                    st.error(f"Unsupported file type: {file.name}")
                    continue

                all_transactions.append(df)

            except Exception as e:
                st.error(f"Error processing {file.name}: {str(e)}")
                continue

            progress_bar.progress((idx + 1) / len(uploaded_files))

    if all_transactions:
        # Combine all transactions
        combined_df = pd.concat(all_transactions, ignore_index=True)

        # Remove duplicates based on date and description
        combined_df = combined_df.drop_duplicates(subset=['date', 'description'], keep='first')

        # Categorize transactions
        combined_df = st.session_state.categorizer.categorize_dataframe(combined_df)

        # Sort by date descending
        combined_df = combined_df.sort_values('date', ascending=False)

        # Store in session state
        st.session_state.transactions = combined_df
        st.session_state.categorized = True

        st.success(f"Successfully processed {len(uploaded_files)} file(s) with {len(combined_df)} transactions!")
        st.rerun()


def show_transaction_interface():
    """Display main transaction review interface"""
    df = st.session_state.transactions

    # Apply year filter if selected
    if st.session_state.get('filtered_year'):
        df = df[df['year'] == st.session_state.filtered_year]

    # Summary metrics
    st.header("📈 Summary")

    col1, col2, col3, col4 = st.columns(4)

    business_summary = st.session_state.categorizer.get_business_summary(df)
    personal_summary = st.session_state.categorizer.get_personal_summary(df)

    with col1:
        st.metric("Total Transactions", len(df))

    with col2:
        st.metric("Business Expenses", f"${business_summary['total_expenses']:,.2f}")

    with col3:
        st.metric("Personal Expenses", f"${personal_summary['total_expenses']:,.2f}")

    with col4:
        business_count = len(df[df['type'] == BUSINESS_TYPE])
        st.metric("Business Trans.", business_count)

    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 All Transactions",
        "🏢 Business Expenses",
        "🏠 Personal Expenses",
        "📊 Category Summary"
    ])

    with tab1:
        show_all_transactions(df)

    with tab2:
        show_business_transactions(df)

    with tab3:
        show_personal_transactions(df)

    with tab4:
        show_category_summary(df)


def show_all_transactions(df):
    """Display all transactions with editing capability"""
    st.subheader("All Transactions")

    # Filters
    col1, col2 = st.columns(2)

    with col1:
        filter_type = st.multiselect(
            "Filter by Type",
            options=[BUSINESS_TYPE, PERSONAL_TYPE],
            default=[BUSINESS_TYPE, PERSONAL_TYPE]
        )

    with col2:
        filter_category = st.multiselect(
            "Filter by Category",
            options=sorted(df['category'].unique()),
            default=[]
        )

    # Apply filters
    filtered_df = df.copy()
    if filter_type:
        filtered_df = filtered_df[filtered_df['type'].isin(filter_type)]
    if filter_category:
        filtered_df = filtered_df[filtered_df['category'].isin(filter_category)]

    # Display editable dataframe
    st.info(f"Showing {len(filtered_df)} of {len(df)} transactions")

    # Format for display
    display_df = filtered_df.copy()
    if 'date' in display_df.columns:
        display_df['date'] = pd.to_datetime(display_df['date']).dt.strftime('%Y-%m-%d')

    display_columns = ['date', 'description', 'amount', 'category', 'type']
    display_columns = [col for col in display_columns if col in display_df.columns]

    st.dataframe(
        display_df[display_columns],
        use_container_width=True,
        height=400
    )

    # Manual categorization section
    with st.expander("✏️ Manually Adjust Categories"):
        st.markdown("Select a transaction to recategorize:")

        # Create a selection dropdown with date and description
        transaction_options = []
        for idx, row in filtered_df.iterrows():
            date_str = pd.to_datetime(row['date']).strftime('%Y-%m-%d')
            desc = str(row['description'])[:50]
            transaction_options.append((idx, f"{date_str} - {desc}"))

        if transaction_options:
            selected_idx = st.selectbox(
                "Select Transaction",
                options=[opt[0] for opt in transaction_options],
                format_func=lambda x: next(opt[1] for opt in transaction_options if opt[0] == x)
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                new_type = st.selectbox(
                    "Type",
                    options=[BUSINESS_TYPE, PERSONAL_TYPE],
                    index=0 if st.session_state.transactions.loc[selected_idx, 'type'] == BUSINESS_TYPE else 1
                )

            with col2:
                # Get categories for selected type
                if new_type == BUSINESS_TYPE:
                    available_categories = list(BUSINESS_CATEGORIES.keys())
                else:
                    available_categories = list(PERSONAL_CATEGORIES.keys())

                current_category = st.session_state.transactions.loc[selected_idx, 'category']
                try:
                    current_idx = available_categories.index(current_category)
                except ValueError:
                    current_idx = 0

                new_category = st.selectbox(
                    "Category",
                    options=available_categories,
                    index=current_idx
                )

            with col3:
                st.write("")  # Spacer
                st.write("")  # Spacer
                if st.button("Update Category"):
                    st.session_state.transactions = st.session_state.categorizer.update_transaction_category(
                        st.session_state.transactions,
                        selected_idx,
                        new_category,
                        new_type
                    )
                    st.success("Category updated!")
                    st.rerun()


def show_business_transactions(df):
    """Display only business transactions"""
    business_df = df[df['type'] == BUSINESS_TYPE].copy()

    st.subheader(f"Business Expenses: ${abs(business_df[business_df['amount'] < 0]['amount'].sum()):,.2f}")

    if business_df.empty:
        st.info("No business transactions found.")
        return

    # Format for display
    display_df = business_df.copy()
    if 'date' in display_df.columns:
        display_df['date'] = pd.to_datetime(display_df['date']).dt.strftime('%Y-%m-%d')

    display_df['amount'] = display_df['amount'].abs()

    display_columns = ['date', 'description', 'category', 'amount']
    display_columns = [col for col in display_columns if col in display_df.columns]

    st.dataframe(
        display_df[display_columns],
        use_container_width=True,
        height=400
    )


def show_personal_transactions(df):
    """Display only personal transactions"""
    personal_df = df[df['type'] == PERSONAL_TYPE].copy()

    st.subheader(f"Personal Expenses: ${abs(personal_df[personal_df['amount'] < 0]['amount'].sum()):,.2f}")

    if personal_df.empty:
        st.info("No personal transactions found.")
        return

    # Format for display
    display_df = personal_df.copy()
    if 'date' in display_df.columns:
        display_df['date'] = pd.to_datetime(display_df['date']).dt.strftime('%Y-%m-%d')

    display_df['amount'] = display_df['amount'].abs()

    display_columns = ['date', 'description', 'category', 'amount']
    display_columns = [col for col in display_columns if col in display_df.columns]

    st.dataframe(
        display_df[display_columns],
        use_container_width=True,
        height=400
    )


def show_category_summary(df):
    """Display summary by category"""
    st.subheader("Expenses by Category")

    summary = st.session_state.categorizer.get_category_summary(df)

    # Show only expenses (negative amounts)
    expenses_df = df[df['amount'] < 0].copy()

    if expenses_df.empty:
        st.info("No expense transactions found.")
        return

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Business Expenses")
        business_summary = summary[summary['Type'] == BUSINESS_TYPE]
        if not business_summary.empty:
            st.dataframe(business_summary, use_container_width=True, hide_index=True)
        else:
            st.info("No business expenses")

    with col2:
        st.markdown("### Personal Expenses")
        personal_summary = summary[summary['Type'] == PERSONAL_TYPE]
        if not personal_summary.empty:
            st.dataframe(personal_summary, use_container_width=True, hide_index=True)
        else:
            st.info("No personal expenses")


def generate_export(year=None):
    """Generate and download Excel export"""
    exporter = TaxExporter()

    df = st.session_state.transactions

    # Filter by year if specified
    if year:
        df = df[df['year'] == year]

    with st.spinner("Generating Excel report..."):
        excel_file = exporter.export_to_excel(df, year)

        # Generate text summary
        text_summary = exporter.generate_tax_summary_text(df, year)

    # Download button
    year_suffix = f"_{year}" if year else ""
    filename = f"tax_expenses{year_suffix}_{datetime.now().strftime('%Y%m%d')}.xlsx"

    st.download_button(
        label="📥 Download Excel Report",
        data=excel_file,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # Show text summary
    st.text(text_summary)


if __name__ == "__main__":
    main()
