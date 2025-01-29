import pandas as pd
import sqlalchemy
from jira import JIRA

# Connect to database
engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost/data_pipeline")
query = "SELECT * FROM product"
df = pd.read_sql(query, engine)
print(df)


# Function to check null values
def check_null_values(dataframe):
    null_counts = dataframe.isnull().sum()  # Count nulls in each column
    return null_counts[null_counts > 0]  # Return columns with null values

# Check for null values
null_results = check_null_values(df)

# Print results
print("Columns with null values and their counts:")
print(null_results)


def check_duplicates(dataframe):
    duplicate_rows = dataframe[dataframe.duplicated()]  # Find duplicate rows
    return duplicate_rows

# Check for duplicate rows
duplicates = check_duplicates(df)

# Print results
if duplicates.empty:
    print("No duplicate rows found.")
else:
    print("Duplicate rows:")
    print(duplicates)


def detect_outliers_percentiles(dataframe, column, lower_percentile=0.01, upper_percentile=0.99):
    lower_bound = dataframe[column].quantile(lower_percentile)
    upper_bound = dataframe[column].quantile(upper_percentile)

    # Identify outliers
    outliers = dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)]
    return outliers


# Detect outliers in the "amount" column
outliers_percentiles = detect_outliers_percentiles(df, "amount")

# Print results
if outliers_percentiles.empty:
    print("No outliers detected using percentiles.")
else:
    print("Outliers detected using percentiles:")
    print(outliers_percentiles)


# Run all data quality checks
def run_quality_checks(dataframe):
    errors = {}

    # Check for null values
    null_values = check_null_values(dataframe)
    errors['null_values'] = null_values if not null_values.empty else "No null values detected."

    # Check for duplicates
    duplicates = check_duplicates(dataframe)
    errors['duplicates'] = duplicates if not duplicates.empty else "No duplicate rows found."

    # Check for outliers in 'amount' column
    outliers = detect_outliers_percentiles(dataframe, 'amount')
    errors['outliers'] = outliers if not outliers.empty else "No outliers detected."

    # Print the results in a structured way
    for check, result in errors.items():
        print(f"{check}:")
        if isinstance(result, pd.DataFrame):
            print(result)  # If result is a DataFrame (duplicates or outliers), print it
        else:
            print(result)  # Otherwise, print a simple message
        print("-" * 40)


# Run the quality checks
run_quality_checks(df)


# jira_url = 'https://rohinu1999-1738069281360.atlassian.net/jira/software/projects/SCRUM/boards/1'
# username = "rohinu1999@gmail.com"
# token = "https://rohinu1999-1738069281360.atlassian.net/rest/api/3/issue/1"
#
# jira = JIRA(server=jira_url, basic_auth=(username, token))
#
# def create_jira_ticket(summary, description):
#     issue_dict = {
#         'project': {'key': 'PROJECT_KEY'},
#         'summary': summary,
#         'description': description,
#         'issuetype': {'name': 'Bug'}
#     }
#     new_issue = jira.create_issue(fields=issue_dict)
#     print(f"Created JIRA issue: {new_issue.key}")














