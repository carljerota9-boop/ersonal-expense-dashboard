import datetime
import random

# Set random seed for reproducible dummy data
random.seed(42)

# 1. Generate at least 50 complete dummy data entries (Personal Expense Topic)
categories = ["Food & Dining", "Transportation", "Utilities", "Shopping", "Entertainment", "Healthcare"]
descriptions = {
    "Food & Dining": ["Grocery Run", "Coffee Shop", "Restaurant Dinner", "Fast Food Lunch", "Snacks"],
    "Transportation": ["Gasoline", "Taxi / Ride Share", "Bus Fare", "Parking Fee", "Car Maintenance"],
    "Utilities": ["Electricity Bill", "Water Bill", "Internet Subscription", "Mobile Phone Plan"],
    "Shopping": ["Clothing", "Books", "Gadget Accessories", "Home Supplies", "Skincare"],
    "Entertainment": ["Movie Ticket", "Streaming Service", "Concert Ticket", "Video Game"],
    "Healthcare": ["Pharmacy / Medicines", "Doctor Consultation", "Vitamin Supplements"]
}

start_date = datetime.date(2026, 10, 1)
data = []

for i in range(1, 61):  # Generating 60 entries (exceeds the 50-entry requirement)
    entry_date = start_date + datetime.timedelta(days=random.randint(0, 60))
    category = random.choice(categories)
    description = random.choice(descriptions[category])
    
    # Realistic amounts based on category
    if category == "Utilities":
        amount = round(random.uniform(800.0, 3500.0), 2)
    elif category == "Food & Dining":
        amount = round(random.uniform(150.0, 1500.0), 2)
    elif category == "Transportation":
        amount = round(random.uniform(100.0, 800.0), 2)
    elif category == "Shopping":
        amount = round(random.uniform(500.0, 4000.0), 2)
    elif category == "Entertainment":
        amount = round(random.uniform(200.0, 2000.0), 2)
    else:  # Healthcare
        amount = round(random.uniform(300.0, 2500.0), 2)
        
    data.append({
        "id": i,
        "date": entry_date.strftime("%Y-%m-%d"),
        "category": category,
        "description": description,
        "amount": amount
    })

# Sort data by date
data = sorted(data, key=lambda x: x["date"])

# 2. Perform Calculations & Summaries
total_expenses = sum(item["amount"] for item in data)
average_expense = total_expenses / len(data)
max_expense = max(data, key=lambda x: x["amount"])
min_expense = min(data, key=lambda x: x["amount"])

# Category breakdown calculations
category_totals = {}
for cat in categories:
    category_totals[cat] = sum(item["amount"] for item in data if item["category"] == cat)

