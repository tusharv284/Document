import zipfile
import os
import pandas as pd

# Create directory
os.makedirs('dashboard', exist_ok=True)

# 1. requirements.txt
with open('dashboard/requirements.txt', 'w') as f:
    f.write('streamlit==1.38.0\npandas==2.2.2\nnumpy==2.1.1\nplotly==5.24.1\nscikit-learn==1.5.2\n')

# 2. app.py - short version for demo
app_code = """
import streamlit as st
st.title('Universal Bank Dashboard')
st.write('Files ready for deployment!')
"""
with open('dashboard/app.py', 'w') as f:
    f.write(app_code)

# 3. Sample CSV since original not accessible here
df_sample = pd.DataFrame({
    'ID': range(1,101),
    'Age': np.random.randint(25,65,100),
    'Income': np.random.randint(30,150,100),
    'Personal Loan': np.random.choice([0,1],100,p=[0.9,0.1])
})
df_sample.to_csv('dashboard/UniversalBank_sample.csv', index=False)

# 4. README.md
with open('dashboard/README.md', 'w') as f:
    f.write('# Universal Bank Personal Loan Dashboard\\n\\nDeployed with Streamlit Cloud')

# Create ZIP
with zipfile.ZipFile('universal-bank-dashboard.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk('dashboard'):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), '.'))

print('ZIP created: universal-bank-dashboard.zip')
print('Contents:')
print(os.listdir('dashboard'))