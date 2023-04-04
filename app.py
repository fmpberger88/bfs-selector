import streamlit as st
import pandas as pd
import base64


# Funktion zum
def read_data(data):
    if data is not None:
        # DataFrame aus der hochgeladenen CSV-Datei erstellen
        df = pd.read_csv(data, sep=",")
    return df


# Funktion zum Filtern des Datensatzes nach Bfs_Gemeindenummern
def filter_by_bfs(df, bfs):
    df = df[df["bfs_nr"] == bfs]
    return df


# Streamlit-App
# Seitentitel
st.title('BfS-Nummer Filter')
st.text("""Mit dieser Applikation kannst du einen beliebigen Datensatz im CSV Format
mittels der BfS-Nummer filtern. Voraussetzung dafür ist, dass du die Variabel 
mit den BfS-Nummern in \"bfs_nr\" benennst!""")

# Datei-Upload
data = st.file_uploader("CSV-Datei hochladen", type="csv")
if data is not None:
    df = read_data(data)
    # Filtereinstellungen
    st.write(df)
    st.write(df.columns)
    st.write('Filtereinstellungen')
    bfs = st.text_input('BfS Gemeindenummer')
    if bfs:
        bfs = int(bfs)
    else:
        bfs = None

    # Filter anwenden
    filtered_df = filter_by_bfs(df, bfs)

    # Gefilterten Datensatz anzeigen
    st.write('Gefilterter Datensatz')
    st.write(filtered_df)

    # Download-Button für den gefilterten Datensatz
    csv = filtered_df.to_csv(index=False, sep=";")
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_data.csv">Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
else:
    st.warning('Bitte eine CSV-Datei hochladen')