# 3. Generate HTML & CSS Dashboard
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Expense Dashboard - Final Project</title>
    <!-- Tailwind CSS for modern styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js for visualizations -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen p-6">

    <div class="max-w-7xl mx-auto space-y-6">
        
        <!-- Header Section -->
        <header class="bg-white rounded-2xl shadow-sm p-6 border border-slate-100 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
            <div>
                <span class="text-xs font-semibold uppercase tracking-wider text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full">Fundamentals of Analytics Modeling</span>
                <h1 class="text-2xl md:text-3xl font-bold text-slate-900 mt-2">Personal Expense Analytics Dashboard</h1>
                <p class="text-sm text-slate-500 mt-1">Comprehensive summary of recorded transactions, category distributions, and trends.</p>
            </div>
            <div class="text-right bg-slate-50 px-4 py-3 rounded-xl border border-slate-200">
                <p class="text-xs text-slate-500 font-medium">Submission Deadline</p>
                <p class="text-sm font-bold text-slate-800">First Week of December 2026</p>
            </div>
        </header>

        <!-- Summary Cards (Key Figures) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between">
                <div>
                    <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Total Expenses</p>
                    <h3 class="text-2xl font-bold text-slate-900 mt-1">₱{total_expenses:,.2f}</h3>
                    <span class="text-xs text-emerald-600 font-medium mt-1 inline-block">60 Total Records</span>
                </div>
                <div class="p-3 bg-indigo-50 text-indigo-600 rounded-xl">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
            </div>

            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between">
                <div>
                    <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Average per Transaction</p>
                    <h3 class="text-2xl font-bold text-slate-900 mt-1">₱{average_expense:,.2f}</h3>
                    <span class="text-xs text-slate-500 font-medium mt-1 inline-block">Mean calculation</span>
                </div>
                <div class="p-3 bg-blue-50 text-blue-600 rounded-xl">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                </div>
            </div>

            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between">
                <div>
                    <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Highest Transaction</p>
                    <h3 class="text-xl font-bold text-slate-900 mt-1">₱{max_expense['amount']:,.2f}</h3>
                    <span class="text-xs text-rose-600 font-medium mt-1 inline-block truncate max-w-[140px]">{max_expense['description']}</span>
                </div>
                <div class="p-3 bg-rose-50 text-rose-600 rounded-xl">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                </div>
            </div>

            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between">
                <div>
                    <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Lowest Transaction</p>
                    <h3 class="text-xl font-bold text-slate-900 mt-1">₱{min_expense['amount']:,.2f}</h3>
                    <span class="text-xs text-emerald-600 font-medium mt-1 inline-block truncate max-w-[140px]">{min_expense['description']}</span>
                </div>
                <div class="p-3 bg-emerald-50 text-emerald-600 rounded-xl">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"></path></svg>
                </div>
            </div>
        </div>

        <!-- Charts Section (1-2 charts required) -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
                <h3 class="text-lg font-bold text-slate-900 mb-4">Expenses by Category</h3>
                <div class="relative h-72">
                    <canvas id="categoryChart"></canvas>
                </div>
            </div>

            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
                <h3 class="text-lg font-bold text-slate-900 mb-4">Spending Trend Over Time</h3>
                <div class="relative h-72">
                    <canvas id="trendChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Data Table Section (At least 50 complete dummy entries) -->
        <div class="bg-white rounded-2xl shadow-sm border border-slate-100 overflow-hidden">
            <div class="p-6 border-b border-slate-100 flex justify-between items-center">
                <div>
                    <h3 class="text-lg font-bold text-slate-900">Recorded Data Entries ({len(data)} Records)</h3>
                    <p class="text-xs text-slate-500 mt-0.5">Complete dataset satisfying project requirement of at least 50 records.</p>
                </div>
            </div>
            <div class="overflow-x-auto max-h-96">
                <table class="w-full text-left border-collapse">
                    <thead class="bg-slate-50 text-slate-600 uppercase text-xs sticky top-0 border-b border-slate-200">
                        <tr>
                            <th class="p-4 font-semibold">#</th>
                            <th class="p-4 font-semibold">Date</th>
                            <th class="p-4 font-semibold">Category</th>
                            <th class="p-4 font-semibold">Description</th>
                            <th class="p-4 font-semibold text-right">Amount (PHP)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-sm text-slate-700">
"""

for item in data:
    html_content += f"""
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-4 font-medium text-slate-400">{item['id']}</td>
                            <td class="p-4">{item['date']}</td>
                            <td class="p-4"><span class="px-2.5 py-1 bg-slate-100 text-slate-700 rounded-md text-xs font-medium">{item['category']}</span></td>
                            <td class="p-4">{item['description']}</td>
                            <td class="p-4 text-right font-semibold text-slate-900">₱{item['amount']:,.2f}</td>
                        </tr>
    """

html_content += f"""
                    </tbody>
                </table>
            </div>
        </div>

    </div>

    <!-- Chart Scripts -->
    <script>
        // Category Breakdown Doughnut Chart
        const catCtx = document.getElementById('categoryChart').getContext('2d');
        new Chart(catCtx, {{
            type: 'doughnut',
            data: {{
                labels: {list(category_totals.keys())},
                datasets: [{{
                    data: {list(category_totals.values())},
                    backgroundColor: [
                        '#6366f1', '#3b82f6', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6'
                    ],
                    borderWidth: 2,
                    borderColor: '#ffffff'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom',
                        labels: {{ boxWidth: 12, font: {{ family: 'Inter', size: 12 }} }}
                    }}
                }}
            }}
        }});

        // Trend Line Chart (Aggregated or Sampled)
        const trendCtx = document.getElementById('trendChart').getContext('2d');
        new Chart(trendCtx, {{
            type: 'line',
            data: {{
                labels: { [item['date'] for item in data[::3]] },  // Sampled dates
                datasets: [{{
                    label: 'Transaction Amount (₱)',
                    data: { [item['amount'] for item in data[::3]] },
                    borderColor: '#6366f1',
                    backgroundColor: 'rgba(99, 102, 241, 0.05)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.3
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }}
                }},
                scales: {{
                    y: {{ beginAtZero: true, grid: {{ color: '#f1f5f9' }} }},
                    x: {{ grid: {{ display: false }} }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

# Write to file
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Dashboard successfully generated as 'dashboard.html'!")