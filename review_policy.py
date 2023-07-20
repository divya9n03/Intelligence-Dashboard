import streamlit as st
import pandas as pd
import requests
import io
# Function to read and process CSV files


def fetch_csv_from_github(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Read CSV data using pandas
            csv_data = pd.read_csv(io.StringIO(response.text))
            return csv_data
        else:
            print(
                f"Error: Unable to fetch CSV file. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def process_csv(files):
    github_raw_url = "https://raw.githubusercontent.com/divya9n03/Intelligence-Dashboard/e62118b7f6f9496fdf2f7ff78215e56655597161/review_main_v1.csv"
    github_url_2 = "https://raw.githubusercontent.com/divya9n03/Intelligence-Dashboard/e62118b7f6f9496fdf2f7ff78215e56655597161/review_main_v2.csv"
    csv_data = fetch_csv_from_github(github_raw_url)
    csv_data2 = fetch_csv_from_github(github_url_2)
    csv_data['Slno'] = csv_data['Slno'].map(lambda x: round(x, 1))
    print(csv_data)
    csv_data2['Slno'] = csv_data2['Slno'].map(lambda x: round(x, 1))
    if csv_data is not None and csv_data2 is not None:
        return [csv_data, csv_data2]


# def process_csv(files):

#     files = [r"C:\Users\Divya\Downloads\review_v1.csv",
#              r"C:\Users\Divya\Downloads\review_v2.csv"]
#     dataframes = [pd.read_csv(file, encoding='') for file in files]
#     #print(dataframes)
#     # Your data processing logic here...
#     return dataframes

# Main function


def main():
    st.title("Policy review")

    # File uploader for multiple CSV files
    st.header("Upload policy files")
    uploaded_files = st.file_uploader(
        "Upload multiple CSV files",  accept_multiple_files=True)

    # Check if files are uploaded
    if st.button('Check files'):

        # Process CSV files
        dataframes = process_csv(uploaded_files)
        print(type(dataframes))

        # Display tables
        st.header("Result Tables")
        num_files = len(dataframes)
        for idx, dataframe in enumerate(dataframes, 1):
            expander = st.expander(f"Table {idx}")
            with expander:
                st.dataframe(dataframe)

        # Display additional text
        st.header("The differences between the policies are:")
        st.write("1. Clause [5.4] under policy named Level 3 approval of revised credit methodology indicates changes.\n Additional data found: \n\n In any exceptional scenarios, escalated approval of CEO is needed.")
    else:
        st.write("Please upload one or more CSV files.")


if __name__ == "__main__":
    main()
