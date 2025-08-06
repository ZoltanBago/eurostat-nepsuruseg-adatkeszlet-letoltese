#!/usr/bin/env python
# coding: utf-8

# # EUROSTAT | Népsűrűség adatkészlet letöltése
# ---
# Az **Eurostat**, *Population Density*, vagyis a népsűrűség nevű adatkészletét fogjuk letölteni. 
# 
# Ehhez szükségünk lesz a következő könyvtárakra:
# 
# - Pandas
# - Pandasdmx
# 
# Amennyiben nincsenek telepítve, akkor a **`pip install pandas`** és a **`pip install pandasdmx`** parancsal kell kezdenünk.

# In[ ]:


pip install pandas


# In[ ]:


pip install pandasdmx


# ## 1. Az adatkészlet megkeresése az Eurostat oldalán
# ---
# Keressük meg az **Eurostat** oldalán a *Popular Density* nevű adatkészletet:
# 
# https://ec.europa.eu/eurostat/databrowser/view/tps00003/default/table?lang=en&category=t_demo.t_demo_ind    
#     
# *"Ratio between the annual average population and the land area. The land area concept (excluding inland waters, such as lakes, wide rivers, estuaries) should be used wherever available; if not available, then the total area (including inland waters) is used."*    
# 
# „Az éves átlagos népesség és a szárazföldi terület aránya. A szárazföldi terület fogalmát (a belvizek, például tavak, széles folyók, torkolatok nélkül) kell használni, ahol lehetséges; ha nem áll rendelkezésre, akkor a teljes területet (a belvizekkel együtt) kell használni.”
# 
# (Forrás: Eurostat)
# 
# ---   
# Az adatkészlet kódja, ami számunkra fontos:      
# 
# - tps00003
#     
# Ez a kód az **`Online data code: tps00003`** az adatkészlet fejlécében található, de az URL címben is benne van a view és a default között. 

# ## 2. A Pandas és a Pandasdmx könyvtárak importálása
# ---

# In[ ]:


# Szükséges könyvtárak importálása
import pandas as pd
import pandasdmx as sdmx


# ## 3. Csatlakozás az Eurostat API-hoz
# ---
# Az első lépésben létrehozzuk a kapcsolatot az Eurostat szerverével. 
# 
# Ehhez szükséges az **`estat = sdmx.Request('ESTAT')`** változó. 
# 
# Amennyiben valamilyen hiba történik, akkor a hibaüzenet meg fog jelenni. 

# In[ ]:


# Csatlakozunk az Eurostat API-hoz:
try:
    estat = sdmx.Request('ESTAT')

except Exception as e:
    print(f"Hiba történt a csatlakozás során: {e}")
    exit()


# ## 4. Az Eurostat adatkészlet kódjának alkalmazása
# ---
# - Létrehozunk egy változót, esetünkben a **`database_code = 'tps00003'`**, amely tartalmazza az adatkészlet kódját. Ezt az adatkészletet akarjuk letölteni.  
# 
# - A **`data_response = estat.data(resource_id=database_code)`** változó segítségével egy kérést intézünk a szerverhez.
# 
# - Mivel a kért adatok SDMX formátumban vannak, ezért a **`data = data_response.to_pandas()`** változó átalakítja nekünk pandas DataFrame-be. Az SDMX, vagyis Statistical Data and Metadata eXchange szabvány támogatja a statisztikai adatok és metaadatok cseréjét, leírását és megosztását.
# 
# - A **`print(data.head())`** megmutatja a Dataframe első 5 sorát. 
# 
# - Végül a **`data.to_csv(output_filename, index=True)`** elmenti a DataFramet egy csv fájlba.

# In[ ]:


#Az adatkészletünk kódja, a tps00003, ezt szeretnénk letölteni az Eurostat-ról:
database_code = 'tps00003'

print(f"Letöltés indítása: {database_code}...")

try:
    # Az adatok lekérdezése:
    data_response = estat.data(resource_id=database_code)
    
    # Pandas dataframe formába konvertáljuk:
    data = data_response.to_pandas()
    
    # Az adatok megjelenítése:
    print("\nSikeresen letöltött adatok:")
    
    # Az első 5 sor kiírása:
    print(data.head())
    
    # Az adatok mentése csv fájlba:
    output_filename = f"{database_code}_data.csv"
    data.to_csv(output_filename, index=True)
    
    print(f"\nAz adatok elmentve a(z) '{output_filename}' fájlba.")
    
except Exception as e:
    print(f"Hiba történt az adatok letöltése vagy feldolgozása során: {e}")


# ## 5. A kimenet
# ---
# Ha mindent jól csináltunk, akkor a következő kimenetnek kell megjelennie:
# 
#     Letöltés indítása: tps00003...
# 
#     Sikeresen letöltött adatok:
#     geo  unit     freq  TIME_PERIOD
#     AL   PER_KM2  A     2012           100.7
#                     2013           100.6
#                     2014           100.4
#                     2015           100.1
#                     2016            99.9
#     Name: value, dtype: float64
# 
#     Az adatok elmentve a(z) 'tps00003_data.csv' fájlba.
#     
# A végén egy csv fájlt kell kapnunk, amely 6 oszlopból és 442 sorból áll.  
# 
# ---

# In[ ]:




