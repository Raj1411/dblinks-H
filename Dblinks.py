import streamlit as st
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.chrome.options import Options
import streamlit.components as stc
import base64
import io, os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




st.title('Extract Dropbox Links')

webdriveroptions = Options()
webdriveroptions.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
webdriveroptions.add_argument("--headless")
webdriveroptions.add_argument("--disable-dev-shm-usage")
webdriveroptions.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=webdriveroptions)



headers1 = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}



url1=st.text_input('Enter Dropbox link')
if url1=="":
    ""
else:
    driver.get(url1)
sleep(2)

# Add a placeholder
if url1=="":
    ""
else:
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
  # Update the progress bar with each iteration.
        latest_iteration.text(f'Progress {i+1}')
        bar.progress(i + 1)
        sleep(0.1)



SCROLL_PAUSE_TIME = 1


# Get scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
       print("break")
       break
    last_height = new_height


a=driver.find_elements_by_xpath("//a[@href]")

links=[]
for i in a:
    ax=i.get_attribute('href')
    if "https://www.dropbox.com/sh" in ax:
        links.append(ax)


if url1=="":
    ""
else:
    st.write('Extraction is Completed')


if url1=="":
    ""
else:
    towrite = io.BytesIO()
    df=pd.DataFrame(links,columns=['Links'])
    # df.to_excel('Links.xlsx')
    driver.close()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True)
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="DropboxLink.xlsx">Download file</a>'
    st.markdown(linko, unsafe_allow_html=True)