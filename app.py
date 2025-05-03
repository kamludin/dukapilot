import streamlit as st
import pandas as pd
from datetime import date

# Set up the page with more professional config
st.set_page_config(
    page_title="Duka Manager Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Professional Styling
st.markdown("""
    <style>
    /* Main app styling - Modern professional look */
    .main {
        background-color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Sidebar - Premium dark theme */
    .sidebar .sidebar-content {
        background-color: #0f172a;
        background-image: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        color: white;
        padding: 2rem 1.5rem;
    }
    .sidebar .sidebar-title {
        color: white;
        font-weight: 700;
        font-size: 1.75rem;
        margin-bottom: 2rem;
        letter-spacing: -0.5px;
    }
    .sidebar .stRadio > div {
        flex-direction: column;
        gap: 0.75rem;
    }
    .sidebar .stRadio > label {
        font-size: 1.05rem;
        color: #e2e8f0 !important;
        transition: all 0.3s;
    }
    .sidebar .stRadio > label:hover {
        color: white !important;
    }
    [data-testid="stRadio"] div[role="radiogroup"] label {
        padding: 10px 18px;
        border-radius: 8px;
        margin-bottom: 8px;
        transition: all 0.3s;
    }
    [data-testid="stRadio"] div[role="radiogroup"] label:hover {
        background-color: rgba(255,255,255,0.08);
    }
    [data-testid="stRadio"] div[role="radiogroup"] label div:first-child {
        margin-right: 12px;
    }
    
    /* Cards - Premium elevated design */
    .card {
        background: white;
        border-radius: 14px;
        padding: 28px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.03);
        margin-bottom: 28px;
        border: 1px solid #e2e8f0;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
    }
    .alert-card {
        border-left: 5px solid #ef4444;
        background-color: #fef2f2;
    }
    
    /* Buttons - Premium styling */
    .stButton > button {
        border-radius: 10px !important;
        padding: 12px 28px !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        font-size: 1rem !important;
    }
    .stButton > button.primary-btn {
        background-color: #3b82f6 !important;
        color: white !important;
    }
    .stButton > button.primary-btn:hover {
        background-color: #2563eb !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(59, 130, 246, 0.15) !important;
    }
    .stButton > button.danger-btn {
        background-color: #ef4444 !important;
        color: white !important;
    }
    .stButton > button.danger-btn:hover {
        background-color: #dc2626 !important;
        box-shadow: 0 6px 12px rgba(239, 68, 68, 0.15) !important;
    }
    
    /* Typography - Modern professional */
    .section-title {
        color: #1e293b;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 10px;
        margin-bottom: 24px;
        font-weight: 700;
        font-size: 1.75rem;
        letter-spacing: -0.5px;
    }
    h1 {
        color: #1e293b !important;
        font-weight: 800 !important;
        margin-bottom: 2rem !important;
        font-size: 2.5rem !important;
        letter-spacing: -1px;
    }
    h2 {
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
    }
    h3 {
        color: #1e293b !important;
        font-weight: 600 !important;
        font-size: 1.4rem !important;
    }
    
    /* Data tables - Premium look */
    .dataframe {
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        border: 1px solid #e2e8f0 !important;
    }
    .stDataFrame {
        border-radius: 12px;
    }
    table thead tr th {
        background-color: #f1f5f9 !important;
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
    }
    table tbody tr td {
        border-bottom: 1px solid #e2e8f0 !important;
        font-size: 0.9rem !important;
    }
    table tbody tr:hover td {
        background-color: #f8fafc !important;
    }
    
    /* Profit display - Premium impact */
    .profit-display {
        text-align: center;
        margin: 50px 0;
        padding: 40px;
        background: white;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        transition: all 0.3s;
    }
    .profit-display:hover {
        box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    }
    .profit-amount {
        font-size: 4rem;
        color: #10b981;
        margin: 24px 0;
        font-weight: 800;
        letter-spacing: -2px;
        background: linear-gradient(90deg, #10b981 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Empty state - More elegant */
    .empty-state {
        text-align: center;
        padding: 60px 40px;
        color: #64748b;
        background: white;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        border: 2px dashed #e2e8f0;
        transition: all 0.3s;
    }
    .empty-state:hover {
        border-color: #3b82f6;
    }
    .empty-state h3 {
        color: #64748b !important;
        margin-bottom: 20px;
        font-size: 1.5rem;
    }
    
    /* Form elements - Premium */
    .stTextInput input, .stNumberInput input, .stTextArea textarea {
        border-radius: 10px !important;
        border: 1px solid #cbd5e1 !important;
        padding: 10px 14px !important;
        font-size: 1rem !important;
    }
    .stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
    }
    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }
    
    /* Footer - More premium */
    footer {
        color: #64748b !important;
        font-size: 0.95rem !important;
        text-align: center;
        padding: 24px !important;
        margin-top: 40px !important;
    }
    
    /* Divider - More elegant */
    .stMarkdown hr {
        margin: 2.5rem 0;
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, #e2e8f0 50%, transparent 100%);
    }
    
    /* Success/error messages - Better */
    .stAlert {
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize data (same as before)
if 'products' not in st.session_state:
    st.session_state.products = pd.DataFrame(columns=[
        'Product Name', 'Cost Price', 'Selling Price', 
        'Quantity Bought', 'Quantity Sold', 'Profit', 'Date'
    ])

if 'report_data' not in st.session_state:
    st.session_state.report_data = pd.DataFrame(columns=[
        'Product Name', 'Cost Price', 'Selling Price', 
        'Quantity Bought', 'Quantity Sold', 'Profit', 'Date'
    ])

# Helper functions (same as before)
def add_products(new_products):
    new_products['Date'] = date.today().strftime("%Y-%m-%d")
    new_products['Profit'] = (
        (new_products['Selling Price'] - new_products['Cost Price']) * 
        new_products['Quantity Sold']
    )
    st.session_state.products = pd.concat([st.session_state.products, new_products], ignore_index=True)
    st.session_state.report_data = pd.concat([st.session_state.report_data, new_products], ignore_index=True)
    st.success(f"✅ Added {len(new_products)} products")

def get_todays_profit():
    if not st.session_state.products.empty:
        today = date.today().strftime("%Y-%m-%d")
        today_sales = st.session_state.products[st.session_state.products['Date'] == today]
        if not today_sales.empty:
            return today_sales['Profit'].sum()
    return 0

def get_todays_sales_count():
    if not st.session_state.products.empty:
        today = date.today().strftime("%Y-%m-%d")
        today_sales = st.session_state.products[st.session_state.products['Date'] == today]
        return today_sales['Quantity Sold'].sum()
    return 0

def check_low_stock():
    if not st.session_state.products.empty:
        st.session_state.products['Remaining Stock'] = (
            st.session_state.products['Quantity Bought'] - 
            st.session_state.products['Quantity Sold']
        )
        low_stock = st.session_state.products[
            (st.session_state.products['Remaining Stock'] <= 5) & 
            (st.session_state.products['Remaining Stock'] > 0)
        ]
        return low_stock
    return pd.DataFrame()

# Sidebar menu with premium styling
with st.sidebar:
    st.title("Duka Manager Pro")
    st.markdown("""
        <div style="margin-bottom: 40px; color: #94a3b8; font-size: 0.95rem;">
            Premium Inventory Management Solution
        </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio("Navigation Menu", 
                   ["Dashboard", "Products", "Reports", "Data Management"],
                   label_visibility="collapsed")

# Main app with premium layout
st.title("Shop Inventory Manager")
st.markdown("""
    <div style="margin-bottom: 30px; color: #64748b; font-size: 1.1rem;">
        Streamline your business operations with powerful inventory tracking and sales analytics
    </div>
""", unsafe_allow_html=True)

if menu == "Dashboard":
    st.markdown("<h2 class='section-title'>Daily Sales Summary</h2>", unsafe_allow_html=True)
    today_profit = get_todays_profit()
    items_sold = get_todays_sales_count()

    if today_profit > 0:
        st.markdown(f"""
        <div class="profit-display">
            <h3>Today's Performance</h3>
            <div class="profit-amount">KSh {today_profit:,.2f}</div>
            <p style="font-size: 1.1rem; color: #64748b;">Items sold today: <strong>{items_sold}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
            <h3>📊 No Sales Recorded Today</h3>
            <p style="font-size: 1.05rem;">Add today's sales to begin tracking your performance</p>
        </div>
        """, unsafe_allow_html=True)
    
    low_stock_items = check_low_stock()
    if not low_stock_items.empty:
        st.markdown("""
        <div class="card alert-card">
            <h3>⚠️ Stock Level Alerts</h3>
            <p style="font-size: 1.05rem;">These products are running low and need attention:</p>
        </div>
        """, unsafe_allow_html=True)
        
        alert_df = low_stock_items[['Product Name', 'Remaining Stock']].copy()
        alert_df['Remaining Stock'] = alert_df['Remaining Stock'].astype(int)
        
        def style_low_stock(val):
            if isinstance(val, (int, float)):
                return 'color: #ef4444; font-weight: 600;' if val <= 5 else ''
            return ''
        
        st.dataframe(
            alert_df.style.applymap(style_low_stock),
            use_container_width=True,
            height=min(300, 75 * len(alert_df))
        )

elif menu == "Products":
    st.markdown("<h2 class='section-title'>Product Management</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>✏️ Add Today's Sales</h3>
        <p style="font-size: 1.05rem; color: #64748b;">Enter product details below to track today's sales performance</p>
    </div>
    """, unsafe_allow_html=True)

    new_products = pd.DataFrame(columns=[
        'Product Name', 'Cost Price', 'Selling Price', 
        'Quantity Bought', 'Quantity Sold'
    ])
    for _ in range(3):
        new_products.loc[len(new_products)] = ['', 0, 0, 0, 0]

    edited_df = st.data_editor(
        new_products,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "Cost Price": st.column_config.NumberColumn(
                format="KSh %.2f",
                help="The price you paid for the product"
            ),
            "Selling Price": st.column_config.NumberColumn(
                format="KSh %.2f",
                help="The price you sold the product for"
            ),
            "Quantity Bought": st.column_config.NumberColumn(
                help="Total quantity purchased"
            ),
            "Quantity Sold": st.column_config.NumberColumn(
                help="Quantity sold today"
            )
        }
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("💾 Save Products", type="primary", key="save_products"):
            valid_products = edited_df[edited_df['Product Name'] != '']
            if not valid_products.empty:
                invalid_prices = valid_products[valid_products['Selling Price'] <= valid_products['Cost Price']]
                if not invalid_prices.empty:
                    st.error(f"❌ Selling price must be higher than cost price for: {', '.join(invalid_prices['Product Name'])}")
                else:
                    add_products(valid_products)
                    st.rerun()
            else:
                st.error("Please add at least one product")

elif menu == "Reports":
    st.markdown("<h2 class='section-title'>Business Analytics</h2>", unsafe_allow_html=True)

    if st.session_state.report_data.empty:
        st.info("No sales data available. Add products to generate reports")
    else:
        report_df = st.session_state.report_data.copy()
        report_df['Remaining Stock'] = (
            report_df['Quantity Bought'] - 
            report_df['Quantity Sold']
        )

        display_df = report_df.copy()
        display_df['Cost Price'] = display_df['Cost Price'].apply(lambda x: f"KSh {x:,.2f}")
        display_df['Selling Price'] = display_df['Selling Price'].apply(lambda x: f"KSh {x:,.2f}")
        display_df['Profit'] = display_df['Profit'].apply(lambda x: f"KSh {x:,.2f}")

        st.dataframe(
            display_df,
            use_container_width=True,
            height=600
        )

        csv = report_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Full Report (CSV)",
            data=csv,
            file_name=f"duka_report_{date.today()}.csv",
            mime="text/csv",
            help="Download complete sales history as CSV file"
        )

elif menu == "Data Management":
    st.markdown("<h2 class='section-title'>Data Administration</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>🔒 Data Management Console</h3>
        <p style="font-size: 1.05rem; color: #64748b;">Manage your sales data while preserving historical records</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧹 Clear Today's Sales Data")
    st.markdown("""
    <div style="background: #f8fafc; padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #e2e8f0;">
        <p style="font-size: 1.05rem; color: #64748b; margin-bottom: 15px;">
            This action will clear today's sales from the dashboard while preserving all data in reports.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Clear Today's Sales", key="clear_today", type="primary"):
        if not st.session_state.products.empty:
            today = date.today().strftime("%Y-%m-%d")
            st.session_state.products = st.session_state.products[st.session_state.products['Date'] != today]
            st.success("Today's sales cleared from dashboard. All report data preserved.")
            st.rerun()
        else:
            st.warning("No sales data available to clear")

# Premium footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 30px 20px 20px;">
        <p style="font-size: 0.95rem; margin-bottom: 8px;">Duka Manager Pro © 2023 | Premium Inventory Solution</p>
        <p style="font-size: 0.85rem; color: #94a3b8;">Designed for Kenyan Entrepreneurs | Version 2.0</p>
    </div>
""", unsafe_allow_html=True)