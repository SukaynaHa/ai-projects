{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "1cce0c75-403f-4052-ac7f-3c75645e0c3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74fb0d11-26d2-4adb-8000-4e3d89a30571",
   "metadata": {},
   "source": [
    "# 🧠 Preparing the Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "fe1dc806-5981-46e8-b445-7dca6330fa6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Path to dataset files: C:\\Users\\Sakena\\.cache\\kagglehub\\datasets\\sulianova\\cardiovascular-disease-dataset\\versions\\1\n"
     ]
    }
   ],
   "source": [
    "import kagglehub\n",
    "\n",
    "# Download latest version\n",
    "path = kagglehub.dataset_download(\"sulianova/cardiovascular-disease-dataset\")\n",
    "\n",
    "print(\"Path to dataset files:\", path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "965db3d3-0fb0-4665-8f1b-b130ed205fb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df = pd.read_csv('cardio_train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "id": "e899641c-6e17-416b-8919-4291479f3b9c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id;age;gender;height;weight;ap_hi;ap_lo;cholesterol;gluc;smoke;alco;active;cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0;18393;2;168;62.0;110;80;1;1;0;0;1;0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1;20228;1;156;85.0;140;90;3;1;0;0;1;1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2;18857;1;165;64.0;130;70;3;1;0;0;0;1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3;17623;2;169;82.0;150;100;1;1;0;0;1;1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4;17474;1;156;56.0;100;60;1;1;0;0;0;0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  id;age;gender;height;weight;ap_hi;ap_lo;cholesterol;gluc;smoke;alco;active;cardio\n",
       "0              0;18393;2;168;62.0;110;80;1;1;0;0;1;0                               \n",
       "1              1;20228;1;156;85.0;140;90;3;1;0;0;1;1                               \n",
       "2              2;18857;1;165;64.0;130;70;3;1;0;0;0;1                               \n",
       "3             3;17623;2;169;82.0;150;100;1;1;0;0;1;1                               \n",
       "4              4;17474;1;156;56.0;100;60;1;1;0;0;0;0                               "
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "id": "f061431f-67d3-43c3-b9fe-85b614bba96a",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_df = pd.read_csv('cardio_train.csv', sep=';')  # Replace with actual delimiter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "id": "098130d2-5924-400c-8637-a85da868b9f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>18393</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>20228</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>18857</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>17623</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>17474</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id    age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  \\\n",
       "0   0  18393       2     168    62.0    110     80            1     1      0   \n",
       "1   1  20228       1     156    85.0    140     90            3     1      0   \n",
       "2   2  18857       1     165    64.0    130     70            3     1      0   \n",
       "3   3  17623       2     169    82.0    150    100            1     1      0   \n",
       "4   4  17474       1     156    56.0    100     60            1     1      0   \n",
       "\n",
       "   alco  active  cardio  \n",
       "0     0       1       0  \n",
       "1     0       1       1  \n",
       "2     0       0       1  \n",
       "3     0       1       1  \n",
       "4     0       0       0  "
      ]
     },
     "execution_count": 194,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "id": "54a4b0c2-c087-4635-a1b5-5da7e69c5b4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "old_df = pd.read_csv('heart_attack_prediction_dataset.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "ac497020-8ce0-4731-96cc-1f424804b187",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Patient ID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Cholesterol</th>\n",
       "      <th>Blood Pressure</th>\n",
       "      <th>Heart Rate</th>\n",
       "      <th>Diabetes</th>\n",
       "      <th>Family History</th>\n",
       "      <th>Smoking</th>\n",
       "      <th>Obesity</th>\n",
       "      <th>...</th>\n",
       "      <th>Sedentary Hours Per Day</th>\n",
       "      <th>Income</th>\n",
       "      <th>BMI</th>\n",
       "      <th>Triglycerides</th>\n",
       "      <th>Physical Activity Days Per Week</th>\n",
       "      <th>Sleep Hours Per Day</th>\n",
       "      <th>Country</th>\n",
       "      <th>Continent</th>\n",
       "      <th>Hemisphere</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>BMW7812</td>\n",
       "      <td>67</td>\n",
       "      <td>Male</td>\n",
       "      <td>208</td>\n",
       "      <td>158/88</td>\n",
       "      <td>72</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>6.615001</td>\n",
       "      <td>261404</td>\n",
       "      <td>31.251233</td>\n",
       "      <td>286</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>Argentina</td>\n",
       "      <td>South America</td>\n",
       "      <td>Southern Hemisphere</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>CZE1114</td>\n",
       "      <td>21</td>\n",
       "      <td>Male</td>\n",
       "      <td>389</td>\n",
       "      <td>165/93</td>\n",
       "      <td>98</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>4.963459</td>\n",
       "      <td>285768</td>\n",
       "      <td>27.194973</td>\n",
       "      <td>235</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>Canada</td>\n",
       "      <td>North America</td>\n",
       "      <td>Northern Hemisphere</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "  Patient ID  Age   Sex  Cholesterol Blood Pressure  Heart Rate  Diabetes  \\\n",
       "0    BMW7812   67  Male          208         158/88          72         0   \n",
       "1    CZE1114   21  Male          389         165/93          98         1   \n",
       "\n",
       "   Family History  Smoking  Obesity  ...  Sedentary Hours Per Day  Income  \\\n",
       "0               0        1        0  ...                 6.615001  261404   \n",
       "1               1        1        1  ...                 4.963459  285768   \n",
       "\n",
       "         BMI  Triglycerides  Physical Activity Days Per Week  \\\n",
       "0  31.251233            286                                0   \n",
       "1  27.194973            235                                1   \n",
       "\n",
       "   Sleep Hours Per Day    Country      Continent           Hemisphere  \\\n",
       "0                    6  Argentina  South America  Southern Hemisphere   \n",
       "1                    7     Canada  North America  Northern Hemisphere   \n",
       "\n",
       "   Heart Attack Risk  \n",
       "0                  0  \n",
       "1                  0  \n",
       "\n",
       "[2 rows x 26 columns]"
      ]
     },
     "execution_count": 196,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "old_df.head(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c3f0050-d156-4590-aa03-6326c2446c91",
   "metadata": {},
   "source": [
    "# 📉 Data Cleaning and Optimization\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "id": "40859033-a186-4a97-bae7-034c302c274a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 70000 entries, 0 to 69999\n",
      "Data columns (total 13 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   id           70000 non-null  int64  \n",
      " 1   age          70000 non-null  int64  \n",
      " 2   gender       70000 non-null  int64  \n",
      " 3   height       70000 non-null  int64  \n",
      " 4   weight       70000 non-null  float64\n",
      " 5   ap_hi        70000 non-null  int64  \n",
      " 6   ap_lo        70000 non-null  int64  \n",
      " 7   cholesterol  70000 non-null  int64  \n",
      " 8   gluc         70000 non-null  int64  \n",
      " 9   smoke        70000 non-null  int64  \n",
      " 10  alco         70000 non-null  int64  \n",
      " 11  active       70000 non-null  int64  \n",
      " 12  cardio       70000 non-null  int64  \n",
      "dtypes: float64(1), int64(12)\n",
      "memory usage: 6.9 MB\n"
     ]
    }
   ],
   "source": [
    "new_df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "id": "ba1de962-5efd-4d41-9c7f-8874fd2fabc8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    168\n",
       "1    156\n",
       "2    165\n",
       "3    169\n",
       "4    156\n",
       "Name: height, dtype: int64"
      ]
     },
     "execution_count": 198,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['height'].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "id": "09e90981-a36e-4cf5-8aee-f210bb2e0dea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0         62.0\n",
       "1         85.0\n",
       "2         64.0\n",
       "3         82.0\n",
       "4         56.0\n",
       "         ...  \n",
       "69995     76.0\n",
       "69996    126.0\n",
       "69997    105.0\n",
       "69998     72.0\n",
       "69999     72.0\n",
       "Name: weight, Length: 70000, dtype: float64"
      ]
     },
     "execution_count": 199,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['weight']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "id": "69b821ad-f68b-4c7b-bda8-07e4449b34e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo',\n",
       "       'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'BMI'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 200,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 1: Calculate BMI in new data \n",
    "new_df['BMI'] = new_df['weight'] / (new_df['height']/100)**2\n",
    "\n",
    "new_df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "id": "f08a9fcd-44d5-465d-9ca9-44c2b10f2609",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Patient ID', 'Age', 'Sex', 'Cholesterol', 'Blood Pressure',\n",
       "       'Heart Rate', 'Diabetes', 'Family History', 'Smoking', 'Obesity',\n",
       "       'Alcohol Consumption', 'Exercise Hours Per Week', 'Diet',\n",
       "       'Previous Heart Problems', 'Medication Use', 'Stress Level',\n",
       "       'Sedentary Hours Per Day', 'Income', 'BMI', 'Triglycerides',\n",
       "       'Physical Activity Days Per Week', 'Sleep Hours Per Day', 'Country',\n",
       "       'Continent', 'Hemisphere', 'Heart Attack Risk'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 201,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "old_df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "id": "1f49fc6a-0b94-4bd4-8efc-710c1568b509",
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Step 2: Select columns to merge from old data\n",
    "# # Define columns to merge (EXCLUDING 'Patient ID')\n",
    "# cols_to_merge = ['Triglycerides', 'Physical Activity Days Per Week', 'Stress Level', 'Sleep Hours Per Day', 'Family History']\n",
    "\n",
    "# # Merge without 'Patient ID'\n",
    "# merged_df = pd.merge(\n",
    "#     new_df, \n",
    "#     old_df[cols_to_merge],  # No 'Patient ID' here\n",
    "#     left_index=True,         # Use index if no key column exists\n",
    "#     right_index=True, \n",
    "#     how='left'\n",
    "# )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "id": "874ccc83-17ec-46b9-a680-2b56d109c1d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# merged_df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "id": "d68c6347-7379-4618-81fd-6db1a6c4ebae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# merged_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "id": "7542e77a-636d-4f66-89cd-cb357b2e8ad2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# merged_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "id": "18ad389f-46a4-4059-a229-ad2878c117ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gluc\n",
       "1    59479\n",
       "3     5331\n",
       "2     5190\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 206,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['gluc'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "id": "7b385734-1e07-4bc7-ae3c-d314884a3081",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    1\n",
       "2    1\n",
       "3    1\n",
       "4    1\n",
       "5    2\n",
       "6    1\n",
       "7    3\n",
       "8    1\n",
       "9    1\n",
       "Name: gluc, dtype: int64"
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['gluc'].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "id": "c50bc391-46bb-4b59-9201-e627822f7b23",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a diabetes_signal based on gluc value\n",
    "new_df['diabetes_signal'] = new_df['gluc'].apply(lambda x: 1 if x > 1 else 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "id": "3629c461-f1b6-43fd-bf78-361e630c83e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "cols_to_merge = ['Triglycerides', 'Physical Activity Days Per Week', 'Family History']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "id": "62cd7ff7-5d68-4036-afa9-147ccc5429ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                    No Heart attak risk  Has heart attak risk  Total\n",
      "No Family History                  2848                  1595   4443\n",
      "Has Family History                 2776                  1544   4320\n",
      "Total                              5624                  3139   8763\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# - 'Family History': 1 = لديه عامل وراثي, 0 = لا يوجد\n",
    "# - 'cardio': 1 = لديه ذبحة قلبية, 0 = لا يوجد\n",
    "# جدول تقاطعي (Cross-Tabulation)\n",
    "contingency_table = pd.crosstab(\n",
    "    old_df['Family History'], \n",
    "    old_df['Heart Attack Risk'], \n",
    "    margins=True,\n",
    "    margins_name=\"Total\"\n",
    ")\n",
    "contingency_table.columns = [\"No Heart attak risk\", \"Has heart attak risk\", \"Total\"]\n",
    "contingency_table.index = [\"No Family History\", \"Has Family History\", \"Total\"]\n",
    "print(contingency_table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "id": "ec525ca7-48cf-4bf1-bd2d-2356ff13ae28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "النسب المئوية لكل فئة:\n",
      "                    No Risk  Has Risk\n",
      "No Family History      64.1      35.9\n",
      "Has Family History     64.3      35.7\n"
     ]
    }
   ],
   "source": [
    "#نسبة الاصابة هل تزداد حسب تاريخ العائلة الصحي أم لا\n",
    "# 2. تسمية الصفوف والأعمدة\n",
    "contingency_table.columns = [\"No Risk\", \"Has Risk\", \"Total\"]\n",
    "contingency_table.index = [\"No Family History\", \"Has Family History\", \"Total\"]\n",
    "\n",
    "# 3. حساب النسب المئوية\n",
    "valid_rows = contingency_table.iloc[:-1, :-1]  # استبعاد صف وإجمالي العمود\n",
    "valid_totals = contingency_table.iloc[:-1, -1]  # إجمالي كل فئة\n",
    "\n",
    "# 4. تجنب القسمة على صفر\n",
    "valid_totals = valid_totals.replace(0, 1)  # إذا كان الإجمالي صفراً، استبدله بـ 1\n",
    "\n",
    "# 5. حساب النسب المئوية\n",
    "percentages = valid_rows.div(valid_totals, axis=0) * 100\n",
    "percentages = percentages.round(1)\n",
    "\n",
    "# 6. عرض النتائج\n",
    "print(\"\\nالنسب المئوية لكل فئة:\")\n",
    "print(percentages)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb95e491-c449-4219-b9a5-4631fa4549e1",
   "metadata": {},
   "source": [
    "اذا بغض النظر عن التاريخ الصحي للعائلة يوجد احتمال 36 بالمئة لحصول سكتة قلبية او اصابة بامراض القلب "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "id": "c55c1c3c-3044-4961-a94f-7b758bb92045",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# دالة لتوليد قيمة Family_History بناءً على قيمة cardio\n",
    "def assign_family_history(row):\n",
    "    # احتمال وجود تاريخ عائلي بناءً على التحليل (تقريبًا 36%)\n",
    "    probability = 0.36\n",
    "    return np.random.choice([1, 0], p=[probability, 1 - probability])\n",
    "\n",
    "# إنشاء عمود Family_History باستخدام الدالة\n",
    "new_df['Family_History'] = new_df.apply(assign_family_history, axis=1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "id": "a1359aa5-6f38-4989-b9fd-39b920efd4f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Family_History\n",
       "0    44684\n",
       "1    25316\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df['Family_History'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "id": "ae28c99c-e6a5-4b88-92ac-bbdf51ae8f80",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData = new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "id": "734345d5-ed68-4f1b-91bc-29687b243938",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>18393</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>21.967120</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>20228</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>34.927679</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>18857</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>23.507805</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>17623</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>28.710479</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>17474</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.011177</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id    age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  \\\n",
       "0   0  18393       2     168    62.0    110     80            1     1      0   \n",
       "1   1  20228       1     156    85.0    140     90            3     1      0   \n",
       "2   2  18857       1     165    64.0    130     70            3     1      0   \n",
       "3   3  17623       2     169    82.0    150    100            1     1      0   \n",
       "4   4  17474       1     156    56.0    100     60            1     1      0   \n",
       "\n",
       "   alco  active  cardio        BMI  diabetes_signal  Family_History  \n",
       "0     0       1       0  21.967120                0               1  \n",
       "1     0       1       1  34.927679                0               1  \n",
       "2     0       0       1  23.507805                0               0  \n",
       "3     0       1       1  28.710479                0               1  \n",
       "4     0       0       0  23.011177                0               1  "
      ]
     },
     "execution_count": 215,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "id": "cc57f1a4-4016-4bc0-b1cf-8b82c9dd1b50",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData['Heart Attack Risk'] = hearGardaData['cardio']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "id": "942ee427-dea8-487c-a7e8-17c5081d968f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    18393\n",
       "1    20228\n",
       "2    18857\n",
       "3    17623\n",
       "4    17474\n",
       "Name: age, dtype: int64"
      ]
     },
     "execution_count": 217,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData['age'].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "id": "47639a68-813f-44d6-8a28-cf8ca916dae2",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData['age'] =(hearGardaData['age'] / 365.25).round().astype(int)  # قسمة على عدد الأيام في السنة (مع احتساب السنوات الكبيسة)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "id": "a00d84df-ddaa-4111-a5e9-1f413975881d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>21.967120</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>55</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>34.927679</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>23.507805</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>48</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>28.710479</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>48</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.011177</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  \\\n",
       "0   0   50       2     168    62.0    110     80            1     1      0   \n",
       "1   1   55       1     156    85.0    140     90            3     1      0   \n",
       "2   2   52       1     165    64.0    130     70            3     1      0   \n",
       "3   3   48       2     169    82.0    150    100            1     1      0   \n",
       "4   4   48       1     156    56.0    100     60            1     1      0   \n",
       "\n",
       "   alco  active  cardio        BMI  diabetes_signal  Family_History  \\\n",
       "0     0       1       0  21.967120                0               1   \n",
       "1     0       1       1  34.927679                0               1   \n",
       "2     0       0       1  23.507805                0               0   \n",
       "3     0       1       1  28.710479                0               1   \n",
       "4     0       0       0  23.011177                0               1   \n",
       "\n",
       "   Heart Attack Risk  \n",
       "0                  0  \n",
       "1                  1  \n",
       "2                  1  \n",
       "3                  1  \n",
       "4                  0  "
      ]
     },
     "execution_count": 219,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "id": "85e1f3e8-3428-4f11-a303-5ded58367028",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Assuming you have a DataFrame named 'df'\n",
    "hearGardaData.rename(columns={'ap_hi': 'Systolic'}, inplace=True)\n",
    "hearGardaData.rename(columns={'ap_lo': 'Diastolic'}, inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "id": "8760910a-c3c9-4b42-99b8-d2fc9165e82f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>21.967120</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>55</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>34.927679</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>23.507805</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>48</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>28.710479</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>48</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.011177</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  age  gender  height  weight  Systolic  Diastolic  cholesterol  gluc  \\\n",
       "0   0   50       2     168    62.0       110         80            1     1   \n",
       "1   1   55       1     156    85.0       140         90            3     1   \n",
       "2   2   52       1     165    64.0       130         70            3     1   \n",
       "3   3   48       2     169    82.0       150        100            1     1   \n",
       "4   4   48       1     156    56.0       100         60            1     1   \n",
       "\n",
       "   smoke  alco  active  cardio        BMI  diabetes_signal  Family_History  \\\n",
       "0      0     0       1       0  21.967120                0               1   \n",
       "1      0     0       1       1  34.927679                0               1   \n",
       "2      0     0       0       1  23.507805                0               0   \n",
       "3      0     0       1       1  28.710479                0               1   \n",
       "4      0     0       0       0  23.011177                0               1   \n",
       "\n",
       "   Heart Attack Risk  \n",
       "0                  0  \n",
       "1                  1  \n",
       "2                  1  \n",
       "3                  1  \n",
       "4                  0  "
      ]
     },
     "execution_count": 221,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "id": "69fc4a81-07ee-42bc-9c9f-15a6c32028d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>69995</th>\n",
       "      <td>99993</td>\n",
       "      <td>53</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>76.0</td>\n",
       "      <td>120</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>26.927438</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69996</th>\n",
       "      <td>99995</td>\n",
       "      <td>62</td>\n",
       "      <td>1</td>\n",
       "      <td>158</td>\n",
       "      <td>126.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>50.472681</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69997</th>\n",
       "      <td>99996</td>\n",
       "      <td>52</td>\n",
       "      <td>2</td>\n",
       "      <td>183</td>\n",
       "      <td>105.0</td>\n",
       "      <td>180</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>31.353579</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69998</th>\n",
       "      <td>99998</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>163</td>\n",
       "      <td>72.0</td>\n",
       "      <td>135</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>27.099251</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69999</th>\n",
       "      <td>99999</td>\n",
       "      <td>56</td>\n",
       "      <td>1</td>\n",
       "      <td>170</td>\n",
       "      <td>72.0</td>\n",
       "      <td>120</td>\n",
       "      <td>80</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>24.913495</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          id  age  gender  height  weight  Systolic  Diastolic  cholesterol  \\\n",
       "69995  99993   53       2     168    76.0       120         80            1   \n",
       "69996  99995   62       1     158   126.0       140         90            2   \n",
       "69997  99996   52       2     183   105.0       180         90            3   \n",
       "69998  99998   61       1     163    72.0       135         80            1   \n",
       "69999  99999   56       1     170    72.0       120         80            2   \n",
       "\n",
       "       gluc  smoke  alco  active  cardio        BMI  diabetes_signal  \\\n",
       "69995     1      1     0       1       0  26.927438                0   \n",
       "69996     2      0     0       1       1  50.472681                1   \n",
       "69997     1      0     1       0       1  31.353579                0   \n",
       "69998     2      0     0       0       1  27.099251                1   \n",
       "69999     1      0     0       1       0  24.913495                0   \n",
       "\n",
       "       Family_History  Heart Attack Risk  \n",
       "69995               1                  0  \n",
       "69996               0                  1  \n",
       "69997               1                  1  \n",
       "69998               0                  1  \n",
       "69999               0                  0  "
      ]
     },
     "execution_count": 222,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.tail(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "id": "fa80dad3-9079-468b-a3c6-1261348bea76",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData=hearGardaData.drop(columns=['id','cardio'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "552c62ea-96bd-4104-bc4c-c4b38198d3d6",
   "metadata": {},
   "source": [
    "# 🔍Exploratory Data Analysis (EDA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "id": "2960c19c-ac5f-45c1-b101-51e6cb9aa1df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age                  0\n",
       "gender               0\n",
       "height               0\n",
       "weight               0\n",
       "Systolic             0\n",
       "Diastolic            0\n",
       "cholesterol          0\n",
       "gluc                 0\n",
       "smoke                0\n",
       "alco                 0\n",
       "active               0\n",
       "BMI                  0\n",
       "diabetes_signal      0\n",
       "Family_History       0\n",
       "Heart Attack Risk    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 224,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "id": "4b32ad17-9501-48ab-bc5b-6506728193c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>21.967120</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>34.927679</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.507805</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>48</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>28.710479</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>48</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.011177</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69995</th>\n",
       "      <td>53</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>76.0</td>\n",
       "      <td>120</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>26.927438</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69996</th>\n",
       "      <td>62</td>\n",
       "      <td>1</td>\n",
       "      <td>158</td>\n",
       "      <td>126.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>50.472681</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69997</th>\n",
       "      <td>52</td>\n",
       "      <td>2</td>\n",
       "      <td>183</td>\n",
       "      <td>105.0</td>\n",
       "      <td>180</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>31.353579</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69998</th>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>163</td>\n",
       "      <td>72.0</td>\n",
       "      <td>135</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>27.099251</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69999</th>\n",
       "      <td>56</td>\n",
       "      <td>1</td>\n",
       "      <td>170</td>\n",
       "      <td>72.0</td>\n",
       "      <td>120</td>\n",
       "      <td>80</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>24.913495</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>70000 rows × 15 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       age  gender  height  weight  Systolic  Diastolic  cholesterol  gluc  \\\n",
       "0       50       2     168    62.0       110         80            1     1   \n",
       "1       55       1     156    85.0       140         90            3     1   \n",
       "2       52       1     165    64.0       130         70            3     1   \n",
       "3       48       2     169    82.0       150        100            1     1   \n",
       "4       48       1     156    56.0       100         60            1     1   \n",
       "...    ...     ...     ...     ...       ...        ...          ...   ...   \n",
       "69995   53       2     168    76.0       120         80            1     1   \n",
       "69996   62       1     158   126.0       140         90            2     2   \n",
       "69997   52       2     183   105.0       180         90            3     1   \n",
       "69998   61       1     163    72.0       135         80            1     2   \n",
       "69999   56       1     170    72.0       120         80            2     1   \n",
       "\n",
       "       smoke  alco  active        BMI  diabetes_signal  Family_History  \\\n",
       "0          0     0       1  21.967120                0               1   \n",
       "1          0     0       1  34.927679                0               1   \n",
       "2          0     0       0  23.507805                0               0   \n",
       "3          0     0       1  28.710479                0               1   \n",
       "4          0     0       0  23.011177                0               1   \n",
       "...      ...   ...     ...        ...              ...             ...   \n",
       "69995      1     0       1  26.927438                0               1   \n",
       "69996      0     0       1  50.472681                1               0   \n",
       "69997      0     1       0  31.353579                0               1   \n",
       "69998      0     0       0  27.099251                1               0   \n",
       "69999      0     0       1  24.913495                0               0   \n",
       "\n",
       "       Heart Attack Risk  \n",
       "0                      0  \n",
       "1                      1  \n",
       "2                      1  \n",
       "3                      1  \n",
       "4                      0  \n",
       "...                  ...  \n",
       "69995                  0  \n",
       "69996                  1  \n",
       "69997                  1  \n",
       "69998                  1  \n",
       "69999                  0  \n",
       "\n",
       "[70000 rows x 15 columns]"
      ]
     },
     "execution_count": 225,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.dropna()  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "id": "90a994cf-4a81-4c4b-b01c-7f08d7498073",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age                    int64\n",
       "gender                 int64\n",
       "height                 int64\n",
       "weight               float64\n",
       "Systolic               int64\n",
       "Diastolic              int64\n",
       "cholesterol            int64\n",
       "gluc                   int64\n",
       "smoke                  int64\n",
       "alco                   int64\n",
       "active                 int64\n",
       "BMI                  float64\n",
       "diabetes_signal        int64\n",
       "Family_History         int64\n",
       "Heart Attack Risk      int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 226,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "id": "a27448f2-3b77-4776-9a37-86a79f90d226",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "      <td>70000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>53.303157</td>\n",
       "      <td>1.349571</td>\n",
       "      <td>164.359229</td>\n",
       "      <td>74.205690</td>\n",
       "      <td>128.817286</td>\n",
       "      <td>96.630414</td>\n",
       "      <td>1.366871</td>\n",
       "      <td>1.226457</td>\n",
       "      <td>0.088129</td>\n",
       "      <td>0.053771</td>\n",
       "      <td>0.803729</td>\n",
       "      <td>27.556513</td>\n",
       "      <td>0.150300</td>\n",
       "      <td>0.361657</td>\n",
       "      <td>0.499700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6.760171</td>\n",
       "      <td>0.476838</td>\n",
       "      <td>8.210126</td>\n",
       "      <td>14.395757</td>\n",
       "      <td>154.011419</td>\n",
       "      <td>188.472530</td>\n",
       "      <td>0.680250</td>\n",
       "      <td>0.572270</td>\n",
       "      <td>0.283484</td>\n",
       "      <td>0.225568</td>\n",
       "      <td>0.397179</td>\n",
       "      <td>6.091511</td>\n",
       "      <td>0.357368</td>\n",
       "      <td>0.480484</td>\n",
       "      <td>0.500003</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>30.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>55.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>-150.000000</td>\n",
       "      <td>-70.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.471784</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>48.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>159.000000</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>23.875115</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>54.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>165.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>26.374068</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>58.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>170.000000</td>\n",
       "      <td>82.000000</td>\n",
       "      <td>140.000000</td>\n",
       "      <td>90.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>30.222222</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>65.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>250.000000</td>\n",
       "      <td>200.000000</td>\n",
       "      <td>16020.000000</td>\n",
       "      <td>11000.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>298.666667</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age        gender        height        weight      Systolic  \\\n",
       "count  70000.000000  70000.000000  70000.000000  70000.000000  70000.000000   \n",
       "mean      53.303157      1.349571    164.359229     74.205690    128.817286   \n",
       "std        6.760171      0.476838      8.210126     14.395757    154.011419   \n",
       "min       30.000000      1.000000     55.000000     10.000000   -150.000000   \n",
       "25%       48.000000      1.000000    159.000000     65.000000    120.000000   \n",
       "50%       54.000000      1.000000    165.000000     72.000000    120.000000   \n",
       "75%       58.000000      2.000000    170.000000     82.000000    140.000000   \n",
       "max       65.000000      2.000000    250.000000    200.000000  16020.000000   \n",
       "\n",
       "          Diastolic   cholesterol          gluc         smoke          alco  \\\n",
       "count  70000.000000  70000.000000  70000.000000  70000.000000  70000.000000   \n",
       "mean      96.630414      1.366871      1.226457      0.088129      0.053771   \n",
       "std      188.472530      0.680250      0.572270      0.283484      0.225568   \n",
       "min      -70.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "25%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "50%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "75%       90.000000      2.000000      1.000000      0.000000      0.000000   \n",
       "max    11000.000000      3.000000      3.000000      1.000000      1.000000   \n",
       "\n",
       "             active           BMI  diabetes_signal  Family_History  \\\n",
       "count  70000.000000  70000.000000     70000.000000    70000.000000   \n",
       "mean       0.803729     27.556513         0.150300        0.361657   \n",
       "std        0.397179      6.091511         0.357368        0.480484   \n",
       "min        0.000000      3.471784         0.000000        0.000000   \n",
       "25%        1.000000     23.875115         0.000000        0.000000   \n",
       "50%        1.000000     26.374068         0.000000        0.000000   \n",
       "75%        1.000000     30.222222         0.000000        1.000000   \n",
       "max        1.000000    298.666667         1.000000        1.000000   \n",
       "\n",
       "       Heart Attack Risk  \n",
       "count       70000.000000  \n",
       "mean            0.499700  \n",
       "std             0.500003  \n",
       "min             0.000000  \n",
       "25%             0.000000  \n",
       "50%             0.000000  \n",
       "75%             1.000000  \n",
       "max             1.000000  "
      ]
     },
     "execution_count": 227,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6fb19bbb-d95f-4885-8e7c-9066f4414938",
   "metadata": {},
   "source": [
    "### outliers Systolic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 228,
   "id": "eb6532fc-73fb-426f-b657-1f66449b9e61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>567</th>\n",
       "      <td>14</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>927</th>\n",
       "      <td>14</td>\n",
       "      <td>90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>979</th>\n",
       "      <td>11</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1600</th>\n",
       "      <td>12</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1627</th>\n",
       "      <td>14</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1772</th>\n",
       "      <td>11</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1876</th>\n",
       "      <td>902</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2014</th>\n",
       "      <td>906</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2167</th>\n",
       "      <td>14</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2203</th>\n",
       "      <td>12</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Systolic  Diastolic\n",
       "567         14         90\n",
       "927         14         90\n",
       "979         11         80\n",
       "1600        12         80\n",
       "1627        14         80\n",
       "1772        11         60\n",
       "1876       902         60\n",
       "2014       906          0\n",
       "2167        14         80\n",
       "2203        12         80"
      ]
     },
     "execution_count": 228,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.loc[(hearGardaData['Systolic'] <= 50) | (hearGardaData['Systolic'] >= 250), ['Systolic', 'Diastolic']].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "id": "6e11d046-ec97-484d-91e2-5f6521fd4af7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "228"
      ]
     },
     "execution_count": 229,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(hearGardaData.loc[(hearGardaData['Systolic'] <= 50) | (hearGardaData['Systolic'] >= 250), ['Systolic', 'Diastolic']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "id": "6256c3e7-c9b7-4cae-ba8b-60fa861cc079",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(120)"
      ]
     },
     "execution_count": 230,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "systolic_mode = hearGardaData['Systolic'].mode()[0]\n",
    "systolic_mode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "id": "fe51d2cc-d26a-47d1-8063-dde0d0abf77f",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData.loc[(hearGardaData['Systolic'] <= 50) | (hearGardaData['Systolic'] >= 250), 'Systolic'] = systolic_mode"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "242c6dfd-f8f8-4c25-ba5c-532f992344f4",
   "metadata": {},
   "source": [
    "### outliers Diastolic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "id": "fb9d624f-a7e9-4edd-bb98-af17682a27cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>228</th>\n",
       "      <td>160</td>\n",
       "      <td>1100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>241</th>\n",
       "      <td>160</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>260</th>\n",
       "      <td>140</td>\n",
       "      <td>800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>329</th>\n",
       "      <td>160</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>345</th>\n",
       "      <td>140</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>418</th>\n",
       "      <td>150</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>473</th>\n",
       "      <td>150</td>\n",
       "      <td>1033</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>474</th>\n",
       "      <td>120</td>\n",
       "      <td>150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>559</th>\n",
       "      <td>200</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>613</th>\n",
       "      <td>140</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Systolic  Diastolic\n",
       "228       160       1100\n",
       "241       160       1000\n",
       "260       140        800\n",
       "329       160       1000\n",
       "345       140       1000\n",
       "418       150         30\n",
       "473       150       1033\n",
       "474       120        150\n",
       "559       200       1000\n",
       "613       140       1000"
      ]
     },
     "execution_count": 232,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.loc[(hearGardaData['Diastolic'] <= 30) | (hearGardaData['Diastolic'] >= 150), ['Systolic', 'Diastolic']].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "id": "a788c6e1-f552-4740-b075-ad0328530009",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 233,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(hearGardaData.loc[(hearGardaData['Diastolic'] <= 30) | (hearGardaData['Diastolic'] >= 150), ['Systolic', 'Diastolic']].head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "id": "ccb5abd5-d96a-4976-9cf3-3a42d8ced21d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(80)"
      ]
     },
     "execution_count": 234,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Diastolic_mode = hearGardaData['Diastolic'].mode()[0]\n",
    "Diastolic_mode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "id": "5aac4358-0a0e-4b13-94be-2558aab28dc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData.loc[(hearGardaData['Diastolic'] <= 30) | (hearGardaData['Diastolic'] >= 150), 'Diastolic'] = systolic_mode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "9a784850-abd5-4005-8fe2-1bd81509ab9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# #option 2 \n",
    "# # استبدال بالقيمة المتوسطة (median)\n",
    "# diastolic_median = hearGardaData['Diastolic'].median()\n",
    "# hearGardaData.loc[(hearGardaData['Diastolic'] <= 30) | (hearGardaData['Diastolic'] >= 150), 'Diastolic'] = diastolic_median\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d908247-d934-41d5-9ef2-6486200318c8",
   "metadata": {},
   "source": [
    "### height & weight"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "id": "ff15e2bd-b28b-4bc4-815c-89b2dd22bd93",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count    70000.000000\n",
      "mean        74.205690\n",
      "std         14.395757\n",
      "min         10.000000\n",
      "25%         65.000000\n",
      "50%         72.000000\n",
      "75%         82.000000\n",
      "max        200.000000\n",
      "Name: weight, dtype: float64\n",
      "count    70000.000000\n",
      "mean       164.359229\n",
      "std          8.210126\n",
      "min         55.000000\n",
      "25%        159.000000\n",
      "50%        165.000000\n",
      "75%        170.000000\n",
      "max        250.000000\n",
      "Name: height, dtype: float64\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAHHCAYAAACiOWx7AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAN81JREFUeJzt3QucTfX+//HPMBiXXCaMkWuSO+OWCOXSUOokfp2UonKJQ4UicgklHeWScjh1Cv2i5HeiQu6pmMldhCaKqIapXMZtXGbW//H5nrP2f+8xly/NZe89r+fjsexZa31n77X2mpn99r2tEMdxHAEAAECG8mW8GwAAAIrQBAAAYIHQBAAAYIHQBAAAYIHQBAAAYIHQBAAAYIHQBAAAYIHQBAAAYIHQBAAAYIHQBCDLPfLII1KlSpWr/t5ixYqJP5gzZ46EhITIwYMHc/w909fU13711VclJ4wdO9a8HoD0EZqAPOLDDz80H4qLFi26bF+DBg3Mvs8///yyfZUqVZIWLVqIvzl79qz5oF+3bp1VeS2n5+guhQoVkoiICLntttvkpZdekt9++y1Xjisn+fOxAYGA0ATkES1btjSP69ev99memJgo3377rYSGhsqGDRt89h0+fNgs7vfaeuuttyQuLk6yOwCMGzfuigPAk08+Kf/7v/8rb775pgwdOlTCw8Pl+eefl1q1asnatWt9yj788MNy7tw5qVy5crYfV26/Z6NGjTLnCiB9oRnsAxBEypcvL1WrVr0sNMXGxoret/u+++67bJ+7fqWhqUCBAuKvWrVqJf/zP//js+2bb76R6Oho6dq1q+zZs0ciIyPN9vz585slO505c0aKFi2a6++ZhmZdAKSPmiYgD9Hws337dp8aBa1dqlOnjtxxxx3y9ddfS0pKis8+bcq65ZZbPNvee+89ady4sRQuXNjU0nTr1s3URmXWp+mPP/4wNTfFixeXkiVLSs+ePU1Y0efXvkOp/fLLL9K5c2fTv6lMmTLyzDPPSHJysqe/j25TWnPiNrlp09PV0ObJadOmyYkTJ+SNN97IsE/Tli1bpEOHDlK6dGnzHmgQfeyxx6yOy+2v9cMPP8idd94p11xzjXTv3j3d98w1depUU9ulr3frrbeamkFv2sSoS2rez5nZsaXVp+nSpUvywgsvSLVq1Uxzpj7Xc889J+fPn/cpp9vvuusuE7JvuukmCQsLk+uvv17efffdK7gKgP8jNAF5LDRdvHhRNm7c6BOMtM+SLidPnvT5QNZ9NWvWlGuvvdasT5gwQXr06CHVq1eXKVOmyKBBg2TNmjXSunVrEzjSo0Hs7rvvlvfff9+EJX2e+Ph483VaNBxpMNHX1Y7QGhQmT55smtSUfvjPnDnTfH3vvfea5jZdunTpctXvjdY+aShZuXJlumUSEhJMjZQGkOHDh8vrr79uQo+GTdvj0iCi51a2bFlzblq7lRENHtOnT5cBAwbIiBEjzPVp27atHD169IrO72res969e8uYMWOkUaNGJrjpdZg4caIJyqnt37/fvIe33367uValSpUyoW337t1XdJyAX3MA5Bm7d+929Nf+hRdeMOsXL150ihYt6sydO9esR0REODNmzDBfJyYmOvnz53f69Olj1g8ePGjWJ0yY4POcu3btckJDQ3229+zZ06lcubJn/d///rd53WnTpnm2JScnO23btjXbZ8+e7fO9um38+PE+r9OwYUOncePGnvXffvvNlHv++eetzv3zzz835RcuXJhumQYNGjilSpXyrOtx6fccOHDArC9atMisb968Od3nyOi43HMbPnx4mvu83zN9TS1buHBh5+eff/Zs37hxo9k+ePBgz7Zbb73VLJk9Z0bHptu8PxJ27Nhh1nv37u1T7plnnjHb165d69mmr6HbvvzyS8+2hIQEp1ChQs7TTz+dzjsFBB5qmoA8RDs7a+2N21dJm8e0T407Ok4f3c7g2tdJa3zc/kwfffSRqTH661//Kr///rtnKVeunKl5SmvknWv58uWmz06fPn082/Lly2dqT9LTr1+/y/oi/fjjj5KdtOns1KlT6e7XZkW1ZMkSU2N3tfr3729dVpsor7vuOs+6Nn81a9ZMli1bJtnJff4hQ4b4bH/66afN49KlS322165d21wj75qtGjVqZPs1A3ISoQnIQ7TPigYjt++SBiRtJrrhhhsuC03uoxua9u3bZzqMa0DSD0TvZe/evabpKj0//fST6VxdpEgRn+3u66amfWLc/jcube45fvy4ZKfTp0+bfkbp0eYpbU7TPkHap+mee+6R2bNnX9bHJyPa2bpChQrW5fX9Tu3GG2/M9rmj9JppsE19jTQka3jU/amnpkgtJ64ZkJMYKgHkMRqCPv30U9m1a5enP5NLv9Zh+NoJW2ujdMSdduhVGrI0dH322WdpjijLygkps3vEWlq05uj777+XunXrpltGz////u//TOjU93DFihWmE7j24dFtNu+BdqjWMJKV9Lg00Kbmdpz/s8/9Z65ZWscFBCpCE5CH52vS0KSduV06Kk4/1HUeH+0sriO8XDqCSj8AdbSY1nRcCR35pc13Ok+Qd22Tdh6+Wlk9e7WGIR1VqJ20M3PzzTebRTu0z58/33QG/+CDD0zH6aw+Lq3hS03DnfdIO63RSasZLHVt0JUcm14zDcr6+tqs69IO6Nrp/0rmrgKCBc1zQB7TpEkT0/w1b948U6PkXdOkgUlHSs2YMcP0dfKen0lHWWltgjZNpa490HWdUiA9GkS0JkcncHTpB7K+ztVyw1dGo/Zsad8uDY8aPjLqZ6VNTanPPSoqyjy6TXRZeVxq8eLF5jq5Nm3aZAKtThHhHWi/++47n1nN9ZxST1Z6JcfmBmadisGbjppUnTp1uupzAgIVNU1AHlOwYEFp2rSpfPXVVyYkae2SNw1R2tykvEOTfjC/+OKLZti79qfRDsra/+fAgQPm1ix9+/Y1cymlRctqB2btRKy1SzqNwSeffCLHjh0z+6+mdkanB9DOxwsWLDA1XzpnlDatZdS8pvS8k5KSTNOVBj0NFnosJUqUMOehfXbSM3fuXPnHP/5hhuzr+6GdxjUI6txTbsi42uNKj/Yp0uugncc1mGmI0c78w4YN85TRJkINMxpOe/XqZfqXzZo1y8y/pTO+X817pnNX6ZQQOs2Dhiztz6WBTd8DvZ5t2rS5qvMBAlpuD98DkPNGjBhhhoi3aNHisn0fffSR2XfNNdc4ly5dumy/Th/QsmVLM1WBLjVr1nQGDBjgxMXFpTvU3R3u/uCDD5rnLVGihPPII484GzZsMK/1wQcf+HyvPm9mQ+JVTEyMmYagYMGCmU4/4E454C4FChRwypQp47Ru3dpMl6BD5FNLPeXAtm3bnAceeMCpVKmSGU5ftmxZ56677nK2bNlidVzpnVtGUw688sorzuTJk52KFSua12zVqpXzzTffXPb97733nnP99deb14yKinJWrFiR5nVI79jSen91Sopx48Y5VatWNe+XHoP+7CQlJfmU09fo1KnTZceU3lQIQKAK0X9yO7gByJu06UlrbbR/lfes4wDgjwhNAHKEdrLW5iGXNo/p7Np6W5IjR4747AMAf0SfJgA54oknnjDBqXnz5qZvjk6WGRMTIy+99BKBCUBAoKYJQI7QofnawVw7gmtHbO3grJ2bBw4cmNuHBgBWCE0AAAAWmKcJAADAAqEJAADAAh3Bs4jObvzrr7+ayf6y+jYKAAAge2gvJZ2oVu+1mdl9IQlNWUQDU8WKFXP7MAAAwFU4fPiwVKhQIcMyhKYsojVM7puut1QAAAD+T281pJUe7ud4RghNWcRtktPARGgCACCw2HStoSM4AACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACAhVCbQgD8V536URIfH59hmcjISNm9c0eOHRMABCNCExDgNDBFT1icYZmVIzvn2PEAQLCieQ4AAMACoQkAAMACoQkAAMACoQkAAMACoQkAAMACoQkAAMACoQkAAMACoQkAAMDfQ9OXX34pd999t5QvX15CQkJk8WLfCfocx5ExY8aY2YwLFy4s7du3l3379vmUOXbsmHTv3l2KFy8uJUuWlF69esnp06d9yuzcuVNatWolYWFhUrFiRZk0adJlx7Jw4UKpWbOmKVOvXj1ZtmxZNp01AAAIRLkams6cOSMNGjSQGTNmpLlfw8306dNl1qxZsnHjRilatKh06NBBkpKSPGU0MO3evVtWrVolS5YsMUGsb9++nv2JiYkSHR0tlStXlq1bt8orr7wiY8eOlTfffNNTJiYmRh544AETuLZv3y6dO3c2y7fffpvN7wAAAAgUIY5W5/gBrWlatGiRCStKD0troJ5++ml55plnzLaTJ09KRESEzJkzR7p16yZ79+6V2rVry+bNm6VJkyamzPLly+XOO++Un3/+2Xz/zJkzZeTIkXLkyBEpWLCgKTN8+HBTq/Xdd9+Z9fvvv98EOA1drptvvlmioqJMYLOh4axEiRLmGLXWC8gp4WUirG6jcuy3ozl2TAAQKK7k89tv+zQdOHDABB1tknPpSTVr1kxiY2PNuj5qk5wbmJSWz5cvn6mZcsu0bt3aE5iU1lbFxcXJ8ePHPWW8X8ct475OWs6fP2/eaO8FAAAEL78NTRqYlNYsedN1d58+li1b1md/aGiohIeH+5RJ6zm8XyO9Mu7+tEycONGEOHfRvlIAACB4+W1o8ncjRowwVXnucvjw4dw+JAAAkBdDU7ly5czj0aO+/TB03d2njwkJCT77L126ZEbUeZdJ6zm8XyO9Mu7+tBQqVMi0fXovAAAgePltaKpataoJLWvWrPFs035D2lepefPmZl0fT5w4YUbFudauXSspKSmm75NbRkfUXbx40VNGR9rVqFFDSpUq5Snj/TpuGfd1AAAAcjU06XxKO3bsMIvb+Vu/PnTokBlNN2jQIHnxxRflk08+kV27dkmPHj3MiDh3hF2tWrWkY8eO0qdPH9m0aZNs2LBBBg4caEbWaTn14IMPmk7gOp2ATk2wYMECee2112TIkCGe43jqqafMqLvJkyebEXU6JcGWLVvMcwEAAKjQ3HwbNJi0adPGs+4GmZ49e5ppBYYNG2amAtB5l7RGqWXLlibc6ASUrnnz5plw065dOzNqrmvXrmZuJ5d20l65cqUMGDBAGjduLKVLlzYTZnrP5dSiRQuZP3++jBo1Sp577jmpXr26mZKgbt26OfZeAAAA/+Y38zQFOuZpQm5hniYAyOPzNAEAAPgTQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAIAFQhMAAECgh6bk5GQZPXq0VK1aVQoXLizVqlWTF154QRzH8ZTRr8eMGSORkZGmTPv27WXfvn0+z3Ps2DHp3r27FC9eXEqWLCm9evWS06dP+5TZuXOntGrVSsLCwqRixYoyadKkHDtPAADg//w6NP3973+XmTNnyhtvvCF79+416xpmXn/9dU8ZXZ8+fbrMmjVLNm7cKEWLFpUOHTpIUlKSp4wGpt27d8uqVatkyZIl8uWXX0rfvn09+xMTEyU6OloqV64sW7dulVdeeUXGjh0rb775Zo6fMwAA8E+h4sdiYmLknnvukU6dOpn1KlWqyPvvvy+bNm3y1DJNmzZNRo0aZcqpd999VyIiImTx4sXSrVs3E7aWL18umzdvliZNmpgyGrruvPNOefXVV6V8+fIyb948uXDhgrzzzjtSsGBBqVOnjuzYsUOmTJniE64AAEDe5dc1TS1atJA1a9bI999/b9a/+eYbWb9+vdxxxx1m/cCBA3LkyBHTJOcqUaKENGvWTGJjY826PmqTnBuYlJbPly+fqZlyy7Ru3doEJpfWVsXFxcnx48fTPLbz58+bGirvBQAABC+/rmkaPny4CSM1a9aU/Pnzmz5OEyZMMM1tSgOT0polb7ru7tPHsmXL+uwPDQ2V8PBwnzLabyr1c7j7SpUqddmxTZw4UcaNG5el5wsAAPyXX9c0ffjhh6bpbP78+bJt2zaZO3euaVLTx9w2YsQIOXnypGc5fPhwbh8SAADIqzVNQ4cONbVN2jdJ1atXT3766SdTy9OzZ08pV66c2X706FEzes6l61FRUeZrLZOQkODzvJcuXTIj6tzv10f9Hm/uulsmtUKFCpkFAADkDX5d03T27FnT98ibNtOlpKSYr7VJTUON9ntyaXOe9lVq3ry5WdfHEydOmFFxrrVr15rn0L5PbhkdUXfx4kVPGR1pV6NGjTSb5gAAQN7j16Hp7rvvNn2Yli5dKgcPHpRFixaZEW333nuv2R8SEiKDBg2SF198UT755BPZtWuX9OjRw4yI69y5sylTq1Yt6dixo/Tp08eMutuwYYMMHDjQ1F5pOfXggw+aTuA6f5NOTbBgwQJ57bXXZMiQIbl6/gAAwH/4dfOcTg2gk1v+7W9/M01sGnIef/xxM5mla9iwYXLmzBkzNYDWKLVs2dJMMaCTVLq0X5QGpXbt2pmaq65du5q5nbxH3K1cuVIGDBggjRs3ltKlS5vXYLoBAADgCnG8p9fGVdNmQQ1f2ilcZx4Hckp4mQiJnrA4wzIrR3aWY7/59tsDAFzZ57dfN88BAAD4C0ITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACAhVCbQgCCX536URIfH59hmcjISNm9c0eOHRMA+BNCEwBDA1P0hMUZllk5snOOHQ8A+Bua5wAAACwQmgAAACwQmgAAACwQmgAAACzQERzIJYxWA4DAQmgCcgmj1QAgsNA8BwAAYIGaJiAPSDx1WsLLRGRS5lSOHQ8ABCJCE5AHOCkpmTYFLhzYNseOBwACEc1zAAAAFghNAAAAFghNAAAAFghNAAAAFghNAAAAFghNAAAAFphyAPBjzK8EAP6D0AT4MeZXAgD/QfMcAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAABAMISmX375RR566CG59tprpXDhwlKvXj3ZsmWLZ7/jODJmzBiJjIw0+9u3by/79u3zeY5jx45J9+7dpXjx4lKyZEnp1auXnD592qfMzp07pVWrVhIWFiYVK1aUSZMm5dg5AoEi8dRpCS8TkeFSp35Ubh8mAGSLUPFjx48fl1tuuUXatGkjn332mZQpU8YEolKlSnnKaLiZPn26zJ07V6pWrSqjR4+WDh06yJ49e0wAUhqY4uPjZdWqVXLx4kV59NFHpW/fvjJ//nyzPzExUaKjo03gmjVrluzatUsee+wxE7C0HID/cFJSJHrC4gzLrBzZOceOBwBykl+Hpr///e+m1mf27NmebRqMvGuZpk2bJqNGjZJ77rnHbHv33XclIiJCFi9eLN26dZO9e/fK8uXLZfPmzdKkSRNT5vXXX5c777xTXn31VSlfvrzMmzdPLly4IO+8844ULFhQ6tSpIzt27JApU6YQmgAAgP83z33yyScm6Nx3331StmxZadiwobz11lue/QcOHJAjR46YGiJXiRIlpFmzZhIbG2vW9VFrjNzApLR8vnz5ZOPGjZ4yrVu3NoHJpbVVcXFxprYrLefPnzc1VN4LAAAIXlcVmq6//nr5448/Ltt+4sQJsy+r/PjjjzJz5kypXr26rFixQvr37y9PPvmkaYpTGpiU1ix503V3nz5q4PIWGhoq4eHhPmXSeg7v10ht4sSJJqC5i9aIAQCA4HVVoengwYOSnJycZu2LdtzOKikpKdKoUSN5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Zl2bybS5bPjw4Z4yvXv3loceesh8vX79emnVqpUULlxYKlasKE8++aScOXMm3ea57777Tlq2bClhYWHmDuqrV682z7948WKf4/jxxx+lTZs2UqRIEXMH+tjYWLN93bp18uijj8rJkyfN9+kyduzYbH9fAGQNQhOAoKEB6NSpU7J9+3az/sUXX0jp0qVNWHHptttuu01++OEH6dixo3Tt2lV27twpCxYsMCFq4MCBaT63BrHOnTubILRx40Z58803ZeTIkWmW1e3PPPOMCW033nijPPDAA3Lp0iVp0aKFCWHFixeX+Ph4s2g5AIGB0AQgaJQoUUKioqI8IUkfBw8ebELU6dOn5ZdffpH9+/fLrbfeKhMnTpTu3bvLoEGDpHr16ibQTJ8+Xd59911JSkq67LlXrVplgpbu19ojrXGaMGFCmsehQahTp04mMI0bN05++ukn87oFCxY0x6g1TOXKlTNLsWLFsv19AZA1CE0AgooGIg1LjuPIV199JV26dJFatWqZWiStZSpfvrwJSd98843plK2hxV06dOggKSkpcuDAgcueNy4uzjThadBx3XTTTWkeQ/369T1fR0ZGmseEhIRsOV8AOYeO4ACCija9vfPOOyYUFShQQGrWrGm2aZA6fvy4CVVKa54ef/xx048ptUqVKv2pY9DXdWmtktIwBiCwEZoABGW/pqlTp3oCkoaml19+2YSmp59+2mxr1KiR7NmzR2644Qar561Ro4YcPnxYjh49KhEREZ4pCa6UNtG5HdUBBBaa5wAElVKlSpnmsXnz5pmwpFq3bi3btm2T77//3hOknn32WYmJiTEdv7XD9r59++Tjjz9OtyP47bffLtWqVZOePXuajuMbNmyQUaNG+dQm2dAReVrLtWbNGvn999/l7NmzWXLeALIfoQlA0NFgpLU5bmgKDw83UwRofyStMVIarLSPkwYprZ1q2LChjBkzxvR5Skv+/PnN1AIaeJo2bWqmLnBHz+kUBLa0w3m/fv3k/vvvN/NATZo0KUvOGUD2C3G0tyQA4IppbZOOotORcVoLBSC4EZoAwNKiRYvMKDsdfadB6amnnjLNgToyD0DwoyM4AFjSDubaF+rQoUNm0sz27dvL5MmTc/uwAOQQapoAAAAs0BEcAADAAqEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJAABAMvf/AFxh/Dt3cPoiAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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yxZp1qyZnDx5Ut555x2ZO3eutGjRwpSZNWuWVK9e3QSt2267TeLi4uT777+XVatWSVhYmNSrV09Gjx4tgwcPlhEjRkiRIkVkxowZUrlyZZk4caLZh/7+119/LZMnT5aoqKg8OXcAAOBbfLqmKS0NSSo0NNQ8anjS2qdWrVq5y1SrVk0qVqwo69evN8/1sXbt2iYwOTQIJScnS2JioruM5z6cMs4+0pOSkmL24bkAAID8y29CU2pqqmk2u+OOO6RWrVpm3ZEjR0xNUcmSJb3KakDSbU4Zz8DkbHe2ZVZGg9DZs2cz7G9VokQJ91KhQoVsPFsAAOBr/CY0ad+mnTt3yrx588QXxMbGmpovZzlw4EBeHxIAACiofZocMTExsnTpUlm7dq1cf/317vXh4eGmg/eJEye8apt09Jxuc8ps3LjRa3/O6DrPMmlH3Onz4sWLS9GiRdM9Jh1lpwsAACgYfLqmyeVymcC0aNEiiY+PN521PTVo0EAKFy4sq1evdq/TKQl0ioEmTZqY5/q4Y8cOSUpKcpfRkXgaiGrUqOEu47kPp4yzDwAAgCBfb5LTkXGffPKJmavJ6YOkfYi0Bkgfu3btKgMGDDCdwzUI9e7d24QdHTmndIoCDUdPPPGEjBs3zuxj6NChZt9OTdEzzzwjU6dOlUGDBslTTz1lAtqCBQvks88+y9PzBwAAvsOna5qmT59u+gs1b95cypUr517mz5/vLqPTAtx3331mUkudhkCb2j7++GP39kKFCpmmPX3UMPWPf/xDOnfuLKNGjXKX0RosDUhau1S3bl0z9cDbb7/NdAMAAMA/apq0eS4rISEhMm3aNLNkJCIiQpYtW5bpfjSYbd269YqOEwAA5H8+XdMEAADgKwhNAAAAFghNAAAAFghNAAAA/t4RHACQ95JPnZbQMt63mkpLRzYnbt+Wa8cE5AVCEwAgU67UVIkcszjTMnFDonPteIC8QvMcAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACABUITAACAhSCbQgDgr2rWqSeHDx/OtEzyqVO5djwA/BehCUC+poEpcsziTMssjGmRa8cDwH/RPAcAAGCB0AQAAGCB0AQAAGCB0AQAAGCBjuAAgL8t+dRp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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# ملخص إحصائي\n",
    "print(hearGardaData['weight'].describe())\n",
    "print(hearGardaData['height'].describe())\n",
    "\n",
    "# رسم توزيع الوزن والطول (اختياري لو تريد تصور أوضح)\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "sns.histplot(hearGardaData['weight'], bins=50)\n",
    "plt.title('Weight Distribution')\n",
    "plt.show()\n",
    "\n",
    "sns.histplot(hearGardaData['height'], bins=50)\n",
    "plt.title('Height Distribution')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "id": "80450a19-dc39-4f89-b733-cf01ac3e497f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 238,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# عدد القيم الشاذة للوزن\n",
    "len( hearGardaData[(hearGardaData['weight'] <= 30) | (hearGardaData['weight'] >= 200)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "id": "b51927a5-e3af-4de8-84e5-9618c7dd3e55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 239,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len( hearGardaData[(hearGardaData['weight'] <= 30)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 240,
   "id": "ca05ad0b-4bb1-4ec7-a4b5-4c1a4a35aba5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 240,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len( hearGardaData[(hearGardaData['weight'] >= 200)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "id": "3d623e10-b8bc-463b-b703-09cdd4f42cae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>weight</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>435</th>\n",
       "      <td>46</td>\n",
       "      <td>200.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3752</th>\n",
       "      <td>42</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18559</th>\n",
       "      <td>50</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26806</th>\n",
       "      <td>64</td>\n",
       "      <td>23.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29488</th>\n",
       "      <td>56</td>\n",
       "      <td>22.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33817</th>\n",
       "      <td>59</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34276</th>\n",
       "      <td>40</td>\n",
       "      <td>28.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41905</th>\n",
       "      <td>58</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50413</th>\n",
       "      <td>41</td>\n",
       "      <td>200.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57858</th>\n",
       "      <td>51</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60188</th>\n",
       "      <td>60</td>\n",
       "      <td>21.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60699</th>\n",
       "      <td>52</td>\n",
       "      <td>29.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       age  weight\n",
       "435     46   200.0\n",
       "3752    42    30.0\n",
       "18559   50    30.0\n",
       "26806   64    23.0\n",
       "29488   56    22.0\n",
       "33817   59    11.0\n",
       "34276   40    28.0\n",
       "41905   58    30.0\n",
       "50413   41   200.0\n",
       "57858   51    10.0\n",
       "60188   60    21.0\n",
       "60699   52    29.0"
      ]
     },
     "execution_count": 241,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.loc[(hearGardaData['weight'] <= 30) | (hearGardaData['weight'] >= 200), ['age', 'weight']].head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "5db9d06f-7fd0-4cf7-87c1-b17e70bd61ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>435</th>\n",
       "      <td>46</td>\n",
       "      <td>1</td>\n",
       "      <td>186</td>\n",
       "      <td>200.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>57.810151</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50413</th>\n",
       "      <td>41</td>\n",
       "      <td>2</td>\n",
       "      <td>180</td>\n",
       "      <td>200.0</td>\n",
       "      <td>150</td>\n",
       "      <td>90</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>61.728395</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       age  gender  height  weight  Systolic  Diastolic  cholesterol  gluc  \\\n",
       "435     46       1     186   200.0       130         70            1     1   \n",
       "50413   41       2     180   200.0       150         90            1     1   \n",
       "\n",
       "       smoke  alco  active        BMI  diabetes_signal  Family_History  \\\n",
       "435        0     0       0  57.810151                0               0   \n",
       "50413      0     0       1  61.728395                0               0   \n",
       "\n",
       "       Heart Attack Risk  \n",
       "435                    0  \n",
       "50413                  1  "
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.loc[(hearGardaData['weight'] == 200)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "id": "c3298ed9-0af0-4c27-9243-73e438a78a04",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData = hearGardaData[(hearGardaData['weight'] > 30)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "id": "3563a55e-0d92-4985-a52c-c65640e6df30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "86"
      ]
     },
     "execution_count": 244,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# عدد القيم الشاذة للطول\n",
    "len( hearGardaData[(hearGardaData['height'] <= 120) | (hearGardaData['height'] >= 210)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "id": "2a3d6c16-31e7-485d-9d6b-897f8340f5e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "85"
      ]
     },
     "execution_count": 245,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len( hearGardaData[(hearGardaData['height'] <= 120) ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "id": "3535192c-f246-47d2-a2e6-21a17356688f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>height</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>224</th>\n",
       "      <td>60</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3420</th>\n",
       "      <td>40</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3735</th>\n",
       "      <td>48</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4212</th>\n",
       "      <td>44</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6486</th>\n",
       "      <td>58</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6821</th>\n",
       "      <td>59</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7116</th>\n",
       "      <td>56</td>\n",
       "      <td>117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7305</th>\n",
       "      <td>43</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7598</th>\n",
       "      <td>40</td>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8171</th>\n",
       "      <td>48</td>\n",
       "      <td>97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8677</th>\n",
       "      <td>54</td>\n",
       "      <td>119</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9284</th>\n",
       "      <td>40</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9603</th>\n",
       "      <td>62</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11183</th>\n",
       "      <td>60</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11230</th>\n",
       "      <td>50</td>\n",
       "      <td>110</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12770</th>\n",
       "      <td>54</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13265</th>\n",
       "      <td>61</td>\n",
       "      <td>71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13952</th>\n",
       "      <td>40</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14323</th>\n",
       "      <td>60</td>\n",
       "      <td>67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15167</th>\n",
       "      <td>43</td>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       age  height\n",
       "224     60      76\n",
       "3420    40     100\n",
       "3735    48     120\n",
       "4212    44     120\n",
       "6486    58     250\n",
       "6821    59     120\n",
       "7116    56     117\n",
       "7305    43     120\n",
       "7598    40      70\n",
       "8171    48      97\n",
       "8677    54     119\n",
       "9284    40     120\n",
       "9603    62     120\n",
       "11183   60     120\n",
       "11230   50     110\n",
       "12770   54      75\n",
       "13265   61      71\n",
       "13952   40     120\n",
       "14323   60      67\n",
       "15167   43      70"
      ]
     },
     "execution_count": 246,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.loc[(hearGardaData['height'] <= 120) | (hearGardaData['height'] >= 210), ['age', 'height']].head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "id": "1c8385db-00db-4f71-985c-2633d93a7653",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData = hearGardaData[(hearGardaData['height'] > 120) & (hearGardaData['height'] <= 210)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "id": "26920d84-3c26-4376-ba71-5709a96c5d63",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 248,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len( hearGardaData[(hearGardaData['height'] <= 120) & (hearGardaData['height'] >= 210)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "id": "b59bfca6-4aaf-459a-be39-4abb690eaf2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(69904, 15)"
      ]
     },
     "execution_count": 249,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "401ff9a2-0940-48ef-978e-33037904775e",
   "metadata": {},
   "source": [
    "### colesterol"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b09e597b-6748-4c05-b9b7-661d2a4b02b1",
   "metadata": {},
   "source": [
    "#### Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "id": "9ec9dcb8-8a36-4e21-ae4a-3b0e5a3b7bc2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['age', 'gender', 'height', 'weight', 'Systolic', 'Diastolic',\n",
       "       'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'BMI',\n",
       "       'diabetes_signal', 'Family_History', 'Heart Attack Risk'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 250,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.columns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "id": "a855a272-f2f0-4a49-a7bf-622f55e4c486",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cholesterol\n",
       "1    52308\n",
       "2     9538\n",
       "3     8058\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 251,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData['cholesterol'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "id": "4aac395c-4b4e-4a3d-a49c-1b224b1bf9e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# hearGardaData['cholesterol'] = hearGardaData['cholesterol'].map({1: 'normal', 2: 'above_normal', 3:'well_above_normal'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "id": "31caa68a-01ac-4d09-bb83-042b0be8767c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        1\n",
       "1        3\n",
       "2        3\n",
       "3        1\n",
       "4        1\n",
       "        ..\n",
       "69995    1\n",
       "69996    2\n",
       "69997    3\n",
       "69998    1\n",
       "69999    2\n",
       "Name: cholesterol, Length: 69904, dtype: int64"
      ]
     },
     "execution_count": 253,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData['cholesterol']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 254,
   "id": "4d86f007-4b2e-4c6e-bcb2-3b0280f819dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# hearGardaData = pd.get_dummies(hearGardaData, columns=['cholesterol'], drop_first=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "id": "a8d36b51-ca1a-4715-8ec8-4df557516a2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>21.967120</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>34.927679</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  gender  height  weight  Systolic  Diastolic  cholesterol  gluc  smoke  \\\n",
       "0   50       2     168    62.0       110         80            1     1      0   \n",
       "1   55       1     156    85.0       140         90            3     1      0   \n",
       "\n",
       "   alco  active        BMI  diabetes_signal  Family_History  Heart Attack Risk  \n",
       "0     0       1  21.967120                0               1                  0  \n",
       "1     0       1  34.927679                0               1                  1  "
      ]
     },
     "execution_count": 255,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.head(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7064b8ae-0a93-486d-a022-4b5d6f8922d4",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "id": "d7d3dc95-ce2c-4381-9e6e-ac53b546e86d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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1FTtmmuuUcFYLDHJ/0Q620VEREQU7VjTRERERBQABk1EREREAWDQRERERBQABk1EREREAWDQRERERBQABk1EREREAWDQRERERBQABk1EREREAWDQRERERBQABk1EFLN+8YtfwGQy+bZu3brh7LPPxpYtW3znGMfWrl1b770Oh0OdL8dWrlxZ7/x33303rH8OIgoPBk1EFNMkSDpy5IjaZJV3q9WK8847r945ffr0wUsvvVTvtXfeeQfJyclhvlsiiiQGTUQU0+x2O3Jzc9U2btw43HvvvcjLy0NhYaHvnKuvvhpvvPEGampqfK+9+OKL6nUiih0MmoiIvCorK/Hqq69i8ODBaujNMHHiRPTv3x//93//p54fOHAAn3/+Oa666qoI3i0RhRuDJiKKaYsXL1bDbLKlpKTg/fffx5tvvgmzuf5/Hq+99lqVXRIvv/wyzjnnHHTv3j1Cd01EkcCgiYhi2vTp07F582a1rVu3DrNnz8acOXOwf//+euddeeWVWLNmDfbu3auCJgmiiCi2MGgiopiWlJSkhuNkO/HEE/HCCy+gqqoK//jHP+qdJ8N1UiB+3XXXoba2VgVWRBRbGDQREfmRlgEyNOdf9G2Q7JK0F/j5z38Oi8USkfsjosixRvCziYgiTvot5efnq8clJSV49tlnVUH4+eef32R7AplVl5qaGoE7JaJIY9BERDFt6dKl6NGjh3osheDDhg3DokWLMG3atCazUFlZWRG4SyKKBiZN07RI3wQRERFRtGNNExEREVEAGDQRERERBYBBExEREVEAGDQRERERBYBBExEREVEAGDQRERERBYBBExEREVEAGDQRERERBYBBExEREVEAGDQRERERBYBBExERERFa9/8BJ2J6PLBwKKUAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=hearGardaData,x=\"BMI\",hue=\"Heart Attack Risk\",kde=True,bins=10)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ad432a20-de5d-4c49-ba2b-e01c2eeb5a5c",
   "metadata": {},
   "source": [
    "if your BMI is:\n",
    "\n",
    "below 18.5 – you're in the underweight range\n",
    "between 18.5 and 24.9 – you're in the healthy weight range\n",
    "between 25 and 29.9 – you're in the overweight range\n",
    "between 30 and 39.9 – you're in the obese range\n",
    "Reference:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "id": "a56962ed-4f9a-49b8-82ce-3644f8e5779a",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData.loc[(hearGardaData.BMI <= 18.4), 'BMI'] = 1\n",
    "hearGardaData.loc[(hearGardaData.BMI > 18.4) & (hearGardaData.BMI < 25), 'BMI'] = 2\n",
    "hearGardaData.loc[(hearGardaData.BMI >= 25) & (hearGardaData.BMI < 30), 'BMI'] = 3\n",
    "hearGardaData.loc[(hearGardaData.BMI >= 30) & (hearGardaData.BMI < 40), 'BMI'] = 4\n",
    "hearGardaData.loc[(hearGardaData.BMI >= 40), 'BMI'] = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 258,
   "id": "84319782-87ea-4880-b37e-aff3568b38d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=hearGardaData,x=\"BMI\",hue=\"Heart Attack Risk\",kde=True,bins=10)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "id": "f617790d-9d1f-4377-9dcc-f16af6849102",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "BMI\n",
       "2.0    25851\n",
       "3.0    25086\n",
       "4.0    16588\n",
       "5.0     1801\n",
       "1.0      578\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 259,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData['BMI'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "id": "b6adeaa5-b30c-4d46-838f-073dd6482907",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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BiK0XZi8n5VXZOnToebYhshgMMgw9Pvvv2Pz5s2y4fPViF5igigpEgYOHIiYmBhZFGwieqyJsNO5c2fzPps2bap2HLGPWE9ERERka+lqsl9++QVLliyRYxGJtj5iEe16BFEtJnqMiV5nSUlJ+Ouvv/Dggw/KHmjdunWT+4hu+iL4TJ06FUeOHJFd6V977TV5bFMpjxi3KCEhAS+99BJOnjyJb775BsuXL8eMGTMseflERERkJSwaiL799lvZs0zUxYoSH9OybNkyuV10mRfd6UXoCQ8PxwsvvICJEydi5cqV5mPY2dnJ6jZxK0p8pkyZIkPT7NmzzfuIkqfVq1fLUqHu3bvL7vfz5s1jl3siIiKyfBsiUWV2JaIhsxi88WpEL7Q1a9ZccR8Rug4fPnzN50hERETNn1WNQ0RERERkCQxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgMRERERKR4DERERESkeAxEREREpHgqS58AERGR0mi1WsQlZFRbF5OQgY4RWoudk9IxEBERETWyuLg4rEiwR6za27zueEIOJsXFITIy0qLnplQMRERERBbgGxiI0HZh5sdZeUUWPR+lYxsiIiIiUjwGIiIiIlI8VpkREVm4cW1WVhZU7inysbiv1QZa+rSIFIclREREFm5cm5d0FEg/IhdxX6wjosbFEiIiIgvzcnNCsL+nvJ+W7GTp0yFSJJYQERERkeIxEBEREZHiMRARERGR4jEQERERkeKxUTWRBWg0GkRFRV22vnfv3lCr1RY5JyIiJWMgIrIAEYY+XbYRQaEdzOvSE09hBoBBgwZZ9NyIiJSIgYjIQkQYCu3Sy9KnQURElm5D9N5776Fv375wc3ODv78/xo8ff9mAZOXl5Xj66afh4+MDV1dXTJw4EZmZmdX2SU5Oxu233w5nZ2d5nBdffBGVlZXV9tm6dSt69eolqyPCwsKwcOHCRrlGIiIisn4WDUTbtm2TYWfv3r3YsGEDKioqMGrU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iIiIiKghMBARERGR4jEQERERkeIxEBEREZHiMRARERGR4jEQERERkeIxEBEREZHiMRARERGR4jEQERERkeIxEBEREZHiMRARERGR4jEQERERkeIxEBEREZHiMRARERGR4qksfQJERETUcLRaLeISMqqti0nIQMcIrcXOyRoxEBERETVjcXFxWJFgj1i1t3nd8YQcTIqLQ2RkpEXPzZowEBERETVzvoGBCG0XZn6clVdk0fOxRmxDRERERIrHQERERESKx0BEREREisdARERERIrHQERERESKx0BEREREisdARERERIrHQERERESKx0BEREREisdARERERIrHQERERESKx7nMiKjJzNidlZUFlXuKfCzua7WBlj4tImomWEJERE1mxu68pKNA+hG5iPtiHRFRfWAJERE1GV5uTgj295T305KdLH06RNSMsISIiIiIFI+BiIiIiBSPgYiIiIgUj22IiIiIqN56g8YlZFRbF5OQgY4RWlg7BiIiIiKqF6Ln54oEe8Sqvc3rjifkYFJcHCIjI2HNGIiIiIio3vgGBiK0XZj5cVZeEZoCtiEiIiIixWMgIiIiIsVjICIiIiLFYyAiIiIixWMgIiIiIsVjICIiIiLFs2gg2r59O8aOHYsWLVrAxsYGf/zxR7XtBoMBs2bNQlBQEJycnDBy5EicPn262j65ubmYPHky3N3d4enpiUcffRTFxcXV9jl69CiGDh0KR0dHBAcHY86cOY1yfURERNQ0WDQQlZSUoHv37vj6669r3C6CyxdffIG5c+di3759cHFxwejRo1FeXm7eR4Sh2NhYbNiwAatWrZIh6/HHHzdvLywsxKhRoxASEoKoqCh8+OGHePPNN/H99983yjUSERGR9bPowIxjxoyRS01E6dBnn32G1157DePGjZPrfvrpJwQEBMiSpPvuuw8nTpzA2rVrceDAAfTp00fu8+WXX+K2227DRx99JEueFi9eLIcSnz9/PhwcHNClSxdER0fjk08+qRacqtJoNHKpGqqI6OrE/7WsrCyo3FPM68RjrTbQoudFRNRk2xAlJiYiIyNDVpOZeHh4oH///tizZ498LG5FNZkpDAlif1tbW1miZNrnpptukmHIRJQyieHF8/Lyanzt9957T76WaRHVbER0dfL/VdJRIP2IeRGPxXoiImtmtYFIhCFBlAhVJR6btolbf3//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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.histplot(data=hearGardaData,x=\"age\",hue=\"Heart Attack Risk\",bins=100,kde=True)\n",
    "plt.show()\n",
    "# We can s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "id": "849b8465-b777-4a81-b553-c2ac383b0de3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "smoke\n",
       "0    63742\n",
       "1     6162\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 261,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "smoking_counts=hearGardaData[\"smoke\"].value_counts()\n",
    "smoking_counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "id": "a9341bd4-38b1-410b-8f9c-d345df75aaae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Wdn92rdvn/sOwRo1asRbp1mfCxcuHG95hQoV3NflpDcdq86rbvri6LJly9qTTz5pP//8c1i5AwcOWKtWrdJtP4HMitAEIEPSlxlcuHAh2X+nYPTwww/b8ePH7csvv7SM5sYbb3ShaM+ePTZ9+nRbsGCB9erVK6xMdHS05c6dO932EcisCE0ArorPP//cbr/9dsubN6+rIfntb3/rvujY8/e//919CfI111zjLvqPPPKIxcbGxqu9+uSTT6xevXouFPzjH/+wF154wb755ptgDUxS3xGmoKWg0blzZ7f9N998M2z7+tLlY8eOBbelmp2mTZvaDz/8YP379w8ul59++sk6depkv/rVryxfvnxWs2ZN++c//xn2eJcuXbLRo0db5cqV3f7qS19ffvnlBPft4sWL1r17d6tataoLRInJkSOHOz963ObNm9tDDz1kixcvTrTJ7dy5c9anTx8rVaqU5cmTx8qXL2+jRo1KdPsjRoxwZTdu3JhoGSCrIjQBSHO7du2ye+65x9q3b+8uxrNmzXIhShdzz/nz5+3FF190AUgXfPX5UfNfXEOGDLE//elPtnXrVrv77rvtmWeeCda+6NahQ4dE92PZsmV26tQpFzZ+85vf2LvvvhsMbrfccotrgitYsGBwW88++6y9//77VqZMGRs5cmRwuZw5c8aFt/nz59vmzZtdM5nC2Nq1a4OPN3ToULevzz33nH377bc2c+ZMK1myZLz9Onv2rAs/6t/02WefuXDlh87RwoULXXNjYvRl0v/+979t9uzZtn37dnvnnXdcc2NCgbJv37729ttvu32oVauWr30AspIc6b0DADK2efPmWYECBeLVmoRSzcajjz5q/fr1c/evv/56dzG/4447bPLkya4GRLUsnuuuu86tb9CggZ04cSJs+wovCkserfNqXy5HNUsdO3Z0/YHUp0mPM2fOHBfOFDwKFSrkamnibkvlvRowj2p6FKo8ChwKMAonDRs2tF9++cXGjx9vEydOtK5du7oylSpVsttuuy1s2zq+Nm3auOCkUKd9SMqmTZvcMescK7jJq6++mmh51VrpfOtxdWyqaYpLzZwKkV9//bULszo2APERmgBckWbNmrngE0p9hXQR9qj2SDVMquUIrdlQ89Xu3butWrVqFhMT45rDVPbIkSNunXfRr169evDv1ISXEuqUrlojhQKP9lFBKqEarctRaPnjH//oQtJ///tf1wym4KOmOlFNmO7fddddSW5HTXyqyVq6dKlrurycKlWquJojBSY1T6p2SoEtMTo2hUz9nWr77r33XmvRokVYGTU9qvlwzZo1VqxYMd/nAMhqaJ4DcEXy58/v+uyE3uLWVKg25amnnnIXeO+mcLRjxw5X+6ImspYtW7qmMQWrr776yubOnev+VmEk7uOlhJrGFDQaNWrkaqZ0Gzx4sAtR//nPf5K9vTFjxriaJG1DNUQ6Jh2Dt79+ApC0bt3aBcrVq1f7Kq8aMZ1j1ZSp6U+1YOrXlZi6deu6YKqmz9OnT7tO8A8++GBYGYUqBT/VlAFIHDVNANKcLtzq06OLfWJNTupYrRCgTuKybt063yEibnNgQlSjpP5PcWuVnn76aZs2bZp77MS2ldDyL774wu6///5gjZpqxhS+vFoxNYkpOC1ZssR69OiR6H5p5JsC0H333ef6R6nJMjmGDRtmd955p9tO6dKlEyyjMKq+XropMKnGSdMUFClSxK3XY7dt29Z1jlcIUxMmgPioaQKQ5lQbs2rVKtfxWzUyqmH68MMPgx3B1fFZwWTChAn23XffueYn1Yz4oU7NqknRdn/88UfXJBaX1q1fv96FFwWU0Juax9566y3Xr0fbUq2Ygo62pU7j3mOsXLnS1cZouReKNGpNx6WmONWkHTp0KPiY6qel4x40aJDrXK3O8Gr+Ch2x51Hz2ksvveSazkKbD/1o3Lix67StpsKEqL+TRvVt27bNhTr14VLfrLjzUf361792Ixg1gvC9995L1j4AWQWhCUCa00V9xYoV7qKtaQduuukmGz58eLBmpHjx4m6qAF3QVVOjWp9XXnnF17Y1Ik81J+pbpe3EHfYvCirarobzx6WwoKkNPv74YzeCrmfPnq5GRtvSdAFe53ONVFNTopZ7NTyqQVOTnKYlUBCJO9GnRs2pdkvHqn5b2m7oNAqh1ElezWxqrlMQSw71SZo6dart3bs33jp1YNdxqC+YOtbrOHSs2bLF/+9ftVAKkBoFqP5fAMJFBdQbEwAAAEmipgkAAMAHQhMAAIAPhCYAAAAfCE0AAAA+EJoAAAB8IDQBAAD4QGgCAADwgdAEAADgA6EJAADAB0ITAACAD4QmAAAAHwhNAAAAdnn/D9/vw0ajDhiXAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Plot smoking vs heart problems\n",
    "sns.countplot(data=hearGardaData, x='Heart Attack Risk', hue='smoke')\n",
    "plt.title('Heart Problems by Smoking Status')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "id": "4d2790e3-2050-4474-9666-29298fb8da78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABOcAAAHyCAYAAACgQao+AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAWeJJREFUeJzt3QmcXfP9N/Bf9gVJGmRB7GrNUrEFtYZYa21RJQgtRUlUiJLU0tqLElsV/fdflaL2Chp77DuxFE3FFokSIUQiuc/r+3ueO8+dyWSbTHKSmff79bqZueeee+45596Z+eZzfkuTUqlUSgAAAADAItd00b8kAAAAABCEcwAAAABQEOEcAAAAABREOAcAAAAABRHOAQAAAEBBhHMAAAAAUBDhHAAAAAAURDgHAAAAAAURzgEAAABAQYRzAEC9OuSQQ9LSSy+dGoLrr78+NWnSJP3nP/+pt23GtmKbse2Fuc/PPvtsvb6nq666alqUfv3rX+fjKMI222yTNthgg9QYxfsc7zcAsOgI5wBgCffKK6+kfffdN62yyiqpdevWacUVV0w77LBDuvTSS4vetUZp8ODBOVTab7/9it4VAACWAMI5AFiCPf7442mjjTZKL730UjriiCPSZZddlg4//PDUtGnTdMkllxS9e41OqVRKf/3rX3ProzvvvDN98cUXRe/SEuvUU09NX3/9ddG7AQCw0DVf+C8BACwsv/nNb1L79u3TM888kzp06FDtsQkTJhS2X43VQw89lN5///30wAMPpH79+qW///3vqX///kXv1hKpefPm+caS69tvv00zZ85MLVu2LHpXAGCxpuUcACzB3nnnnbT++uvPEsyFTp06VbsfXS2POeaYdNNNN6X11lsvtWnTJvXp0yd3iw1XXXVVWnPNNXPX2Bhzq7Zx1uK5vXv3zs9dbrnl0k9+8pP0wQcfzHU/X3zxxbT88svn7X755Zd5WTzvsMMOS507d06tWrXKx3HttdfO03Ffd911abvttsvHGM+N47niiitmWS9asO22227pscceS5tsskk+ttVXXz39z//8zyzrjhkzJm8zjm2llVZKZ511Vg4W5sdf/vKXvC/bbrtt6tu3b74/r9544430ox/9KJ+n2Ie11147/epXv6q2zgsvvJB23nnn1K5duzyu3/bbb5+efPLJWrf3zTffpEGDBuXtLbXUUmmvvfZKEydOnGW9yy+/PJ/7OI8rrLBCOvroo9OkSZNSXcRnLMaKm9s4ZtOnT0+nn356WmuttfJ7suyyy6Ytt9wy3X///XMcc678Gb7tttvymHDlz83IkSNrDUqjVWlsf4011sif7/kdx+65555Lm2++eX4/VltttXTllVdWPRaf4zivxx133CzPi4C2WbNm6eyzz57j9v/73/+mgw46KL+f8TMcQW60gq1tTML4fET39Y4dO+ZjimO74447ah1vcPTo0XN976OVZ3zG47Petm3b/JmNn4HaxOfh+OOPT926dcvnPH5PnHvuudV+PspjKV5wwQXp4osvzuc81n3ttdfmcpYBAJcjAWAJFuPMPfHEE+nVV1+dpwHsH3300fwf+ghgQoQHEV7FOGkR0vz85z9Pn332WTrvvPNycBYtwCr/43/ooYemjTfeOD/v448/zl1nIwiI0Ki2gDBEq75oRRZhwu23356DjnjuZpttVhW2RIhwzz33pAEDBqTJkyfnIGBOIoiLUOYHP/hBbl0VXUhj3yMsKB9b2dtvv51Djdh2hB8RAEZQFCFjbCOMHz8+hxPR0ufkk0/OgcbVV1+d93VeRRh2yy23pBNOOCHfP+CAA/L5im136dJljs99+eWX0/e///3UokWL9NOf/jSHWRG8xnFF68gQwUmsE0FOvF+xbgROEXg+/PDDadNNN622zWOPPTZ95zvfScOGDcvBSQQmca5HjBhRtU6EVRGSRZB41FFHpTfffDOf23jP4n2N11gY4nXjMxRdsCM0jfc8JrB4/vnn83iJcxJBa7RIjPd7mWWWSb///e/TPvvsk8aNG5dDvhCfx5122il17do1H9+MGTPSGWeckT9n8yp+DnbZZZccmMZ7+be//S2fo2gFFj8bEY5G6BXn83e/+10O48qia3OEXwceeOBstx+f1d133z09/fTTebvrrLNO/vmoraVlvPdbbLFFHk+y/PmM/dlzzz3zZy72Y37f+6FDh+ZwLo4xbnHud9xxxzRt2rRq2/rqq6/S1ltvncP0n/3sZ2nllVfO3emHDBmSPvroo7ztmsH51KlT8+c4wrkIEwGAuSgBAEus++67r9SsWbN869OnT2nw4MGle++9tzRt2rRZ1o0/+61atSqNHTu2atlVV12Vl3fp0qU0efLkquVDhgzJy8vrxvY6depU2mCDDUpff/111Xp33XVXXm/o0KFVy/r3719aaqml8vePPfZYqV27dqVdd921NHXq1Kp1BgwYUOratWvpk08+qbaP+++/f6l9+/alr776ao7HXdvj/fr1K62++urVlq2yyip5/x555JGqZRMmTMjn4YQTTqhadvzxx+f1nnrqqWrrxb5Unoc5ufnmm/O6b731Vr4f57N169aliy66qNp6sa1Y77rrrqtattVWW5WWWWaZ0rvvvltt3ZkzZ1Z9v+eee5ZatmxZeuedd6qWffjhh/l58fyy2G5sv2/fvtWeP3DgwPw5mTRpUtXxxfZ23HHH0owZM6rWu+yyy/Lzr7322mrvaZzLuYnnDRs2bJbl8dzYRlnPnj3zZ2JOYjs1S9W4H/v89ttvVy176aWX8vJLL720atnuu+9eatu2bemDDz6oWhbvS/PmzWfZZm223nrrvN6FF15Yteybb74p9erVK/8clH++4mct1rvnnnuqPb9Hjx55G3Nyyy235OdefPHFVcvifdhuu+1m+Xxsv/32pe7du1f7GYr3dvPNNy+ttdZadX7v4z2oXO+UU07Jz698r84888z88/yvf/2r2v6ffPLJeZvjxo2r9rmOn/fYPgAw73RrBYAlWLQyipZz0YIsusNFi7dopRYtbGp2eQvRDTJaZZWVW1tFy6NohVRz+b///e/8NVo1xRh20VoputSV7brrrrnFz9133z3Laz344IN5X+I1o6VTtKIJkbFEa59oNRTff/LJJ1W3WP/zzz/PrXjmpLJFW6wfz43WPbG/cb9SdDONFmdl0XoquoyWjy384x//yC35ohVX5XpzavlUU3RhjdaB0eUvxPmM8zO3rq3R3fCRRx7JrbGiVVKlchfMaPl133335ZZS0S23LFqG/fjHP86tyaL1WaVouVTZhTPOQWzn3Xffzff/+c9/5lZS0UoxJhApi4lFonVebe9pfYlWltEa7K233prv50Yrv+gyWdajR4+8v+X3M44xji3OVXTTLYv3JboEz6tokRktxcqixVzcj5+D6O5a3pd4jcr3OFqxRkvI6PI9J9EVN1omxvkui/ehZsvPTz/9NLdgjRZ8McFI+WclusTGz0ucw5pdy+f1vY8WdpXr1dZiNbqyx/OjJV7lz2oce2wzPruV4nfJ/LRQBACMOQcAS7zoZhrhV3TDiy5y0d0s/hMfXTlrjvdUM/yJySRCjCVV2/LY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65ff67Zt25a23Xbb0uOPP15tndhubP+ZZ56p9T2Nr5Uuu+yy/PmJ96Bz586lo446qvTZZ5/N8p7GuZybGTNmlE466aTScsstl/cv9vXtt9/Oz41tlJ111lmlTTbZJB9rmzZt8uv/5je/KU2bNq1qnWHDhuX9ndtnONTcfhg1alT+rMbPxBprrFG65pprSieccEI+t3MTn4P111+/9Oyzz5b69OmTnxOvEedqdnbZZZe8fzXfjzmZOHFi6cc//nFpmWWWKbVv3750yCGHlEaPHp23c+ONN1Zb95133ikdfPDB+eck3qv4jO62226lm2++uU7vfbxXp59+eqlr1675PYjPaHwGazuXX3zxRWnIkCH5d0ucz3h/N99889IFF1xQ9Z7N7ncJADB3TeKf+Q30AABgSROt1caMGVPr+IILKlqvRmuy+RnXrjbRHTe29dhjj+WWfwBAw2fMOQAAGpyvv/662v0I5GIsxvLEJPUpulNHF+QYe25B9jG638Y4cDF+YHRxBgAaB2POAQDQ4MS4bDFGWnx999130xVXXJHHKoyx4epLzGo7evTodM011+Rx5mIMxPkdMzICuj59+uSxA2MClRgz8re//W0erxEAaByEcwAANDgxycVf//rXNH78+NSqVascgEXotdZaa9Xba8QEJzFJysorr5z+9Kc/pS5duszX82OilAsvvDBPmjJ16tQ8Y220nKuviTEAgCWDMecAAAAAoCDGnAMAAACAggjnAAAAAKAgwjkAAAAAKIhwDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOeAxc4hhxySll566dRYfPzxx2nfffdNyy67bGrSpEm6+OKLU2Oz6qqr5vcdAFj0ov749a9/vVC2/dBDD+Xt33zzzfW2zdjX2OaS5Ntvv02DBw9O3bp1S02bNk177rlnamyi1ouaD5iVcA5Ir7zySg6HVlllldS6deu04oorph122CFdeumlRe9aozBw4MB07733piFDhqQ///nPaaeddip6lwCABuLyyy/PQdamm25a9K40atdee206//zzc839pz/9Kdd/AGXNq74DGqXHH388bbvttmnllVdORxxxROrSpUt677330pNPPpkuueSSdOyxxxa9iw3eAw88kPbYY4/0y1/+suhdAQAamL/85S+5tdLTTz+d3n777bTmmmsWvUuNtt6LC+AXXXRR0bsCLIaEc9DI/eY3v0nt27dPzzzzTOrQoUO1xyZMmFDYfjUmcZ5rnvsFMXXq1NSyZcvcZaIxim4jM2fOzOcAABqzsWPH5guxf//739PPfvazHNQNGzas6N1qlOq73otaZ9q0abnXS2NUKpVyzdumTZuidwXqReP8nxtQ5Z133knrr79+rcVCp06dqt2PLhHHHHNMuummm9J6662X/xj26dMnd4sNV111Vb4aG0XCNttsk/7zn//Mss14bu/evfNzl1tuufSTn/wkffDBB3PdzxdffDEtv/zyebtffvllXhbPO+yww1Lnzp1Tq1at8nFEl4G5if2KY7n++uvnOubKF198kY4//vh8xTleI85JdPl9/vnnqz3vqaeeyt1RI+hs27Zt2nrrrdPo0aPnuB/x+vF6UVwMHz48f185fsq///3v9MMf/jB17Ngxb3OzzTZLd999d63juNx4443p1FNPzVdkY93JkyfP9nX/+9//poMOOii1a9cuv+/9+/dPL730Uq3n5I033sjdL2If4n3daKON0h133FHrccTxDho0KL9PSy21VNprr73SxIkTq60bx3rWWWellVZaKe9ntNocM2ZMrfs5adKkfO5jbJY49/HZOvfcc3MxWvO9vOCCC/JYfWussUZe97XXXpvjuQeAxiDCuO985ztp1113zX/P4/68ijprwIABaYUVVsh/W1dbbbV01FFH5UBofmqVsvj7HReFowaImmL77bfPLfnqq1acnzFto56MW6UYziVqyTiOOGdR89xwww2znJP5rT3LtcqDDz6Ya55yvRc1XJgyZUo64YQTquqdtddeO9c1UTPVVofHexivG+uOHDlytq8b5ztq2nj/yjVX1Ee1nZP5rbmuvvrqqppr4403zhf5a7rtttvSBhtskN/r+HrrrbfOdj+jhotjinXj3EaQ/Nlnn1VbL/Z7t912y0PBxHsTn4/4vwc0FFrOQSMX48w98cQT6dVXX81/OOfm0UcfzeHM0Ucfne+fffbZ+Q9lDHAbY5r8/Oc/z39MzzvvvFy8RBP+yhDn0EMPzX/E43kxEUJ0nY1Q54UXXpjt1cT4g9+vX7/8h/j222/Pf4zjuVEAlguVCITuueeeXERGMBUFRn048sgj8wDG8RoRSEaw9dhjj6XXX389bbjhhnmdOMadd945F5JxNTparF133XVpu+22y+drk002qXXbW221VR5jLoKyCPwOPvjgqsfi+DbffPP01VdfpV/84hd5sogYn+QHP/hB3p8IviqdeeaZuaVYdI395ptvZttqLAqg3XffPXdtiQJ7nXXWyec0ArqaooDcYostcuB38skn58Dtb3/7Wx7A+JZbbpllH6ILdBSzcQ6igItCK87biBEjqtYZOnRoDud22WWXfIuQc8cdd6xW6Ic47gg4owiOAi26XceV/xiX76OPPppl0ow433H19Kc//WkuFOM/CQDQ2EWQs/fee+e64IADDkhXXHFFrquiFpuTDz/8MNcvEdrE39aoF+JvctQg8Tc6tje/tco555yTa6SoVT7//PNcKx544IH5AueC1ooL6g9/+EM+hggwjzvuuFxTvPzyy3nffvzjH+d16lp7xnpR70UwGReY47jCuuuumwO4OF8R3MV2evXqlcOnE088MZ/vml1go+aMWixeP4LLOU2uEDVTnOOo+6KOjgux8TWObUFqrggs4+J1rBvnIl4jPmMR1LZo0SKvc99996V99tkn185xvFE/x/sawWxNsZ3y+x7vQbT2vOyyy/L7He97eZvhzTffzJ/jeE4MxxNBJjQYJaBRu++++0rNmjXLtz59+pQGDx5cuvfee0vTpk2bZd34ldGqVavS2LFjq5ZdddVVeXmXLl1KkydPrlo+ZMiQvLy8bmyvU6dOpQ022KD09ddfV61311135fWGDh1atax///6lpZZaKn//2GOPldq1a1faddddS1OnTq1aZ8CAAaWuXbuWPvnkk2r7uP/++5fat29f+uqrr2Z7zLFP8ZrXXXddrcc4bNiwqvuxraOPPnq225o5c2ZprbXWKvXr1y9/Xxavv9pqq5V22GGH2T638jVrvsbxxx+flz/66KNVy7744ou8zVVXXbU0Y8aMvOzBBx/M662++upzPOayW265Ja9/8cUXVy2LbW233XaznJPtt9++1L1792rnPY5x8803z8dcFs+J5/bt27faORg4cGD+XE2aNCnfnzBhQqlly5b5vaxc75RTTsnPj/e97Mwzz8yfgX/961/V9v/kk0/O2xw3bly19zI+I7F9AOD/evbZZ/PfyPvvvz/fj7+9K620Uum4446ba/1z8MEHl5o2bVp65plnZlm3/Dd8fmuVddddt/TNN99UrXvJJZfk5a+8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uUEUUDGJQYxjEVfg4vs5Ofzww/M24msUgxHU/etf/6q2ThSuMeV7FLI9e/bM3VNj2zFYcIzXUi5gr7nmmrxv66+/fj6+GIctJkuI/YsgMIrb+XXyySenv/71r3m7MUhwjBESRU6MGxOFYbxuXUSxHeOpxEDDcTU13vMozsvnq7L7RwR2Mchz9+7d8zmOK8zxnkUBF4Mmx/iE8yOuOkc32bPPPjv/hyEK0hdeeCEX3RGWVjrxxBPzfsV6hxxySA5Bo+B/5ZVX0s0335wHmq75HAAg5b+fUcPEZF+12WyzzfLf5GhdF63EavPb3/42D+cRNVtM8BDdPuNiXQx3EmO/xQQK9V2r1LVWnJOo86Ju2GmnnXIQ9M4776T//d//rer5UBZdfLt06ZJbcMUkGhEGRpAVgWC5RduC1p61iYvPMS7gr371q1zbRL0Z5z2GdYkJs2ru57yKYzjuuONyvRqfgzj+qNvKNVdlvbcwaq6o9eLcRR152GGH5XMTF2ejVq68mB3v889+9rO8foxzHe9DfA6i1V181uK9jzocGoWip4sFinXPPfeUDjvssNI666xTWnrppUstW7YsrbnmmqVjjz229PHHH1dbN35lHH300dWWladVP//886stf/DBB/Pym266qdryESNGlL73ve+VWrVqVerYsWPpwAMPLL3//vvV1onp3WNK90oxbf16661X6tKlS+mtt97Ky2L/Yn+6detWatGiRX5s++23L1199dVzPe6Y7n7AgAGl9u3bl5ZZZpnSj370o9KECRPyPg8bNiyv880335ROPPHEUs+ePfM6sU/x/eWXXz7L9l544YXS3nvvnaeXj2OL6d5jm6NGjZrrvtR2XsM777xT2nfffUsdOnQotW7durTJJpuU7rrrrnk6z3MyceLE0o9//ON8THH8hxxySGn06NF5OzfeeOMs+3DwwQfncxvneMUVVyzttttupZtvvrlqneuuuy4/95lnnql13+Jr2YwZM0qnn356qWvXrqU2bdqUttlmm9Krr76az1e875W++OKL0pAhQ/LnMT6Xyy23XGnzzTcvXXDBBaVp06bN8fMHAI3V7rvvnuuGKVOmzHad+Nsff9ejvgqV9U/Zu+++m2uA5ZdfPtc2q6++eq5Xoj6qj1ql/Dc86oj5rRVjX+f1v7IXXnhhrl9ie1tssUXp2WefLW299db5VnbVVVeVttpqq6o6bo011sg14Oeff15tWwtSe8brrb/++rMsj3pn4MCBpRVWWCFvc6211sp1zcyZM+epXpydb7/9tnTaaaflfYyaa7vttiu9/vrr+RiPPPLIeq25avv83HLLLaV11103n8+o4f/+97/nWi9qvpri/PXu3TvvZ9Sn3bt3Lw0ePLj04YcfVq0Tz9t1113n+fhhSdMk/ik6IASgWLfddltuPRlXw8szkwEA0HBEN9EYh++ss87KrfWAxYcx5wAa4Vg0lWKsj+hqEF1wY7ILAAAaVr1XOc5veZI1YPFhzDmARjjOYBRsffr0yQMux6DRMc5gjC9jpiwAgCVfjB99/fXX5zF+Y9zk6B0RYwTGuG56ScDiRzgH0MjE5BoxQHBMtDF16tS05ppr5pZzMXsbAABLvh49euQZW88777w0efLkqkkioksrsPgx5hwAAAAAFMSYcwAAAABQEOEcAAAAABTEmHP1ZObMmenDDz9MyyyzTGrSpEnRuwMALCFihJEvvvgirbDCCqlpU9dNF0fqPABgYdZ5wrl6EgVbt27dit4NAGAJ9d5776WVVlqp6N2gFuo8AGBh1nnCuXoSV1LLJ7xdu3ZF7w4AsISIWfQi+CnXEix+1HkAwMKs84Rz9aTcxSEKNkUbADC/dJdcfKnzAICFWecZ2AQAAAAACiKcAwAAAICCCOcAAAAAoCDGnAMACpta/ttvv00zZsxIDVmzZs1S8+bNjSkHADQa6rz5I5wDABa5adOmpY8++ih99dVXqTFo27Zt6tq1a2rZsmXRuwIAsFCp8+afcA4AWKRmzpyZxo4dm680rrDCCrmQaaityuKqcRSoEydOzMe81lprpaZNjSoCADRM6rymddqWcA4AWKSiiInCrVu3bvlKY0PXpk2b1KJFi/Tuu+/mY2/dunXRuwQAsFCo81rXaTsu3QIAhWhMLcga07ECADSm2qdpPRxr4zlbAAAAALCYEc4BAPw/hxxySNpzzz2L3g0AABpRnSecAwAAAICCCOcAAOpx1q5vv/226N0AAGAJqvOEcwDAYueLL75IBx54YFpqqaVS165d00UXXZS22WabdPzxx+fHv/nmm/TLX/4yrbjiinmdTTfdND300ENVz7/++utThw4d0r333pvWXXfdtPTSS6eddtopffTRR1XrzJgxIw0aNCivt+yyy6bBgwfnoqtSzDZ29tlnp9VWWy3PxtWzZ8908803Vz0er9mkSZN0zz33pN69e6dWrVqlxx57bJGcIwCAJZE6b1bCOQBgsRPF1OjRo9Mdd9yR7r///vToo4+m559/vurxY445Jj3xxBPpxhtvTC+//HL64Q9/mIuyt956q2qdr776Kl1wwQXpz3/+c3rkkUfSuHHjcqFXduGFF+bi7tprr82F1qeffppuvfXWavsRBdv//M//pCuvvDKNGTMmDRw4MP3kJz9JDz/8cLX1Tj755HTOOeek119/PfXo0WOhnhsAgCWZOq8WJerF559/HhFs/goAzN7XX39deu211/LX2kyePLnUokWL0k033VS1bNKkSaW2bduWjjvuuNK7775batasWemDDz6o9rztt9++NGTIkPz9ddddl/8uv/3221WPDx8+vNS5c+eq+127di2dd955VfenT59eWmmllUp77LFHvj916tT8mo8//ni11xkwYEDpgAMOyN8/+OCD+XVuu+22Oh+zGmLx5z0CgHmjzqtbDdG8tsCOxd+EMS8VvQvMRaf1exa9CwBLpH//+99p+vTpaZNNNqla1r59+7T22mvn71955ZXcVeG73/1utedFF4jotlDWtm3btMYaa1Tdj24TEyZMyN9//vnnuetDdJMoa968edpoo42qujy8/fbb+arsDjvsUO11pk2blr73ve9VWxbPAwBgztR5tRPOAQBLlC+//DI1a9YsPffcc/lrpRhzpKxFixbVHosxQ2qONTK31wl33313HvOkUow5UinGQwEAYMF82UjrPOEcALBYWX311XPB9cwzz6SVV1656grov/71r7TVVlvlq5lxRTWujn7/+9+v02vEFdq4wvrUU0/lbYaYfSsKwQ033DDfX2+99XJxFmOYbL311vV4hAAAjZM6r3bCOQBgsbLMMsuk/v37pxNPPDF17NgxderUKQ0bNiw1bdo0XxWNbg4xw9fBBx+cB/uNIm7ixIlp1KhReZDeXXfddZ5e57jjjsuD+6611lppnXXWSb/73e/SpEmTqu1HDCwcgwPHbF5bbrllLh5jAON27drlfYSFwfAliz/DlwDUjTqvdsI5AGCxEwXUkUcemXbbbbdcIA0ePDi99957qXXr1vnx6667Lp111lnphBNOSB988EFabrnl0mabbZbXn1fx3BiPJIqvKAgPO+ywtNdee+XCrOzMM89Myy+/fJ7NK8ZI6dChQ77iesoppyyU4wYAaOjUebNqErNC1LKc+TR58uTcdDLe6PhwLWyuqC7+XFEFqN3UqVPT2LFj02qrrVZVhM3NlClT8nggcQV1wIABqSEd86KuIZh/6jxqUucB1E6d17pONYSWcwDAYueFF15Ib7zxRp7JK4qZM844Iy/fY489it41AAAWgDpvVsI5AGCxdMEFF6Q333wztWzZMvXu3Ts9+uijuVsDAABLNnVedcI5AGCxE4P/xoxaAAA0LOq8WTWtZRkAAAAAsAgI5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoSPOiXhgAoDYTxry0yF6r0/o95/s5jzzySDr//PPTc889lz766KN06623pj333HOh7B8AQEOizqudlnMAAPNhypQpqWfPnmn48OFF7woAAA2gztNyDgBgPuy88875BgBAw7JzQXWelnMAAAAAUBDhHAAAAAAURDgHAAAAAAURzgEAAABAQYRzAAAAAFAQs7UCAMyHL7/8Mr399ttV98eOHZtefPHF1LFjx7TyyisXum8AACx5dZ5wDgBgPjz77LNp2223rbo/aNCg/LV///7p+uuvL3DPAABYEus84RwAsFjptH7PtDjbZpttUqlUKno3AACWOOq82hlzDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoLGHc+ecc05q0qRJOv7446uWTZ06NR199NFp2WWXTUsvvXTaZ5990scff1zteePGjUu77rpratu2berUqVM68cQT07ffflttnYceeihtuOGGqVWrVmnNNddM119//SyvP3z48LTqqqum1q1bp0033TQ9/fTTC/FoAQAAAGAxCeeeeeaZdNVVV6UePXpUWz5w4MB05513pptuuik9/PDD6cMPP0x777131eMzZszIwdy0adPS448/nv70pz/l4G3o0KFV64wdOzavs+2226YXX3wxh3+HH354uvfee6vWGTFiRBo0aFAaNmxYev7551PPnj1Tv3790oQJExbRGQAAAACgMSo8nPvyyy/TgQcemP7whz+k73znO1XLP//88/THP/4x/e53v0vbbbdd6t27d7ruuutyCPfkk0/mde6777702muvpf/93/9NvXr1SjvvvHM688wzcyu4COzClVdemVZbbbV04YUXpnXXXTcdc8wxad99900XXXRR1WvFaxxxxBHp0EMPTeutt15+TrTEu/baaws4IwAAAAA0Fs2L3oHothot2/r27ZvOOuusquXPPfdcmj59el5ets4666SVV145PfHEE2mzzTbLX7t37546d+5ctU60eDvqqKPSmDFj0ve+9728TuU2yuuUu89GiBevNWTIkKrHmzZtmp8Tz52db775Jt/KJk+eXA9nAwDoscYWi+y1Xn5n9Hytf/bZZ6e///3v6Y033kht2rRJm2++eTr33HPT2muvvdD2kUVPnQcAja/OK7LWK7Tl3I033pi7kcbB1zR+/PjUsmXL1KFDh2rLI4iLx8rrVAZz5cfLj81pnSiyvv766/TJJ5/k7rG1rVPeRm1in9u3b19169at23wfPwCwZIlhNuLCYrTiv//++/OFxB133DFNmTKl6F2jHqnzAKBxerigWq+wlnPvvfdeOu644/LBxiQMS5poaRfj1JVF2KdwA4CGbeTIkdXux1i3MSFVtMLfaqutCtsv6pc6DwAap5EF1XqFhXNxYDHhQsyiWhYt2B555JF02WWX5QkbosvppEmTqrWei9lau3Tpkr+PrzVnVS3P5lq5Ts0ZXuN+u3btchPFZs2a5Vtt65S3UZuY+TVuAEDjFWPkho4dOxa9K9QjdR4AsChrvcK6tW6//fbplVdeyTOolm8bbbRRnhyi/H2LFi3SqFGjqp7z5ptvpnHjxqU+ffrk+/E1tlE5q2q0xIvgLSZ2KK9TuY3yOuVtRNfZmGyicp2ZM2fm++V1AABqinohxrDdYost0gYbbFD07gAAsITWeoW1nFtmmWVmObillloqLbvsslXLBwwYkLsUREIZgduxxx6bA7OYDCJEv98I4Q466KB03nnn5THiTj311Nw/uHy188gjj8wt8QYPHpwOO+yw9MADD6S//e1v6e6776563XiN/v3750Bwk002SRdffHHuTxyztwIA1CbqjVdffTU99thjRe8KAABLcK1X+Gytc3LRRRflmVP32WefPGNWzLJ6+eWXVz0e3VHvuuuuPDtrhHYR7kXIdsYZZ1Sts9pqq+UgbuDAgemSSy5JK620Urrmmmvytsr222+/NHHixDR06NAc8PXq1Sv3M645SQQAQDjmmGNyDRLDcURtAQBAw3HMIq71Fqtw7qGHHqp2PyaKGD58eL7NziqrrJL+8Y9/zHG722yzTXrhhRfmeuLjBgAwO6VSKbfkv/XWW3PdEhcBAQBoGEoF1XqLVTgHALC4d2+44YYb0u23356H6IgW96F9+/Z5oikAAJZcRdV6hU0IAQCwpLniiivyrF3RKr9r165VtxEjRhS9awAALKG1npZzAMBi5eV3RqfFuasDAAANr84rstbTcg4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMACtGYZj5tTMcKANCYap9SPRyrcA4AWKRatGiRv3711VepsSgfa/nYAQAaInVe3TSv4/MAAOqkWbNmqUOHDmnChAn5ftu2bVOTJk1SQ72SGgVbHGsccxw7AEBDpc6rG+EcALDIdenSJX8tF24NXRRs5WMGAGjI1HnzTzgHACxycQW1a9euqVOnTmn69OmpIYsuDlrMAQCNhTpv/gnnAIDCRDEjuAIAaHjUefPOhBAAAAAAUBDhHAAAAAAURDgHAAAAAAURzgEAAABAQYRzAAAAAFAQ4RwAAAAAFEQ4BwAAAAAFEc4BAAAAQEGEcwAAAABQEOEcAAAAABREOAcAAAAABRHOAQAAAEBBhHMAAAAAUBDhHAAAAAAURDgHAAAAAAURzgEAAABAQYRzAAAAAFAQ4RwAAAAAFEQ4BwAAAAAFEc4BAAAAQEGEcwAAAABQEOEcAAAAABREOAcAAAAABRHOAQAAAEBBhHMAAAAAUBDhHAAAAAAURDgHAAAAAAURzgEAAABAQYRzAAAAAFAQ4RwAAAAAFEQ4BwAAAAAFEc4BAAAAQEGEcwAAAABQEOEcAAAAABREOAcAAAAABRHOAQAAAEBBhHMAAAAAUBDhHAAAAAAURDgHAAAAAAURzgEAAABAQYRzAAAAAFAQ4RwAAAAAFEQ4BwAAAAAFEc4BAAAAQEGEcwAAAABQEOEcAAAAABREOAcAAAAABRHOAQAAAEBBhHMAAAAAUBDhHAAAAAAURDgHAAAAAAURzgEAAABAQYRzAAAAAFAQ4RwAAAAAFEQ4BwAAAAAFEc4BAAAAQEGEcwAAAADQGMO5K664IvXo0SO1a9cu3/r06ZPuueeeqsenTp2ajj766LTsssumpZdeOu2zzz7p448/rraNcePGpV133TW1bds2derUKZ144onp22+/rbbOQw89lDbccMPUqlWrtOaaa6brr79+ln0ZPnx4WnXVVVPr1q3Tpptump5++umFeOQAAAAAUHA4t9JKK6VzzjknPffcc+nZZ59N2223Xdpjjz3SmDFj8uMDBw5Md955Z7rpppvSww8/nD788MO09957Vz1/xowZOZibNm1aevzxx9Of/vSnHLwNHTq0ap2xY8fmdbbddtv04osvpuOPPz4dfvjh6d57761aZ8SIEWnQoEFp2LBh6fnnn089e/ZM/fr1SxMmTFjEZwQAAACAxqRJqVQqpcVIx44d0/nnn5/23XfftPzyy6cbbrghfx/eeOONtO6666YnnngibbbZZrmV3W677ZZDu86dO+d1rrzyynTSSSeliRMnppYtW+bv77777vTqq69Wvcb++++fJk2alEaOHJnvR0u5jTfeOF122WX5/syZM1O3bt3Ssccem04++eR52u/Jkyen9u3bp88//zy3AlzYJox5aaG/Bgum0/o9i94FAJYAi7qGYP6p86hJnQdAfdYQi82Yc9EK7sYbb0xTpkzJ3VujNd306dNT3759q9ZZZ5110sorr5zDuRBfu3fvXhXMhWjxFgdfbn0X61Ruo7xOeRvR6i5eq3Kdpk2b5vvldWrzzTff5NepvAEAsORT5wEAi1Lh4dwrr7ySx5OL8eCOPPLIdOutt6b11lsvjR8/Prd869ChQ7X1I4iLx0J8rQzmyo+XH5vTOlFkff311+mTTz7JwWBt65S3UZuzzz47p5/lW7S0AwBgyafOAwAaVTi39tpr57HgnnrqqXTUUUel/v37p9deey0t7oYMGZKbJZZv7733XtG7BABAPVDnAQCLUvNUsGgdFzOoht69e6dnnnkmXXLJJWm//fbLXU5jbLjK1nMxW2uXLl3y9/G15qyq5dlcK9epOcNr3I++vm3atEnNmjXLt9rWKW+jNtHSL24AADQs6jwAoFG1nKspJmOIcT4iqGvRokUaNWpU1WNvvvlmGjduXB6TLsTX6BZbOavq/fffn4O36BpbXqdyG+V1ytuIcDBeq3Kd2Ie4X14HAAAAABpcy7noMrDzzjvnSR6++OKLPDPrQw89lO699948vseAAQPSoEGD8gyuEbjF7KkRmMVMrWHHHXfMIdxBBx2UzjvvvDxG3KmnnpqOPvroqqudMY5dzMI6ePDgdNhhh6UHHngg/e1vf8szuJbFa0R32o022ihtsskm6eKLL84TUxx66KGFnRsAAAAAGr5Cw7lo8XbwwQenjz76KIdxPXr0yMHcDjvskB+/6KKL8syp++yzT25NF7OsXn755VXPj+6od911Vx6rLkK7pZZaKodsZ5xxRtU6q622Wg7iBg4cmLvLrrTSSumaa67J2yqLLrQTJ05MQ4cOzQFfr1690siRI2eZJAIAAAAA6lOTUqlUqtctNlIx+2sEjDFocLTyW9gmjHlpob8GC6bT+j2L3gUAlgCLuoZg/qnzqEmdB0B91hCL3ZhzAAAAANBYCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMAAACAggjnAAAAAKAgwjkAAAAAKIhwDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMAAACAggjnAAAAAKAgwjkAAAAAKIhwDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMAAACAggjnAAAAAGBJCue22267NGnSpFmWT548OT8GAAAAACykcO6hhx5K06ZNm2X51KlT06OPPlqXTQIAAABAo9N8flZ++eWXq75/7bXX0vjx46vuz5gxI40cOTKtuOKK9buHAAAAANBAzVc416tXr9SkSZN8q637aps2bdKll15an/sHAAAAAA3WfIVzY8eOTaVSKa2++urp6aefTssvv3zVYy1btkydOnVKzZo1Wxj7CQAAAACNO5xbZZVV8teZM2curP0BAAAAgEZjvsK5Sm+99VZ68MEH04QJE2YJ64YOHVof+wYAAAAADVqdwrk//OEP6aijjkrLLbdc6tKlSx6Driy+F84BAAAAwEIK584666z0m9/8Jp100kl1eToAAAAAkFJqWpcnffbZZ+mHP/xh/e8NAAAAADQidQrnIpi777776n9vAAAAAKARqVO31jXXXDOddtpp6cknn0zdu3dPLVq0qPb4L37xi/raPwAAAABosOoUzl199dVp6aWXTg8//HC+VYoJIYRzAAAAALCQwrmxY8fW/54AAAAAQCNTpzHnAAAAAICCWs4ddthhc3z82muvrev+AAAAAECjUadw7rPPPqt2f/r06enVV19NkyZNStttt1197RsAAAAANGh1CuduvfXWWZbNnDkzHXXUUWmNNdaoj/0CAAAAgAav3saca9q0aRo0aFC66KKL6muTAAAAANCg1euEEO+880769ttv63OTAAAAANBg1alba7SQq1QqldJHH32U7r777tS/f//62jcAAAAAaNDqFM698MILs3RpXX755dOFF14415lcAQAAAIAFCOcefPDBujwNAAAAAFjQcK5s4sSJ6c0338zfr7322rn1HAAAAACwECeEmDJlSu6+2rVr17TVVlvl2worrJAGDBiQvvrqq7psEgAAAAAanaZ1nRDi4YcfTnfeeWeaNGlSvt1+++152QknnFD/ewkAAAAADVCdurXecsst6eabb07bbLNN1bJddtkltWnTJv3oRz9KV1xxRX3uIwAAAAA0SHVqORddVzt37jzL8k6dOunWCgAAAAALM5zr06dPGjZsWJo6dWrVsq+//jqdfvrp+TEAAAAAYCF1a7344ovTTjvtlFZaaaXUs2fPvOyll15KrVq1Svfdd19dNgkAAAAAjU6dwrnu3bunt956K/3lL39Jb7zxRl52wAEHpAMPPDCPOwcAANBQ9Vhji6J3gXnw8juji94FgIUXzp199tl5zLkjjjii2vJrr702TZw4MZ100kl12SwAAAAANCp1GnPuqquuSuuss84sy9dff/105ZVX1sd+AQAAAECDV6dwbvz48alr166zLF9++eXTRx99VB/7BQAAAAANXp3CuW7duqXRo2ftvx/LVlhhhfrYLwAAAABo8Oo05lyMNXf88cen6dOnp+222y4vGzVqVBo8eHA64YQT6nsfAQAAAKBBqlM4d+KJJ6b//ve/6ec//3maNm1aXta6des8EcSQIUPqex8BAAAAoEGqUzjXpEmTdO6556bTTjstvf7666lNmzZprbXWSq1atar/PQQAAACABqpO4VzZ0ksvnTbeeOP62xsAAAAAaETqNCEEAAAAALDghHMAAAAA0BjDubPPPjt3i11mmWVSp06d0p577pnefPPNautMnTo1HX300WnZZZfN3Wj32Wef9PHHH1dbZ9y4cWnXXXdNbdu2zduJCSu+/fbbaus89NBDacMNN8zj4q255prp+uuvn2V/hg8fnlZdddU8ucWmm26ann766YV05AAAAABQcDj38MMP5+DtySefTPfff3+aPn162nHHHdOUKVOq1hk4cGC6884700033ZTX//DDD9Pee+9d9fiMGTNyMBezxj7++OPpT3/6Uw7ehg4dWrXO2LFj8zrbbrttevHFF9Pxxx+fDj/88HTvvfdWrTNixIg0aNCgNGzYsPT888+nnj17pn79+qUJEyYswjMCAAAAQGPSpFQqldJiYuLEibnlW4RwW221Vfr888/T8ssvn2644Ya077775nXeeOONtO6666YnnngibbbZZumee+5Ju+22Ww7tOnfunNe58sor00knnZS317Jly/z93XffnV599dWq19p///3TpEmT0siRI/P9aCkXrfguu+yyfH/mzJmpW7du6dhjj00nn3zyXPd98uTJqX379nmf27Vrlxa2CWNeWuivwYLptH7PoncBgCXAoq4hmH/qPGrq+4OfF70LzIOX3xld9C4AjdzkeawhFqsx52JnQ8eOHfPX5557Lrem69u3b9U666yzTlp55ZVzOBfia/fu3auCuRAt3uIEjBkzpmqdym2U1ylvI1rdxWtVrtO0adN8v7wOAAAAANS35mkxES3VorvpFltskTbYYIO8bPz48bnlW4cOHaqtG0FcPFZepzKYKz9efmxO60SA9/XXX6fPPvssd4+tbZ1oqVebb775Jt/KYlsAACz51HkAwKK02LSci7HnotvpjTfemJYEMZlFNE0s36ILLAAASz51HgDQ6MK5Y445Jt11113pwQcfTCuttFLV8i5duuQupzE2XKWYrTUeK69Tc/bW8v25rRP9fdu0aZOWW2651KxZs1rXKW+jpiFDhuRuuOXbe++9t0DnAACAxYM6DwBoNOFczEURwdytt96aHnjggbTaaqtVe7x3796pRYsWadSoUVXL3nzzzTRu3LjUp0+ffD++vvLKK9VmVY2ZXyN4W2+99arWqdxGeZ3yNqLrbLxW5TrRzTbul9epqVWrVvk1Km8AACz51HkAQKMZcy66ssZMrLfffntaZpllqsaIi+4D0aItvg4YMCANGjQoTxIRhVHMnhqBWczUGnbcccccwh100EHpvPPOy9s49dRT87ajsApHHnlknoV18ODB6bDDDstB4N/+9rc8g2tZvEb//v3TRhttlDbZZJN08cUXpylTpqRDDz20oLMDAAAAQENXaDh3xRVX5K/bbLNNteXXXXddOuSQQ/L3F110UZ45dZ999skD88Ysq5dffnnVutEdNbrEHnXUUTm0W2qppXLIdsYZZ1StEy3yIogbOHBguuSSS3LX2WuuuSZvq2y//fZLEydOTEOHDs0BX69evdLIkSNnmSQCAAAAAOpLk1L0LWWBxSxe0dIvxiVZFF0fJox5aaG/Bgum0/o9i94FAJYAi7qGYP6p86ip7w9+XvQuMA9efmd00bsANHKT57GGWCwmhAAAAACAxqjQbq3QkPVYY4uid4F54IoqAAAARdJyDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMAAACAggjnAAAAAKAgwjkAAAAAKIhwDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMAAACAggjnAAAAAKAgwjkAAAAAKIhwDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMAAACAggjnAAAAAKAgwjkAAAAAKIhwDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMAAACAggjnAAAAAKAgwjkAAAAAKIhwDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAAAoinAMAAACAggjnAAAAAKAgwjkAAAAAKIhwDgAAAAAKIpwDAAAAgIII5wAAAACgIMI5AAAAACiIcA4AAAAACiKcAwAAAICCCOcAAAAAoCDCOQAAAAAoiHAOAAAAABpjOPfII4+k3XffPa2wwgqpSZMm6bbbbqv2eKlUSkOHDk1du3ZNbdq0SX379k1vvfVWtXU+/fTTdOCBB6Z27dqlDh06pAEDBqQvv/yy2jovv/xy+v73v59at26dunXrls4777xZ9uWmm25K66yzTl6ne/fu6R//+MdCOmoAAAAAWAzCuSlTpqSePXum4cOH1/p4hGi///3v05VXXpmeeuqptNRSS6V+/fqlqVOnVq0TwdyYMWPS/fffn+66664c+P30pz+tenzy5Mlpxx13TKusskp67rnn0vnnn59+/etfp6uvvrpqnccffzwdcMABOdh74YUX0p577plvr7766kI+AwAAAAA0Zk1K0TxtMRAt52699dYcioXYrWhRd8IJJ6Rf/vKXednnn3+eOnfunK6//vq0//77p9dffz2tt9566ZlnnkkbbbRRXmfkyJFpl112Se+//35+/hVXXJF+9atfpfHjx6eWLVvmdU4++eTcSu+NN97I9/fbb78cFEa4V7bZZpulXr165WBwXkQI2L59+7yP0YpvYZsw5qWF/hosmL4/+HnRu8A8ePmd0UXvAtDILeoagvmnzqMmdd6SQZ0HLCk1xGI75tzYsWNzoBZdWcvigDbddNP0xBNP5PvxNbqyloO5EOs3bdo0t7Qrr7PVVltVBXMhWt+9+eab6bPPPqtap/J1yuuUXwcAAAAAFobmaTEVwVyIlnKV4n75sfjaqVOnao83b948dezYsdo6q6222izbKD/2ne98J3+d0+vU5ptvvsm3yjQUAIAlnzoPAFiUFtuWc4u7s88+O7fkK99iogkAAJZ86jwAYFFabMO5Ll265K8ff/xxteVxv/xYfJ0wYUK1x7/99ts8g2vlOrVto/I1ZrdO+fHaDBkyJPcZLt/ee++9BThaAAAWF+o8AGBRWmzDueiKGuHYqFGjqnUpiLHk+vTpk+/H10mTJuVZWMseeOCBNHPmzDw2XXmdmMF1+vTpVevEzK5rr7127tJaXqfydcrrlF+nNq1atcqD+VXeAABY8qnzAIBGE859+eWX6cUXX8y38iQQ8f24cePy7K3HH398Ouuss9Idd9yRXnnllXTwwQfnGVjLM7quu+66aaeddkpHHHFEevrpp9Po0aPTMccck2dyjfXCj3/84zwZxIABA9KYMWPSiBEj0iWXXJIGDRpUtR/HHXdcnuX1wgsvzDO4/vrXv07PPvts3hYAAAAANMgJISIA23bbbavulwOz/v37p+uvvz4NHjw4TZkyJf30pz/NLeS23HLLHKK1bt266jl/+ctfcoi2/fbb51la99lnn/T73/++6vEYJ+S+++5LRx99dOrdu3dabrnl0tChQ/M2yzbffPN0ww03pFNPPTWdcsopaa211kq33XZb2mCDDRbZuQAAAACg8WlSKpVKRe9EQxBdbiMIjHFJFkXXhwljXlror8GC6fuDnxe9C8yD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AAAAUBDhHAAAAAAURDgHULBDDjkk7bnnnkXvBgAAc/Gf//wnNWnSJL344otF7wrQgAjnAAAAAKAgwjkAAAAAKIhwDqCGm2++OXXv3j21adMmLbvssqlv375pypQpVd1Pf/vb36bOnTunDh06pDPOOCN9++236cQTT0wdO3ZMK620Urruuuuqbe+VV15J2223XdX2fvrTn6Yvv/xytq//zDPPpOWXXz6de+65+f6kSZPS4Ycfnpe1a9cub+ull15a6OcBAKAxGjlyZNpyyy1zrRe122677Zbeeeed2a4/ZsyYvE7Uacsss0z6/ve/X7X+zJkzc70YNWKrVq1Sr1698vYBKgnnACp89NFH6YADDkiHHXZYev3119NDDz2U9t5771QqlfLjDzzwQPrwww/TI488kn73u9+lYcOG5WLsO9/5TnrqqafSkUcemX72s5+l999/P68foV6/fv3y4xG63XTTTemf//xnOuaYY2p9/dj+DjvskH7zm9+kk046KS/74Q9/mCZMmJDuueee9Nxzz6UNN9wwbb/99unTTz9dhGcGAKBxiPpt0KBB6dlnn02jRo1KTZs2TXvttVcO2mr64IMP0lZbbZWDt6jjolaLOjIu3oZLLrkkXXjhhemCCy5IL7/8cq4Lf/CDH6S33nqrgCMDFldNSuX/cQKQnn/++dS7d+882O8qq6xS7bFoORdh3b///e9cpIV11lknderUKYd1YcaMGal9+/bpmmuuSfvvv3/6wx/+kEO29957Ly211FJ5nX/84x9p9913zyFftMCL7UbruP79+6eDDz44P3e//fbL6z722GNp1113zeFcFH1la665Zho8eHBuhQcAwMLzySef5B4M0Rti6aWXTquttlp64YUXciu4U045Jd14443pzTffTC1atJjluSuuuGI6+uij83plm2yySdp4443T8OHDF/GRAIsrLecAKvTs2TO3SoturdFiLcK1zz77rOrx9ddfvyqYCxGuxbplzZo1y90fIkwL0foutlkO5sIWW2yRr7xGEVcWre7i9f785z9XBXMhuq9GF9jYZhSD5dvYsWPn2L0CAIC6iVZt0ZNi9dVXz11VV1111bx83Lhxs6wbs7ZGN9bagrnJkyfni7FR+1WK+1EjApQ1r/oOgByu3X///enxxx9P9913X7r00kvTr371qxyehZqFV5MmTWpdVlu3hzlZY401cgB37bXX5pZy5W1GMNe1a9fcYq+mGAcFAID6FT0cogdFXKRdYYUVcl23wQYbpGnTps2ybowpDLCgtJwDqCHCtbiiefrpp+cuCy1btky33nprnba17rrr5tZvMXZJ2ejRo3Pru7XXXrtq2XLLLZfHKXn77bfTj370ozR9+vS8PMaXGz9+fGrevHnuylp5i+cAAFB//vvf/+beDaeeemruTRG1XGUvipp69OiRHn300ararVK0uotwL2q/SnF/vfXWWyj7DyyZhHMAFaKFXMzGGgMAR9eFv//972nixIm5MKuLAw88MLVu3TqPJ/fqq6+mBx98MB177LHpoIMOyl1iK8XYdRHQvfHGG7krRQwkHDPF9unTJ88SGy35Yiy8aNUXrfliHwEAqD8xiVf0Zrj66qvzRdOozWJyiNmJSb6i+2qMNRy1WXSJjWFKysOXnHjiiencc89NI0aMyMtOPvnk3BX2uOOOW4RHBSzuhHMANa5wxuQOu+yyS/rud7+br5rGDFs777xznbbXtm3bdO+99+aZVWPg33333Tdfhb3ssstqXb9Lly65CIwBhyPYi24UMYFEzAJ26KGH5n2K4u/dd9+dJdwDAGDBRO+GmOAhZl2NrqwDBw5M559//mzXjyAvarcYimTrrbfOE4tFd9jyECW/+MUvcrh3wgkn5HGKR44cme6444601lprLcKjAhZ3ZmsFAAAAgIJoOQcAAAAABRHOAQAAAEBBhHMAAAAAUBDhHAAAAAAURDgHAAAAAAURzgEAAABAQYRzAAAAAFAQ4RwAAAAAFEQ4BwAAAAAFEc4BAAAAQEGEcwAAAABQEOEcAAAAAKRi/B8/vaVbaUPmbAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1500x500 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=True)\n",
    "fig.suptitle('Smoke and Alcohol using by gender')\n",
    "\n",
    "# Bulbasaur\n",
    "sns.countplot(ax=axes[0], x=hearGardaData.smoke,hue=hearGardaData.gender)\n",
    "axes[0].set_title(\"Smoke use for gender\")\n",
    "\n",
    "# Charmander\n",
    "sns.countplot(ax=axes[1], x=hearGardaData.alco,hue=hearGardaData.gender)\n",
    "axes[1].set_title(\"Alcohol use for gender\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "id": "2762cc62-450f-4f54-812b-43ff5d4cca33",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender\n",
       "1    45470\n",
       "2    24434\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 264,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Total number of male and female\n",
    "gender_count=hearGardaData[\"gender\"].value_counts()# 1 Male 2 Female\n",
    "gender_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "id": "f3d447d0-03bf-45ad-afdb-6d66c11d6d3f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "gender\n",
       "1    22588\n",
       "2    12345\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 265,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sex_heart_attacks = hearGardaData[hearGardaData['Heart Attack Risk'] == 1]['gender'].value_counts()\n",
    "sex_heart_attacks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "id": "4de8118a-4e68-4035-9ed3-806ea6014abe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 69904 entries, 0 to 69999\n",
      "Data columns (total 15 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   age                69904 non-null  int64  \n",
      " 1   gender             69904 non-null  int64  \n",
      " 2   height             69904 non-null  int64  \n",
      " 3   weight             69904 non-null  float64\n",
      " 4   Systolic           69904 non-null  int64  \n",
      " 5   Diastolic          69904 non-null  int64  \n",
      " 6   cholesterol        69904 non-null  int64  \n",
      " 7   gluc               69904 non-null  int64  \n",
      " 8   smoke              69904 non-null  int64  \n",
      " 9   alco               69904 non-null  int64  \n",
      " 10  active             69904 non-null  int64  \n",
      " 11  BMI                69904 non-null  float64\n",
      " 12  diabetes_signal    69904 non-null  int64  \n",
      " 13  Family_History     69904 non-null  int64  \n",
      " 14  Heart Attack Risk  69904 non-null  int64  \n",
      "dtypes: float64(2), int64(13)\n",
      "memory usage: 8.5 MB\n"
     ]
    }
   ],
   "source": [
    "hearGardaData.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "id": "dd6e2aae-c988-4c61-a8d1-bce4652471b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>Systolic</th>\n",
       "      <th>Diastolic</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>BMI</th>\n",
       "      <th>diabetes_signal</th>\n",
       "      <th>Family_History</th>\n",
       "      <th>Heart Attack Risk</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>48</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>48</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  gender  height  weight  Systolic  Diastolic  cholesterol  gluc  smoke  \\\n",
       "0   50       2     168    62.0       110         80            1     1      0   \n",
       "1   55       1     156    85.0       140         90            3     1      0   \n",
       "2   52       1     165    64.0       130         70            3     1      0   \n",
       "3   48       2     169    82.0       150        100            1     1      0   \n",
       "4   48       1     156    56.0       100         60            1     1      0   \n",
       "\n",
       "   alco  active  BMI  diabetes_signal  Family_History  Heart Attack Risk  \n",
       "0     0       1  2.0                0               1                  0  \n",
       "1     0       1  4.0                0               1                  1  \n",
       "2     0       0  2.0                0               0                  1  \n",
       "3     0       1  3.0                0               1                  1  \n",
       "4     0       0  2.0                0               1                  0  "
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
   "id": "712954ed-b686-4e77-8542-bea46b478454",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABKUAAAJOCAYAAABm7rQwAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAbVdJREFUeJzt3QeYVOX5P+6XXqSKChIRsSOisfeKijV2o9hL1MTYiGhMbNiNNc0SNaixm2gsiRpFMfbeNajYQcWCoCKguP/reX/f2f/usgsL7J5t931dw7JzZs68M3Nm9sxnnvc5rcrKysoSAAAAABSodZE3BgAAAABBKAUAAABA4YRSAAAAABROKAUAAABA4YRSAAAAABROKAUAAABA4YRSAAAAABROKAUAAABA4YRSAAAAABROKAVQsJVXXjm1atUqdejQIX3++eepqdh4443zuCueFlhggbToooum9dZbLx1++OHpgQceSGVlZTWuY7/99svXu+qqq1Jjuk9jxoxp1OMMp5xySh5T/GysGuMYY3u8/fbb0957752WWWaZ1K1bt9S+ffu08MILp/XXXz+NGDEiPfHEE6kpKL3umNW7776bH5slllhirq4Xl6/Na730XtGYtu2iNNW/WfP6/j+vSn83Kp7atm2bFlpoobTRRhulP//5z+m7776r9roxhrh8jKm5vQcDzIlQCqBATz/9dHrppZfy/2fMmJGuvfba1BQ/oOy77775tP3226eVVlopjRs3Lv3pT39KQ4YMST/+8Y/T888/36Q+TDS0uvpAQmXvvPNOWmONNdIOO+yQX2s//PBD2mSTTdKuu+6aVl999bzdnnfeeWmdddZJO+20U0MPFxrd++Pc/s2aU3DaEt7rllpqqfK/kbvssktabLHF0n//+9/0y1/+Mr//fPvttw09RIBGpW1DDwCgJbnyyivzzx/96Edp/Pjx+fcjjzwyNSXxAb+6b2EffvjhdMwxx6SnnnoqV6A89NBD+YN/RWeddVb69a9/naurGoNrrrkmTZ06NS2++OKpsYsPNLvvvnv+1p05e++999Laa6+dJk6cmEOnCE1XXXXVWS4XVVLnnntueu211xpknNCYNYe/WUWLv39VK+9uvPHGtMcee6RHH300vxdFhWZFa665Znr99ddT586dCx4tQMNTKQVQkAg/brjhhvz/v/3tb6lLly7p5Zdf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Heehhx5a1rFjx7IBAwbkcQ0dOjTfZiyL5+GHH36YZZ3xOJfuz+abb56fo8UWW6ysW7duZUceeWReFuuvavXVV8/L4n7vueee+f4cd9xx5ctPPvnkvDx+VnXCCSfkZa1atSpbf/318/NS2p7atGlTduWVV9b6vtfm9mpSus4+++yTt9HYLnbdddey7bbbrmyBBRbIy9ZZZ52yqVOn1riOF154oXxbiuvNjzfffLPsxz/+cfn6ll566fz87LXXXmU77LBD+TYWp3jcPvzww0rXnzJlStmQIUPKt7U11lijbLfddsv3Kf5f2hZef/318uvE4xnnxeNbk9JtVnXDDTfk5yuWDR48uGyPPfYo23DDDfPzevTRR9d4vXifKN3PeJzXXXfdvL3G+0WcX1rnt99+W36deA3WtC3WxqRJk/Lrq/TeFI/nzjvvXLbIIouUde3atcZtfU63O7vX7u9+97vyx2CttdbK23k8D/F76fGZ02u+qtJ9qPieVJ3S66W618PNN99c1rlz57w8XutbbLFFfg1vtdVW+fc4/6c//Wm17xOxDcXl4/lafvnl83P929/+ttr7Utv3tTm9P9bn36xjjjkmn7fQQgvl10rcbpw+++yzWr/Xlbad1q1b58c9Xgel2yq911X3Onj33XfLX9PxfMTjWnoNde/efZbHrab3wCeeeKKsZ8+eednZZ59dVlulvxuze0298cYbZW3bts2X+89//jPH940Yd5wf20b8zYltPv6Gl9YR77W1ed/+5JNP8t/mWBav1WnTptX6fgHUN6EUQD3Ze++98w5gBCy1cdFFF+XLDxw4sNL5EydOLDvssMPyh5v4kNGvX7/8++eff1626aab5uvce++91a4zPoTETn/sjMcHjfiwuOyyy+ad0iuuuKJWHzyq7sBXPEXwEsFDBA2//OUvy0aPHl1tUDO7UOqjjz7KO/5bb711Dn/iw0QEOCussEK+n//73/+qXdfll1+eP6iUPgxWXG9dhVKxvueeey6HI/HBOx7DCPguuOCCsu+++67adcbOfnxwWnLJJcvatWuXP6THB6O33nprth/I33vvvfyBY9FFFy3/wFFx/HMKiSK4i8cwxhnXLwVCTz755Fzd99re3pyu8/bbb+f73bt377zdRiB00kknlX3zzTdzXE8p5Kxpu54bsT3eeuut+bFdaqmlyrp06ZKfl/jQvPbaa5cdddRRZY899liN1585c2bZ9ddfnx/buC9x3XiMV1xxxbL9998/h6ozZsyok1AqPPzwwzn8jNdAbNurrLJK2WWXXTbH68V2d+mll5Ztsskm5dtAbHsRSsXrqOpjOb+hVPj000/LfvGLX+THNV4bffv2zYFfhIE1rX9+Qqlw++235wAxwrd4LiOA+/vf/17r13x9hFKlcUcwFttFjC3C7Fh3BAjx/hav/4pimzn33HNz+BjPc4S4EaJEUFHTfZmb+zi798f6/JsVweexxx6bX++l0DZOMfbavtfFazaC9NVWWy0/xxHMxHN+4403zvF18NVXX5Wdc845OayMv3exXca648uB0vVr8x744osv5tdPLI+QsK5CqXDIIYeUB/Rzet+49tpr8/tMbFexjZTuTwSe8d5T9e/t7N63I0iO24zl8YVJbd6LAYrQKv6Z+/oqABpaTDlacskl81S+mD5UX0fSgyJFA+Do0xPTTWKq5OyOPgkAQNOmpxRAIxe9YqqKHh7R8yN6xcRhswVSNAfRu6vUa2X48OECKQCAZk6lFEAjFx/MozlsNMft1atXGj9+fG4O/vXXX+ejN0Vj8dJh4aEpGjVqVD5U+jPPPJObQg8ePDg999xz1R59CwCA5sPeHkAjd8IJJ+SjNL344ou5MiqO9BRH1IkKqagmiaAKmrKHHnooH7msR48e+YiRF110kUAKAKAFUCkFAAAAQOH0lAIAAACgcEIpAAAAAArXIhs2/PDDD2nChAmpa9eujuwDAAAAUIeiU9RXX32V+vbtm1q3rrkeqkWGUhFIOVIVAAAAQP354IMP8pHEa9IiQ6mokCo9ON26dWvo4QAAAAA0G1OmTMnFQKX8pSYtMpQqTdmLQEooBQAAAFD35tQySaNzAAAAAAonlAIAAACgcEIpAAAAAAonlAIAAACgcEIpAAAAAAonlAIAAACgcEIpAAAAAAonlAIAAACgcEIpAAAAAAonlAIAAACgcEIpAAAAAAonlAIAAACgcEIpAAAAAAonlAIAAACgcEIpAAAAAArXKEOp8ePHp7322iv16tUrderUKQ0ePDg988wz5cv322+/1KpVq0qnLbfcskHHDAAAAEDttU2NzKRJk9J6662XNtlkk3T33XenhRdeOL355pupZ8+elS4XIdSoUaPKf+/QoUMDjBYAAACAZhFKnXPOOalf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118/V0FtueWWqW3bWa/WtWvXfOrfv3/aYost0oknnpjee++9dPnll6c//elPqUePHumkk06qj/sAAAAAQHMMpe677740ZMiQuV55BFSnn356OuaYY3IVFQAAAADUevrevARSFUWV1CqrrOIRBwAAAKD2oRQAAAAANMjR9yp6+eWX09NPP5122WWX1K1bt3zet99+mxuaR9+pTp065Sl7hx56aJ0OFgAAgLr1QatWDT0EaHG87uYjlIo+UY888kjaf//9y8/7zW9+ky677LLUpUuX9Nlnn6XDDjssLbXUUmnzzTefl5sAAACgHpW1K0utysrSOdUcyAqofx3bt089e/ZMLdk8vfs89dRTaZNNNkmt/i/Z+/7779OoUaPSmmuumcaMGZO++OKLtOqqq6bf//73QikAAIBG6IcOP6SyVq3SueeemwsKaFrGjRuXRowY4flrwnr27Jn69u2bWrJ5CqU+/fTT1K9fv/LfYyrflClT8nS9jh075gd1++23T//+97/rcqwAAADUsQg0Bg0a1NDDYB55/mhxjc7btm2bpk+fXv57VEdF1VRUT5X06tUrT+MDAAAAgDoJpZZYYon04IMPlv9+yy23pAEDBqT+/fuXnzd+/PgcTAEAAABAnYRSe++9d3rxxRfTWmutlTbccMP8/2HDhlW6zEsvvZSWWWaZeVk9AAAAAM3cPIVSv/zlL9Ouu+6annnmmXwUvq222ioffa/k1VdfzUHVpptuWpdjBQAAAKAlNzrv0KFDuummm3Jz8+gl1bVr10rLe/funZ5//vk8zQ8AAAAA6qRS6oADDkgXXnhh6tat2yyBVFhooYXSyiuvnLp37z7X6z7llFNy0FXxtPzyy5cvnzZtWjrssMNyv6ouXbqknXfeOX3yySfzcjcAAAAAaEqh1PXXX58mTpyY6ksczvKjjz4qP8UUwZKjjz463Xnnnbm5+kMPPZQmTJiQdtppp3obCwAAAACNZPreUkstlcOi+tK2bdvUp0+fWc6fPHlyuvLKK3MoVupXNWrUqDRw4MD0xBNPpLXXXrvexgQAAABAI5i+969//SuNHz8+1Yc333wz9e3bNy255JJpzz33TO+//34+/9lnn03fffdd2myzzcovG1P7Fl988fT444/Xy1gAAAAAaCSVUtHH6cEHH0zrrrtuOvbYY9Maa6yRm5tH/6eqIjCaG2uttVa66qqr0nLLLZersUaOHJk22GCD9Morr6SPP/44tW/fPvXo0aPSdeK2Y1lNpk+fnk8l0aAdoL58UM17IVC/vO4AAFpIKBUVTBFAlZWVpSOOOKLGy8Vlvv/++7la91ZbbVX+/5VWWimHVP37908333xz6tSp07wMN5111lk53AKoT2XtylKrsrJ0Ttt5emsF5lPH9u1Tz549G3oYAADU0jx9ctpnn32qrYqqD1EVteyyy6a33norbb755mnGjBnpyy+/rFQtFUffq64HVcnxxx+fhg8fXqlSql+/fvU+dqBl+aHDD6msVat07rnn5t57NC3jxo1LI0aM8Pw1YRFIxfR/AACacSgV0+uK8vXXX+cPCnvvvXdabbXVUrt27dLo0aPzFMIwduzY3HNqnXXWqXEdHTp0yCeAIkSgEUcRpWny/AEAQDEa3RyTY445Jm233XZ5yt6ECRPSySefnNq0aZP22GOP1L1793TggQfmqqcFF1wwdevWLR1++OE5kHLkPQAAAICmo9GFUh9++GEOoD7//PO08MILp/XXXz898cQT+f/hwgsvTK1bt86VUtG8fOjQoeniiy9u6GEDAAAAUEQo9dVXX6U//elP6f77788VTRWPblcSfadi6t3cuPHGG2e7vGPHjunPf/5zPgEAAADQgkKpTz/9NK277ro5cIopdNE4PKbWRRPyb7/9Nl8mGo1G/ycAAAAAqKp1mgennHJKDqSuueaaNGnSpHze0Ucfnb755pv05JNPpjXXXDMtscQS6dVXX52X1QMAAADQzM1TKPXvf/87DRkyJO211155il5Fa6yxRrr77rvTu+++m0aOHFlX4wQAAACgpYdSH330UVpllVXKf4+j45Wm7YWePXumrbbaKt188811M0oAAAAAmpV5CqWif9R3331XKYSKo+ZVFL2mPvnkk/kfIQAAAADNzjyFUksuuWSenlcSVVP33Xdf+vzzz/PvUTV15513psUXX7zuRgoAAABAyw6ltthiizR69Og0derU/PshhxySJk6cmFZeeeW06667phVXXDE3Qt9vv/3qerwAAAAAtNRQ6tBDD02XX355eSi10047pXPPPTcffe8f//hH+vjjj9Pw4cPTiBEj6nq8AAAAADQDbeflSosuumj66U9/Wum8X/3qV+moo45Kn332WVpkkUVmOSofAAAAAMxXKFWTOApf796963KVAAAAADRD8xVKPf/88+mGG25I//vf//JUvvvvvz+f/95776Unn3wybbbZZmnBBResq7ECAAAA0NJDqWOPPTadf/75qaysLP9ecbpenDds2LC8/Mgjj6ybkQIAAADQshudjxo1Kp133nlp2223TS+99FI6/vjjKy1fYokl0pprrpnuuOOOuhonAAAAAC29Uuriiy9OAwcOzEfaa9u2bWrfvv0sl1l++eXLp/MBAAAAwHxXSr322mtp8803z4FUTaLh+cSJE+dl9QAAAAA0c/MUSkUYNWPGjNleZsKECalLly7zOi4AAAAAmrF5CqUGDx6cHnjggTRz5sxql5eOxLfaaqvN7/gAAAAAaIbmKZQ64IAD0htvvJEOPfTQNH369ErLpkyZkvbbb7/08ccfp5/97Gd1NU4AAAAAWmKj8w8//DAttthi5aFUVEJdeeWV6aabbko9evTI58cR915//fX0zTff5GBql112qb+RAwAAAND8K6Viyt7f/va38t+vv/76dNlll6UBAwak8ePHp7KysvTMM8+kxRdfPF1yySXpr3/9a32NGQAAAICWEkq1b9++vPrps88+y+fF9LwXX3wxff3117mSKqbuvfrqq+mQQw6pzzEDAAAA0FJCqQibdtxxx3Trrbfmqqk777yzfFmnTp1S3759HW0PAAAAgLoNpRZaaKH097//PV133XVpxowZaYcddsi9pb766qvargIAAAAA5q7Reckee+yRNt1003TQQQelq666Kj3wwAPp+OOPz9VS1dlnn33m9iYAAAAAaObmOpQKvXv3ztP3olIqgqlf/OIXs1wmGp+3atVKKAUAAABA3YRSU6dOTb/61a/S1Vdfnbp27Zp+/vOf11gpBQAAAADzHUo98sgjaf/990/jxo1LG220Ua6U6t+//9yuBgAAAIAWrNaNzqO5+YgRI9Imm2ySxo8fny644IL04IMPCqQAAAAAqL9KqVVXXTW99tprabXVVkt/+9vf0vLLLz/3twYAAAAAc1Mp9cYbb6STTz45PfHEEwIpAAAAAIqplHr88cdzlRQAAAAAFFYpJZACAAAAoNBQasstt0xPP/30PN3AN998k84+++z05z//eZ6uDwAAAEALDaU+/fTTtPbaa+cj740aNSpNnjx5jteJ3lO//OUv89H5TjvttNS7d++6GC8AAAAALaWn1LPPPpuuvvrqNHLkyHTggQemn/3sZ2m55ZbLU/oibOrRo0eaNm1a+uKLL9LYsWPTM888k7766qvUpk2btPvuu6fTTz89Lb744vV/bwAAAABoXo3O991337TPPvukf//737laasyYMenaa6+d5XKtW7dOK620Utpxxx3TQQcdlBZddNG6HjMAAAAALSWUCq1atUrbbLNNPoXXX389ffjhh+nzzz9PnTp1SgsvvHAaNGhQ6t69e32NFwAAAICWFkpVNXDgwHwCAAAAgDpvdA4AAAAAdUkoBQAAAEDhhFIAAAAAFE4oBQAAAEDhhFIAAAAAFE4oBQAAAEDh2hZ/kxSlzddtGnoI0KJ4zQHMH++jUCyvOaBJh1LPP/98uuGGG9L//ve/NHXq1HT//ffn899777305JNPps022ywtuOCCdTVWaqlnz56pfYf2qfuL3Rt6KNDixGsvXoMA1J59F2g49l2AJhlKHXvssen8889PZWVl+fdWrVqVL4vzhg0blpcfeeSRdTNSaq1v377p3nvuTZMmTWrooTAPxo0bl0aMGJHOPffctNRSSzX0cJhLsVMXr0EAas++S9Nm36Vps+8CNLlQatSoUem8885L2223XTrjjDNytdTZZ59dvnyJJZZIa665ZrrjjjuEUg0k/rD449K0xU7doEGDGnoYAFAI+y5Nn30XAAoJpS6++OI0cODA9I9//CO1bds2tW/ffpbLLL/88uXT+QAAAABgvo++99prr6XNN988B1I16d27d5o4ceK8rB4AAACAZm6eQqkIo2bMmDHby0yYMCF16dJlXscFAAAAQDM2T6HU4MGD0wMPPJBmzpxZ7fLSkfhWW221+R0fAAAAAM3QPIVSBxxwQHrjjTfSoYcemqZPn15p2ZQpU9J+++2XPv744/Szn/2srsYJAAAAQEtvdB6hVFRCXXnllemmm25KPXr0yOfHEfdef/319M033+Rgapdddqnr8QIAAADQUiulwvXXX58uu+yyNGDAgDR+/PhUVlaWnnnmmbT44ounSy65JP31r3+d78GdffbZqVWrVumoo44qP2/jjTfO51U8RcUWAAAAAM28UqokpufF6dtvv02TJk1K3bp1q7Pm5k8//XQOvVZaaaVqb/fUU08t/71z5851cpsAAAAANPJKqYo6deqU+vbtW2eB1Ndff5323HPPdPnll6eePXvOsjxCqD59+pSfIgwDAAAAoIWFUnXtsMMOS9tss03abLPNql1+3XXXpYUWWiituOKK6fjjj89H+5udaMYeDdgrngAAAABoYtP3WrdunXs5zU4sjwqm5ZZbLu24447p8MMPzxVVc3LjjTem5557Lk/fq86wYcNS//79c2XWSy+9lI477rg0duzYdOutt9a4zrPOOiuNHDmyFvcMAAAAgEYbSm244YZp8uTJ6cUXX0xt2rTJzc179+6dPvnkk/T++++nmTNn5l5Q8TOCo6eeeipXNz388MOznWr3wQcfpCOPPDLdd999qWPHjtVe5uCDDy7//+DBg9Oiiy6ahgwZksaNG5eWWmqpaq8T1VTDhw8v/z0qpfr16zcvdx0AAACAhpq+d+211+bG5vvss0965513ciD02GOP5Z/vvvtu2nfffdOXX36Z7r777hxURWPyl19+OZ155pmzXe+zzz6bJk6cmFZdddXUtm3bfHrooYfSH/7wh/z/CLmqWmuttfLPt956q8b1dujQIYdhFU8AAAAANLFQ6phjjsnT56666qq02GKLVVr2ox/9KI0aNSovj8tF8/OLL744rbDCCum2226b7Xqj4inCqxdeeKH8tPrqq+em5/H/qMqqKs4PUTEFAAAAQDOevnf//fenQw45ZLaX2WijjfLR80o9qDbYYIMcYs1O165dc/PyihZYYIHUq1evfH5UYl1//fVp6623zufF1MCjjz46TyeM6YIAAAAANONQatq0aemjjz6a7WVi+bffflspcIopePOjffv2ORC76KKL0jfffJP7Qu28887phBNOmK/1AgAAAFCseUqJoudTHCUvekWts846syx/8skn00033ZTWWGON8vPefvvt3Ax9bo0ZM6b8/xFCRY8pAAAAAFpgKHXaaaelzTffPE/J+8lPfpLWW2+9tMgii+Qm5Y8++mi6884785S9U089NV/+66+/Tvfee2/abbfd6nr8AAAAALSUUCr6Rd11113p4IMPTv/85z/zqVWrVqmsrCwvX3zxxdOll16aLxcioHrkkUdyE3QAAAAAmOcmT1tssUWekhdh04svvpimTJmSunXrllZeeeW0/vrr5yCqpHPnzvl8AAAAAAjz1Xk8gqc48l2cqjN9+vTUoUMHjzQAAAAAlfz/5Ux16LnnnkuHHXZY6tu3b32sHgAAAICWXClV0ZdffpmuvfbadOWVV6aXXnop95fq1KlTXa0eAAAAgGZkvkOp+++/PwdRt99+e56uF2HUOuusk/bff//005/+tG5GCQAAAECzMk+h1AcffJBGjRqVT++//34OouLIeuPHj0/77bdf+utf/1r3IwUAAACg5YVS3333XfrnP/+Zq6JGjx6dZs6cmRZYYIG05557pn322SdtuummqW3btvkEAAAAALNT6wQpmpZ/8cUXqVWrVmmTTTbJQdROO+2UgykAAAAAqJdQ6vPPP0+tW7dORx99dDr22GPTwgsvPFc3BAAAAAAlrVMtRa+oOJreBRdckBZbbLH0k5/8JN1yyy1pxowZtV0FAAAAAMxdKBXNyz/66KN02WWXpVVXXTXdddddaffdd0+9e/dOhxxySHrkkUdquyoAAAAAWrhah1KhS5cu6aCDDkqPP/54evXVV9NRRx2V2rdvny6//PK00UYb5X5TY8eOTe+99179jRgAAACAlhVKVTRw4MB0/vnnp/Hjx6ebb745bbHFFjmUevjhh9NSSy2VhgwZkv72t7/V7WgBAAAAaNmhVEnbtm3TLrvsku6+++707rvvppEjR6b+/funBx98MPehAgAAAIA6D6UqigboJ554Yho3bly67777cs8pAAAAAKiqbaonMX0vTgAAAABQr5VSAAAAAFAbQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACieUAgAAAKBwjTqUOvvss1OrVq3SUUcdVX7etGnT0mGHHZZ69eqVunTpknbeeef0ySefNOg4AQAAAGgmodTTTz+dLrvssrTSSitVOv/oo49Od955Z7rlllvSQw89lCZMmJB22mmnBhsnAAAAAM0klPr666/TnnvumS6//PLUs2fP8vMnT56crrzyynTBBRekTTfdNK222mpp1KhR6bHHHktPPPFEg44ZAAAAgCYeSsX0vG222SZtttlmlc5/9tln03fffVfp/OWXXz4tvvji6fHHH2+AkQIAAAAwL9qmRubGG29Mzz33XJ6+V9XHH3+c2rdvn3r06FHp/N69e+dlNZk+fXo+lUyZMqWORw0AAABAk62U+uCDD9KRRx6ZrrvuutSxY8c6W+9ZZ52VunfvXn7q169fna0bAAAAgCYeSsX0vIkTJ6ZVV101tW3bNp+imfkf/vCH/P+oiJoxY0b68ssvK10vjr7Xp0+fGtd7/PHH535UpVOEXwAAAAA0nEY1fW/IkCHp5ZdfrnTe/vvvn/tGHXfccbnCqV27dmn06NFp5513zsvHjh2b3n///bTOOuvUuN4OHTrkEwAAAACNQ6MKpbp27ZpWXHHFSuctsMACqVevXuXnH3jggWn48OFpwQUXTN26dUuHH354DqTWXnvtBho1AAAAAE06lKqNCy+8MLVu3TpXSkXz8qFDh6aLL764oYcFAAAAQHMKpcaMGVPp92iA/uc//zmfAAAAAGiaGlWjcwAAAABaBqEUAAAAAIUTSgEAAABQOKEUAAAAAIUTSgEAAABQOKEUAAAAAIVrW/xNAtAUffvtt+ntt99OzdW4ceMq/WyullxyydSpU6eGHgYA1Dv7Ls2DfZfmTSgFQK3ETt1OO+2UmrsRI0ak5uzWW29NgwYNauhhAEC9s+/SPNh3ad6EUgDU+luq2Cmg6T+PANAS2HdpHuy7NG9CKQBqJcqmfUsFADQV9l2g8dPoHAAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKJxQCgAAAIDCCaUAAAAAKFyjC6UuueSStNJKK6Vu3brl0zrrrJPuvvvu8uUbb7xxatWqVaXToYce2qBjBgAAAGDutE2NzGKLLZbOPvvstMwyy6SysrJ09dVXp+233z49//zzadCgQfkyP/vZz9Kpp55afp3OnTs34IgBAAAAaPKh1HbbbVfp9zPOOCNXTz3xxBPloVSEUH369GmgEQIAAADQ7KbvVTRz5sx04403pm+++SZP4yu57rrr0kILLZRWXHHFdPzxx6epU6c26DgBAAAAaOKVUuHll1/OIdS0adNSly5d0m233ZZWWGGFvGzYsGGpf//+qW/fvumll15Kxx13XBo7dmy69dZba1zf9OnT86lkypQphdwPAAAAAJpQKLXccsulF154IU2ePDn9/e9/T/vuu2966KGHcjB18MEHl19u8ODBadFFF01DhgxJ48aNS0sttVS16zvrrLPSyJEjC7wHAAAAADS56Xvt27dPSy+9dFpttdVyoLTyyiun3//+99Vedq211so/33rrrRrXF1P8IuAqnT744IN6GzsAAAAATbRSqqoffvih0vS7iqKiKkTFVE06dOiQTwAAAAA0Do0ulIqqpq222iotvvji6auvvkrXX399GjNmTLr33nvzFL34feutt069evXKPaWOPvrotOGGG6aVVlqpoYcOAAAAjeKgYd99911DD4Nmql27dqlNmzbNM5SaOHFi2meffdJHH32UunfvnsOmCKQ233zzPO3u/vvvTxdddFE+Il+/fv3SzjvvnE444YSGHjYAAAA0qLKysvTxxx+nL7/8sqGHQjPXo0eP1KdPn9SqVavmFUpdeeWVNS6LECoangMAAACVlQKpRRZZJHXu3Hm+AwOoLvicOnVqLiiaUyulJhlKAQAAAHM/Za8USEW7G6gvnTp1yj8jmIrtbX6m8jXKo+8BAAAAtVfqIRUVUlDfStvZ/PYuE0oBAABAM2HKHk1pOxNKAQAAAFA4oRQAAABAPdlvv/1Sly5dCrmtJZZYIt9eYx1fVUIpAAAAaOauuuqqPOXqmWeeqXb5xhtvnFZcccXUUK6//vp00UUXzVOD9759++b7dvfdd1d7mYsvvjjf/6pee+21dMopp6R33303NVannHJKvm+lU7t27XLwdMQRR+TG9k2do+8BAAAADSpCqVdeeSUdddRRc3W9Bx54IH300Uc5qLnuuuvSVlttVW0otdBCC81SQRSh1MiRI3MgF9dvzC655JJczfTNN9+k0aNHpz/+8Y/pueeeS4888kily40dOza1bt106o+EUgAAAECDiJBlgQUWmOfrX3vttWnVVVdN++67b/rNb34z3+trrHbZZZccrIVDDjkk7b777ummm25KTz31VFpzzTXLL9ehQ4fUlDSd+AwAAAAoVIQ+q622WurUqVNacMEFcxjywQcfVLrMww8/nHbddde0+OKL51CkX79+6eijj07ffvtttb2Lxo0bl7beeuvUtWvXtOeee+ZKpX/961/pvffeK5+mVpvKpVj/bbfdlse022675d9vv/32SpeJ9bz66qvpoYceKl933F5M54sxh0022aR82ZgxY/J5sZ5tttkmTw2M+7TUUkul0047LU8XrOrJJ5/M96dnz545EFtppZXS73//+9mO/YUXXkgLL7xwHsvXX3+d5tYGG2yQf8ZjWfX+VqwI++6773I12DLLLJM6duyYevXqldZff/1033331ev4akulFAAAALQQkydPTp999tks50d4UdUZZ5yRTjzxxBz4HHTQQenTTz/N08Y23HDD9Pzzz6cePXrky91yyy1p6tSp6ec//3kOPaJ6Jy734Ycf5mUVff/992no0KE5GDnvvPNS586dU58+ffK44vIXXnhhvlxtGm/fcccdOTCJUCrWEQFKTOEbNmxY+WWiT9Xhhx+e1/fb3/42n9e7d+8cMkVfpj/84Q+5wmrgwIF5WelnhFZxneHDh+efMU3wpJNOSlOmTEnnnntu+foj3Nl2223Toosumo488sg8jtdffz3ddddd+ffqPP300/kxWH311XP4FYHf3Cr1wYogbE49qc4666z8/EVFVYw/+orF1L/NN9+83sZXW0IpAAAAaCE222yzGpcNGjSo/P9RtXTyySen008/PYc2JTvttFNaZZVVcp+m0vnnnHNOpeDi4IMPTksvvXRe/v777+cKqpLp06fnCqUISir60Y9+lCZNmpT22muvuariWnfddXNlVohw6he/+EUOz6LKJ+ywww7phBNOyFPfqq47qo0ilIpwJgKtqj2uKt6nQw89NJ/ifsdjEtVTUTUVU+kikIrKolJIF8rKyqod86OPPpqrquK2//GPf9R6ut0XX3yRf8b0xAjI/vznP+f7GAHh7EQFWtzeX/7yl1rdzryOb16ZvgcAAAAtRIQZUd1T9RRTziq69dZb0w8//JCrpKKyqnSKSqCYCvbggw+WX7ZieBOhSVwuwqIIZqKiqqqoqJpfn3/+ebr33nvTHnvsUX7ezjvvnKfg3XzzzfO9/or36auvvsr3KYKaqAj73//+l8+P+/bOO+/k5uwVA6kQ46gqHrOoQBoyZEh+fDvMReCz3HLL5RAqpucdcMABOfSLow1GpdnsxLhi+uKbb745x9uYn/HNK5VSAAAA0ELEFK6YllVVTAOrOK0vQowIlSKAqk67du3K/x/VUDG1LabTRbVTRTEtr6K2bdumxRZbbL7vRzT5jimHUbX11ltvlZ+/1lpr5Sl8hx122HytP4KcqLCKqqSY8lbdfSr1c1pxxRXnuL5p06blHlXRnytCs3gc5kZULXXr1i1XgUV1V4RhtZlWd+qpp6btt98+LbvssnmcW265Zdp7771nCSHnd3zzSigFAAAAVBJVUlHtE9U4bdq0mWV5qedTTGGL6W8xvey4445Lyy+/fG72PX78+NxwO9ZTUVTftG49/5O2IngK6623XrXL33777bTkkkvO07q//PLLtNFGG+UQKEKd6D8VTcKjD1Pcx6r3qTbifse0uOjRdM899+Q+VHMjpumVjr633XbbpcGDB+cm8c8+++xsH8+4XoRncbv/+c9/0hVXXJH7dl166aW5z1RdjW9eCaUAAACASiKIiUqpAQMG5Cqbmrz88svpjTfeSFdffXXaZ599ys+f09HdqqpuultNokroscceS7/85S9zeFRRBEZRCRQ9oaLSaXbrrun8OAJfTA+MKWwVezbF7VZ9jMIrr7wy215dpduKIC2qlqKnVoR9G1fpY1VbEQhGv6/9998/VzVFL63ZiaMmxmXjFI3h4z5FA/SKoVRdjm9u6CkFAAAAVBINzaNCauTIkbM07Y7fI7QJpSqqipeJ///+97+fq9uL6qqqU/3mVCV17LHHpl122aXSKXpgRVBVukxp3VH9VN1thqrLqrtPM2bMyE3OK1p11VVzaBdH+Ku6juoanbdv3z4HXWussUaudnrqqafSvIoqqZgGGU3mZ6f0PFUMtKIfVTScr8/x1ZZKKQAAAGCWKqA4ytzxxx+f3n333XwUu65du+Zqodtuuy0fYe+YY47J0/XisvH/mLIXU96i/1HV3lJzEr2Mok/U8OHDcygS4UkEI9WJwOnHP/5x+VH3qvrJT36SDj/88DzdLoKjWPcll1yS708EMossskjadNNN8zoigIpgJwKxmMIW50eT9uixte+++6YjjjgiVxH97W9/myVoimlzsd4YZ6wrKpHiSHzRCD16UkUj9qqiD9Rdd92Vb2errbZKDz30UK16UlXX0+vII49MI0aMyNPtoldUdVZYYYVc8RSPQVRMPfPMM+nvf/97rjKrTl2Nr7ZUSgEAAACz+PWvf50DpghfomIqgqdoZr7FFlvk4KcUjtx55505lDnrrLPy5aI5+jXXXDNXt/WLX/wiDRs2LI0aNSr/jFCpOhE0RehTU2AVSsuuvfba/DOasEe/pN/97nf5aH3RJyrEkQSjt9LEiRPTgQcemJe99tprqVevXjmYiYAppgCed955uW9WXL+qOFpdHLUupjief/75OVQbPXr0bMcXwV0EVn369MnrrdiofW5EMNi9e/d09tln13iZCNUiVIznJv4fIVOEczHW+h5fbbQqq66mrJmLzvnxxEUSGg82NCaRqEepbJRNDho0qKGHAwAwW/ZdoHGIo6dFFVNMJ4um3NCQ21ttcxeVUgAAAAAUTigFAAAAQOGEUgAAAAAUTigFAAAAQOGEUgAAAAAUTigFAAAAQOGEUgAAAAAUTigFAAAAQOGEUgAAAAAUTigFAAAAQOGEUgAAAECzd8opp6RWrVqlDTfccJZlRx11VFpiiSXq5HZiPXE7cWrbtm3+fd99900ffPBBpctdddVV+TKfffZZrdb77rvv5sv//e9/T81F24YeAAAAAND0TJgwIU2aNKnw2+3Zs2fq27fvPF//4YcfTmPGjEkbb7xxqi+77LJL+tWvfpW+++679PTTT6eTTz45Pf/88+nZZ59N7dq1y5fZZptt0uOPP5569OiRWiqhFAAAADDXgdTQLYemGdNnFH7b7Tu0T/fec+88BVMLLLBAGjRoUDrttNPqNZTq3bt3WnvttfP/N9hggzRt2rT029/+Nj3zzDNpnXXWyecvvPDC+dSSCaUAAACAuRIVUhFITV55cprZZWZht9vm6zap+4vd8+3Pa7XUiSeemLbbbrv02GOPpXXXXbfGy7333nu52um+++5L33//fVp//fXTeeedlwYPHjzXt7nKKqvkn++//355KHXVVVel/fffP3366adpoYUWyuedffbZ6Yorrkgffvhh6tq1a1p55ZXT5ZdfngYMGFDtep977rk0dOjQfH/ieq1bN60uTUIpAAAAYJ5EIPV99+9TU7LtttvmkGjkyJHp3nvvrfYyX331Va6kipDn0ksvTR07dkxnnHFG7kf10ksvpX79+s3VbUbAFWoKl8I111yTA7NTTz01B1eTJ0/OUw2nTJmSqvPoo4/mKYD77LNP+v3vf5/7TTU1QikAAACgRTnhhBPSzjvvnJ566qm05pprzrJ81KhROUh69dVX08CBA/N5G220UVp88cXTRRddlM4///zZrr+srCxXV0VPqZiyd+aZZ6att9662tsqibGstNJK6fjjjy8/b/vtt0/Vuf/++9MOO+yQjjjiiLzupqpp1XUBAAAAzKcdd9wxrbjiirkqqTpRoRTLS4FUWHDBBdPmm2+eHnnkkTmu/+KLL84NzTt37pyrqzp16pRuuOGG2V5n1VVXzc3Qhw8fnm8jAq3q3HXXXbnaK3pUNeVAKgilAAAAgBYlprpFqPOvf/0r92WqKnpWRbPyquK8L774Yo7r32233fJR9yLcisqnN954Ix1yyCGzvc5+++2XLrzwwjylMJqjRxP0I488Mn377beVLnfnnXfmsGv33XdPTZ1QCgAAAGhxIjhabrnl8pH4qoqqqIkTJ85y/ieffJKXzUkESquvvnpujh7VTIcffni68cYb05NPPlnjdVq3bp1DqJgyGI3Oo79UVFxFc/WKLrjggrTCCiukIUOG5Ms1ZUIpAAAAoMWJECiqpW6//fbcvLyiCJNefvnlNHbs2ErVU9HLKZbNrVNOOSV169at1tPtfvSjH+Uj/0WPqddff73SsgUWWCD9+9//Tr169crBVARlTZVQCgAAAGiRhg0blpZccsn04IMPVjp///33T/37989Ht4sKp3/+859piy22SG3btk1HHXXUXN9OVFdFtVRMvasaMpXE9L5f//rX+bYeeuihHGC9+OKLOXiqKgKu//znP7lX1WabbZY+//zz1BQJpQAAAIB50ubrNqnt5LaFneL26nT8bdpUOtpdSdeuXdOYMWPSyiuvnA4++OC05557pp49e6b//ve/qV+/fvN0W9HAPNZ7zjnnVLt83XXXzQ3ODzzwwLTlllum6667LveYit+rE+O577770syZM3NgNnny5NTUtCqL4xS2MFOmTEndu3fPT1iki9CYxPzhnXbaKd16661p0KBBDT0cAIDZsu8CjcO0adPSO++8kwYMGJA6duxY77c3YcKENHTLoWnG9BmpaO07tE/33nNv6tu3b+G3Te22t9rmLm1rXAIAAABQjQiEIhiKPktFiwohgVTzIJQCAAAA5loEQ8Ih5oeeUgAAAAAUTigFAAAAQOGEUgAAAAAUTigFAAAAQOGEUgAAAAAUTigFAAAAQOGEUgAAAAAUTigFAAAAQOHaFn+TAAAAQFM3YcKENGnSpMJvt2fPnqlv377ztY6VV145vfTSS+m///1v2mCDDSotGzNmTHrsscfSb37zmzmu55RTTkkjR44s/33BBRdMAwcOzNfdeuutK122VatW6dxzz03HHHNMrca48cYbpy5duqS77rorNVdCKQAAAGCuA6mhWw5NM6bPKPy223don+695955DqZeffXVHEiF66+/vtpQ6rzzzqtVKBU6deqUHnjggfLH5cwzz0zbbbddevjhh9O6665bfrnHH3889e/ff57G3Fw1ulDqkksuyad33303/z5o0KB00kknpa222ir/Pm3atPSrX/0q3XjjjWn69Olp6NCh6eKLL069e/du4JEDAABAyxAVUhFITV55cprZZWZht9vm6zap+4vd8+3Payh13XXXpdatW6eNNtoo3XLLLekPf/hDateu3TyPKda19tprl/++1lprpX79+qWrr766UihV8TI00p5Siy22WDr77LPTs88+m5555pm06aabpu233z4nmeHoo49Od955Z95wHnrooZxC7rTTTg09bAAAAGhxIpD6vvv3hZ3mNwArKytLN9xwQ84ahg8fnj7//PN0zz33zDId75tvvsnT7eIU0+jmxo9+9KO08MILp/fff7/S+bGuqMAqefTRR9OGG26Yunfvnrp27ZoGDx6cg6yafPvtt2mbbbZJSy65ZHr77bdTc9DoKqWixK2iM844I1dOPfHEEzmwuvLKK3N5XWxAYdSoUXm+ZiyXOgIAAAA1iV5RMTMrZmTFzKtevXrljKGURRx00EHpww8/zOeVpuR169Ztrm7j66+/Tl988UUaMGBAjZeZMmVKDpjWX3/9HJJ16NAhvfbaa+nLL7+scZ0xxo8++ihPC4zgqzlodKFURTNnzswVUZFQrrPOOrl66rvvvkubbbZZ+WWWX375tPjii+e5mTWFUjHNL04Vn3yarkiHm0sqXJ1x48ZV+tlcRbofc68BoLmz79I82HeB5iHCpo4dO+YZVzFlb5dddkl/+9vfcugTTcWjGCZOVafkzcn333+ff8ZsrmOPPTZXPh155JE1Xv6NN95IkydPTmeddVaukApDhgyp9rIxVTFaGkU7o2jMvsgii6TmolGGUi+//HIOoeIBj43itttuSyussEJ64YUXUvv27VOPHj0qXT76SX388cc1ri+e5Ird8GnaYqeuJUzZHDFiRGrObr311twzDgCaO/suzYN9F2j6IjiKwpc4Kl5MmQvDhg1Ll112Wc4d9t5773labxTSVOxJ1aZNm3T77ben5ZZbrsbrLLXUUrkC6+c//3k64ogj0iabbJKn/FX12Wef5WURpD344IP5yIPNSaMMpeKJiwAqUsO///3vad999839o+bV8ccfn+eKVqyUiqZjNN1vqWKngKb/PAJAS2DfpXmw7wJN33/+85/06aef5mlwpWlyUaW06KKL5gqqeQ2loooyKph++OGH9Oabb6Zf//rXaZ999kmvvPJKXnd1Ily677770sknn5xvNwKzOArgH//4x/LKqVJFVVRKXXTRRc0ukGq0oVRUQy299NL5/6uttlp6+umn0+9///v005/+NM2YMSNvPBWrpT755JPUp0+fGtcXczPjRPMQL3jfUgEATYV9F4DGIYKnsP/+++dTRRFWTZw4cZ6mxsVUv9VXXz3/f80118yFNnEEvlNPPTX3yK7Jmmuume6+++48zTuqoI455pi0ww47VJoOHUfvixZGUWgT/a/22muv1Jw0uqPvVSfSxugJFQFVlMSNHj26fNnYsWNzR/uY7gcAAABQ1dSpU/OUugh9IgCqeIpG41GpdNNNN5UXylTsSz23IqDaY4898oHZZtdqqOKXFzGlMKbyvfPOO7mVUUVHHXVUOv3009N+++2XZ5M1J42uUiqm2kUDr2he/tVXX+Ukc8yYMenee+/Ncz4PPPDAnBAuuOCCef7l4YcfngMpR94DAAAAqhOBVDQzj/5NG2+88SzLf/e73+X8ITKGgQMH5pAqZmxFpVJkD7PrD1WdE088Md1444152t3ZZ589y/J//etf6corr0w77rhjzj8ivIqpe+utt17uH1VdVhIVVdEDK5Zvu+22qTlodKFUlMvF3Ms4zGGEUCuttFIOpDbffPO8/MILL8ylcTvvvHNOLuMQjhdffHFDDxsAAABanDZft2kStxeBU4Q/1QVSIXpZR0VSTJ2LnlO/+MUv8kHTIqPYcMMNc7HM3IgQa/fdd8/T9yJQKjVWL4mWRa1bt06//e1v823E1Lwtttgi32ZNYjpgBFNxxMC77rorT+tr6lqVlZWVpRYmGp3HBhGN1CPxBAAAgKYspnzF1K8BAwZUW2lT1yZMmJCGbjk0zZg+IxWtfYf26d577k19+/Yt/Lap3fZW29yl0VVKAQAAAI1bBEIRDMWR4YoWR6ETSDUPQikAAABgrkUwJByi2R99DwAAAIDmRSgFAAAAQOGEUgAAAAAUTigFAAAAzURZWVlDD4EWoKyOtjOhFAAAADRx7dq1yz+nTp3a0EOhBZj6f9tZabubV46+BwAAAE1cmzZtUo8ePdLEiRPz7507d06tWrVq6GHRDCukpk6dmrez2N5iu5sfQikAAABoBvr06ZN/loIpqC8RSJW2t/khlAIAAIBmICqjFl100bTIIouk7777rqGHQzPVrl27+a6QKhFKAQAAQDMSgUFdhQZQnzQ6BwAAAKBwQikAAAAACieUAgAAAKBwQikAAAAACtciG52XlZXln1OmTGnooQAAAAA0K6W8pZS/1KRFhlJfffVV/tmvX7+GHgoAAABAs81funfvXuPyVmVziq2aoR9++CFNmDAhde3aNbVq1aqhhwM0o28DIuz+4IMPUrdu3Rp6OAAAs2XfBagvETVFINW3b9/UunXNnaNaZKVUPCCLLbZYQw8DaKZip86OHQDQVNh3AerD7CqkSjQ6BwAAAKBwQikAAAAACieUAqgjHTp0SCeffHL+CQDQ2Nl3ARpai2x0DgAAAEDDUikFAAAAQOGEUgAAAAAUTigF0AgsscQS6aKLLmroYQAALdy7776bWrVqlV544YWGHgrQAgilgBZnv/32yztbVU9vvfVWQw8NAGCe920OPfTQWZYddthheVlcBqCxEUoBLdKWW26ZPvroo0qnAQMGNPSwAADmSb9+/dKNN96Yvv322/Lzpk2blq6//vq0+OKLN+jYAGoilAJapDj0cZ8+fSqd2rRpk26//fa06qqrpo4dO6Yll1wyjRw5Mn3//ffl14tvGi+77LK07bbbps6dO6eBAwemxx9/PFdZbbzxxmmBBRZI6667bho3blz5deL/22+/ferdu3fq0qVLWmONNdL9998/2/F9+eWX6aCDDkoLL7xw6tatW9p0003Tiy++WK+PCQDQdMX+SwRTt956a/l58f8IpFZZZZXy8+655560/vrrpx49eqRevXrlfZqK+y3VeeWVV9JWW22V92Nif2bvvfdOn332Wb3eH6BlEEoB/J+HH3447bPPPunII49Mr732Wg6frrrqqnTGGWdUutxpp52WLxe9FpZffvk0bNiwdMghh6Tjjz8+PfPMM6msrCz98pe/LL/8119/nbbeeus0evTo9Pzzz+cqre222y69//77NY5l1113TRMnTkx33313evbZZ/OO5pAhQ9IXX3xRr48BANB0HXDAAWnUqFHlv//1r39N+++/f6XLfPPNN2n48OF5nyX2TVq3bp123HHH9MMPP9T4RVl8ORbBVlwnQq1PPvkk7bbbbvV+f4Dmr1VZfHoCaEGip8K1116bq6FK4tu/SZMm5eAnwqWSuNyxxx6bJkyYUF4pdcIJJ+RgKjzxxBNpnXXWSVdeeWXeEQxROh87gBXL56taccUVc9+HUngVjc6POuqofHrkkUfSNttsk0OpqOgqWXrppfNYDj744Hp4VACAprxvE+HR5Zdfnqulxo4dm8+PL88++OCDXH0dlVHxZVtVUfEUldkvv/xy3j+JRufR0iC+SPvxj3+cTj/99PzF3b333lt+nQ8//LD8dpZddtlC7yvQvLRt6AEANIRNNtkkXXLJJeW/x7S7lVZaKT366KOVKqNmzpyZ+zFMnTo1T9cLcbmSKGEPgwcPrnReXGfKlCl56l1USp1yyinpX//6V+5dFdMBI7CqqVIqpunFdaKkvqK4zpzK6wGAlivCpfhiK8KnqD2I/y+00EKVLvPmm2+mk046KT355JM5kCpVSMV+SYRS1e2XPPjgg3nqXlWxXyKUAuaHUApokSKEisqjiiIIih5SO+200yyXr1hV1a5du/L/R+VUTeeVdvKOOeaYdN9996Xzzjsv32anTp3SLrvskmbMmFHt2GIciy66aBozZswsy+JbTgCAmkTldqkS+89//vMsy6OFQP/+/XNVVd++ffP+SoRRs9svieucc845syyL/RWA+SGUAvg/0bcpytCrhlXzK6qvoqw++jWUdu6iNH524/j4449T27Zt87Q+AIDait6VETDFl2RDhw6ttOzzzz/P+zoRSG2wwQb5vGgbMDuxX/KPf/wj75PEvglAXdLoHOD/RCn7Nddck6ulXn311fT666/n/lDRQ2p+LLPMMvnoN9EYPUrgozF6Tc1Ew2abbZb7VO2www7pP//5Tw6wHnvssfTb3/42NxgFAKhJHE049mHioC3x/4p69uyZ2wP85S9/yUcOfuCBB3LT89k57LDD8oFW9thjj/T000/nKXvRXyr6Z0abA4D5IZQC+D/xbeJdd92Vg6A11lgjrb322unCCy/MJe7z44ILLsg7geuuu24uf4/biW8daxLfbP773/9OG264Yd7hi14Nu+++e3rvvffKe1gBANQkelrGqao40l584RZH9o0pe0cffXQ699xzZ7uumOIXVd8RQG2xxRa5j2YcmCVaCsT6AOaHo+8BAAAAUDjRNgAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFAAAAACFE0oBAAAAUDihFABAM7PxxhunVq1aNfQwAABmSygFAFALL7zwQjr00EPTCiuskLp165bat2+f+vTpkzbffPN0/vnnp08//bShhwgA0KS0KisrK2voQQAANFY//PBDOvbYY3Pw1KZNm7ThhhumlVZaKS2wwAJp4sSJ6fHHH0+vvvpq/n3s2LHpRz/6UaOolHrooYeS3TwAoDFr29ADAABozH7729/mQGrVVVdNN910U1p66aVnucxzzz2XjjvuuPTtt982yBgBAJoi0/cAAGrwxhtvpHPPPTctvPDC6Z577qk2kAoRWN13331piSWWqHT+Sy+9lHbfffe06KKL5ul+/fv3T4cffnj6/PPPK13u3XffzT2g9ttvv/TWW2+lHXfcMfXs2TNXX2222WbpxRdfrPZ2H3nkkbTRRhvly/Xq1Sv99Kc/TR988EGN9ycqp/7617+m9dZbL09B7Ny5c1p99dXzeVWdcsopeUxjxoxJV111Vb6PcfmowgIAqAsqpQAAanD11VenmTNnpkMOOSQHU3PStu3/v2t1xx13pN122y21bt06bb/99qlfv37ptddeS3/605/Svffem5588skcPFUNp9Zee+00aNCgdMABB6Rx48al22+/PW2yySbp9ddfT7179y6/7OjRo9NWW22V1x9hVN++ffN5EThVXW8pkNpzzz3TDTfckJZZZpk0bNiwHJRFmHbggQfmsZ133nmzXC9CuQcffDDfhy222CJPYQQAqAtCKQCAGkS/qBCh0NyISqi99947LbTQQunRRx/NFVIlN954Y9pjjz3SSSedlP74xz9Wul70gTr77LPzVMCSE088MZ1++ulp1KhR6de//nV5n6uDDz44ff/99+m///1vWn/99cuDp7322itdf/31s4zpiiuuyIHU/vvvny677LLUrl27fP6MGTPSLrvskqcoxrhWW221WcYUAdrgwYPn6jEAAJgT0/cAAGrw8ccf559RhVRVTGuLKW4VT3FeuOaaa9KUKVPSWWedVSmQCjGdL6bCRThV1YABA9KIESMqnRdVTOHpp5+uNG3v7bffTttuu215IBViut2ZZ55ZbTVTVGjFNL8///nP5YFUiGqpM844I/8/QquqIvwSSAEA9UGlFADAPIgAauTIkbOcHz2Xnnjiifz/qDCKKXhVTZs2LX322Wf5FNVUJT/+8Y/zdLyKFltssfzzyy+/LD+v1GNqgw02mGXdEYLFVMGYClgyderU9PLLL+dw7ZxzzpnlOt99913++b///W+WZWuuuWaNjwEAwPwQSgEA1CB6OEUvpwkTJqTll1++0rJSdVTFKXklX3zxRf4ZVUmz880331QKpaL5eE19qqK3VcnkyZPzz0UWWaTGcVcMpSZNmpSn9o0fP77aIK3ieKpbFwBAfTB9DwCgBuuuu27+GY2+50YpXIrqpAiDajpVndpXW927d88/J06cWO3yTz75pNrxRL+o2Y2nuvsZUwIBAOqDUAoAoAb77rtvnk73l7/8JU+1q6211lqrUqP0urbyyivnnw8//PAsy9577730wQcfVDqva9euaeDAgbnqq+I0QACAhiSUAgCowbLLLpuOPfbYXJG01VZbpbfeeqvay1UNeuIIdxEE/fa3v02vvvrqLJePHk+lvlPzIpqbR1P0u+66Kzc9L4lqp9/85jeVpvqVHHHEEfl2f/azn1U7Te+dd96pNOUPAKC+6SkFADAbcWS6GTNmpAsuuCD3ldpwww1zpVLnzp1zWPXSSy+lp556KnXp0iU3Kg8LL7xwPpLdrrvumi+75ZZb5utOnz49Bz8PPfRQnhp4zz33zNOYStVbW2+9ddpss83ST3/609zE/IEHHkgfffRRWmmllfK4KjrkkENyEHb11VenRx99NF8vrhNT/aLBeTRlv/7669MSSyxRJ48bAMCcCKUAAOYQAJ1//vlpr732Spdeemn673//m55++ukcMC244IJp0KBB6dxzz0377LNPpcbj22yzTXr++efzsvvvvz/dd999aYEFFshH04tKqljf/IhQafTo0emEE05It9xyS+rUqVMaMmRI/n+MpbreUFdddVUOsi6//PJcZfX111/nMS+zzDLpvPPOy+sEAChKq7Ko8wYAAACAAukpBQAAAEDhhFIAAAAAFE4oBQAAAEDhhFIAAAAAFE4oBQAAAEDhhFIAAAAAFE4oBQAAAEDhhFIAAAAAFE4oBQAAAEDhhFIAAAAAFE4oBQAAAEDhhFIAAAAAFE4oBQAAAEAq2v8Hqyq3P/u7yv8AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1200x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# 1. Prepare the data\n",
    "hearGardaData['gender_label'] = hearGardaData['gender'].map({1: 'Male', 2: 'Female'})\n",
    "\n",
    "# 2. Create the plot\n",
    "plt.figure(figsize=(12, 6))\n",
    "sns.boxplot(\n",
    "    x='gender_label',\n",
    "    y='age',\n",
    "    hue='Heart Attack Risk',\n",
    "    data=hearGardaData,\n",
    "    palette={0: 'green', 1: 'red'},\n",
    "    hue_order=[0, 1]\n",
    ")\n",
    "\n",
    "# 3. Customize the plot\n",
    "plt.title('Age Distribution by Gender and Heart Attack Risk', fontsize=16)\n",
    "plt.xlabel('Gender', fontsize=14)\n",
    "plt.ylabel('Age (Years)', fontsize=14)\n",
    "plt.legend(\n",
    "    title='Heart Attack Risk',\n",
    "    labels=['No Risk', 'At Risk'],\n",
    "    title_fontsize=12,\n",
    "    fontsize=11\n",
    ")\n",
    "\n",
    "# 4. Show the plot\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "id": "3c4181d0-979d-4aa3-b6d7-e09e8bc98065",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['age', 'gender', 'height', 'weight', 'Systolic', 'Diastolic',\n",
       "       'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'BMI',\n",
       "       'diabetes_signal', 'Family_History', 'Heart Attack Risk',\n",
       "       'gender_label'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 269,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "id": "dccd62e2-2aa7-4f8f-8d97-28ba11d5bf05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAHHCAYAAACiOWx7AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAALoFJREFUeJzt3QucTeX+x/HfjDEzLplxHWQYpUIuk3HtdpLJ5HaOcKLEJCoOcvlHnEScSlGhDCqnqEMNlQrhaNyKqdFI4RilFIVBGJcYjP1//Z7/Wfu/98zgmTFjz+Xzfr3W2Xut9ey1nr3OC9+e2/ZzuVwuAQAAwEX5X/w0AAAAFKEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJAADAAqEJQIH34IMPSkREhK+rAaCYIzQBuGwzZswQPz8/adGiRa6vsXfvXnn66adl8+bNUpDCmn4vZytXrpw0btxYXnrpJUlPT/d19QBcYQFX+oYAip558+aZlqCkpCTZuXOn1KlTJ1ehafz48eY6kZGRXufeeOMNOX/+vPhCUFCQzJ4927w/evSofPDBB/L444/Lxo0b5b333vNJnQD4Bi1NAC7Lrl27ZMOGDfLyyy9L5cqVTYDKayVLljThxRcCAgLkgQceMNugQYMkISFBmjZtKvHx8SboXQ4NgqdPn86zugLIX4QmAJdFQ1L58uWlQ4cO0q1btwuGJm2lGTZsmGlJ0gBUo0YN6d27txw6dEjWrFkjzZo1M+X69Onj7g6bM2dOljFNZ8+elQoVKphymR07dkyCg4NNS5BDu9HGjRtnWr/0vuHh4TJy5Mhcd6/5+/vLHXfcYd7//PPPObqHficNXvqMbrzxRlN2+fLl5py2WkVFRclVV11lugEbNmwo06ZN8/r8Tz/9JH/961/N9y9durS0bNlSli5d6lVGn6XeZ8GCBfLss8+a56zPpE2bNqYVMLOvvvpK7r77bgkJCTHX/NOf/iTr16/P1bMBijq65wBcFg0AXbp0kcDAQLnvvvtk5syZpuvKCUHqxIkTctttt8n27dvloYcekiZNmpiw9Mknn8ivv/4q9erVkwkTJsjYsWPlkUceMWXVzTffnG2r0z333CMffvihvPbaa+a+jo8++sgElR49erhbcv785z/LF198Ya6r99myZYtMmTJFvv/+e1M+N3788UfzWrFixRzfY9WqVSbQaHiqVKmSCYMrV640z06DzQsvvGDK6bPS8DJkyBCzn5qaap7HH3/8IY899pi599y5c82933//ffNMPD3//PMm4GmATEtLk0mTJknPnj1NSPKsS7t27UxY09Cn5d966y2588475fPPP5fmzZvn6vkARZYLAHLp66+/dulfIytXrjT758+fd9WoUcM1ZMgQr3Jjx4415T788MMs19DPqI0bN5oyb731VpYysbGxrlq1arn3V6xYYcouXrzYq1z79u1d11xzjXv/nXfecfn7+7s+//xzr3KzZs0yn1+/fv1Fv5/et0yZMq6DBw+abefOna7nnnvO5efn52rUqFGO76H7Wnbbtm1eZfV5lStXznXu3LkL1mXo0KHm8573OX78uKt27dquiIgIV0ZGhjm2evVqU65evXqu9PR0d9lp06aZ41u2bHE/9+uuu84VExPj/v9A/fHHH+aad91110WfDVAc0T0H4LJamcLCwqR169ZmX7uFunfvbrqaMjIy3OV08LTOOsvcGuJ8Jqe0JURbaXRckePIkSOmxUbv71i4cKFp+albt65p2XI2/bxavXr1Je918uRJM1ZLN+1++/vf/y6tWrWSRYsW5eoe2v1Vv359r2OhoaHmPlr/C/n0009Ny8+tt97qPla2bFnTuqXdhP/5z3+8ymv3pWcrnNN6p118Smcp/vDDD3L//ffL77//7q631kNbvNatW+ezwfdAQUX3HIBc0VCk4UgDkw4Gd+iyAzolXwdMt23b1t2d1bVr1zwdnK3Xmz9/vumO07FB2l2n4508Q5OGAu3m0sCTnQMHDlzyXjoeaPHixea93qd27dpmnFBu76Gfz+xvf/ub6bLTrrKrr77aPLd7773XjDVy/PLLL9ku6aCBzTnfoEED9/GaNWt6ldNxZ064dOqtYmNjL/jdtVvP+RwAQhOAXNLxMPv27TPBKbup99oK5YSm/KDjlnRM07Jly6Rz584mdGhrj7ZoObSlRAdU68y+7OiA7UspUaKEREdHX/B8Tu9RqlSpLGWqVKliWn5WrFhhvo9uOrZIB8rruKXc0Hpn5/96Cf+v3mry5MlZlnjwbMkC8P8ITQByRUOR/mMfFxeX5Zy2+mj31axZs0xIuPbaa2Xr1q0XvV5Ou+luv/12qVatmumi0y4rDXFPPvmkVxm977fffmu6m3LTDWgjr+6hXWmdOnUymwYabX3SUPjUU0+ZbsFatWrJjh07snwuJSXFvOr5nNZb6Uy9i4VCAP+PMU0AcuzUqVMmGHXs2NEsM5B505lhx48fN7PjlHalabBwxgFl1/JRpkwZ99IENnSml95Lu87eeecdOXfunFfXnNIurt9++80sjpndd9DxO5crL+6hY4oyf7dGjRqZ986yBe3btzeLhyYmJrrL6bVff/11MwMv8zipS9EZcxqcXnzxRTO7MbODBw/m6HpAcUBLE4Ac0zCkoUinu2dH1w9yFrrUIDNixAgzLV7XGNIlB/Qf7MOHD5vraGuUdqnpP+A6IFr3da0iDVE6hie7MUAOvfarr75qpstrF5kzvsfRq1cv023Xv39/MyD7lltuMWOxtHVGj2t3mC5UeTny4h79+vUzz0MHj+t4KR2fpN9Lu82c7zRq1Ch59913zbgnXXJA12rSrjsdT6YD7TVo5YSW15XO9Xq6ZpQOHNfxVBoA9XtoC5QzlgvAf/l6+h6AwqdTp06u4OBg18mTJy9Y5sEHH3SVLFnSdejQIbP/+++/uwYNGuS6+uqrXYGBgWZpAp3S75xXH3/8sat+/fqugIAAr+UHMi854NCp8uHh4absM888k209zpw543rhhRdcN954oysoKMhVvnx5V1RUlGv8+PGutLQ0qyUHLsX2HlrPgQMHZvn8+++/72rbtq2rSpUq5tnUrFnT9eijj7r27dvnVe7HH390devWzRUaGmqef/PmzV1LlizxKuMsObBw4UKv47t27cp2SYdvvvnG1aVLF1fFihVN3fU533vvva6EhIRLfm+guPHT/3ECFAAAALLHmCYAAAALhCYAAAALhCYAAAALhCYAAAALhCYAAAALhCYAAAALLG6ZR/RnD/bu3WsW5cuvn2sAAAB5S1de0sV6q1evfslFYglNeUQDk82PfwIAgIJnz549ZkX+iyE05RFtYXIeuv78AAAAKPiOHTtmGj2cf8cvhtCUR5wuOQ1MhCYAAAoXm6E1DAQHAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwEGBTCACQ/6JGvO3rKgAFTvLk3lJQ0NIEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABggdAEAABQ0EPT008/LX5+fl5b3bp13edPnz4tAwcOlIoVK0rZsmWla9eukpqa6nWN3bt3S4cOHaR06dJSpUoVGTFihJw7d86rzJo1a6RJkyYSFBQkderUkTlz5mSpS1xcnEREREhwcLC0aNFCkpKS8vGbAwCAwsbnLU033nij7Nu3z7198cUX7nPDhg2TxYsXy8KFC2Xt2rWyd+9e6dKli/t8RkaGCUxnzpyRDRs2yNy5c00gGjt2rLvMrl27TJnWrVvL5s2bZejQodKvXz9ZsWKFu0x8fLwMHz5cxo0bJ5s2bZLGjRtLTEyMHDhw4Ao+CQAAUJD5uVwuly9bmj766CMTZjJLS0uTypUry/z586Vbt27mWEpKitSrV08SExOlZcuWsmzZMunYsaMJU2FhYabMrFmz5IknnpCDBw9KYGCgeb906VLZunWr+9o9evSQo0ePyvLly82+tiw1a9ZMpk+fbvbPnz8v4eHhMnjwYBk1apTVdzl27JiEhISYepcrVy5Png+A4iVqxNu+rgJQ4CRP7p2v18/Jv98+b2n64YcfpHr16nLNNddIz549TXebSk5OlrNnz0p0dLS7rHbd1axZ04Qmpa8NGzZ0ByalLUT6ALZt2+Yu43kNp4xzDW2l0nt5lvH39zf7TpnspKenm/t4bgAAoOjyaWjSFh7tTtMWn5kzZ5qutNtuu02OHz8u+/fvNy1FoaGhXp/RgKTnlL56BibnvHPuYmU05Jw6dUoOHTpkuvmyK+NcIzsTJ040ydTZtGUKAAAUXQG+vHm7du3c7xs1amRCVK1atWTBggVSqlQpKchGjx5txkE5NIQRnAAAKLp83j3nSVuVrr/+etm5c6dUrVrVdJ3p2CNPOntOzyl9zTybztm/VBntt9RgVqlSJSlRokS2ZZxrZEdn4uk1PDcAAFB0FajQdOLECfnxxx+lWrVqEhUVJSVLlpSEhAT3+R07dpgx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0W6zW265RRo0aGCO7d+/37QUhYaGepXVgKTnnDKegck575y7WBkNOqdOnZJDhw6Zbr7syjjXyG48liZTZ9NWKQAAUHQVmNCkY5u0++y9996TwmD06NGmZczZ9uzZ4+sqAQCAfBQgBcCgQYNkyZIlsm7dOqlRo4b7eNWqVU3XmY498mxt0tlzes4pk3mWmzO7zrNM5hl3uq99l6VKlZISJUqYLbsyzjUy01l4ugEAgOLBpy1NOgZdA9OiRYtk1apVUrt2ba/zUVFRUrJkSUlISHAf0yUJdImBVq1amX193bJli9csN52Jp4Gofv367jKe13DKONfQLkC9l2cZ7S7UfacMAAAo3gJ83SWnM+M+/vhjs1aTM35IxwhpC5C+9u3b1ywFoIPDNQjpbDYNMjpzTukSBRqOevXqJZMmTTLXGDNmjLm20xLUv39/Mytu5MiR8tBDD5mAtmDBAjOjzqH3iI2NlaZNm0rz5s1l6tSpZumDPn36+OjpAACAgsSnoWnmzJnm9Y477vA6/tZbb8mDDz5o3k+ZMsXMZNNFLXXGms56mzFjhrusdqtp196AAQNMmCpTpowJPxMmTHCX0RYsDUi65tO0adNMF+Ds2bPNtRzdu3c3SxTo+k4avCIjI81yBJkHhwMAgOKpQK3TVJixThOAy8U6TUBWrNMEAABQyBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALATYFELBETXibV9XAShwkif39nUVABQDtDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAABYIDQBAAAU9NC0bt066dSpk1SvXl38/Pzko48+8jrvcrlk7NixUq1aNSlVqpRER0fLDz/84FXm8OHD0rNnTylXrpyEhoZK3759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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='active', data=hearGardaData)\n",
    "plt.title('Active Persone')\n",
    "plt.xlabel('Active') \n",
    "plt.ylabel('Count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "id": "1145751f-42c0-449e-bb51-bea3366f9e95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABKUAAAPeCAYAAADd/6nHAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAWBVJREFUeJzt3Qm0lVXd+PENMoqCihMmKuWsKIkTZZZpYmqlYomakKKm4QSJihqo9WZpKpgDmW+ilam8pTlChmnmiJipqKSlaQ6AI0oCKue/fnv9z1n3wgUudN0XLp/PWue9nHOe85znDPRyv+69n1aVSqWSAAAAAKCg1iWfDAAAAACCKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAMuJs846K7Vq1arIc33hC1/Il6q77747P/f//d//FXn+b33rW2mjjTZKy7L33nsvHXnkkWndddfN781JJ520xPuIx8XnWjV27Nh82wsvvLDE+4rPa+utt04rour3M36uaH9XAWB5JkoBQDOoxofqpUOHDmm99dZLffv2TRdffHF69913m+R5XnnllfwL8mOPPZaWNcvysTXGD3/4w/w5HnvssemXv/xlOuyww1JLE6/xpptuau7DaLERrTEXAGjJ2jT3AQDAiuycc85JPXr0SB988EF67bXX8i+rMeLmwgsvTDfffHPaZpttatueeeaZ6bTTTlvi8HP22WfnUUe9evVq9OP+8Ic/pI/boo7t5z//eZo3b15alt11111p5513TiNHjmyyfUbY6t+/f2rfvn1aVqLUgQcemPbbb7+0LNt1113T+++/n9q1a5eWB1tssUUOmXUNHz48rbLKKumMM85otuMCgNJEKQBoRl/+8pfT9ttvX+8X04gd++67b/rqV7+ann766dSxY8d8X5s2bfLl4/Sf//wnrbzyys3+y33btm3Tsm769Olpyy23bNJ9rrTSSvnCkmndunUebbi8WGedddI3v/nNerf96Ec/SmuuueYCtwNAS2b6HgAsY774xS+m733ve+lf//pX+tWvfrXIdWruvPPOtMsuu6TVVlstj7LYbLPN0umnn57vi1FXO+ywQ/7z4YcfXpsOFFPO6q5BNHny5DzSJGJU9bHzrylV9dFHH+VtYh2lTp065XD20ksv1dsmRj7FmlDzq7vPxR1bQ2tKzZo1K333u99N3bt3zyOJ4rX+5Cc/SZVKpd52sZ/jjjsuTzuL1xfbbrXVVmn8+PGNjk2DBg3K4SBCx7bbbpuuvvrqBaZePf/88+m2226rHfui1oGaM2dOGjJkSFprrbXSqquumt+3f//73wts19CaUr///e/TPvvsk6d3xmv51Kc+lb7//e/nz6Ih8Xl+5jOfyTEzRuGNGTOmweOJEV4bb7xx3me8p6ecckq+ve77GO95vPbqa6z7ub788svpiCOOyO9T9T3+xS9+scBz/fSnP833xfdr9dVXzxH22muvTUviuuuuS717987vXefOnVPPnj3T6NGjF7um1KWXXpo++clP5vdixx13TPfee+9C10u74YYb0v/8z/+k9ddfP3/uu+++e3ruuefq7S8e//Wvfz1tsMEGtfctPtcYpdWU4jsd3/+vfe1rC9w3e/bs1KVLl/Ttb3+73vFff/31i/27GR566KG011575X3EZ/L5z38+3XffffW2ienDMWIzjiFe59prr52+9KUvpUcffbRJXycAGCkFAMugmMYVv2DGNLqjjjqqwW2mTJmSR1TFFL+YBhi/PMYv0dVfMGOKUNw+YsSIdPTRR6fPfe5z+fYIFlVvvPFGHq0VU8ZihEYEhkWJX9rjF+BTTz01x5tRo0alPfbYI68LVR3R1RiNObb5f0mPX7L/9Kc/5WAU0/0mTJiQhg0bluPIRRddVG/7v/zlL+l3v/td+s53vpNDRqzT1a9fv/Tiiy+mrl27LvS4Ii5EsIj3McJWRJ1x48blGPP222+nE088sTb1KmJEBIwIZSGC08LEgugRGA855JD8GmM0XISmxohQFcFx6NCh+Wc8Nt63mTNnpvPPP7/etm+99Vbae++90ze+8Y108MEH59ASa17FyLcISCGmRcZ7Ge9RvPfxep544on8Hv7973+vrSEVrzGOO2JObBciiIVp06blqYvVABiv/Y477sifTRxXddH3mIZ5wgkn5CmA8d5FUHn88cdzGIn3ojEivMZriUj04x//ON8WIwjjex77XJjLL788H1t8t+KzitAX0xAjjMXnNr8YqRQjrk4++eT0zjvvpPPOOy8deuih+Vir4rsQownjPY3v0cMPP5yjWwTGuK+pxPsafx/jGN588820xhpr1O675ZZb8ns8/4iqxvzdjO9O/H2PwBdRMl7vVVddlUN4BLf4rMMxxxyTT2oQ71+MBoz/nYjvS7zv2223XZO9TgCIf+QBAIVdddVVMbynMmnSpIVu06VLl8qnP/3p2vWRI0fmx1RddNFF+fqMGTMWuo/Yf2wTzze/z3/+8/m+MWPGNHhfXKr+9Kc/5W0/8YlPVGbOnFm7/YYbbsi3jx49unbbhhtuWBk4cOBi97moY4vHx36qbrrpprztD37wg3rbHXjggZVWrVpVnnvuudptsV27du3q3fa3v/0t3/7Tn/60siijRo3K2/3qV7+q3TZ37txKnz59Kqusskq91x7Ht88++1QW57HHHsv7/M53vlPv9kMOOSTfHp/r/N+L559/vnbbf/7znwX2+e1vf7uy8sorV2bPnr3A53nBBRfUbpszZ06lV69elbXXXju/jvDLX/6y0rp168q9995bb5/xPYjH33fffbXbOnXq1OBnOWjQoEq3bt0qr7/+er3b+/fvn7+31WP+2te+Vtlqq60q/40TTzyx0rlz58qHH3640G2q38/4WX3dXbt2reywww6VDz74oLbd2LFj83YNfbe32GKL/Liq+E7H7U888cQiP4tzzz03fwf/9a9/LfTvamPE+1T3uKZOnZr3cfnll9fb7qtf/Wplo402qsybN2+J/m7G9ptsskmlb9++tcdWX1OPHj0qX/rSl2q3xWc4ePDgJTp+AFgapu8BwDIqRsUs6ix8MWWvOr1raRcFj9FVMX2usQYMGJBHHlXFCJhu3bql22+/PX2cYv+x1lKMuqkrRilFh4pROnXFCJHqqJ4Qo8li2tc///nPxT5PTH+KkTl117eK533vvffSPffcs1THHuY/9upoosWpOwItvg+vv/56Hv0TI3aeeeaZetvGmmPVaV0hRkjF9Rg5E9P6QozoidFRm2++ed5X9RKjZUKMRluUeL9/+9vfpq985Sv5z3X3EWePjFFG1Wle8R2NUUSTJk1KSyv2EdMIY8RUYz3yyCN5dE+MMqy7DluMfIqRUg2Jvwd111Krjt6r+52p+1nEMcVrjpFv8T789a9/TU1p0003TTvttFP69a9/XbstRk3Fdz1ex/xTeRf3dzNGTD377LN5hFq8N9XPLF5HjEL785//XPvfkXjPY4RYnIwAAD5OohQALKMigtT9JXN+Bx10UPrsZz+bp1jFtLuYghfTtZYkUH3iE59YokXN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2bNneuSRR2r3VyqVNGLEiNStW7d8/x577JGeffbZevt4880306GHHpo6d+6cVltttTRo0KD03nvv1dvm8ccfT5/73OdShw4dUvfu3dN55523wLGMGzcubb755nmbOI7bb7/9Y3zlAAAAACuuZo1Sb731VvrsZz+b2rZtm+6444701FNPpQsuuCCtvvrqtW0iHl188cVpzJgx6aGHHkqdOnVKffv2TbNnz65tE0FqypQp6c4770y33npr+vOf/5yOPvro2v0zZ85Me+65Z9pwww3T5MmT0/nnn5/OOuusdMUVV9S2uf/++9PBBx+cg9Zf//rXtN9+++XLk08+WfAdAQAAAFgxtKrEUKRmctppp6X77rsv3XvvvQ3eH4e23nrrpe9+97vp5JNPzre98847aZ111kljx45N/fv3T08//XTacsst06RJk9L222+ftxk/fnzae++907///e/8+MsvvzydccYZ6bXXXkvt2rWrPfdNN92UnnnmmXz9oIMOSrNmzcpRq2rnnXdOvXr1ykFscSJ8denSJR9fjNgCAAAAWBHNbGQjadaRUjfffHMOSV//+tfT2muvnT796U+nn//857X7n3/++RySYspeVbyonXbaKT3wwAP5evyMKXvVIBVi+9atW+eRVdVtdt1111qQCjHaaurUqXm0VnWbus9T3ab6PPObM2dOfpPrXgAAAABonGaNUv/85z/zKKZNNtkkTZgwIR177LHphBNOSFdffXW+P4JUiJFRdcX16n3xM4JWXW3atElrrLFGvW0a2kfd51jYNtX753fuuefmQFa9xDpVAAAAACwHUWrevHlpu+22Sz/84Q/zKKlYB+qoo45q1HS55jZ8+PA8DK16eemll5r7kAAAAACWG80apeKMerEeVF1bbLFFevHFF/Of11133fxz2rRp9baJ69X74uf06dPr3f/hhx/mM/LV3aahfdR9joVtU71/fu3bt8/zIuteAAAAAFgOolSceS/Wdarr73//ez5LXujRo0eOQhMnTqzdH2s3xVpRffr0ydfj59tvv53Pqld111135VFYsfZUdZs4I98HH3xQ2ybO1LfZZpvVzvQX29R9nuo21ecBAAAAoIVEqSFDhqQHH3wwT9977rnn0rXXXpuuuOKKNHjw4Hx/q1at0kknnZR+8IMf5EXRn3jiiTRgwIB8Rr399tuvNrJqr732ytP+Hn744Xw2v+OOOy6fmS+2C4ccckhe5HzQoEFpypQp6frrr0+jR49OQ4cOrR3LiSeemM/ad8EFF+Qz8p111lnpkUceyfsCAAAAoGm1qlQqldSMbr311rw+07PPPptHRkUoisBUFYc3cuTIHKtiRNQuu+ySLrvssrTpppvWtompehGPbrnllnzWvX79+qWLL744rbLKKrVtHn/88Ry7Jk2alNZcc810/PHHp1NPPbXesYwbNy6deeaZ6YUXXsiLr5933nlp7733btLTHQIAAAC0ZI1tJM0epVoKUQoAAAAgNbqRNOv0PQAAAABWTKIUAAAAAMW1Kf+ULI96D7umuQ8BAJrU5PMHNPchAACs0IyUAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAABWrCh11llnpVatWtW7bL755rX7Z8+enQYPHpy6du2aVlllldSvX780bdq0evt48cUX0z777JNWXnnltPbaa6dhw4alDz/8sN42d999d9puu+1S+/bt08Ybb5zGjh27wLFceumlaaONNkodOnRIO+20U3r44Yc/xlcOAAAAsGJr9pFSW221VXr11Vdrl7/85S+1+4YMGZJuueWWNG7cuHTPPfekV155JR1wwAG1+z/66KMcpObOnZvuv//+dPXVV+fgNGLEiNo2zz//fN5mt912S4899lg66aST0pFHHpkmTJhQ2+b6669PQ4cOTSNHjkyPPvpo2nbbbVPfvn3T9OnTC74TAAAAACuOVpVKpdKcI6VuuummHIvm984776S11lorXXvttenAAw/Mtz3zzDNpiy22SA888EDaeeed0x133JH23XffHKvWWWedvM2YMWPSqaeemmbMmJHatWuX/3zbbbelJ598srbv/v37p7fffjuNHz8+X4+RUTvssEO65JJL8vV58+al7t27p+OPPz6ddtppjXotM2fOTF26dMnH3blz59TS9B52TXMfAgA0qcnnD2juQwAAaJEa20iafaTUs88+m9Zbb730yU9+Mh166KF5Ol6YPHly+uCDD9Iee+xR2zam9m2wwQY5SoX42bNnz1qQCjHCKV78lClTatvU3Ud1m+o+YpRVPFfdbVq3bp2vV7dpyJw5c/Lz1L0AAAAA0DjNGqVihFJMt4sRS5dffnmeave5z30uvfvuu+m1117LI51WW221eo+JABX3hfhZN0hV76/et6htIiK9//776fXXX8/TABvaprqPhpx77rm5+lUvMbIKAAAAgMZpk5rRl7/85dqft9lmmxypNtxww3TDDTekjh07pmXZ8OHD8zpUVRG5hCkAAACAxmn26Xt1xaioTTfdND333HNp3XXXzVPrYu2nuuLse3FfiJ/zn42ven1x28Scxghfa665ZlpppZUa3Ka6j4bEmfxiH3UvAAAAACyHUeq9995L//jHP1K3bt1S7969U9u2bdPEiRNr90+dOjWvOdWnT598PX4+8cQT9c6Sd+edd+ZAtOWWW9a2qbuP6jbVfcQUwXiuutvEQudxvboNAAAAAC0oSp188snpnnvuSS+88EK6//770/77759HLR188MF5naZBgwblKXJ/+tOf8mLkhx9+eA5Fcea9sOeee+b4dNhhh6W//e1vacKECenMM89MgwcPziOZwjHHHJP++c9/plNOOSWfve+yyy7L0wOHDBlSO454jp///Ofp6quvTk8//XQ69thj06xZs/LzAQAAANDC1pT697//nQPUG2+8kdZaa620yy67pAcffDD/OVx00UX5THj9+vXLZ7uLs+ZFVKqKgHXrrbfmiBSxqlOnTmngwIHpnHPOqW3To0ePdNttt+UINXr06LT++uunK6+8Mu+r6qCDDkozZsxII0aMyIub9+rVKy++Pv/i5wAAAAA0jVaVSqXSRPtaocVC5zG665133mmR60v1HnZNcx8CADSpyecPaO5DAABYoRvJMrWmFAAAAAArBlEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAABgxY1SP/rRj1KrVq3SSSedVLtt9uzZafDgwalr165plVVWSf369UvTpk2r97gXX3wx7bPPPmnllVdOa6+9dho2bFj68MMP621z9913p+222y61b98+bbzxxmns2LELPP+ll16aNtpoo9ShQ4e00047pYcffvhjfLUAAAAAK7ZlIkpNmjQp/exnP0vbbLNNvduHDBmSbrnlljRu3Lh0zz33pFdeeSUdcMABtfs/+uijHKTmzp2b7r///nT11Vfn4DRixIjaNs8//3zeZrfddkuPPfZYjl5HHnlkmjBhQm2b66+/Pg0dOjSNHDkyPfroo2nbbbdNffv2TdOnTy/0DgAAAACsWFpVKpVKcx7Ae++9l0cxXXbZZekHP/hB6tWrVxo1alR655130lprrZWuvfbadOCBB+Ztn3nmmbTFFlukBx54IO28887pjjvuSPvuu2+OVeuss07eZsyYMenUU09NM2bMSO3atct/vu2229KTTz5Ze87+/funt99+O40fPz5fj5FRO+ywQ7rkkkvy9Xnz5qXu3bun448/Pp122mmNeh0zZ85MXbp0ycfduXPn1NL0HnZNcx8CADSpyecPaO5DAABokRrbSJp9pFRMz4uRTHvssUe92ydPnpw++OCDerdvvvnmaYMNNshRKsTPnj171oJUiBFO8eKnTJlS22b+fcc21X3EKKt4rrrbtG7dOl+vbgMAAABA02qTmtF1112Xp8vF9L35vfbaa3mk02qrrVbv9ghQcV91m7pBqnp/9b5FbRPh6v33309vvfVWngbY0DYxMmth5syZky9VsT8AAAAAGqfZRkq99NJL6cQTT0y//vWv8+Liy5tzzz03D0WrXmK6HwAAAADLeJSKKXOxkHisJ9WmTZt8icXML7744vznGKkUU+ti7ae64ux76667bv5z/Jz/bHzV64vbJuY0duzYMa255ppppZVWanCb6j4aMnz48Dw3snqJyAYAAADAMh6ldt999/TEE0/kM+JVL9tvv3069NBDa39u27ZtmjhxYu0xU6dOTS+++GLq06dPvh4/Yx91z5J355135uC05ZZb1rapu4/qNtV9xBTB3r1719smFjqP69VtGtK+ffv8PHUvAAAAACzja0qtuuqqaeutt653W6dOnVLXrl1rtw8aNCgNHTo0rbHGGjn6xNnwIhTFmffCnnvumePTYYcdls4777y8ftSZZ56ZF0+PaBSOOeaYfFa9U045JR1xxBHprrvuSjfccEM+I19VPMfAgQNzCNtxxx3z2f9mzZqVDj/88KLvCQAAAMCKolkXOl+ciy66KJ8Jr1+/fnlR8Thr3mWXXVa7P6bd3XrrrenYY4/NsSqiVsSlc845p7ZNjx49coAaMmRIGj16dFp//fXTlVdemfdVddBBB6UZM2akESNG5LDVq1evNH78+AUWPwcAAACgabSqVCqVJtrXCi3OvhcLnsf6Ui1xKl/vYdc09yEAQJOafP6A5j4EAIAVupE025pSAAAAAKy4RCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAAAAAChOlAIAAACgOFEKAAAAgOJEKQAAAACKE6UAAAAAWD6i1Cc/+cn0xhtvLHD722+/ne8DAAAAgCaPUi+88EL66KOPFrh9zpw56eWXX16aXQIAAACwAmmzJBvffPPNtT9PmDAhdenSpXY9ItXEiRPTRhtt1LRHCAAAAMCKHaX222+//LNVq1Zp4MCB9e5r27ZtDlIXXHBB0x4hAAAAACt2lJo3b17+2aNHjzRp0qS05pprflzHBQAAAEALtkRRqur5559v+iMBAAAAYIWxVFEqxPpRcZk+fXptBFXVL37xi6Y4NgAAAABaqKWKUmeffXY655xz0vbbb5+6deuW15gCAAAAgI81So0ZMyaNHTs2HXbYYUvzcAAAAABWcK2X5kFz585Nn/nMZ5r+aAAAAABYISxVlDryyCPTtdde2/RHAwAAAMAKYamm782ePTtdccUV6Y9//GPaZpttUtu2bevdf+GFFzbV8QEAAADQAi1VlHr88cdTr1698p+ffPLJevdZ9BwAAACAjyVK/elPf1qahwEAAADA0q8pBQAAAADFR0rttttui5ymd9ddd/03xwQAAABAC7dUUaq6nlTVBx98kB577LG8vtTAgQOb6tgAAAAAaKGWKkpddNFFDd5+1llnpffee++/PSYAAAAAWrgmXVPqm9/8ZvrFL37RlLsEAAAAoAVq0ij1wAMPpA4dOjTlLgEAAABogZZq+t4BBxxQ73qlUkmvvvpqeuSRR9L3vve9pjo2AAAAAFqopYpSXbp0qXe9devWabPNNkvnnHNO2nPPPZvq2AAAAABooZYqSl111VVNfyQAAAAArDCWKkpVTZ48OT399NP5z1tttVX69Kc/3VTHBQAAAEALtlRRavr06al///7p7rvvTquttlq+7e2330677bZbuu6669Jaa63V1McJAAAAwIp+9r3jjz8+vfvuu2nKlCnpzTffzJcnn3wyzZw5M51wwglNf5QAAAAAtChLNVJq/Pjx6Y9//GPaYostardtueWW6dJLL7XQOQAAAAAfz0ipefPmpbZt2y5we9wW9wEAAABAk0epL37xi+nEE09Mr7zySu22l19+OQ0ZMiTtvvvuS7NLAAAAAFYgSxWlLrnkkrx+1EYbbZQ+9alP5UuPHj3ybT/96U+b/igBAAAAaFGWak2p7t27p0cffTSvK/XMM8/k22J9qT322KOpjw8AAACAFX2k1F133ZUXNI8RUa1atUpf+tKX8pn44rLDDjukrbbaKt17772N3t/ll1+ettlmm9S5c+d86dOnT7rjjjtq98+ePTsNHjw4de3aNa2yyiqpX79+adq0afX28eKLL6Z99tknrbzyymnttddOw4YNSx9++GG9be6+++603Xbbpfbt26eNN944jR07doFjiUXaY+RXhw4d0k477ZQefvjhJXlrAAAAAPi4otSoUaPSUUcdlQPS/Lp06ZK+/e1vpwsvvLDR+1t//fXTj370ozR58uT0yCOP5LWqvva1r6UpU6bk+2ONqltuuSWNGzcu3XPPPXkNqwMOOKD2+I8++igHqblz56b7778/XX311Tk4jRgxorbN888/n7fZbbfd0mOPPZZOOumkdOSRR6YJEybUtrn++uvT0KFD08iRI/MIsG233Tb17ds3TZ8+fUneHgAAAAAaqVWlUqk0duMNN9wwjR8/Pk/Va0hM5dtzzz3z6KWltcYaa6Tzzz8/HXjggWmttdZK1157bf5zdf/x3A888EDaeeed86iqfffdN8eqddZZJ28zZsyYdOqpp6YZM2akdu3a5T/fdttt6cknn6w9R//+/dPbb7+dX0uIkVEx0ivWygpxBsGYohgjwE477bRGHXeMHosw98477zQY7ZZ3vYdd09yHAABNavL5A5r7EAAAWqTGNpIlGikVU+fatm270PvbtGmTY9DSiFFP1113XZo1a1aexhejpz744IN661RtvvnmaYMNNshRKsTPnj171oJUiBFO8eKro61im/nXuoptqvuIUVbxXHW3ad26db5e3aYhc+bMyc9T9wIAAABA4yxRlPrEJz5Rb8TR/B5//PHUrVu3JdlleuKJJ/J6UbHe0zHHHJNuvPHGvG7Va6+9lkc6rbbaavW2jwAV94X4WTdIVe+v3reobSIivf/+++n111/PQayhbar7aMi5556bq1/1EiOrAAAAAPgYotTee++dvve97+UFyOcXgSfWZIrpdEtis802y2s9PfTQQ+nYY49NAwcOTE899VRa1g0fPjwPQ6teXnrppeY+JAAAAIDlRpsl2fjMM89Mv/vd79Kmm26ajjvuuByUqms9xdnrYsTRGWecsUQHEKOh4ox4oXfv3mnSpElp9OjR6aCDDspT62Ltp7qjpWIK4brrrpv/HD/nP0te9ex8dbeZ/4x9cT3mNHbs2DGttNJK+dLQNtV9NCRGdsUFAAAAgI95pFRMaYuz3G299dZ5pND++++fL6effnq+7S9/+csC0+CWVCwyHus1RaCK9asmTpxYu2/q1Kl5EfVYcyrEz5j+V/cseXfeeWcOTjEFsLpN3X1Ut6nuI6JYPFfdbeIY4np1GwAAAACacaRU9Qx8t99+e3rrrbfSc889l+LkfZtssklaffXVl/jJI2x9+ctfzouXv/vuu/lMe3fffXeaMGFCXqdp0KBBaejQofmMfBGa4mx4EYrizHshzvQX8emwww5L5513Xl4DKkZzDR48uDaKKdapirPqnXLKKemII45Id911V7rhhhvyGfmq4jli2uD222+fdtxxxzRq1Ki84Prhhx++xK8JAAAAgI8hSlVFhNphhx3SfyNGOA0YMCC9+uqrOUJts802OUh96UtfyvdfdNFF+Ux4/fr1y6On4qx5l112We3xMe3u1ltvzWtRRazq1KlTjkvnnHNObZsePXrkADVkyJA8LXD99ddPV155Zd5XVUwVjLMGjhgxIoetXr16pfHjx//Xo74AAAAAaFirSgx14r8WZ/OLsBaLnseorpam97BrmvsQAKBJTT5/QHMfAgDACt1IlmhNKQAAAABoCqIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAACtWlDr33HPTDjvskFZdddW09tprp/322y9NnTq13jazZ89OgwcPTl27dk2rrLJK6tevX5o2bVq9bV588cW0zz77pJVXXjnvZ9iwYenDDz+st83dd9+dtttuu9S+ffu08cYbp7Fjxy5wPJdeemnaaKONUocOHdJOO+2UHn744Y/plQMAAACs2Jo1St1zzz05OD344IPpzjvvTB988EHac88906xZs2rbDBkyJN1yyy1p3LhxeftXXnklHXDAAbX7P/rooxyk5s6dm+6///509dVX5+A0YsSI2jbPP/983ma33XZLjz32WDrppJPSkUcemSZMmFDb5vrrr09Dhw5NI0eOTI8++mjadtttU9++fdP06dMLviMAAAAAK4ZWlUqlkpYRM2bMyCOdIj7tuuuu6Z133klrrbVWuvbaa9OBBx6Yt3nmmWfSFltskR544IG08847pzvuuCPtu+++OVats846eZsxY8akU089Ne+vXbt2+c+33XZbevLJJ2vP1b9///T222+n8ePH5+sxMipGbV1yySX5+rx581L37t3T8ccfn0477bTFHvvMmTNTly5d8jF37tw5tTS9h13T3IcAAE1q8vkDmvsQAABapMY2kmVqTak42LDGGmvkn5MnT86jp/bYY4/aNptvvnnaYIMNcpQK8bNnz561IBVihFO8AVOmTKltU3cf1W2q+4hRVvFcdbdp3bp1vl7dZn5z5szJz1H3AgAAAEDjLDNRKkYmxbS6z372s2nrrbfOt7322mt5pNNq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zO8AAAAAwIqpVSWGIy0DYqTUjTfemGNQiMOKEVTf/e5308knn5xve+edd9I666yTxo4dm/r375+efvrptOWWW6ZJkyal7bffPm8zfvz4tPfee6d///vf+fGXX355OuOMM9Jrr72W2rVrl7c57bTT8qisZ555Jl8/6KCDciCLqFW18847p169euUg1hgRv7p06ZKPMUZttTQWFgWgpVnRFxZdHvn3CAAtzeQW+u+RxjaSZXZNqeeffz6HpJiyVxUvaKeddkoPPPBAvh4/Y8peNUiF2L5169Z5ZFV1m1133bUWpEKMtpo6dWp66623atvUfZ7qNtXnAQAAAKBptUnLqAhSIUZG1RXXq/fFz7XXXrve/W3atElrrLFGvW169OixwD6q962++ur556KepyFz5szJl7oVEAAAAIDGWWZHSi3rzj333Dxyq3qJBdQBAAAAWM6j1Lrrrpt/Tps2rd7tcb16X/ycPn16vfs//PDDfEa+uts0tI+6z7Gwbar3N2T48OF5bmT18tJLL/0XrxYAAABgxbLMRqmYchdRaOLEifWmyMVaUX369MnX4+fbb7+dz6pXddddd6V58+bltaeq28QZ+T744IPaNnGmvs022yxP3atuU/d5qttUn6ch7du3z4t11b0AAAAAsBxEqffeey899thj+VJd3Dz+/OKLL+az8Z100knpBz/4Qbr55pvTE088kQYMGJDPqFc9Q98WW2yR9tprr3TUUUelhx9+ON13333puOOOy2fmi+3CIYcckhc5HzRoUJoyZUq6/vrr0+jRo9PQoUNrx3HiiSfms/ZdcMEF+Yx8Z511VnrkkUfyvgAAAABoYQudR/jZbbfdateroWjgwIFp7Nix6ZRTTkmzZs1KRx99dB4Rtcsuu+R41KFDh9pjfv3rX+d4tPvuu+ez7vXr1y9dfPHFtftjvac//OEPafDgwal3795pzTXXTCNGjMj7rPrMZz6Trr322nTmmWem008/PW2yySbppptuSltvvXWx9wIAAABgRdKqUqlUmvsgWoKYWhgBLNaXaolT+XoPu6a5DwEAmtTk8wc09yGwhPx7BICWZnIL/fdIYxvJMrumFAAAAAAtlygFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAAAUJ0oBAAAAUJwoBQAAAEBxohQAAAAAxYlSAAAAABQnSgEAAABQnCgFAAAAQHGi1HwuvfTStNFGG6UOHTqknXbaKT388MPNfUgAAAAALY4oVcf111+fhg4dmkaOHJkeffTRtO2226a+ffum6dOnN/ehAQAAALQoolQdF154YTrqqKPS4Ycfnrbccss0ZsyYtPLKK6df/OIXzX1oAAAAAC1Km+Y+gGXF3Llz0+TJk9Pw4cNrt7Vu3Trtscce6YEHHlhg+zlz5uRL1TvvvJN/zpw5M7VEH815v7kPAQCaVEv9/9ktmX+PANDSzGyh/x6pvq5KpbLI7USp/+/1119PH330UVpnnXXq3R7Xn3nmmQW2P/fcc9PZZ5+9wO3du3f/WI8TAGgaXX56THMfAgCwguvSwv898u6776YuXbos9H5RainFiKpYf6pq3rx56c0330xdu3ZNrVq1atZjA5bf/5oQYfull15KnTt3bu7DAQBWUP5NAvy3YoRUBKn11ltvkduJUv/fmmuumVZaaaU0bdq0erfH9XXXXXeB7du3b58vda222mof+3ECLV/8488/AAGA5ubfJMB/Y1EjpKosdP7/tWvXLvXu3TtNnDix3uinuN6nT59mPTYAAACAlsZIqTpiOt7AgQPT9ttvn3bcccc0atSoNGvWrHw2PgAAAACajihVx0EHHZRmzJiRRowYkV577bXUq1evNH78+AUWPwf4OMSU4JEjRy4wNRgAoCT/JgFKaVVZ3Pn5AAAAAKCJWVMKAAAAgOJEKQAAAACKE6UAAAAAKE6UAgAAAKA4UQoAAACA4kQpgGY2b9689NFHHzX3YQAAABQlSgE0o6eeeioNGDAg9e3bNx177LHp/vvvb+5DAgBWQP4DGdAcRCmAZjJ16tT0mc98Jv8jcIcddkgPPPBAOvHEE9PFF1/c3IcGAKxA/v73v6dRo0alV199tbkPBVjBtGnuAwBYEVUqlXTNNdfkEVK/+c1v8m2nn356DlJXXXVVmj17djrllFOa+zABgBbuueeeS3369ElvvfVWeuONN9LQoUPTmmuu2dyHBawgRCmAZtCqVav0yiuvpNdee61226qrrppOOOGE1KFDh3TdddelT3ziE+nQQw9t1uMEAFquWbNmpXPPPTd99atfzaO2jzvuuPThhx/m/zAmTAEliFIAzTBKKqLUdtttl5599tk8jW+zzTarhakjjjgi33bZZZel/fffP6288srNfcgAQAvUunXr1Lt379S1a9d00EEH5RDVv3//fJ8wBZTQqhK/HQFQ3D/+8Y+088475/86OXr06LTKKqvUgtVLL72UNtxww3T77benvfbaq7kPFQBowaOlOnXqVLt+/fXXp4MPPjh997vfTaeddloOVnGm4H/961+pR48ezXqsQMtjpBRAM/nUpz6VbrjhhvTlL385dezYMZ111lm1/yLZtm3btM0226QuXbo092ECAC1YNUjFiVdi5FSMmIr/SHbIIYfk/1B20kknpZ/85Cc5Sv3yl780ghtoUqIUQDPabbfd0rhx49LXv/71fMabb3zjGzlGxSLo06dPT927d2/uQwQAVgArrbRSjlExKiqm8EWQOuyww9LNN9+cR3dPmjRJkAKanOl7AMuARx99NJ/t5oUXXkht2rTJ/zCMxc4//elPN/ehAQArkOqvhxGldt999/TYY4+lu+++O/Xs2bO5Dw1ogUQpgGXEzJkz05tvvpnefffd1K1bN4uLAgDNIqbyDRs2LI0aNSpHqRjFDfBxMH0PYBnRuXPnfAEAaG5bbbVVHsktSAEfJyOlAAAAqKd6RmCAj1Prj3XvAAAALHcEKaAEUQoAAACA4kQpAAAAAIoTpQAAAAAoTpQCAAAAoDhRCgAAAIDiRCkAAAAAihOlAIAW4Qtf+EI66aSTatc32mijNGrUqEY/fuzYsWm11VZLLfk9KeVb3/pW2m+//Yo/LwCwfGnT3AcAAPBxmDRpUurUqVPx523VqlW68cYbl4ko87vf/S61bds2LUsiWF199dULvX/DDTdML7zwQtFjAgCah5FSAECLtNZaa6WVV145rcjWWGONtOqqq6ZlyejRo9Orr75au4Srrrqqdj1iIgCwYhClAIDlzqxZs9KAAQPSKquskrp165YuuOCCBbaZf/rehRdemHr27JlHT3Xv3j195zvfSe+9994Cj7vpppvSJptskjp06JD69u2bXnrppXr3//73v0/bbbddvv+Tn/xkOvvss9OHH35Ye86w//775xFT1euLe1ylUklnnXVW2mCDDVL79u3Teuutl0444YRGvReXXXZZ7XjXWWeddOCBBy50+l5En3322Sd17Ngx9ejRI1177bULvE9x3FdeeWV+DRH1Yt8333xz7f6PPvooDRo0KD8+9rPZZpvl0NRYXbp0Seuuu27tEmLaZPz59NNPT4cffni97T/44IO09tprp//93/+tvabjjjsuX2Jfa665Zvre976X38OqOXPmpJNPPjl94hOfyJ/3TjvtlO6+++5GHyMAUIYoBQAsd4YNG5buueeeHHr+8Ic/5ODw6KOPLvIxrVu3ThdffHGaMmVKnj521113pVNOOaXeNv/5z3/S//zP/6Rrrrkm3Xfffentt99O/fv3r91/77335hh24oknpqeeeir97Gc/y2tRxWNCdZRPdeRP9friHvfb3/42XXTRRfn2Z599NoexCGiL88gjj+R4dc4556SpU6em8ePHp1133XWh28cxvPLKK/n9iue84oor0vTp0xfYLoLZN77xjfT444+nvffeOx166KHpzTffzPfNmzcvrb/++mncuHH5tYwYMSLHpBtuuCH9t4488sj8GqojqMKtt96aP5eDDjqodlt8fm3atEkPP/xwDmIRHCOkVUWweuCBB9J1112XX8PXv/71tNdee+X3FgBYhlQAAJYj7777bqVdu3aVG264oXbbG2+8UenYsWPlxBNPrN224YYbVi666KKF7mfcuHGVrl271q5fddVVMdSm8uCDD9Zue/rpp/NtDz30UL6+++67V374wx/W288vf/nLSrdu3WrXY/sbb7yx3jaLe9wFF1xQ2XTTTStz585dovfit7/9baVz586VmTNnNnj/5z//+dp7Un0tkyZNqt3/7LPP5tvqvk9x/cwzz6xdf++99/Jtd9xxx0KPY/DgwZV+/frVrg8cOLDyta99rVGvYf73a8stt6z8+Mc/rl3/yle+UvnWt75V7zVtscUWlXnz5tVuO/XUU/Nt4V//+ldlpZVWqrz88ssLfAbDhw9v1DEBAGUYKQUALFf+8Y9/pLlz5+YpWXXXToppZIvyxz/+Me2+++55Sless3TYYYelN954I4/CqYrRNzvssEPt+uabb56nlj399NP5+t/+9rc8KimmDVYvRx11VB7ZU3c/81vc42Ikz/vvv5+n9cXtsVB6dWrfonzpS1/KC4PH4+L1/PrXv17occRIqnh9MYWwauONN06rr776Attus802tT/H9LfOnTvXG1F16aWXpt69e+d1u+K1xIirF198MTWFGC0VI83CtGnT0h133JGOOOKIetvsvPPOeZphVZ8+ffIoqJha+MQTT+Sfm266ab33O0bWxXcHAFh2OPseANDixdnc9t1333TsscfmKXMRsf7yl7/ktZEicDV2QfRYgyqmth1wwAEL3BdrOi3t42KNq4hGEc7uvPPOvN7V+eefn0PKos6eF3Etpi3GdLyYxhhT6WJtqpg2GDFtac3/nBGAYtpeiClxsV5TrOMVMSiOIY71oYceSk0hphiedtppefrd/fffn9eu+tznPtfox8d7vdJKK6XJkyfnn3VFnAIAlh2iFACwXPnUpz6Vo0lEkFgYPLz11lvp73//e/r85z/f4GMiUERUiZASa0uFhtZAitFJsU7TjjvumK9HKIp1pbbYYot8PUYZxW0xwmhh4thipE5djXlcLBr+la98JV8GDx6cR2nFqJ+6I5saEqOf9thjj3wZOXJkjlGxXtb8ASxGksXr++tf/5pHOYXnnnsuv3dLItba+sxnPpPDWVVTjkDq2rVr2m+//fJoqQhT8y98HuYPYA8++GBekD0i1Kc//en8/sfIriWJWQBAeaIUALBcidEuMcIpFjuPgBFnZjvjjDNqsakhEYPiLG4//elPc/SJsDJmzJgGg9Lxxx+fF0SP2BMLZsdUsWqkipFIMeIqYlic5S6eM6bmPfnkk+kHP/hB3ibOZjdx4sT02c9+Np9JL6bHLe5xseh5hJSYkhijtn71q1/lSBVT8xYlFgH/5z//mRc3j+e5/fbbc3xraCpjRK4IV0cffXS6/PLL82v97ne/m5+n7lS4xYn4EwvBT5gwIY9i+uUvf5lHZsWfm0pM4Yv3K96TgQMHLnB/TBUcOnRo+va3v51HisXnWj0DY0zbi4XZY8RV3BaRasaMGfkziWmJcfZBAGDZYE0pAGC5E9PFYhRMBKYILbvssktt9E9Dtt1223yGth//+Mdp6623zmsvnXvuuQtsF0Ho1FNPTYccckiOShHArr/++tr9ffv2zSEopsrF2lMRrOKseXXjUYSQmIIXU/IiiDTmcTG66ec//3l+zggnMY3vlltuydFtUeJxv/vd79IXv/jFPJorQttvfvObtNVWWzW4fcSkddZZJ0es/fffP69fFdPvFjX1cH4RgmIUVpwNLyJarMtVd9RUU4jPtFu3bvl9W2+99Ra4P4JTrMEVsTBGlcVZDSO2VcUoq9gmolsEuhh5FeGsOrIOAFg2tIrVzpv7IAAAKO/f//53jmfVReCXFbEuVCxIH3Fp/mmIX/jCF1KvXr3SqFGjmu34AICmYfoeAMAKItaaiuDTs2fPfOa/U045JU83jJFTy4KYevj666/n0WYxCuyrX/1qcx8SAPAxEqUAAJZR9957b/ryl7+80PsjMC2JWFfr9NNPz+tQxbS9WLA8pjIu6gx/JcVaUbE21frrr5/X2Yp1vQCAlsv0PQCAZVSsm/Tyyy8v9P5Fnc0PAGBZJ0oBAAAAUJyz7wEAAABQnCgFAAAAQHGiFAAAAADFiVIAAAAAFCdKAQAAAFCcKAUAAABAcaIUAAAAAMWJUgAAAACk0v4faNTv0DxMk3AAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1200x1000 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Example: count how many of each 'Diet' type\n",
    "plt.figure(figsize=(12, 10))\n",
    "sns.countplot(x='diabetes_signal', data=hearGardaData)\n",
    "plt.title('Distribution of diabetes_signal Types')\n",
    "plt.xlabel('diabetes_signal Type')\n",
    "plt.ylabel('Count')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "id": "a8487fef-558e-4c1d-8cae-b74c77757bfa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['age', 'gender', 'height', 'weight', 'Systolic', 'Diastolic',\n",
       "       'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'BMI',\n",
       "       'diabetes_signal', 'Family_History', 'Heart Attack Risk',\n",
       "       'gender_label'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 272,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "id": "6f6c9355-e520-4569-bd0f-65314cb31f79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABGYAAAPaCAYAAADV5l5zAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQABAABJREFUeJzs/WeMHNmanou+K1y68t47FqtYZNGbZrO93739nj3u3jnSzBEgAQIEQSMBEiRIkIEgQfol6IckSD90Z450r84ZbTuzTXvLZjfZ9J5FVrG895U2Ita6+FZkZmVWZWbRk51cT6OaVZmR4TLsG9/3vkwIIaBQKBQKhUKhUCgUCoVCoXjkaI9+kgqFQqFQKBQKhUKhUCgUCkIJMwqFQqFQKBQKhUKhUCgUjwklzCgUCoVCoVAoFAqFQqFQPCaUMKNQKBQKhUKhUCgUCoVC8ZhQwoxCoVAoFAqFQqFQKBQKxWNCCTMKhUKhUCgUCoVCoVAoFI8JJcwoFAqFQqFQKBQKhUKhUDwmlDCjUCgUCoVCoVAoFAqFQvGYUMIMACEEVlZW5L8KheLJQO2XCsWThdonFYonD7VfKhQKRXGghBkAq6urKC8vl/8qFIonA7VfKhRPFmqfVCiePNR+qVAoFMWBEmYUCoVCoVAoFAqFQqFQKB4TSphRKBQKhUKhUCgUCoVCoXhMKGFGoVAoFAqFQqFQKBQKheIxoYQZhUKhUCgUCoVCoVAoFIrHhPG4JqxQKBRPK47jIm4zMCYQ9OsFh01EoxS7AWaaME1TvmY7Aq4ADB0wNCZfi8fi4BzQNcDy++RrruNA2AlA02H4kq+5Luy4AzDAH/Bey4cbXQWTIzXBTAtMNyAcm0YM6AaY4c0Pj0UA15bT0QIl6c8L+qwThwCDZvnhOA5YPELvQPhCMAzvFBSPO7SIME0GjTugBRGCe9MxLGi+QP55tG3AjgFMhx4I3uE3oCgGYnEbjstgaAJ+v7ctKhR3ixOPAY4NoRkwA/mPNYrcRGMOXA6YmoBP7YeKh4QbC4O5DoRuQPeHHvfsKBQPBSXMKBQKxSNkNSowOMMwuQSYOkNXHUddGRDyZxcw2pEIxNI0xMglwElA1LQh1rYHK7aJqxNANA5UlQA9jQIaBC6P61iOaCjxC+xodFBqucDQGWBhHDD9wK7nEddLMTLHMbJggvScbbU2GioYgoHsUwGPrEKszsMZvkzKELSKeujt/XA1C3zsCsTsMFioEvqOZ8CcBJzbFyGWZ8F8Qegd/WAllXI87vhN8OkhOX1zxxFgcRrO+A35ntbQBd7QiYVEEOfHNNgu0FjmYme9Ay2yCJfGSRdiZdUwOnZDWCHo/vWbJte1waJh8JEr4AsTgOmDaNsFVl4LPVj6SL5LxeMhGrWxmjBwfVJDOMZQHhTobRII6DYCAetxz57iG0IiFoEej4APXYRYmwfzl8Dt3A0eqIAZVDd+WxGOOliJabg+yRBLsPT5yG/a8FtqP1Q8GJzoGlgsDHfoPERkBSxYDnTugfAHYQTUuV5RXChhRqFQKB4RKxGBj64IJJz11xbWgPpygYOdPC3OJCIR8OsngJnb6eFEeT1uzwKXJtc/uxoDRuaBZ7o1LEeE/Hs1RqIPw8F2gebOAxCjVwAsS1Hm42sMkfh6hc7pYR1VcxzPdtsIBrwnnW5kBfz2Rbij19LDueFluJO3YB7+NvTWHbCnBoGeI0B0DYmvf0OlMd48hpfBFyahd+4Ba+6Fe+uMfN3c8wrsi59CrC2uj3N1AXx8AFUH3sTCmldl01vrAJMDsG+eXl/u8DISU0MwD7wJ+FvSr7PwChInf+VV6iRxlmagNW6D6D4EI7heuaMoHmKxOMaWTJwbFrQVyNdomx9bEDjWY6DOsNOVZQpFIfTVBdhn35UVienj1/w4jJ7DsBu3w8wQghXZRCI2Bud0XJtAxn4IjM4LvNhnwq90GcUDIEEPhhYmYV/6NP2a3E9nR2DsfgkJ3QdLiYCKIkJ5zCgUCsUjIGFzXB3PFmVSTC8zrMXX/2axtSxRhnCa+nF5cvMNJ91TXBoV2NbgXRynODuiwxaeCKO9+Ae4PcMRyZhGioWwJsWh9LQdO0uUScNdONe/khM0WnfABIdz9Yu0KJOJO3TBa0mi8ZVWQcTWskSZ9LxHluFOD+H5bm8craXxtJizcSGdK1+Ah5e98ccicG6cyhJl0rM5eQssEd08DkVRkBAmLozkfu/MEBB3CrcGKhSEG16Bc+V4WpTJxBk4Dd3JcbBUpLFhJEWZbLgAzt4WCEfdxzFbiiLDsONwrp3I+Z5z9QQMW53rFcWFEmYUCoXiEUC2LuObtYk0I3Prv/Ppwew3LT+WEyY230J4rMWAjR0cdIEcSQDY9RYcYWJ4If8NKz35TMS9GxF6YpwPsTQDxl2wUJn0f8kltqSnvzQLtvslaFVNcGdG8g83NYhafwQlfqqNX8x5oySnHV2VPhAEtU8Vmk8+M5z3PcU3GxIXadvORcwGEk62QKlQ5IS8r0gAz4XgaRFYkZuFtXxnI2A5Athc7YeK+0ckPP+nnFCLN72vUBQRSphRKB4izug1JM5/BE43lQ8AutkV0TwXk4pvNCzjOpZcYza9fy/jpP/FYvLfzPHnnnZymuxOTgt3MDeMQcg7aFF44jQultJj7nQp5RIVnLbiKUV99YoHsaGoY0hB1NpRPBn76aOaD4Xi0aA8ZhSKh4Sg9gvyykjE4JoWtJ3P3d/4XAeJr34pf/e98kdgFpUYKO6VWELA4d71NwVJ6Ml0o43Ysahs75ECg27BCATgciGfzpOYQClIAYshkbCh2xGZKARNy0odiiaENNttqwH6mgCLR8Go1YdpELqJ+WWgKpSAEwZcZkFv7IQ7MwRj36vQdFM+wa3VIatKqDpmI21VAg2+MH68y5bpRAkjgF9fMBC0AKu+GhAxHO0U8JkWfAh70waDMEysRAOIcg5D2OCra9Cqm4CaWmi7vwXbYeCCQWdcJiaJm6cRNUrhlJYjgJg05tUau4HadjBqaaLliYfhnn0XWkUtZBFPRQ0YtR5ZpXIczPVK3IWuw3YZ9IURaIzhre2rYKgAWBD6C9+Dzl3ZPiU0XaY7uec/AEwLfG1Jfhfkd8NLqqBTIhMNyxi44YNz9SS0uvbc36Ob/NI0A0Yec0/XTQA0LCVDaRrgL4Gu5642oqd1wkmA0UZk+tMpVRvh1FqViCc3GB1asCzvdqkoTMjn7XP72zmaQ1G53Qmm49aiH4OzGix93XtGociL4QOj/fDw92C6VIblyuO2q/vhfva/oIXKH/ccPtFUlTBQDeer/TZCLJY8XuoYDZdgYBqwNGpPVc9+FfeHvM41fdCO/QgGnb/l9ZUORzfBv/gpGAUbKBRFBBN09/iUs7KygvLyciwvL6OsTF0wKx4MfHkOiS9/IW/sZDTxi3+Qd9jE2fdlAo21/3WwPDGA7sRN2Bc/kb8bO5+TPh/FzMPaLylqen4NOHfbM8slwaSjjgQThqAv+4bOWVuGe+MUxCy14gigvBbGjmcR1svx/hVDtlSQWPJmbwR8YgAupRjZccAKwCAD3LoOTMVCOD8sEE0A39sdhxZbgXvthEw9IjGB1XdB37YfDgkP1BpU3Qxj5wvQhAPn1hnwqdtSmCGvFtZzFGfnqzGyuK6pH2qNo8Udhjt4FqAoatOC3roTenMPEoPngfHr8kJG3/MKdF8A9vWvZEsSbZRaTQuM3sNwrDLwj/7MEzye/13EtZD0D7g9r8kYVFrGva0c1UEHv71sSZ+c8iDwSncUYnkGYuCU12qkG0BzH4z2XTIpiV/+VC6jdui7MEwDzvWT6RYkrbIBRu8z4L4SOJ/8T7DSahg7j4FZAbijV+GOXfNKmP0hGNv2g1U1QlCqE4mdsTCM538PLLIE5/opiPCSF9Xd0AVj2z55o64H1vcjZ20FLs3j7LAXPV5eA733WXB/KayMeFyKByePGvc2fY8x2UJGiVCsvjMr6YlEUkHGoVdPQKzMectY3wlj+yFoGxKheGQFzk36Hoe877GkEkbvEbCSKmj+b1a895NwrozFEtC5DT5xA2LYSyyDLwitaz9Q0wYr+M1ap4rHB6XP0fHIuZU8dhom9NY+6C074GgGrG+I+e/j2C+j0QR8Ig53+BJcStpzHbBACfTug0BFgzJfVzwQ4vE4DDcOMTUE5/al9fNye7+X7GiZMAwlziiKByVnKxQPCXkDqhvQm7fL9Bq6QcsFtSaRJwbd4FHrUz7c2RGwUAVYoNS7qVfcEyTKfHbNE2UIElcGp4Hj10k8WdepnfAqnFO/8m7mU+4uy7NwTv4VQiKM0uQ1++u9MfBbZ+HePOOJMkQiKo1y+dhVVPrjCMeBN/oBLbHmjTP1/QkBMXUL7pl3YOx+JTmD49Dgwj7zLvjk4HriEaUYnf41DtYuoqvOi8o+3OGiJX4D7tXj3o0FYSfgDp6TAobZudd7zbCksJA49eukKCPHCD43Kl8z7LX0Mia0AL68Bdya9UQZgqp0jg9omAsb+HZylPtbOcTCJPiFDz1RhnAdYOQinMufSm+Z1DIaPksmKGX6wvDFKSRO/QqaEwVq9nnrxArAufaljMpO95XHwnAufw4xMwJe0yL/ZntfA4sswz7znifKyBG6Uhyzz74vfXCyvsevfwVBZsqp9JXlOfk9aBnGgU7Mi811B057F39yZcSkyTAfuQwntX5TSVEn/8oTZZLLSF45cv1mtBpyOY/0Pd5a/x7XFmGffmd9vhV3hS4cuDdPQ5BJNIkyBEUeXz0OQYle8eRrCkUBbDsGPj3kGQCn9m0yPh+6IAVk2s4U+bFEHM7lz+COXPGO+8lrGYceHi2Mw3HU+lPcP1Q5y4cvwxn4Ovu8PPC19yCMyp4ViiJCCTMKxUOCry1KEYUqHQixkltMcelJuqaDldcWNl5dXfBMV4NlshpHcW/tS1Qpk4ulCBDOaBNy58akwLIJwaXw8fw27wZQdxNwxwdyjpMuHPzCE2sCWkxW36RFnsxRUqXG2hJYZQPw0h/JbUXkEfLcgZPY2xBBTSnQVhqR85ILmU7EPXHD6H8BztAFr1x/I9RqN30b7OU/Bg7/CJGEhvm13KeG86MabNsbR4UVBR84mXM4LEx4F1FVbdCe/7G3flI30VkL48gLe71/J+Cv9kx9ZXXSZpzBszCS4zBLK71UphyQ8JG57ii+O33jlTUgl2KaHfW+Y81JeFU6OXBHrkKzvWkLSokYOJXbpDi2BndpOmNelqSIk3N5SPCJPBjvqacJ2VY4mXt/E0PnwBxlBqnYGj0Rh0MVhTngM7eT7auKvCRi3rE1B5RqxeLhRz5LiuJDo+ur0as536PX6bytUBQTSphRKB4SdFNGbRhUrUAl0vmekPOlaa8SpqJePoEnz4pN4yKvDbrZJKEnVA6xtiB9NxR3Bz1cSVXK5GJ2xbvZdhIJsLn8SUJicRIGHATJ/iVGF6B5OkLpe0umBlAVh1iayj/OuRFo1c0wTROcRKF8wy3NQBMubtA1MY07+bQy57BUvVHdCuYLyAqVvMPNj8MQceilpZhbzd/dSpU/rvDavRhNt0Astbs8D9Z3BDqYbGvKB1+Ygk7b/N7npZiZFxJGkuIIiSoFE6GS03Po5kpWPOVGLE0m/XbILyaaNxFKTi/5PQrXlvOcd9rTw9JfSv4+n3+5ZbWNUJGyd0u6OisXtE2mthGFohBU3Vjgpk5VtBUmXS2Yi0TSz0uhuE/kebfgeVnFZSuKCyXMKBQPAboxows76rkmY1DmL0malm6GUyVMsBRaSaXX2rK6sHl89FnyxiBhJlAiDdBUOtPdQx6teTx+JX4r+SaZ2Fr5/QWY6ZMji9C1Zx7D1zTkuyKlG88gNi++kLxZkDf1vgI+GTTtDePOP6wFhOfAKBip0LQtP4RmgnOOQIHF0TLXHxnjFjBZZT5/0vvFADMDW0xbAxantza0TpvwsoLLzpLrj9H3WGBd0joRqfQVbYt1mZweo9NmoW3DH/LMgAlfgeWW240yqb1bGG3ThdDyx8IrFHd+7Mw4zio2U+AYKI9raj9UPABYHuP99fdVho2iuFBbtELxMIityWoJEmQkgZKcT/hldUx0FayhE0gagZKAQ8aoWcMlP0vCTOopn4itAtTapLhjKH2JjH7JU2YjdC9dm1ydZFSL1j44E7lbJlj7boyvJi9MSfAIVcJo7JQGtrJdSDdkJRRVTAiqmKLvywyAtfVLIc5p3o04LClyWIllGINfQW/ognPyF8DwCKxjr+VtUdJbeuGYAbzdNQcYfrCKOriVbbCrO2BzHabGYSyPQ5+47AkdsSicsWvQ23ZKT4Cc42zdCTscBk7+FFUv/ImcL5l0vYHWKg5T99I2uGaB1bYlPXg2jtCQQiP//P+B3d4Ps32n9LPJBRkF28wEbnwJ9vzvylY9o6VXVpGl1yWtR6oSo4QqKozQDOhN23OXOJMRb02zNxu6DtGyA64dg9m5R1aeSYHTsODODIObQZgpk0qTUlpKIXK0F1GVmhS5CF8ARke/9MLJuS6be9Z/r22DO3AmZ0UVDScKCTeK3JDQRj852tPI1FlWKCoUW0DHEmodFbkqCSlhLXXuVuREK60E6HicozJGq20B133qya/ivhHJ9LRcrd2yelwd7xVFhjpuKhQPAR72TiKphCW6yKMTy8YQtEzBhdETJn8oZwm1PCnRjSM9ZU8+qVIVM3cPRWJT+lJFcLMoc6yHZVWLCCsE1n1480jqOmXL0ddD3p9rogTW/lfhzk/APvse7PMfSsNXKvU2d7+E4WVvG/jFGQbe1IfhqmN4d7ASH90K4YObIXw81YTw7u9DNrXI9rQVcIrl3vX8pooKanejxBD+0f8F4+xfIiF0uHu+hbPuLrw7UIqPbgXx7kAJvor0wD3ww7R/Ch+7DlbVAI0EwI3rpGuf13J38qfyb1NzcGw7l+skk/KAwK4WhrMjnp7/2aBPpipJ0SITSoDa/ybcpIiC4UtgwXIpDG1Ea+7xxKxP/qf8Wyah7Htd+i5lrcvYGoy+5+BMe+1l7qlfQO/oByur2fRFmrtfhptRxSQowaF1BxJn3oN98lewT/1aGvfSvmTUNq+vh1AZzL2vbn5SbvlhUqJVMuKaqmEojjsl/mRi9D2bFli9aQdg9L/obWCZs1leB71tF3R1UXnXcMOCse+NzQKMLwi9/+W8MegKRSZkhm7ufG6zAKObMPe/BtdS6V6FsA0/zH2vbaqMoWM9nReMgFp/ivvHOy+/srnaOHVeVrH2iiJDVcwoFA/TByEpojC6WaOn9fSUNyMOm68ljUGpPSkp4ORqeeJUVZNqz6C2D2r/UMLMPUGR2M/v8Ix+yVOG2peoUoZEGV1fv4HWhQ3UdYDVtcGdGwe4A72mWVa+xISFw11MpjgFtDjsi59DZJi+EnxuHPb1U2jpewGlIQvlfoGpZQMXJ7LFOYrR/uS6jtd3VyLQtQ9aeS2E7J2Ow3r2B9JgkQxntapG2T7kLMxCP/p9uF/+EtB9OD/CMLGcfeM/v8Zw4hbw3LZKGF37PAPq6JqsMqEKFbk8JKDUNIOvLEg/AKPnsIyBtoWOeILjW7sZ5lY4IgmgpowhaAlMLQL9rQwhv4b2Sht8+ha03a9KTwGXvG8CpdDKq+FODsL0B+F2H5TVKfRUVWvvl1UiLlXOCAG9phXCtCDiEej73oCm69KHxz7/wSbDXD59G65hwdy2HyIQlBHbfG4Cxo6j8nshzxeqDqJ15E4PQy+rWv8e3YQUZbKMj11HJq+YJLYk462pl52SRKxnvgdO5stk3l1SBVZWBScWhmnHvRa2pBE3pU5JkWx5VpZTk0jkTg3KCPKUuEPx5G5NM6xjvyONvWkaWnWTFGw3xmor7owENzAeLse2oz+UJug8vAStrEbGkN9cCqBNdxEMqDYKRWFkCtvMCMyDb8njjdyPQ+XQymtgz47BIGHG3KJN9SnG5ibmRA0an/2hrA6l6xGtog4IlmNwtQSthg2fT60/xf3hRNbkud468h3w1XmI1UV5PaOVVsGZGYFm+FQ0u6KoUMKMQvEQoCf8JMpIEUV6XoTSlS+pKhrv7+XkcN6NBPnH5Eo6EFSBk9H2wKxAYRNMRUECFkPA8gSHXFBlEyUJuUOU2mFC330MTAvBufAxEFmGWVGPtgNvQjMtOCsxOBtEmfR4Zoel4FFX5sNqFLg6ntvEjmKpJxaB7qZucCsgY7LFwCm4A6dkdQb5kdgXPgESEa+66uC35edsl2FsIfcyLIYZ4tyEHluDRu08lz7xti3DglbbJo3zEhQ5zDn0tj6g+zAY51heA07d9k4NHbU6Qj7g3DCwHAVMHWiocNGbOA8dnUhQqgnFSwfLoVXWAUtTcC5/4i17VQNYfRfg88G5esKLjK6uhr73O/L9xPnPgPkhOS/azmMQC3OAHsmbYuRO3JRVMs74DZg7jnrzTsZ/JHJUNcokq1R7EQuWQKNWKPm5W7nTqGTS0zl5Q69RqTSljJz6FWSjYO8RGHXtcBbGgQsfesvz/I+lMENmgxRFLr2gSJBJtlwJiksnEYnG17knPQ0SZ2jf1Uq8+VHcHwmH4cKojgujITRXhVARbMfMHDCbrGBrrFS+PYqt0Zw4nJtfI0EJa5UN0Kub4M6OwLn0qTcAHc+gWoULGcF/cYuEFxM9jWUoKwdGZ4HpFapMBerKdCiXHsX9IpMaB055+2ltK/TyWjgTNwB6uCTbhVse9ywqFA8UJcwoFA8B8qmgJJw0yd8pHldWPqSGC2cLNfL3eERWLmSamonoivckPoUUZlTFzEODbrRXU6kTNtyLntiQKajJ1Amq+KBY6AKIjJSYtQKDLocFWK0n0lHFRnpWZrI9XEiQY0nPEtulf1nBeHC/4YPuOuApwYMudCZvZo9zbUlWllAL1UpkXTy6PZs9PkrK5oLJmGmqeEknQkWWwUlkzBwnPYUuq4VOhsapac/Pw/3wz7OHiyxDcx0kDAajkNgoOMUsQVBiFf2eSmOIhcEnNixP0kCbO4mC6U1S8EyZ6WQmtFw/iU1ZV7bnpSBcvr48rrMpnYSevJOwlzYAVjxQqMIsxfiC95NJMs1doSgMJbalWosXp+Bu9JqJhgGlpeYlM91QJgRueNBAPwrFfZN5Xp4dhTu7watOpfApigzlMaNQPARkNUtGaoGsiJHtR9kGZjK5KcOTIpXGk1kNI+gCMhFLV93I8dG4qCpH8XDQ9HX/EkrVKqsGK69dT+YJlq//XijtKCNFhm7TSwp4vVaEGHh0BZzimzd6p2SOjwxqmXfoNjNarypDQFcdUFO6IWVq5LJMM9JSvdhWAHr3Ac9bJpl4QFUjJMqQmFAWXB/ntjqgv8Ubt/yo4aUyGYfe9pY/JR42bINBFUQ9z6zPZ0k5RDgMYZhgqWqRinoYr/2x/EFNlzdcqAJcN6FFKMVs/Qk1tQppLb0ApZXJATXAMKTZsTx1pdKWTEu+RsuQnjb51sigJctr48q3LmmdpGKmMjxLWEuv5w3TtG7kmzL/Zbq27qtDBqLltcnpeeOhcn4lyjw8qNItxc5m4IVeoLt+/TWq6lIotoR8qNLpaUHvGJLZXphsL1bkpjTjXNZZC+xuXT/3UMUM/SgU902ml1j3IRhHviv/TbNVSp9C8Q1DVcwoFA8B2W+9wRyUPGIyneVlpDZVP2RU0KSqZ+RwyRvNtEiTGftLaTvxqHoyf4+QNwxVr8ysCARMhrrybI8ZWqfkx4JEHFpdG/jSjKyioRYVqpaQF/FJHxEuk5EaIJY2p3uwug5w3RNuSgJM3kh+dTNHQo8GNFUC7qe/kH8bz/8enDyJF6zrIJDwRDlKYNrZrGF7RRhaeB58ZQ5aeQVEWx2uzQdhJW9S7eU56c/i7HgJcfgwuShAi9pwdJ9MhaJJ3ZwGHC7QUctwtCOB5pIo+PwkRCSMnoZGiEAZRlYDoMAqMT8O3roT+o5j0CvrpcDIF6egBUpgPPdj2LGoFBwNEhWjK9LXRnTtB3MTcG9flClFVnc/xI6DAFUc2TZYoFwKjqxjD8zGbeArM7LyjOab2rfoSZlM+iivBdcM6Z0jRTPDlF4j9H2QgEYtTzRMet02dnnTzNHOROOgNiYJedT0PS89YGh87toCtJpWaF37wBcn01He1EZodB/0qqbIE2p5Rgo02vaDcKdve61nGfBETAqrfG5MtkGRcTQtz/14zFDblYiF4c6NyUhwSkGh40tqmyxmLF3g+W4X9f4I+PI0xOwyastqsHd3FcYipbBkaphSZxSF4YYPWtsuJCrasYJSLEZ1lFguqnwxmBMXvXOsIi8hCzjSbqO1NOr5oIXXsL22HmivwK2VEvh0Ot4qdUZxf1Dqkrb3dekpI8/Ls2PQSquhPf/7skpXpTIpig0lzCgUDxhqQ6I2i5RZbxofJS6t5IjUzkgRoZOMpmcLOMnfMytrZJUGtXPYcXUBeZdE4gKfXxdYTqftkrgFHNvOUF8u1g2A6SbXH5SpQCnkpWZdO4zGbenXrGAAdv9L4Fc+hcj0B6ppg9b7DMzA+s1ybcjGnmbg8qSRLvUOWsDRbS58jCNV/W1rQegHvw1x8YP1ljWquurYD1Q1w/3USzGCsNFXEUfi9G/Bk/HBchyGiZ0HvwWHV3hNT+c/QOLFv44LI8Do4vrF8oVxYGdjKbrqBM6PeTez3bVRNLFZJL74yNvGaLmHLsiKlI79ryMxswIMXQBKqmFV1sE+8052lKWmw9z/OmzNhPjyJzD6n5extHz4MtyRK+vr8tZZaE3dMEgwuv6VFDvsaARGbQsSJ/8y3SZF65wEEGnSaTtwyKsmvACz7wU45z/MbiViDMbul+FoJlKXa7YegHngTdjUjpaKWNYNGN2HIEqq12ebhBnqX//qF95+lQy55qZfVghlih5UhUPLQoa+mduGNCM2fFmiDJe+FZ+nI7PluiyvlYkS9yLOiHgU9o1T4JlR7jdOQu/cKz14aDmKGUt3UKcvIvHVO147SnLdk3DdcvBb0HzrlVMKRT4MfxCrbYfxybXs9jhdC+ClHS+izHSVvFcAU7PRYs4iceL9tOgtj9XBMnRT9aRPpeUo7h8y9nWcRI7zsg/GoW/DUJVtiiJDydkKxQMm3WKU0cqUElYyI7NTnh+ZcZ1UqZEaLj2+yKp3U575ZMBKpsOkbjQVd4TLhTTgXRdlPOgr+WJAIJpZoBJdlV4qGyHPF74wkf47HHXwwUAQw/WvIHHox3D2f0/+O1jzAj65FUQkOVLXdaCNX0Xb3HG80bmAV7eF8Xr3Gl6qG0PJxV9AS0SkoGHuex0JruOD4SrMbv8ubIq93v89RPf/GOf5TlyftaC98icy2tmCA/tShuCQwrFhn/sAJqIwD78N65W/hpkVhtHFzbcaVyZ1RBIajia1JsO1YZ9fF2XS62htEc7NMzBqvdYgs6peCipZooxcQa43bZfudgScQIUUJDNFmfSgEze9BKSdL8qKEjMQgH3u/XXvmtS0Y2twrhyXhRBG205o/a/CuX15k78LfZFk0KxlVBpFHANfztZB7P8OjCPfg3H4O9Cf+SEGtO24vbS+T9nhNbjn309f/K2/EYN74UPYEW+/pv2XUqIyRZn0aifz4Xh4/YV4FM6lz9KiTHo2l2fhjlwGz1ERtRVUmZQlyiQho+p8xsnFhGFH5faVEmXSxCOwL30qfbwUiq0IR118PSSyRBmCBPPPbwAxRz23LISZ2g83VCLS+YDOC24s4zioUNwj3nn5gxzn5bh8nd5XKIoJdeZRKB4wqQqHjRUzsjKGbsSotcEX8G6iyDcj0ySY8IXWjVqTxr/02cyWpZSvCbUzoICHhiKbmL3Z0DZTnJmlDjJZjMThjF7NOx536KI0vyWDZ0qJISPE8xM+nM+RQ0HJSQSPxyBGL4MlojBnBpEZJEq37e7kLRjd++WN/+iE12p1Ypi2jeztw1yhnn4G4/yHsJ79oUwjygmZSCeisIcmIXbW4sZ0fh3+5gzDgXaO7+/XwGenN4kyKfjUkNdClEpLmB3Ls4Icz3T3uR/D1E24V87mnTYJNkZ5DZyFac8PJo+ZHwkSBvnvUFSmY8OZuJ5njAIuRWmXlMN1XQzOABNLGiaWSADNfrpG33VThY1g0ARz4nmTzmT7WsqEkMSW4Uv5l2d8ANoOz2vHnR3OP9zYDeitO4HQnUfKUgWOI1vB8oxz+BI08kPKMA4vNqhiKG38vPE9EuoyzSIVijzYXMPcau6UvIRDlZXZPiqKbOTxfYOAnoLOC4bcDzOqgRWKe0Celzc+/EkiU04dEmxU1YyieFAVMwrFPeKM3fC8RzYgb+5IRElWtWz2j1lev9nbILikhst88s3ppLRRvEm2VaiKmbuDxJdUCE++FCNvQC5vwPOOh57eJMULRyYj5SfVssRo4oUSnJKVFrQ9xHJf76ZTZ0QqiSnPhfH6wAmgpUUuc7zAoDGbgXMBSneXN775oGVOiTbySWn+ZSdRiJkBL+Gq0HKTsTXnELS/kGhZCJdioWgeROFlT+4XJHLFnPynuTgFs6Tmd6t1mXxfULNYgfkksTRVFVdoG/L8gwpvOxthYotp0/TyiGpFg7wQLwCJdwrFFmyVGkTijAIFj+8F3s3p6aVQ3DV0zi+E2s4URYYSZhSKe4DaL5zLnyHx1V96wsnGihkrIE05s0hW0KSqYeS/G31oUq1NVO2QfPIrI7UzEpnkMHQHTeKMEmbuCkMDSgtYcNSWJc1/dWOTiWsmFHnu6hYStvCSj/INR/qcwcDpZp2Sniob8g7LatvhOA5s20ZD+XoCTW+dg/6GOGpLvZv46hIBLeVGQ2JGgeoIMpnVl0dg6AJ1pd5nKGGppxHY3uBVjBDtVRwaXKyFE2AbTKs3JUJRWx1BjsE5tt/0spfVQlw7CZfM+6qavM+XVEJv75c/qbQkWpfcsGBUN4FRvHbnHmh1HRDNfeCdh4D6Lq+yjLZ3SlKRH9ILpi1p1Y1SPNMh0FTuXbiFfMCOehu7GhKoDnnrsq5MwNBE2tQ3ndKyacG1tJcTk8vTmH/a9R1psZWMfvOuS0reSq3LO4WmXeD7IaNq+b0UMbRNS8hwuanb217qO73viJY9w+NHocgHJcxRghedSve1OHilO4ojHTb8ye7GMlUtUxA6vkvouNyy0ztW13Z4x1A6LxT5cUjxiKDzLm1Tmg6tcZt3vCePPzp3yuuC4vZUUzx9FG+9s0KRAT3BvjEJjMwJHOxiqCq5vyQj8oeQni+uAz55C9q2/evToqSlDf4y6chsSmZaW/QSmSj1JdeNWyBZWUPCTahCmgSzQNfm8Zk+iJgSZu4GElH2dQCfXdtcqVAVAkIZ53itpsW7wNwoftEFQuc+fDWoy3Sn57o5umsZbs5u1rl3NHKZnGSffR9sz+vQtx+Bc/KXXsXHBsFDo3aej/+H/Lvixf8TxzpiKHfnYU5cAtwE2qvakejZBtcsgW4vyeFcwycvVHJ54dBNq9BN8PkJKSb0NfWjuZpJf53JJSFFo+0NDE2hKKzwDPiFywjS06eGLpiHvgX74qebll3vOQxuBdOmusb2g0kPlQ3TJuGCRKOpGxBrszD2vSaTFKjCi5KL6Imq3rgNrGufF9U9NyrFMOf6lzJxiFU3Q9T14MJMCL5SF9vaDsGfmIdjmtCp1Y+Es55n4J7+zeYvubRaGlAmTr8r77rq+t/E810xlCVmYE5chuAu2mu7EG/qgO4PwJe8E6NYb7TuAkY2tymx9t0QejIum0Sk7YeQII+Zjd9joAR6Zd363yUVMg6cUqs2YvQclilWdwOtIxK1KHlqU8WQ6Yfe0Fn0KW2UwqH3HYPmD8r1QNu3VlIJ88AbstXLNQPqiZNiS3w6x7FuF9X6mmynFKvzKPOH0NyxGysogSHT9JT9b14sH0TfS1gLNODGfADROENNuYOujsMI2EvgvpDaDxX3DZ2X9b7nMo7342Chcpj7XgOnZFJTCYCK4kIJM4qnAuoXvzDi3UQNzoj7FmaGl324FvoxDrEzqJwZkckyWWa9G1uPktAJhSL/QN4wdANKwsvGYZJmwPJmLnnjl35KnAkJM6pi5q6pLgFe3MFwblhgJepFVXfWAr3NDIEN1S/WnpfhDF+WyTr0XbCKehhdexHhJiYWvWEGpgT6GjmCPoFrU7osgfebwK4mF01lLnD9hPS+EOc+Bva/AuPQd+CSAEF+GPTEp2Eb9O79oJqV9HRFDLWzX0uT19Stv7Y8B//4ZZhHvgf7ay8pinMDZmO39BxyBs95Qorpg96+C3pjN5xYzJs2xWg39ct9gLxrUnRXRqBd/xzO/LpXjLM8KwUGuvCxv/6tbLmh7dbYfhiipErGVhNiZdpbH3tegXvza2+7103oLb3Q2/rgwIDe3Autvh2CMTjDFyFo209NZ2lGijJkdkzz54yse/rI+R29gv5938MHQ+UYnDPwUl8QFeEZ2Kd+A2P/6xChKugH3wandUl+B1RF07QdRudeuLYNQTHWdAO2NIyqqSGI2ZF06pW+PIuQ/7JMdQC8fcv0B8Da+8H9IfDb572WIap869wHnZK4/OuqHe231jPfg331hDType9Ra+iUQlWmmTdFcZNg4AyelwKuTGErrYLRewSs5N68oehYQNMmg00SJQAGrbZVjlPLdZwoMlxmQNMNKXamX1uZgzt5E8aBb8HwqYoZxdZYlo7q1WnYp95Jt//RcYfM3cv6noUItinvigIkmA8jeicu3Fo/Zy6GDQzOl+DlvhCqDCVqKe4fzjQYlg/2mffSrb/kq8cnh2DuexWOkv8URYYSZhRPBfNJ43ZqERlfAA52UkTyvYkzK2s2zuqHwSAwaOzAgblfeE/5Lb9XCRNelgaceYWZ8QHwpen035uGodYUX1AKOEz21zIg15N10w+RmQCjuCNMg6G+AngpRP4wXpUsCSk6lZBkQCd/ilimyg6KNib42gLsS5/BaOxFQ/k+TC0z7KiOgn/xC3Q296Klpx+cbhy5DWP0HMS1EXljnpgahHbwdYiBU3CoWmT3q3L7oa9WkJHtqV9D3/0y3Gd+X5bXs3gYbo7kHRIL7FtnYex/EyyyBM4TSHz9K7CdL8A6/G3vBoNpsiUq8cVPYTz7O1KM0I79LoZmOdZi6xfLtMyVWAIyRJn0skfX5A2KeexHYGTkyzS4c2MQw5dg7n4R7NiPwHUfnHPvQatsgLHvdc/1hjG4K/NIfPYzGM/9EJzbcEuroc2NZoky6emsLcpqGb6Uw5HZsWEMfome2ldwacrCqUGGl3pqoEHImGv36hdgpgltD61LJqfNw0uwv/iZjLfmmgEYhvT2IVFm07Qp6Wn0GtC9D3qyRcoIhuC29XltbMl1SSKrYWSfKpmuy8hr68CbXsshpamZfrBUq1UGJM4Yvc8AnXs8oZWqfe4j4pPaGEncoVQuQR5CtOiGD8zMSG0rYihxSyZ0bYQSuS5/CnHouzBD6oZaURg3vAznyuc5PZmc6ydhJdsvFbmxhYELoyynd8/pIYbnt9sIBFQ1g+L+MJwY7Mubkw3pb/vy5zCf+R6gxHhFEaGEGcVTwcKakDeijZXA1DIwt0p+Ivc2rsnpKJgIoC20hpFIJXYxP8ylGejk70CGeFRhkDT63YiskOGul/hj+aWYk3O40kqZQqMJDhYIeW1QG4exfOCreRJ5FFviNxmyopEy4I7tCSOuDXfsmvzJhE0PoL17B6aWA9DsiIw95iOXoNNPcpj0ZQSZ1dJnaJjpW7IFxZ24sXmakzfh3/Gs/N25sTlaOs3UINCxB/b5D6Ef/aGsvhJnfotcWTQytStQAkcP4PZ89jZE/irmzLW89rNUNkzJYjZFQGcuu0uiz89gHPuxLP936Yda+zYuz/IcRHs/DLphptabQilGta2y6mETCxOo70jgEixZ6WNzJnOvpAkuiT2UwESVKBvHOTsGrbHL+/7mvAqfXIjJAfDWvrQwQ+i6DoTurPKEFdiHM9FINHnAwgm1MtLP0wYJankNH2l7V6lMijuAUtZklV8uyLCcTPpLNle0KjwW1+i8lrsqZiniHauVTY/ivqHK1TxJjTJCm97P8YBTofimomrAFE8F86uemR8Zv5IBLAkz98rUClDGF9FQ6sp0nBlfe7oCJmXsm9nOkImskKGo7MXptCFqLrSSKojVBXnTmtfklEzPElGIYk9heVxs8A/ZxB0XXCXb0bYaZ9ZbhaZ9N0k+VJXjXTxvnLSs2NlyGe+j5U+Omz6/1XS8yqE7GmXWbwUSoeR7NFIqSXpQ61LxRLDlV6a+U8UDYKtj41OOWj0KhULxFFbMjI+P4x/9o3+E3/zmN4hEIuju7sZ//+//HYcOHZLvU+vIP//n/xz/7b/9NywtLeG5557Df/7P/xnbt29/3LOueEKgGGB6gtNZ50URl/iFrKC5izvrNC4XmIsH0SqmYJlVCBguVtAEvuBVDHgx18lUghxQ5YvesRt84ha0pm15p8PKa5Iz70Krac09DJmr0tURPTEokI6juHs0Mpxr6gYn/5Ddr8MOUmsag26vQbvyEURFE0aXk5HlZIarG9IzxG7ZC2H5ocXDMEbPy1YzYfpg7/+eHCer74LwByFa98AVmtwCTdjgJ/8KWmM3Ign6ShkCDV1wx69B2/0a7NIGKQDqThTs+nH5vTuGH85zfwSdOfK71xu6EGs9AMF0MHBYU1cgbp3xBMLIMgwRQ3tVAFcm159wzqxqsBt6YcwM51wHNE5W0wLruR/Lv+3RK8DKPIRmwHnur0FntvSIYb4A9M69XisNVcdM3Qa/fQFaRS2c4/8b/JU/kuvSSYqXm6bT1A13igyBN0MpVjMRK52qZGqQ61LXTKDaM2cmz5/k0LJCyD33DozaFjinfyu/F/J94dN5xl/fLZOeKDVLVuFoBlzdlK1ksgWKMegP4GmcnbBhu8zrZNI4/Knol/sZpyNkdHoqYcbQi9v0NwX5H8lEjlxVM3QcVKlMijs0kZbbkm7Cad0L7i8Fs+Mwxy9AkP9VDv83xTpVpd5z3fpyoK2GSa828vIjDz/63WBKuVE8AKgilYI2clVC0ut3ULGqUHyTeKKFmcXFRSm0vPLKK1KYqa2txcDAACorK9PD/Pt//+/xH//jf8Sf/dmfobOzE//sn/0zvPXWW7hy5Qr8GWaNiqeXaALgAggm74VKA8BcdsL1HbMUhjRpLdfJ26UKJaaDRVENsTgrvUKoygX+oBdnnQetrEb+FIJSnSh5hMaXy4dGDpOMCSQDYGo5UTxYWHk97KN/iCtjwBj5tgpq/wlhz+7vw0IcE5e875gSKboO/wjjqyauTPsQs4Ggrwb9HQ2oCyVwZT6Ea5Ma+puBru1HEHFMnB+kqi3vYraj2kTvM78DXcRxcRSYWBT4/u4SuM/9NVydEBga1mTffnVJEPt630DITOD9qz65XX9vrw7nyO9hKqzjyg2BcJxatDT0NO5G8/O7wGKeQzH//C/Q8eKfYHgBchiCPr/MqlBd2QgsTmYvvD8khZnEl7+QZcSstBpGzyGgrR83F0O4MArsbjWwfe8rQHgFzrWkAS8ZD7fukGKOS+IJiZkf/U9YL/yerPyS+0fmOg6VSz8XsbYEN2nWm4YMXruexY1hSxbuHO4SGJzVcG2yBjWlwPM7nwMjIebCR56RMsWztuyA8eyPwaNx70KOfgyfrE7jC2SUmwGJOu194MMXkBi7LsuiaT4xPQR76ILXFuMvgejaC626SXrF3AuRqIsbU5DzTt8jGY/va3NQ6nNh3UNvPD2MWI0BF4YFJpe8oqaWKqC/leLPi1+coWh1rfdZ8KufZ79BItrOF7w0MIViC0hwtfe9jbmIgYtTftkq6TOB3oZatPUm4Oq6KikvgMkcvLLTM8E/Pyyk6T1VJfc1M1QEBIJB5S+juH/oIZTR9yyci59ses/YeUy+r2ymFcXEEy3M/Lt/9+/Q2toqK2RSkPiSeYH6H/7Df8A//af/FD/4wQ/ka3/+53+O+vp6/PznP8cf/uEfPpb5VjxZUBUCQR4zBLUzjc4DsYSQ8cl3w2LY87cIGd7T2hLLxUgsJJ+EkycMX5i857SVjWjU316oxz3pLyEjs+/RL0eRnwgC+OSqkAJGipkVho+uCLy2y4fmSu8GeVsDw/WpEG5MrW9L9OTw5IgPu1st9DRw3J4DWisZIq6JD694lRME3ajfmtUwswq82GtJY2rCYRY+vw6sxNZvDebXGD68Ary600J3PaSIQ+a0YwsaLo6uP50kYchLX2Loa6yCXlIJlNYiwFfxYivHeCSI4SVLxmWTD4C+41mw1Tm45HvkOtKbRauoR+L8B+nebvKSsU+/A3P/G+isLZHCTGc1h1hcgHPh4/UVZMfhDp6HWFmA0XcUnKZN/i1CyOQyqihzp4dktwl5MjEyyeYCrLIRRlUj+PgNz0i7qglOYx8uTofQWOaipzqGQHwJZQ11uDZp4mAHwKJrcL7+1fq0XRsYvghncQoGGeNSCyClJVFkdUsPtLpWuJOD3jLWtkrTYsZduAtTcr6NF38f7vBVuMMX18dJBsFXjkPv2gveuhOG/+4E0GjUxuc3NCxH1y8dF+T3yPDqTqD6HjQEEtY+uCSkcbX8boR3PJtZoe2SIt+LW5zRyVC6vB764e/BvX0eLLIiI9IpNp7snBhoxaibQkVhEgkbE5EQTt9e31/idOycsLBim9jd5KitqAACGq5PCkwsrq8/Sjk8dUvgaLdAid/ZZJquUNwtunBlOqJ55Ltwb1+U1xD0QIcqz4XreO8rFEXEE/1A4Je//KVsWfq93/s91NXVYf/+/bJlKcXQ0BCmpqbw+uuvp18rLy/HM888gxMnTjymuVY8qcIMPQ0jSpKFVAv3EGi0GBYIilVolld+U2I5siVl1VcvDWIp4lorezDCzJZIYYapyOyHxNRytiiTgsQUqmTpaxZoqWawuYaBDFEmkyvjDLaryTY6w3Bw0Uvd3gQJPCT6fX8/8N29wHKURJnN46SPnh8F2qu9ixFbaLg6nrtkfHCG3mfQ6jug9xyCM3gBxumfoWPqAzwXvIJj/ktoHH4H7omfyjEb2w9Ba98NraYN9qlfexUjOdJKdNszaDLdsPw7F5S0RKKOsftlGPvfkkbC9rkP4E7fhlbT4pn9zo3JyGN39ApETStEIg591/PQ6zukUMImb2CPcQO7o1/Cd/on4Jc+helE5fiDLCojx3OyMitTpbDnLUR3vS0FU/vCx3BHr0OravTiu5dnYZ95F87NMzB3vyQ/prluThNjwr19Cdo9mMquxOi7zL1tnBthiMUSd91KOTC5LspkQjeV4wtCPrAoZqSJ9pc/gXvtOLT2vWC7XwNr6oFz5l3wr/8KeiJZEqZQFMB2WM5UIeL2LEOCK1GhEHFXyxJlMjk/whC3i/s4pHg00HmXju32uQ/ldYPRe1heQ9Df9Pq9nJcViieZJ/rMMzg4KP1i/v7f//v4J//kn+DUqVP4u3/378KyLPzxH/+xFGUIqpDJhP5OvZeLeDwuf1KsrNxjX4viGwFVL1AEcSoOmSpn6O/FNYGmyuwLC8cVMrWJYrVzeTZQEkHIXfGMd0mYMb07pNWKbSib9iJc2RZtSg8KGfdNEd2UUlIEPEn7ZcJ2MbmUv/JgZgXY0cQwNS1QV0JWs7mHJREn4QhUBKmNhWFmNf84x5cYGpJdmhMbum4yoRYoLrzxUPm4wwtXV/hK62DSzWyylUcsTkFf9I6PqUtnPnETWu9R+WSKz+b2nJHDR5ZllYm3cA5QQBTkyzNw67fJuEs+P+59fmVuU/oSn5+A2bYTidV5zz/n1ln5Oi1hVokyTde2079TFU/eac+NQ99Wh4DDwWe9VCYSTd2hpezhFidgJM2zBSWq5TPSpumRl9NdMpU9uSyocsbld/dsxHYg25fyMb7oeWmZRvHtkynSSTqrC+Bf/2XupA6FYgvInynl0ZSLtShHWejJbJJ4EvbLQqlM9EDDcYu7ck/xaJDnXTovJyJwLn+e+32Fooh4oitmOOc4cOAA/s2/+TeyWuZv/a2/hb/5N/8m/st/+S/3Nd5/+2//raysSf1Qu5SieInERbpaJiVokM/M/AY9g57w/OacwIkbQraC5HpavRJlnjCTrJgxNAGf7mLN3witshF6z+FHGmFLUb2yOqAIeJL2S40xWAWuyeV7QmDBXhf88o5L8wQaGqrQOP1GUiAQJB7mf9pIouL6fBactDfs2JD03yi4XdJ7gnt+RWaBkFMSA1nytFHAR0kOavohXFcatUpj4LzTtqRpMahEOSl45oWirFPzkSNCPg3tF0LAFYWXmxm+dVFNK6xmsNS07wJfgVGSv9Ddhl5JLbbAOOm91NdTbPtkluFjIQptFwoF7ujwBcN4coWFJ2G/LHQcupNzk0JxJ1BgxoM+LysUTzJPtDDT2NiInTt3Zr3W19eHkZER+XtDQ4P8d3o6O+2D/k69l4t//I//MZaXl9M/o6PeE1VF8bYybbxBIp+ZhTXPpyjFwJRnYNdaDdya9ipqMlmOUIUBQ4ivyBu6FEHTxYptQe/eD628Fo8UK1A0wsyTtF8ahoau+txXllRxdaDTa2E6up3BNFnav2gjJABausDYgpD3/dtq8z+iba/RcOo6cPxroKU6/6F5Wy2Hnky8IOGlsgQ4vA14fTfDyzsZXu9nONbjTVvO19wNcO5Cb+3LO056z7l6Avz0b6FV1gPU8vPs70J/9negH/k+jOd+D9q+t6DVdchUpje3r0LoJrSa5twjJDGGWvo++//Jdiu9dWf+abfthEPGvcszYMESz3h42z7pZ2PufRXm/teht/SCVdTLaRL0L2vKn7yn17ZgcTGKEzcZtOaeAsu9A06yZYtRSku+mPtgmUxxuVuaqvJ/j121Lkz97sr9fSZDT2P+Ox56z3iAd0RP0j6ZglLAUF4D99k/RPz5v4G1Z/8G4i/8n+BHfgesgnoG7z/xSlH8WBpHVUnu/Y+Oq5QC96TyJOyX5UHPvD4XDeUCpl6glFOhuEOEaYGVVoLvexvx5/4Ea0f/RP5Lf8tAAZXCpygynuhWJkpkun79etZrN27cQHt7e9oImASYDz74APv27UuXdH711Vf423/7b+cdr8/nkz+Kp6eVKeUrk4JuWu05r9WD3qMWpptTQGMl0FkLzCwDt+cEKktYtvEvPI8ZmQCTJGi4WIyZj+0mhTw0ioEnbb8kwa23kQwOM17zAUe2MZy77UWwE5RE8Uw3w/HrIqutiJ4o0uuu0DG5CCzU6uis55he5Zhfy76i3dfK4dNcjK542xH9vr/DwNkNKc+VIYGuBg1/ec77WwcZLTJcGhXSdDEFRZg+18NgCUe2K7nHfwLrhd+HVtsGPusJ2yn09n4If0gKI4RrmDD6noN78SPwlfl1oaWtX7Y72Sf/Er5YGE57P0z6O/xOtjjINJh7X4GjJb/LT/+/YDTt5h5p7puJ1tAJVl4L8fH/kH/b4VVYB9+CfeULuLfOraftNHbD7H8RM9GQfOmjQQuvde6FTRHclAaVOc5dL4HrBkJrI6gKdEnxUu/aB3fwXPZw0m+mA87nP5F/O4mInO8ExWw7yZYpwrBg7nkZ2j3EZvt1B4c6NHx9O/upHqWW9DRqMAuVUOWhrsxLYRrLDrhCd4O3LRbzPkm4VhDO3u/jzG2O6eX1bb6tuhy79n4XviI3P1Y8GPwBC4e7OD656hmmpyBd87keEkHdJ/YS+UnYLw3dxbHtGj6/ke2bRufIfR0Mfr8SSBUPJj0tuv+HOD8iMDG0fmxvqqzH3gM/gM//RNcXKBR3zZN51knyp3/6pzh27JhsZfr93/99nDx5Ev/1v/5X+ZNqSfl7f+/v4V//63+N7du3p+Oym5qa8MMf/vBxz77iCaqYoXjdTMqSQg3FZpMwQ6km1G/eUultVzWlAmPzwL524Xm5yJ5qgaAWh24aWS0IIdPF+FoADqen1Y/Y8M7yS58PwXnBiG7F3UM+Lk0VAq3VlHwkZDtSZx3DZ9eyTYEpiYJa317ayTC/Sn8LlAWYvEAdnuXY3sCwvdGrbFlZFTjaBYQTXMZik3jTXKWBCRcODLzc53mIONBlhdbzvQxzq0Jum9WlDK7LsBR28XKfwPgCA2MCl0d1uf1mMr1M6RgcR7s1sNZ+z2w3HpXVMHpTtyfmUWIRJSHR75SS1LkXEC4YF3BO/ybb/Jc8Vm6fB7f80Dr2gF/7AoISkEwfzIPfkjHYNB4WKJHGfE5kFQa3EW/bDRGsl7HVekc/jJZeaQBMV/Ikisg2IzL63fWyTIbSg6WwKf46M1abWpImBmR8dk3XfnTX+9BT50IsTkLvf1n2nrtz4zIyXq9pkfNB02bOGnZULkKIoDT8JVNhOW3HhlbXJmPtKeHBOvZDL01N0+Esz8N65vtyHBT/TU/kKKHKmZ+A4QtBu8tUJsvvQ3NFHDW7NYwvcMQdoLGCodQvEMhXZrUFlCS3vxPobfLMfulGsrmKIWgBlln8okTc0fHVLS49ejIZmadjt8DuFo6AX5W3Kwpjx+PwjV3CK62tWHRCmI+aKPO5qA3EYI5eAu86+IRfIT9edNdBxdhJvNW9G9MRH9YSOmpDNsrZKszJGSSa+2Bl9pArFPdANObg7DDD1AbPPzKepor3A+0OggG1oyqKhyd6az58+DB+9rOfybLNf/Wv/pUUXige+4/+6I/Sw/zDf/gPEQ6Hpf/M0tISnn/+efz2t7+F37+FV4HiqcB2vQSTjf3QpsFQHvBaTDrqGIZmBSpD3k0PUVvmGWnOrXq/p1KcShCWLQ8bKyuIlbiOqoCDRwmzAt7jKjJhDXhtGIK7cAbPQ69u9tpSFHeN67oYnhW4OqlB1wV2NgMlhlc1lSupiV7//JqQLU4Ti1508Zr0pGNSzNnbzhCJOjg3pkkhp7HCu7EmM9cPLwI2TOxvd9FekUBlsw+jcwKDMzoGZwSqSjw/ktF5r9WuxK/hpV5XCnEJ7omKuaB47bjLcB6Hcaw0AX7pYwgy4aUWpLJqz4Nl5Ir0lqHOKGrFQzwBHl7KmchEiKFz0I58P/03v3UaorQC9uwYzLo28NgaEscp5QkQh95GpO4QykMJODdPedUy/hIYPYdlFYx98VMguuKlRu14FudjndjnzGaLMpnfyfgNWG07sbeRy5hMe+Brb7svqZTbuggvwBnwUqL47pdh9hyWcbf2zTOeobBhwNhxDMwwYQ+c9lqnKupgUnJU205wEpeufQH6erXmXrmOSKBJGw5WNUox524hcYaOGDseoJGoP9k+V5VR0fe0YLtMtqHmYmSO9isND7hwSFGEMDsOcfsCDHEOdYES1AdKpZEoCbLyfdl+eff7+1MDVUlO3IA5cQOtpdXSR4yPrchzh2xzre9cj8JUKO6RuKtjain3A08KaLBb1QNJRXHxRAszxHe/+135kw+qZiDRhn4UilwRsvmM6mrKgKEZYGJByEqHvgy7DGoJIF8aeiJdW8Zkq9NKBKjG8iYPAxJmqMVpOW4+emEm6YlBN9N6UpihNhC6CXaHL8P3/I9lJYHi7uCuwGLUO+GTfy3FXJNwV1eevyKKqiFSiU2ZkPhC0CdXvbRnWRWzMV2H2ps667wI9Mwo9403oST4CGi4MUktLbTl5Z+naEJgF9keuY5MJfIWyN7U/kbVKsJxwSwLYjq3MOItTDw7uYhEQc7lBbo9kd2mJNaWUNrYAGbbEGvJccbW4Fz4aMNwi9AcGz4y7E0l7uSCUpmoxYiEJCpZSyVCrS3C3dDOJFYp+WkbuJOASLVjOQ6cS59umkc5/6llS01q/Dr4eI5lVzx2cgmjKWhPyBUlrlBsRCSPJfL36Nomrzb5d3n1Y5q7Jx8eXk7/Tgl5WWch1/ZS+xSK+6RQchqRUMd7RZGhpEZFURMrIMzUlnoX8sdvUOuJ93cKuvGrLvV8HKiygG62adjSxNymihlK1SZxZjH+GHROMsLU9PRTPhGPetHHDV3ywsidGnz081QEaDpDuX/9jN9R60Woh3z5KxTIMNLQgd2tng9I5utynNT2lizkK7GAo93UKrc+XEWQy2onSqOrCOYXW6hFirbG8qCXCpaCtnF6LfMhJVVWfDaU9IgJJDdwMwi971loPc+khxOhSpl4REIGK+SlQts+JShlryzAR+1CHUCG+TULlSFKCdSmCRZIjVOH1tILrWVHOmFJGuvqBpbJwymP+a43IJNVLzBML3qI2vjkgvuh1bWDZVSHsRIvd1wjQ9+SivXXg2Xee8noIhYsXY8PydyvQ+Xe8gQz1kWhZCnFIyPTuoKO281V2UattA8qFFtBlXPpnmRpMFolj2Pp9++hOu5pQqNjZ4raVulVlj5e0vlGf+Kf+yq+AWSmUN7L+wrFNw115FQ8HRUzeu6EE/KQodaTtmpPjMmEfGnoPapYoMoZ8nAIhhcAs23TuMhnZmmDAXDU1nBmugwd5VE0lz6cp+00z+TrkRJmpBcHXRc1dkFEVuDOjMKgCyZFFtRWFLUZ5le4vNGrKtVkhZSZPMvruu6JMSUJVPnjcBemZMWGU7odlqHLlqJM2muB/Q0RiPAiKuMr6KqtAGsvR1QLySf8k+McIZ+Oo92UVsFkdc3sCnnMMLy1h4o2OHRNQyTOYDhh1JeXyPYl8rXZSF8TsBrX0VTp+Yu01wq0lcRQwpfBwosQgTLErEpcnw/Apwu8sENDhPsQ6jogPVIYd8DnJ6SninHsd8DpqTHTwNYWIBYmIBq6AYqttmUvVhasdRfEynoKHhn60vZHxrx8ZQ5GXTu0kkrYYzekEOTGY+CRGPSOXWAkyFg+iIVJWWmjP/N9CNuW1WaLiQB6mhmYHvSEmsiGsiNpFLxNRlq7s+NgZTUwuvaClXpPtPnSDDQSaHYcgzN1S/rCpNAbt8mn3+StI/cT15Gfp/mledWCSRXN9IG19sFs6YWIrsoqNLOxG8wfgjNOHjemFGlTx4lIXEjhd3bFEwOo5dFnCPjM7OcdbiwM5thyHoVNPj8NYFYw+8bmLhHUhhGPJCufyCuIxhkoHEteJFDKGSWT9ddFoIUXICLLYM3VcPxluDYfginFSnW1rigMN3xgzb0wKmrl8Y8qQGhfJ98rub9bSpgpCInc2w97Lawr8xCxNZg7n5UVuvbUCDj5hykU94mlc3ktPre6+aEYeUHS+UAd7xXFhBJmFEUN3TixAk9RyaQ1X5JJRRAIWMDFUSGNWOtLXGBBADni+UosB7eXguDCewBPHR5fT5VhLmpJY7wX9AXUBjOiHx4kgRLw1aQwM3lL+mbI6N+KOvDRa9KPQz29WicSdfHlLc+DJXVCl0kc2zmqS920OOPXEvCvDcE5fSL9WX3sKl7s/w6+GLJk2hdBT+wP1C7DOflrIOGJGbKOxR9C4MDbOHG7VPrK0Kvf2stwdphnGNlRADtwqEtDXQnH5WkNFaFSNPmFNP798qZIi4ukB3TXAxUhhg8uifRrBxvC0qw3sxS/xPTj6KFvwdUr8fF5b9gf7ymRXis8Kd6ll2n7IZmO5A5eAZ8ahNbaB+PQ23DPvZdd3t/UI2Or5XLSOqvrkOKIffb9tDDojdCEeeAN2LoPgbGvwSevQ3vhD4Dpa7CHzmdPu20nWHs/PrrgrYvv7w3A3Pca7AsfZ41Tq2mFsW0/ErfOwWzslP401sE3YF/8BIKSmTYmQumG9HUhuG5JMcQ+817qm/HGWd+ZFbmtkcDUugOJr38LJLyeM1kz5QvKpKjE7CgsEkBKqxCOCZwb9kTd9KThxag3V3L4rGQbXGwNYmkG9oVP0m0TNE4yXTZ2vXBP4oxIROHcOuf5A234Ho3WXjAS1YqYkoCGvTXzsE+9A57RXkZC4J4Db0Lzr1dIKRSFvJ94Rz/sM+9mC8GmBevAt+BQRY0iL5yE/YpaJL78pde6lDy2UUWiuf91aFbxi8SKh0/Qr8v0tJO3RPKazaO6ROBwF0NQpTIpigy1RSuKGhJmTGNzNcydQJ/pqvWeiJPgUh/wPC1yPZUuMV1wMCwn25mmwhZmoz7srFmDX3cxtvrwbpZYsDydikP/0k0fQdUAdDOY9thQwLZdXJ+kE3z2oY++3+MDWloEIbR4GPz6uigjCS8hePGXeLkrgtd3M7y8k+Fwc1SKGClRJk0sDH7pIxxp824e97RSa5zYlC5AUsGpQYGE0NBWRVHc5JOh4extgT1tDMd6mIzdpvhr6remcaRapXqrInBInNjgj0DVLvbZ96Db3us/OEBVJdObRBnClSa6UfCWPfJvw47BvXES2p7XYBz5PvSDb8vKGhJH+OAZmEe/DfPAm9B7jsC5fjJblJEjtKUIYroxsMnrwDM/AIsuw90gyshBSVxYW8R393p/mzyCxIWPpABk7n8D5u6X5LRYWRWca1/C3LYXzsDXMI68LT2UskQZuTI57PMfwnDWjUiYHYNz9YssUUZ+59ND4HNj63+HV+RnU6JMmnhECkVWTTMSZ96FG4tifMGrptv4PZ4eEojY698vVco4Fz7O9uWhaS1Mwh27Bte+e7GWL81uEmVS36MIb640KjaossE+98Emzx+qcrIvfwYeLeBTpFAkcaOrcK4c31ydZyeQOPseDHvDcUCRBR3f6RyTEmVS0PmAzgtUKahQ3C92ZA3mxd/gmaZVvN4v8EKvkP8+07QiX3fCajtTFBfqMbqiqInbXiTxvUI+M7tagPIAoK9GIDtYNnjMEKWWA51xTIV9qPQ7uLUUlK9V+mxUBxKYWPNhX91qVsz2g0JGHo9cQeLkr6TfBku1cZCnCJVor8yqdKYkCUdgaC63Hk3izNwKR0lQh0v+PGPXcg5HBrXGpXdh7X8LZlkI9lJM3hTmHHZlHiGNBBsfGioYPr2W3zuGUpfIx+a7ByDTmKjK5tSt9coYqsIiaHsmwYaSnxiZ2y7P5B4hXRgnoqhDCXRnDc7w5bzTdkevysQi9+X/A3xuRKY3uZTgRGgGwJO9W/SUtGO3FCgsaoOaHckzQjL8XQKe+wMYhg73ypn80x6+BLO/Ch3VQU9gWluSIoy34FqWqGG4h+Q61Zw4EpTylAshwOfHpTBJ6Vp87Hr+aY9cBqtugR4qBZy4jM/OOUoSn8gsNBaWSVcD0/m/x+E5SnjzdnR3ZmT9i9s47dFr0Jt7ALOAp8/G+bDjcHIIXCkcWpelLxZ1hRxVDOVNDVuaIfUVKpZJsRWyvZDaKnORiELQNlbIb+spRx7f6ZiYAzovGNsPUpP3I58vRXEhr3EWp6Cf+ok8rAcyrkfkmdUlgV5tZ4riQVXMKIq/YuY+2k+paqamlMl4bYrSlHfI+uYSZ2qFqQ7YsjJmMWZgJuJDUygmB68J2DLyb2GDB82DgnriU2IM3ehRjLJ8XdOkXwdfpoQaBUEBPLl8W1JEkoUW3OFg8XDhm8PUDfeGJ4abJ+qZCMsgIafwtKW/rQ5EN1gSZd7bk79NujVvq+QLO4Gd27wFl/Ocj3gEjNvQNM27Icmafyd7WVJCifw9v0BBHijMNOVwhaZNhtWMczRQgdfG4TZUmsiILPm6KLjeRcyrbhPClfNRaNoAv6N1SS2BqUlnVlZthL478gySFJg2ZFVP/vWXE1rncp4LLPfGdVZsbJWOlbm9KhT52PLYudljS7FOoeOql9an4nIUDwDHKXx8V+lfiiJDCTOKouZ+hZlMpDBD6Q15ql5qAgmsJgx8OVGBkOmgNphI+89oZHAae3hPsfXuAzAOvgWtpiXrdUrGETmEGcG5ND8VdoHs2SKEDHVLCnSV1ZR5X67psyCqstdlJqy8AUhWJTBKxso7oAaR9CSyuUB1gdCh+nIGlzPMrVAsN0tXx5AJ8bZ6L66boH9TsdskyslUpHwEQvj4FiAMC1p5/qopVtUIh/ngrq1Bq6jLP5y/BIJSwNr2eOlIqWSkXMOW1UDMjkKYPmgVXntdLsioV5gW1lYcr/0uH1SplkpkYjpYKL+XCHnKyI/Qclc3F5h2nUyEkshlybNzk8m25UtvQ4W+x+ZKJoUm4drptsKco6QUmGQ61B1D3lEFxqnVNKe3y2IlnS6WC9oXclQ0KhSboO0kx0OWzBZhBQoe3/NCx9IiPw4pHhG0LeW76KbXlcm0oshQwoyiqKEn2/fTypRFIropKjuTKr+NppKYfAbeXRFOn0uomiZkuVh8SBUz6XSmHDfo0n8mspJ+2p/CuXUGiRO/gH3pMzxNBAMG9rTmrigoCwiUZJzj9bo2L51oI4xB794P0+9Pp3ugsSfnOMnYdnzNG+7iMNDfmvsCg0ym6Wbf4eQ344kv+9oZ9nUwWSFDbU1NlZ7fzM4WJludCMfweTGlOSBDX6F7CzS04IfRtSe3EGD6oDd0QXz8Z8DJn0oz6VTa0Ub07QeRMErwlTiI8UgIxrYDuZe7ol6mBOHKZ3A//Dn0lp7cN0GaLhOb3JunsW3+fdmqQ142uTA698AVHHrrDtmiZPQcyj3tUHmWaCPFCpqXnN/jARj+pOKlm9Cbt+de7pYd4JoBrXGbTHPbleN7pP38hc4oGvkI7PPvwz77gRSyqGot5/JsP7yeCHWHUIsStZLlFOMMCzqlSN2t2PMNQ+imF2WeA72jH666UFfcAa4vAL1zd873tNo2KWYr8sMy26Y3QOcF7iugXisUd4gwTLDmvpzvsZY+tZ8qio7ivoJTPPXEHqAwI9ssciQypSAhZltFBIcbllHmyy7jLTGdhyrM5EWmvgiIZGoTIQSHS3Gg0oR0XP79NFEdEni2myPoW//e2qs5nu/xhJsUrlkC4/B3wDIqLqjKwTj0HbjW+kWn0AwpWLDOfeviA7WXbT8M0dKPyxPeTfQ8+fAKiq9mKM3QCRorBF7sY/AjhrF5jpd2eF44qzGBkze95B8yoL48JqQhMIk4TnLzujptSTHB2H5o/ckRCQzt/TC6D4IzQ1YInRsBHDME8/DbYGXrogtVdFiHvw1bW58hwQXMfa9KESIt5PhLYOx+Cay8Dn91lsn5+fKWhuVgG4xdz8vkIm+EOvTmXmnaS2bYlJDESk24ug/m4W+DJStZ5Losr5Wv0TyK0WvS78E+/Y40/tXbdq0/cbX8MHYclSlKmBqSwot7+jdAqBLG3lfXKygYg1bfJU2DXZYhXGiGtzwk0KSmTckhe1/NEt6E5YfeuQd61971qgsSO7bth9a+C2J1CUbvEVmlVOoXeHFHdqLby91RVI58Cvfc++Bz49LnJnHmHbl+5LwnlVoSaih5Kp9gsxUsWArryHfBytefWGuVjbCe+a6MLi92XMOC0XPYEyTT+5tf7gN6Uw/MQhVsCkUSkwTpxm4Yvc+sV/7phkyKo+ONrRV3utn94mgWzN0vyuN9Wij2BWHsfA6sugmGoSpmFPcPMzR5Xmb0ECjjvMy2HYTesQdMpacpigwmRAGTgKeElZUVlJeXY3l5GWVl93axrHjycLnAT08K9DZCGq/eL4mz78vWh8wbvDtlOmzhxmII39s2C1N/dLuc4C6c0+/C2HkMRusO+RrdACdO/RoaVQGMXYN19PvQymvxtO2XkagjK1Q0Rh5CAr4NCt7kosDFEYGjHXEE9IQUVRxYODvplzfkfU2ArmtYjXJ8cAn49h4XzIl5vfWaAWH6cXtOQ2Mlk9MxNAFzbhCaoSNR0Q6HM1llYTAO7cqH0Lv2wfWVweBxLItSfHg593ZCrU07m4GFMEODPwx++ldgde0wGralBQp3bgzu0CUYz/4ACZjQDQO3ZjXpf7K3YQ2a7NNmcJiJEyNBdDcw1AdiEE4COlwkBq/A6DkIjYz1yKdFMxBmpXhHxlpns72eY3ddGIyqsjQd3LDgnH0f1u4XPaHlme8C8xNwxq57AkvSA4kEIHvgFIzqJriTgxCr8+uVLL3PQK9u8frJdRqnH4zep9a8hC29ayj5g7Zbra4djCenTdv72fdh7H8TRpnXFkXrwj7/kfRfkibYQkiTYTI8psoLrWs/dBpfeBXOV7+QN2Z6batn/8IAd3oY7vgNGM98H0YwW/gIx4UUyeh7DCwPwzn/weYVpBtSBJICEvntMCYNiWldm33H7vnCklorqcKIZpLarGRb21NwrpTf04lfQN/5LHRqByNhmWlwFiYghi9DO/htmKHiF6gU93/8//S6hmc6Ocr1sHes0XTEmQ8fXPbh5d0CJYEH1AddhPuls7YC5+vfwjj8FrSUp4yuw45GIG5+DW3PG7CCSiRV3P9++t5lDd/enXl9pUMYfvzmko7X+lyEgkqcURQPStJWFC0pg06Ky75fZCsQmXXe481PiUUlDgxLcQO1wbuPyL1XqL2JnqKLlXWfGXd+Qj5x0OrbwcdvgC/NPJHCzMMmszpmIwmHY2gWWI4C71yl7zz7e1/0Ae01XuVLzKYYa4FfnNVzpgPUlAEfXBL44Z4I3OtfgLu2PPBunDoPlMDsPSLfGR3NL96NzAE7mhi+HBD4UV9Cigx0Q5rIkbpERr7a4hoSzV0YngPWYsDg7OabVl3jqOm0oPl94BNXgKnrcKbW04zCB/8AH97MPT8D0xraq4MInPjz7OVZnoU48BYY+fRSgtLSNJwvf7Hp864dg1bbCjclzAgBl0SX3QHYFz7KGtZ69of46dVK/Gh3GGJ2GO7MbbgDpzaPk1JByiqlCa+sDnMSMv2JfrKGm7wFjdqszArP7NOOw711Vv5sgjymNggzIZ8n+JLIYo9ujrD2JuLIiG8SkLLGS/5D3QfvWZiRrQQFPH6KFWlO7cbhXvwYbp4UD4ViKxIusBoD3r9KQvFm36K1KAkzj2XWvhG4dE0RX4Xz+f/O+b7m0n6oVqDi/og5XuDBz/NcX1FKospkUhQTqpVJUbSkEnCsu3zoxRen5E1lFqm0mHu8EQoYLhgEluOPQQsNlUvxJQWfn4BWWuV50vgCXkSxIguWjM/ORyp0h9iq6DD1NgkUBRNzMlIsCk07a3JbtaHRwOSFIwoGKIEL2jrF5oXLNc2t5ik9UhdMp52PF26Xo+ltNPejEeYy/EtPaKsFSiVH8S3WOb2XnM6WxaNbfc+F54d8oLI/QM1eirtmy9bLp74IWPEAULXkW5DjPJFJ+nyiUNwP93daVii+caiKGUXRci8VMxQB6dw8I383ug+k011SEcL32i4gDYBNF8txejpeILb4IaCVVMCdG4dwbK+NY2UWrG2nfI+euG+KR35KiCa4TEEigpZIt9gQpqGhrVrIdqZcNFeRd5HX6xIwGXRN4Dv7KdnRq4ySMgfTcfwGUKLH8INdtpckVNcuW5zIyNZrJwJc3YT7yc+lp4uIRWHrfrRUabg1nXvajZVCtkWVB5lMPCKxUCupQmLbsxBWEMyJw7p9CnxmGCwQghsKws8EmquY9Kt5rtuFrjN5QUPi5Sc3NLTVMFiMA4kwUNUkp6O98sdwHFoOhhJwdNUBg+v6XprWKiDgY3Bf/GPqjZXVN+KT/yHb/viVM+C7j0hzYSdDHMxEq2uT7XWZkJcLSqtgPf+78m97ZhgYvSqNAN/ui0EwA6yqCSIelt4iWqBUtu2507fBb1/0WpGkvYwBvXEb+NwoWP+rsMuaIMBgxJfBLn4AnRKOUvs0GQTrhmw5It8e5gtBxNZktY+M1c5hBO3GUi1cGvSmbjiLU7mXsb5TfvdWbRt4ZBXOwClooXKZ8qa4O8hQmaqN9N4jiNXukL8z4cIcOQ0xeSudgqZQFILSGsmvi1pD+6rCYCQgAxiPlOLkIFAaULJpIfTyWsiG2H1vIFFGCYYMGjj04VNgc+MFE68UijvFZ1AbOPAWZRcIV3rXUcoph453L3nvKxTFhPKYeUL65hUPnuE5zzz1+V5q1biziyxn5LI07ZQCjG7B7HtWvu5ODcobNH374bzJfVtxYyGEuKvh1fYFPEoolcm5/DnMQ2/LVg37/Icw9rwM5gvCGToP2An4jn4fT8t+Gbc5VmNM+sfMrwKWCWyrowt0hpB//ctdiwnZLrS4Qbfym8DLO6mNyRs2SjXxXGBmGbgyqcl2IfKg6W/mqA4kwC6+B7E8L42Y2cHvwnTCsrWFKpco/llv2i59TVxydzn1l0BVC5zuYzg7DEwtZU/b0IFXdzHYNrBC0/G5CJo2FmM+XB4HliPUXkOtTkB9yIapc/zyvE8u4xs7ufS1uTROhsKaFAvJ9Li3iS50NLAv/i/AdWE+92PEtSBG5gQGZnQpcFaVCuxtFTDg4t0r6xfcz/e4MDSGC2MMC2tM3uj01nM0VwPm6Fn5VJVSlkjssM+8AxFezloeet088KbcJsWaZ1BtPvM9iOVZuLcvSdGQlVVJI2MEy8FHroLPjUD0vQDTH5DtR5ToRFVuMl2qZYcnxGgmjKBX4MzDa4hoQdyYomMCeU+R55RAf4uGkB6F6feMi91EAlhbgFhbgDtyBSK8Io2G9fadYKFKoKwWOn0BdJyIJ6BRGf/AaXm8IEHHOvAG7MvHIcJLm4QEY+8rsM+8Rx+UYq+eNGvWSZz5BvEknCsT0SgSzIeZZYZrEwLhOFAeBHY1M5QHOfymUMajii2xbRssHgOLLMqHMWJ1QQrZesduecyKMz8CgW+GuPA49stEJApb82FsgWFgSiCaAKpKvONqqc9B8Buy7hRPNvFEHMJlmF1juDyuy/bDUj9dX7moKaUHagKWpcR4RfGgWpkURQvdUNLN552KMoS8OAtVgFU2yhvFVDUJiRskZNyrKEOETAcrCaNgm8pDgUxHTb+soOCzo9JzhpaFoEhjqgp4mliOMHx0WWBu1auCpe3kyjjFVNNNXsaXI4C+ZoZdLV76Dgke3fXA4W1UD7OOxjluTQMnhzxRhqB46y9uahhbMoHqNm9k1S1SlEl89VcytUfWytvkfXIZ9rkPoNNT/57DwMR1WdXRWQvsaaObTcgEKXqy++x2JltmlqICp4cEyoIME6t+fDHgiTIE3aieHgIG5kw4zCfntSsAuILhgysMYwua3AbJkJgMgT++Rs+KXUBWVHEkND/O3AYujusy1Yw+P7/K8OEVDXFXx5FtQs7PwU4BIRg+vqZJUYagi/NzoxouDAs4LXuluCIr0ISAufc1aXAs46yDZfIGyOh7Vppq07+UNkQpTe7YdTjXvkxul1ThNQ/7zLsQS9PgXfvkvkjtedReaJ/6lVdtQ+syEYM7eA725c/BMtxHSJT5/Drkd0QFTTTo5CKT5soRNzONygFfnIRz9URSQBJSZHGufAFO05aeCcnvPLGGxFd/KStxZGuNk/CWY8cz0HsOry/jtv0w+l+Q36/0sBHCS586+Vdg0rhXcbfQNn1zirZxT5QhaNv/YkBgalkDT1bBKRSFYFQhuDQJ++x7SeNxzxSc9n936DxMofbPQtjMwoURIX/ouE/QeeDTawILESWMKh4QHLg9x/DlLU+UIejfE7d0+boqLVAUG0qYURQtcVvcVVQ2GfyKyBqYv1TG6VJ7gnwST++Fl8GST9bvFWplIi+PtcSjTXogbwutqkFWAbgTA1J0Sr9H7RvxqGwDeRqIxAXODec+k1MEdOoCk5hZEfjihsDkkpCtPl31TN4IfnZN4Nq4QDzurTOba7g2lftQSuKG09gnf6f2JaqwyPSSyRQEpRBY0QT2wv9LCjwnBoDbs14LUnc9k6LC59cFzg8DlUm3O6rAupTHKJhuXqlChujpdnFjUsDO8TVH4sD0koD+6l8H9ryJqKNhcjn38pwd0VBXwvFK+zLqS4X8OxejizoSrg6UlwP73gBfnPCEwcUpr0KouSctuCCyDD497FWjmT5pSJ0L58YpmI7XBmgJG86Nr3IaQZCAg4z2vLk170JuI1Q5c3VcIEbqE50MySB48HzOaZNpr54UUtxYJPf3SNVop98BK62WEeTWke9Aq2mB/fVvgHhkw0wK2NdPgsc2vK7YEtqmB3J3jMl9IeaqyxrF1mjxmDym5ILEYY0/OpP+byIJrslqmVycHxEyrVChuF9sruPyRO5rZqqgsek6Q6EoItQVjKJoIf8M6iO/U1JPyam9gmmafOpNT7elYEM3er77i2D1kpkEFmKbS3wftupPPh4U4UztE1pD5/obSTNj8ZTcIJIwkaosycXUkvdFJGwX415nDRbWvBs+an2aTHapTC/Than3ezRBlSO5x0dVKVRlQpCnjGxfygP5ozDLguHzYTzpbUOVN1fGvKeSYwvedjKzQtu1d0FMaQW5xBaCxkBC0oud5H0j8ootKSFFuAJ6TQPmlvNvjDQ/Mub71E/lspGok4+FNQ62+00YbhwiEQenOOPFKdnGJVu5FtbXBZ8dAQwfeLKdKSdkwE09XPIDLsTyetLYRqgyjHAcjvECnYPTK7Q83vcjaPz5BEqaHqUykZjp2lnzvmnQ8evghk9WpfHJW3mHkwKSq27+7pa1Atsc7Qt20vRdoSiInfCq2PIg1jb0kSqyoPNiPui84Liqck1x/1BFc74qc3o95SWpUBQLSphRFC10wL4r49/oipcE4/PaG1hpjWyb4NND3t/++wvlI8PWoOFuEmamwhZ+ebMWA4v3V5FTCOlzse81GLteANPXVwpLGZomng5hhrraCrWjWYb3psZYQVGPrEZkypKMmi58AZrhKSw9ZfKRaSxdKEmMjPDS497i2pfmc37eyx1K2qPkxNSFHBm1SRXaZ2g8qfW31bRp/UnTXGZ4HyxkBknrxY5vHR2tJxeead5P3ol765IxseX3mI51oJSyAngJU8mhCywLM3zQk8OmjYVzQdO7n97Ip5TM7T8Xd9G5qniayTow5+AeY+yfFrZ66LXV6lUo7oSttiO1nSmKDdUIqihuYeZuKmZiEdnak7pXYqWVgGHBHR+QvixI+rLcD2U+B/PR9Qu+qK3h5GQ5TE3g4mwpKn02aoIP5xGAvLFM3TBuuPikioanAUpSaqkERvNUUTQkvVgNQ0NXHcfofK5xAM+0JxDkMfAVFz6jHAGLoakSqC/3ep5pG5pYTJoLu57o5eoW9KYeuMMXc05bb9oGMT8Oe24Nre190rx6Z30cNf6YNNFNwIcrswHpK7MS9cQE2r7J/4YqWXLNJxkVdzcuQjfLsL3Oxenh3DtEd70Ap23g+P+N2hf+ROoouR5SNVdymJS6JG+QOerLGKZXWM6b44oQAz77K9iHvwOTWgNDFbK1hyWFT2HHpb8OtXDpbbvATEuab1I6Ehn4UvtdKkrbnR6CiKymBRFuWNAau8AnbuZel7WtWAoLMKahs84zAs8F+fj4LbEujNE+vrHtSJoUl0AYyQQlfwB6S6/0s8mF1rx9fT7qO2QbVM55bOr2kqAUdwUZTNO2TdViG6F94W6O+YqnGMMCK6uWLZWb3zNl5awiPxVB7zifq5qhrkzAlE8u1M6ouD98hpDH/Mw28xRBC/DRQyWFoohQWqOiaIndtTCzBmS4u0tvlqZuaUrKKFnmATyJLbUcrCYM2Mky35tLQXkHvK9+BZbOMbH2iN3lUzebT4kRqc/UsKuVSSPfjRzoZPCZ6yf5Eh+wrT57GBI6Xu9eRejG+0gc/wkSJ34OAzZe3MGkEHjihsCJAe+HBJrnegB94Lj8rPvJz6C37ZAeJBshU1xuBqTJLEZPSAHpzW3LaBl9B77TP4Xv7M9ReulnOFJyCzsbErKix6sMENKMeON2Tu8d7Waw4ICf/DnsD/8c9ZWavGDeCMVgl/qEFGUIkzk43LXZH4AMf3e3MYjwqvybLU9hf4e3TjKh2Tq6jcNg3p2zQT5N0rPJgHv7ojTCpR/n1lnpu6N37pX7mn36t7BtF9bht6Xprn32fZnWZF/4WFahmLtfQiLqecc4gxdhkJFwcHMCibHjqExleu+iwLsXKFqcY7uXep8FJYi015AI5z2fcK0gzL2vyISl7C/HhLH75XSCkk4CG8Vpl9Vs/h47dmeLLZYfBhk6b0CmPVFkunoqf9cETBfPdKe2/3VoH6B9oUTFHCvuAI3Mxne9sLmqjWkw97wC20hWkypyYmmO3A837m10PtjXoSEYUKKM4v6hdK9nu0W6WDYF/f3sdoFgUJ1DFcWFqphRFC30RPWuWplia9A23DTTxRvadj6weSr30c0qk+1LDaEEhpYDaCiJy4qZKn8CE2t+7K5de2QdDuSlQzfMokCvfbFBMdcv9nk98uQpQxeSZO4bMIUUblJwTubRDMd6mBzOFUB/bRT6ud/K9I7MlJjztzmmlte/NBJlKJqZvsc9245A810Gq2vDYjyIir2vAuFFuNPDYAZV0WyDoweQgB8Geagc/B58FKl95tfZHgh2AuzaZ9D8b6CqsgUv7KDpuUjYGl7tZ9L3ZmFNoMwPaRiccDgcpnnPLKuaEbM1NFdBVpBMLwt5Y1tfwbASEbCFgUBrH8Ad6DyGehbBW7trMTonELE1NJRxVFHR2PIEUNkA3tgNrbwa+vwtvNrbhvmwjulVDSUWl9OwFoZgBijC6tsQUQfMsZEgo19KMEoRC8O+9Cmsoz9AYuSqfMk0DdgXP872j+Eu3NGrstrLaO+H2/MMtLoOcDAZtc1X5sHnxsAsvxeVbZj42YX1tsP3LzG8tkugtVqTEeDkjdNSBYQshmhcIJS8/3JdIGJUoPToD6TnDV9dhFZWLat8Vlw/AjEbvqQKtWiXomLPy0B42fMGotjzxm7Yug8JrQSpqWtUgdPUDau6Ge7ETVklRNU89KReyyEqKbbGsV2sRBhe69cwuShkbHxVCUNtKRl4uwgZLnx+FZ+qKEw85mAqXomWI9+DWJgAX5oBC5VBr+vAVCyAcm5AbUX5oSCDmWWB53oZZlcEojaZ0jNZxTC7zBE0hTyeKxT3gxtdQ8nEVbyxrRtTET+WYiYq/DYagjH4Jm7CbeuDThXtCkWRoI6aiqKEbqrJCLKQV0cmZPALauVImuE+LAIGR7llY3ApiKW4KS9umkq8m+/qgI2psB+rCR1lvkeYkmSY8obxaaLEz1Di9wSZddZ/d12O0TmOqxM6dE2gppRKaskgeilLlCFszjBFvtE5GJ4FehurUbbnJcQiCZy5qWEpUoKuuhJ0b2uVSUtf3gAiNnCo3UVLz1Ep6vCZwbzGlHzgFPQD1fjkagBv7dHw+Q0SggQOdQI7moBwDHjnAlXGMLyxm0lhRux6GVdGOKaWmGwDqS7xWpVO3hQynch2BXb1HIHratBWxoEz78LSdfRQUlIoAHdqBGLyFhwrAOvItxHvfQEBZwWJ619Bdz5DQ3UzGisbINYi4FevexmXh78NBCshShlcSj/JFGVSCAFn6AKMniNwZsfldpjP1NcduQqruRdGZz/sSBjuqb+CE1sDe+H3YdS1y2HODggMLm0uBP3gMkNvk0BjpSfYXpuAjEun7/WYLwGf30LC1fDuZVpbFp7v7UdZE7AcBo5f8sbxrd1C3qhR2tu5UYGFtVK0VJWiu71FrsNTN4GYA1lF1J1RoSPFGV9QijyK+yfuGjg/4jXbUYQ8tS/RjeG52ySEamgsh7qhVmxJnGv4ehA4KUrRXd+LmuZerEaBy5e991/rZ2mBVbGZSAK4NUM/3vmRziuD00Im4JE5fUM5CTOPey4V33SYk4AYvgBz+ALayqrR7gtBzIZlxD1dURhN2x73LCoUDxQlzCiKNpGJuONWJkpkkR94+OXLjSUxXFsoxXzMRHtZNN0jS4JNKrXpUQozVLUhRSlFGsE55iLexkM33VSNIiOqxQbRwCqRLXN5x5Os3CI409KJUIMz3k8mM2sa2uq83x1qaco3zvASWFLkoJY4EmWIrz2P6iwiCQF/ZSNcGFiOrCc5pdKlUiyGveQmsiCiChRvwV24177MHlAmF3H8+izw450O4HiN33x+HKCfzPlcXQQvqZYx085qDh+H9HDz0EgYbWiXZtt5ocQkx1vZjFKSqPWQPv/Z/wN61d3xEqaiXXk/Tn4/JITdyli1tE7cZKR4wvHELOJz0pY2kKCSqeT2kPoeKSmLfjIhkYBa4Kg9S/Hgico4NG/fvD2b/R7tCiqVSXEn0LGTJ4+dN6e9n0zWYkJWYilys5r0OSNI5M6EHorRcVKhuF8Epaelfl+Zh8B83vcVimJAecwoipLUzTI9xbkTRNLwMzMZ52FRE7DRXRFGd0UELaWxrJ7ZoMFlqeYjRVbMPD2tTHfa4lVq8SxT4AoSZgJJd2DC9IPpXgVKIdJpSIJLnxaCOsjoKWN5hh1JuZ/LG0t5rxCqyD9CXxCCeT45lPSVoq0KeHUXsKNxfVC/ycBiUWigaa8PS/NBhnopaFy6rsFxkO3bUt0MRq18/qTxNZnvahr2taVShZKnEH8JWHu/bHNKr8NgKUQiAaEbYP4MI82mHqC5N9tYV9PBwsuFk89I6Ej6wQiabmpfDdaAHXobrKQcwaSRbya0nFReL5eRAdWl6yc+Wg9aMl4rFUFOUNXF4S7v3xRG8n1qAaPxydVBhshVZHa5PlxZUIkyDxOfub5uSXiX32vGlUyh9DGFIoWRYRpKx4i2aq/6av01tQ8XIuhbXz+0D1IrYSoxjY6RW6UVKhR3QlZSY3kdWPdB+W/O9xWKIkBVzCiKEjJiJe60xZkSmbwbv4y71YcETaaxJHeFSshysBg3Hr0wk1DCTCYkUnTWC1SW0I+GxbDnMeOE2sGe/QPwWBQrPIC4w1ClAeXB9SqKTGopnULznuw3V5joa3RgWbq86KcqlVSqEqUGNVdrmFjwKqWaalvh3DzlVYlsgHXuA9f86KpnMDUXx7YzVAU5wgmGlbCQyVBk6Bt3NM9QuutbKE9w7GgyMLdoo6M8Bm1tVgorbrAa1+b86K43YU+PwoQNrbIW2PEc3NpumfYUswUqWg4joDnQp67CNQJoCkXAdT/0zt1gTb2y7cpdXYROQs6uF+HODEuBR18YA0LV0Dv6obXvhGb6wJdnZSmR1r4LXHBpZMxXZqHXNHmeO9RSNUCtT9kiC/nKpJKRNL8PvO0ZmI11smqHr8zBMP14qd3Eqmvh3at+dFXb6K6KQQ97VU7+qhqZuCT0FbDWWqw4PoQMDiO8DGchipKSSry1swSGqSMcZ/KJeW8jw4EOgakVb12SFOO3GHa2ANVmGH5GrVezch/S2qoxEfahnEx+MhBU3UPTXV2UrVrU0sR8QemJc6/wWFgadst1yTRo5eRi7IOWEtCKPKWDhLAdNRGE3FUgvgoRqMAKD2F0zS/3CXVpo9gKn8bRXc+wvY7L4zgl3XXUeIL34KwmPccy21sV2ZA5fnu1wJ6GKLToMkQ8DNZUhRgLYnDRUuloigeXntZzGHpdl6yS5eEV6NRi7S+BOz0IoYQZRZGhrl4UxV0xc6ceM4mIVwHxmK/DSk0Ht1eCMoLyUT1wopvhgi0kTylkyOwIDe9e9BKWUkk+fc0hfDUclG0xRFdCyAQkSmLKjK2m1qeDnRqEK3DqlsApAG/vM3BxRGBsYV10oO/5yDYGgwl8NehtsN/fF4C+/y24599PtwtJWvqkQPHzc/RoUqAxpKE8KPDJdV329qcgj9oXd5AoxPD1mPcY+Id7YqiOX4L4ej2u22AM+3ccA9Pa4F5+H7RI7kv/B9YqtuOzyyy9jERtqYEj23bDjSVwfCiIyiBwqGUH7AsfActeX5Yc3LRg7P8WHDMIfsVLpDJf+H2IqUEkBk6ng7i16mYZO524+EmWAKXVd3ipKOc/TL/GKhtg9BxCWARBtTe6boI1NcC5ctxro0qhGyjZ+yq+318Fd/IWtK+/Tk/PSaUmaRrcsWso7z4A++xHsJPtUZQcxfZ9Hx9d0xDJ0E3pRu2FXoFARvxUc3AN7s3TsCdvrQ/INDT0v0D1NvQp+ZJwXfDFSZkwlbWMde0wdh7z/GfuEh5dhTt8Be7wpYxpMy/9qb4TWpEbIVJKx3Mti3DO/DYr2rwmVIGG/W9CVzHHijvA7zfQ0+Di+A0Ny9H1k62Pjp29AiUqVagglilwoHYRzql3wJMedXSktcpr0b/nVRi+4j4OKR4NFMCh17bDPf1riKjXM0dnUoqz1w+8BV2Z6CuKDNXKpChaYYbKarU7VTfiUbCMqOzHRYnlSkNgitR+ZDyF5r93QszVcWYou3BjRxPDlwMiS7DoaWD4epB8RbwEp4Od3r9kLHxmiHv9MyS27OcYz+FJQiLcVzcFEmL9cBznBj6brMXq7h/C2fsdOP1vInHodzEQOIibCz45LsJnOTg1iCxRRs67DRy/weBS1BCAYz0AW5mCGFkXZSRCgF89Di0RBvZ9V77kch2fXs8WZYjZVQ3XJwBfwJDTO9AWh3PzdFqUSWMn4Jz9LbRUe9zR3wVia3AH1kUSQm/f5Yk6G6qC+PRt8MgKjKM/grH3VZhHfwC28yWcHg/BYglE4xw2VeiMXcsWZeTMOzKK2xRxaIMkhWVX3VBct1ZSCWPbftjnP0p71sjp7nwVX9zMFmWIcBz48hZDLJrR6z43Cp4pysgXOZyLn0Jz1kdAT5HtM+9tXsaZYbjjN6SX0d0iVhayRRn5ooBz/aRMuip2OCVhnXs3S5RJeS+5Vz6DG9lgeKFQ5CAeS+DMbWSJMvJ1G/j8BkOEYoYUeWGJmCeObrx2WJ71ROtYxlMKheIeccjo/8KHaVEmBf3tXvgIdrj4z3mKpwtVMaMoSig55U79ZQhqNSjob/GICJneDdxy3EhGaz8CyDdECTNZkKAxOJN9wU5+JHTTvtHU0ObA/Br9CK8bTvNMZj1JgMl4ZiLBdQxMbfZAIehViqb+0SHv7xtTAvNhDR8PhqBrIVlVQ4aKqSe6LVUyawkJrmFuNbf4SIJCzGWgbuwGfxjOjUv5l3f0CozeZ+G89EdYXPWSmnIxNKehpyG5ZI4NMbVBnEivlAREeBl47g9gmAbcKySSrMPKapItTbnXh3v7EhZD23Bmol2KTM90M9yeF9jRpIMzBp8TR2L0Wu5pcxd8fgIsVCFv1jeNe3zAq5xxs2+8EkYoq+Ipk6UwpQFp8KeEgY3CSBohY7G13iPerMyN5U6jSi6j3rT9ro47PLoG5/YGcS0DZ+QKjJJKaObDb8l8XFDb5cZktBR8YRLGhu9VocgFpbBNLec+dpIGG00wBDM8ZxTZyCrbPMardF5gXfvJqeeRz5eiyHDiEKsbnmZlBAcwl65dH/+1u0LxoFAVM4qihG7m7thfhv6jp6+PwPh3K8jM1ae7Uph5VEjzNPLBuIen98UKCSsZBRISisuO2tlCAnnRZqbAyFSYtCizPq4UsQIBAuGE5z9EP5lVG16c9Wb/pI3jzoVtA81k1Mt52uA6J7EwGHeg6+Svkn8wmheq6JJQFUgeYUW+HYtAsyww15aVI5nI6rRC82PHYGlCRrJSRVHm9OUyk9iR2eK1AZnYlGd/ln4vObx7tlqXme9LT6p8046ugSf3JVGoesOOp9O17hgab4H1JqhiptiFia2MysnBWqHYgq1Sg+jhjiI/PFqgUoHOCzmOsQrFXbPV8Vwd7xVFhhJmFEUJ3QDfsfkcPfWhG54nQJhJVc08SmEGWnJaBW50nzZ8lo6aZIs8VV61VQlUhTiqQ2zTNYG/QHECiSz0+a4aMrmFNBMmSv1Aew1VvqynyNSWMinA0Dhry/K34FVQ6k/ydxp3qluPUp46aoH68vX3Az6GsyOA0E1oZTX557OiHq7mgxuJFIyIpfQSPZUEpRsF9xm9tBKYnwfXLWgZKQoEVdOw0ur881NSieW4nq4QovVClUi0T5PgSqlMWelRGz9fXpfXN0krrwUzLellIytWSiq96RTY5WiNWCmLGU0DK6/NO6xW1QCNYreSvxdaxvS+d6eYZuFpV9RBGE/GcexhQd4CeaGksCKuFlI8OOi4m0rzqk4eOxsqvGM2EfKry+NCyOM7Qcfi2jagqXf92ETnBTo/KBT3i7QYyHdNQhdYxX2+Uzx9qCOnoiihqoLQnYaexL3+BWbee0rKgxZmZiKP8OYiFUHsJO4rKabYaKlmCLAoavRlmNPXwOgJYKAbL2+rxee3A+kKCiEEWqrI0HfzxUNnrWcivHvlQ0C8gN1tfrltknA4veIlNh3q8hKAasuAvzzjfe5bez0RZGPVDtHfSmlMyYhnjWNPK1AS1DG7IrAS8USf7Y0MC6scVjKh5utRPw537QOfJZVmw5Ngw4TetA2Jj/4/8s+SF/86yvwCK7HNy7O7mUNP3rlw0wet6wD49RObZ5JEIDK2HfoCYtaC0bVHeqqQB4xcZ9E1L5qe2nhy+KI4Xc/g2pS3LfY3uaixEtjb6iV9WLqAbpRDbD8Ih3xicty4a2VVuYVGTYfeusMTYnVDxsTrTd2eyBOeRnt1A4bnN9+QddZw+JLrUguUwiDj4FO/3jx+yy9NjdPzQuvBXyI9djZi9B4B891dqb9mBWB07kFi+vbmFindhN7cAy25PxcrUmSsaQWfG930Hn233LDUEyfFlli6K4+dIb+OuVUhU/XI6Pu5Hob5VS4rVymFTZEHXxCi6xDiVZ0YWgogbOuob0qgoTsCX2wBzK9umBX3j9AtoLEbmBzY9B5r6pHnA4WimFDXL4ribWW6m0Qm4gmqmIm7OuIue8QVM0XeAnGX+EUUjfOnYJz/tUwUIsNWfuEDlA68h9e2r7eTTC+62NPGsK1uvXqFqjt6G4HeJkC3l8FnR8FPfoqACVwaFTg3LDC5CIzMQ5oJ0/aqs3XBhAShl7oTqC/LeM0Cnu1MoMofx0c3vdeYZqCqVMOJG0Ia804uATengePXKOabwebeIX50AbCtMoh9b4OFytcXsrwWYv93ENfWe7R1OHi+F2iuXJ82Va0c7HDRUObCiYfR12Dj3LABo6YZRvfB9X2HMWj1nbB2PQ/qeCIhiE/eBDctmIfezqqSccauwzrwZpaQQUIN3/UqBiI1skrmQEsC9ZEbME//BO3BFXAYMA1NmgNrpdUw+o55AlASraYF5t5XwZkFc+8rYKVVWRUq5v7X4S7NIHHyr8AnbsrvxblxCva1L2HqTApP2+t5+kk6/dvb4GJnM+ke6xeALFAmx5VZvUHJUdaht6FlrF/NH4J1+G05X+srMyjncWMV0Z0i/CGYh96SHjrpaZfVyOmIQPH32ju6BaPvWejNvV6FTEqU6toLrW0XjKcgMlxx/1g+H6pKdXn8vZY8dt6aBj6/LlAR0tZLZxQ5sZmF6fLdeG+gBDdndbn+zk1Y+GCoAtHKLuh0Q61Q3C+GIR+EsLb+jOO9Ada+G/q2ffLBkkJRTDBBj3ufclZWVlBeXo7l5WWUlanotW86tEn/768EtjcATZVbX1yRWac7NQhj+0E8CURsDaenK/Bc8yLqQw+/vYj8OChNxjr8bWhVFPX7ZPC490t7blJGNOZC234YdlM/Ei5DGVZgf/1rYMdLSJQ2SO8CuqG3lsfAbpyAceht2J//BdjLf4LLE0xe/Ofi1V1UCeMZ1IScRdinfwve2g+nsh1UG2EmwjBGTktBAj3PYGrVRFXAxSfXtZy+MFSq/+YuLs2HKel5ZE7IC+iddTGUm3F54zEb9eHajA9HOjlq/QkIJwah6XDOvQ9tzxtI6EG4wqv60ZdGICiCeteLYK4DjQk4Fz8GoyqU5h7vookxaXhLUdXW0R8gcfwnYPvfBKPY6OUZWK296aoZuriyp4eglddDJ3GFvGgMH2JxF7bDYbgxmGPnIBYm5eAkspj7Xpf+NG7CBr/xldx2qUqC0VMzmvbiFNyxG7COfMe7YGM6kIjK4cjvhZVVw/76N7m/08ZujFQ/i6BPQxnNTjJQazkqcGZYx2s7XRnVnAkZAUtPF6YBVKmRJ6qaUs9EIk752XI45guC3eeNH4lTaTGVph0sLfp9knDCq3BO/wrGwW9Do/VJyWOG4fkfnXsP+sG3YQRVVK+iMOGoK9OXchl+0/H7jd1AaeCb8ezyceyXKxGBdy+KnDZj1SUCz2wDQipyXHGf0Dk2cfI30Dr6waqbZLUrXXPw+THw4SuwDn8r62GIQvFNp7hrnhVPJVR9QNxpKpNMZHpCqmWIgEHtIhyLMeORCDMylUm2MqmKmRSu44CPXc37vhi7BrOhG6FQEO5CFCAz2HO/wcZnhPKaNRmfTAlKJI7kY3hOYG+bdyPABwZlK442dAbW0Jms8blrSzA79+LLAQNv9HvpS3kNjG1gZlxDR4eDW7MG1mLAyRFqEcpuWRuYZajqMCEMP8TUABBeAj/xF/IEkdqNUnOuOQk4x/8C+rEfQSzNyNcpDWcjfGUWeO53oRk+iIsfAguTSAxvThTiZTUQe9/E1blS9AdHoZ99P91AkLm2ZDKDk5CvadyFM0PtPAIOpTttwJ0Zgdm9X6ZruQOnZLQ1+c6kI7xzwKcGUdFwAB/dzF11EncYNtZi3OkFIR1fHvQxRivgsVPMSIPjaBjO53+Re4A8STEKxcZUppVonlQ4DnmsLFWhQnlZDOcWZYj5tfU0QoXifqB2YyTC8kFM7vdVoqiiuPhmPA5QKO6ClC8HtV/c8YX+E+StQg/SSy0Xi7FHVKKZMulT5r9p6IKTUoryvi8TJ5JXpVsl62TEChVKAslKBUpVleQc3/pItgrSoulVSo9GJitf8g/H5GzKIo4tU31Sy71FsaXrgBkGBBcQVNWQj+S6pFatgsPJadIC03RF4eknvztGw6TWJRnyFlqvghfsXlC1pU8IW6W93G3SleKpZMvDl9qMCrKV8JKZpqdQ3DNbbUgqTVRRZKiKGUXxCjN3WjETW4NWUY8niRLLwVz0EfVoUxsGY9L8V+FhmAYSDduB2c0GowSr7YCWTANgZGCr6TKRwt72LIQZgJYIQ7/5BUCtLpYPzgt/AoMJNFQIzK0y7G4DygOeGDI2L6QvTGs1kxGtFEcdqO+AO3ZN+pbYDX2eh8byBNjENWiVDWnDO9rGqTIskUNvIJEh5GPgfgZdY2ipcHFzRkdrlYuW0riczu0lPyaXGTqqqG9Hl9Vmgeom0Oj0vqNAVZsXiMA53MufSgNkmrbxwh9ACFea5uZNP6J9itqaKpuAhm3A2jz0XS9AS6YgUYmye+kToK5LRrZTa4+WTPrQWnbAbdsHrhnQnShw/TgQXZUtO7YegIGYTJISawvQG7tlixIJSu7kIMTyLLTaNrjhFTnvWttO8JkRiJV5+bs7ciX3d1rViLmoKRNa9jdG4NddxBwdZyeD0hg01/GEk3E4VWgwz/tFJ0NhWkcJrzKHzLSp7Frx4GDUskXbCrVdduwHM02IeBT85teekfQTVP2oeHKxDCFbPInumgQqfA6ijoYbc36sxoCygPKYKUS1TO8TKA8C26tj8Otele/AnCXPSaaulBnF/cN8fs9TxvLLFMWUmb47PiCraeT7CkURoYQZRdERofskdmfmv1KMoBYe68mqWS41HYytBuSFIrU2PUyk1wXd6KtWpk3Rw5xEhLXF7DdMH4yOXdCT6TeO7oN79PexEPfj2jiwFqeLeh929n4X5XoUK66Fj68zdNUAe9oZHJfh2rjAhWEhfWA664A39zBpHDwwDdSVAYFAGdxDP8RYOISbc5Y0wq0va8DOA7sQ8nFcn/FuPunz+9sFvrq1+SZiVzOZCgt8fkMgYGh4fgfHtoo16GMXwEZvS0GuqrEHdu8OGH4/3r3gPSU+2hFAzQt/CJdEqbO/hUhEgYp6abQrTAtzMZ/0fyn3CfmaffqdDU1HnrAidAPOrXPQm9agt/QBtc1SFCGjXRpcr2+HdfSHcpzOtS/Q1LoPLjOBF/4IU2s6rg7qcl+uCBrY3fsWSvUobM2PgUlgW6ULa+cx2ULmjl6RnjbUKiQTlsgoUNOR+OqXchn15u0wD30L9oWPZHWcVt0EPj+x4cvWYfQcRrvmYJtvGu71czLSO1hSjhc79yMRqIKVUVXnujZYZBXO4HnZ6y6FM4rebt4u06fcseveMjZ0Qe/ofyT+L08LXDegH/0diPAixI0T4NFVaeys9xyBoOO4T5mOKrbGb3I81+3CF1uEcftrKfJW+UtQ37Yf8VADDGmKr4xF80GJf6/1JOBbHYcxdF62hFeW1aK94xASvnKUUAmkQnGfuLpPesshHoYzclWelynAwOjeL430XT2gWj8URYXanhVFRzQu4DeSgkMGfGka7uRNiMxWjWRU75MWE13mo5oFgenwI7q4oSf9qmImi6gWRKzvTfDOg95TGssP0dQHe//3EdXWzUU5TAwv+/HlTWAp4rUkLaxRugcwGQlC1zX5WlUp3dAzfHSZorUhxRaq7royBpy65QkbFUGGi6NCjv/kZAUuTFhSnKBhxxZ1vD8QxCpK0VK+7qHkMxmObmeoKfVeqwx5EdwVIYa4q8nPRuJAgIdhnP0l2MR1gPqyE1Fow+fhv/QbBHhEVsvQsJVBDuf6VxDXjnvVMCTYzY3B+eoXYLEIqoIMH9+kG+ASrJo1cA9+H6DUIfJRKamE2/cyVhr2w2Z+78nW4DnZWmR//VuvWoWqSeyYFC8Sp34N5tgQkzehn/6FrJC5Pq3jq0FdmnLSeqMKo4+uapiLBcA0hs7AHBjjsi3JPvueTFaS3jPRVTi3zsK9fckz/k0uozt0Ac6V414i08hVmeZDIoyMyDb90Bo6pXDDwWDMDUrjY7Ey55kRL8/BOfcerIXbYM56WRKLrCHx1V9JXxpZMRMLy+W0z33ojTe1jKNXkPjqL6V4oHgwCGGATw+CX/gw6TtkS68j9/RvgNUFuK66rFHcGaWRCejnfgWxNO1tR2uL0K98iJLZSzC5elBRCFMkEJo4A/3ap/JmWZ4nFiagn/klSuKbfb8UintBMA0ivAT70mfr5+WVOe/v8MqGR0IKxTcfdQWjKDroZtfa8KCLxBhn8JxMbHGHL6df59E175cnTJixdCHFmfHVRzNfjHxmVMVMFvMrwHs3gjhl78bM9u9ibscPcdF3BO/cKJHxqrEET5v6Xh3PPY4Lo2Tc4h1mq0sFLo3xnN4Fi2FgNQrUhoBjXcBqHJhb21wFQ61PF0c4DB/wWsMYEq4uBaGzt4VswelvZWisZLg6LnD8BlDq98bxwg7H2+5zGOWR+MIXJtDfAilo6k4MmBnaPJNCwL32BXTXizFxHI4vBk28N1SFgaqXMd/3Q4y1fQufLXbiowE/4lwH/JVgL/8R+Mxt2TK4CRJOxgegvfLX5AVXgpu4MZ271O3MMAlcAsbAFzCpGuf6Vzn9RPj8uGxtQUYcNS2jWJqF3r3fS0hybOgtO7wYzooGr7KGxnlz3Wg5E+fmaTDXa0/i8YgUgHJ58YjVec+8gtrbNiyjUL3wDwTdjUEMncv5Hr9+AlrSbFuhKAQdI9xrJ3K+x29fBFPCTEGYG4cYv57zPX7tOOyw99BLobgfZNjAjVM533MGTkFz1QNFRXGhWpkURQdVGGz0g5BP1TmHVtMi43xF4zawQKl8Qsb8QTAyBn3CqPEncHs5iLjLpM3HTMRCXTAhRZsHjqqYySJuc1nVQsysMsysZre6TS4BPU1MZhtR8lE+fzqq+EgkvUpdrmF6Kf93N7YgUN/p/X59OP9w08vkTcNgXn4P4WN/I+0vc11252R/jhKbqKK83Ih5+0Ae+PQQWnd0gDELbo6EpRSyQiFpoOvw9Zjua9OkhGaroYurHI1H3oRBouj0cP5pz47AbO5BYv8bWImQeJFbmKGKngRn8IeXwASXVRJ5xzk3CmPbPjhn3s2aDgtVwB3dkLZFcd9HvuO1bOUzlqVlprhr0lscWx5D8k57fgJaeS14shpPvkaVNa19gO/Japn8JiLF9HzOrSQ8SvFRxWUrCsPofEf7fE4E+NoyUKJiePPBl+byviciq2Dyhjl3wp1CccdseV6OAiHVKqwoHp68u1GF4gFUzGxMZBIrC7LFgFU1yTYHd3bEe31tQQo0TyK1wQR0TeCTkSq8M1QjW1veHapBxH4Iu62smFHCTAqdbHcKrGZ6j2UMWwjyjsn8XD7ILybX77mmnaJQilBqWBKGBM1tKn0r50waUuyRyVBJY+HcsPREt5o2LYOwbVmNwvRCC6RD0Liiq9C3WJmZ6zJViZR7nCb1jW14zch9gSfXC7kEb7FfZS5wgeWRy7qxOoaEz61WmOKOKLgtEU+gyK54Ail0/KC3kx5iijwUOp/cwfpVKO6IrbYjdbxXFBnqzKMoKoQQnjCTsWULevoVXpRmruRRIZ9mz41D1LZBxCKeWPMEQpUxu2pWcWspJCtl6oJxXJgtw/BKAH3VD7hMWKOKGVW6ncIwNHTWkRdM7ifzHbVAwKT3mBQBgybw3HYHJVoMgmKidRMrbgAnBrV0OoWlcbTXMJnAlAt6b2YZSKwKmdB0e1agqw6oKmGyQID8XwZnBCqC3rhEVbM0uC7xA2tel00W9J4/qU+QkXRbSw+c6ydzTltv3YGLEyYmFoEd/Q0ylSknNa0QyRsWU+OoKWXSA2YjpEFUhDSYayvgZo00A+Z5KnGopYibAeDalyh5oVfOd3uVg47yGJhw4AgTNxYCCCc0aTiJqmZpAKvVd3iVKLnGWduKxNe/yn6tvgP2wOnNwzb3yGox5qMVG8j9FJ1ak5JpP8IXkka/7u2LOaet1bbCvvhZ9jTadkF7wtolv7H4vO9Cr2uT6Vup6hl3alBWQArq81MotkAYlvTEom1mE5QC84Q+sHlS0MqrwemmOUc7KbWHppIDFYr7QZj+/OdlXxDCUOdVRXGhpEZFURFLtpVkVczEyJGVcoC9Cy2KIKaLCTIPoyff5PD+pFJqudhXt4KuighKLBc1gQSGlwN5K/nv6ym0EmayIMGjrWbz62Su21bDpHhDBEwXb/VFERg5BeeLn8D98mdwTvwEockzeLM3hqWkhvblWYbtDQylOa4jtjeQmMixGAGmHRJUBJ7vJdED+OKGwIkBgUujAh21DL1NwOlLDGMNL0uh4pltQHJWsoSRo91eexRxelgDq+uQkd4bIfNbHqyUogyx5lhgfc9tnklfEEbvEcyE/VI8cVyOgx3rJsSZHO4kS+QE7LPvg1/8WE5X3kRvnHZVo/xxP/xzoLQKJnPxdl8EfatfIHDmf8N/5mcoufAz7Ncu4sVtMQiYMpLcGb0p/WGkKfMG9O2HwWkFULVOxjKS0S/ikez1FKqQIosz8DVcOwFz90uytSl7JnX5upY8TlAaFwlZdFOXU2RaoXYvOyuGW6tp3rySFPcEN3ywDn8HggvY5z+Cff5D2Jc+lbH15r43YAWDj3sWFd8AzGAIev9LnlF4JoxB3/0KuKmEhUJw3Qej/4XNb5h+GDuPwVT7oeJBYPlg7H0153nZ2POKfF+hKCZUxYyiqCADVSKYEWYkk2XoeitpyMkME1ptO/jcCLTqZs/49hsCVc1MR3xYihuo9Oeta7h7KBo0h5np00yJn2FXC9BZCwzNCmna21bNUB7y3kvBEw7E9S8hZm6vf5i7EMMXwV0HdV0H0VRpor3G66R5rpfJ1KbxRQFTo7hshoDJwaGhPOiN2+VCCjIkNKag388MCTzXC3R0AsdvWGirc1AydxWvb2vFeNiP+aiFcstGW1kc1twg/LU7sFRpSaFymZegfPfL8gkxn7zpeatQtUigFEtOQIpQNF1h+jDn70Td0Trw8etg8TBETRtQ2YTZRABVQY7Xt8dg8Tg004fXdwUwtcgxtaqjxOJSPPJpDoz4Mmj2xfIMmGvLmGq9odOL4YaATtU31CPuOtD3vYWIVYGgmwC/8imwOLW+4BRNPXQGmiagte7EtFOK5o6d4ItTMHuPyAhs+p3isrW6NvDlWfnEgSpqqMyZUpgkug7zwJuyskJOs64drKwGLBCC2f8i3IUpoKoR1rM/kPHbYm0JrKQKemMnHIropBQrenJHJGIwOvfIKjMyTqYn7DoJT6mqGkph4gJ6Sw+00kqvGkfxYKA0rhsnITJ9flzP3FrQN9+xD5ZfRfUqCmOTQfjaAowj34c7Owa2PAURLIfeuA18ZR46pbCpzSgvOo/DXV2Qx1TyL6O4bI2Op6VV8pif8IVgWWoFKu4PunZwDT+MZ38Ed3IIbG0OorTGu5bgQpoDQ4moiiLim3NHqlDcAasxz/sj87pcpsFQaXKGAKNV1oFVrKe2fFMo9TlgEFiKmQ9WmCGfj6Spq2IdEkmocqa6RMgqFC3L5MRDc+NwMkWZDMT4NRjt/TjSFEPcLMOXA0ImMD3fS5HWXtLRmSFgdIHhQCfQXk2NdyTaeEJMLi6NUtuU10al2TFZ7WGKk+isqENnoBRsJQJ+g4QNgdKGDtSWWeiodsGvfAF7+iawbT+M3mdl2589cBKYGkRp92EcaN8lDRsXYqZMWzK0CmxvfAb+SiENkMfHvdao1/o41kQAdZqDxImfQ7fjaHvh99BeGwRjAvaJXwKRReDwt+XTU71tJ9yxazKqmtLPtMpGuZPalLRAYkdTN7TthxG4dVYKGW6mKJMBtQ5ZDZ1oK3MBm27Ov/RMJkMVYGVVEImYrKAg9YtuEIw9L8vKMjF2Dc61L+WTcarakTcOsbBMYGKBEuj9L0MvqZD7gEOtTroJjUSbmhYZl504/lPPg+a5H8mSap6Iw75+UkbsUruDrEJybK8Cz7Vh7H7Jq7whZx/ls/BQUpmcPObLfPQKjJYd9Jj1kc+X4psFHbcSV457x4vmHqCqCVp8Dc5Xv5AeUfrRHygT6ULEIjK9ig9flqI7idIupe/dPA2YFiyqTFbCjOI+0ew4nBM/le3VxtEfAi09QCIC5/j/ludlnc7LymRaUUQoYUZRVKzFhBRltAyjTboJY6kn3Rl8E704yRs1aLqyYuaBoipmCqIXcO2VaT553xQQdgLuyV9AvPg30m1Nn6dTRtc3wrlVgY4a75U5r8grJ8sRgCc/J5O0kj3+MqVoaSYrl8mNhbG0VgZRGodYTnq83DrrxT1nwBbGAKqe0Q0srnljcDiSMeDr80hikSsYPrvO8OM+Jx2/7X72F5sXfW0RWmkVWEkF3Nsj6UoTSoDKGm55DholN9W2goeX8y84CYf0FJuMdTVNijLy8+El+ZMJX5qBSR40jgN3XsZVeWlKk7cA+klN245DT8XiRte89+nzY9c2Lo2XyiTfdCBW5tKVMbI6JnPaMyPyqbsSZR4OPBop8Kar0uUUd4TcTpJm4Hz8xub3oytAeY5eVkU6OMH7hW9OqbMTqjVa8UCgc3QK58ufb3wXInVeViiKBHXlqCi6ViaKB85EULxqERlvhkwXi7EHXLopPWYcWUWhuDuoNa7w+waQ9CPJ3Db3tgHbMoq2Qj7Px5R+6PfMdKNMM2uqWiGphNqTstrwtOR0jPWJUHvPAt3HaprXTkM+KzS/de3SRDeF8JfK9APXdbOmvRHSpzQmPA8n2mZS4oM/APQ+I586p6ftC4GTaGHH5O95148/KAUhzI1v0fKTTJai+SdVNWM5Nw0Z9PykNINMPDOeetNnaB2kpx2ilZhcuIzvkY4X9MRXz5hG8ntmjKXbInNOO1Quh1E8HNgWngJkvK1QbEXWdpLr2Gmp9sNCsBz+XutvagWT6xSKOyYzHS1YA+x8zvs3/b463iuKiye6YuZf/It/gX/5L/9l1mu9vb24ds17mhmLxfAP/sE/wP/6X/8L8Xgcb731Fv7Tf/pPqK+vf0xzrHgSWpnIpyMFNYaIeBhaqALFQonp4HYkKE2Oc3TW3BPeDb7wniB+gzx37hWeiMk2GkEVGqbPa0nxhzbdUMdjCdhck6lH1M9cFtRgkn8Kt6XgR+0zKK+TN+NyXBugdjkyK53u+QFKXYHeJobmCge2q2E1wlEeYOhpoGlyuDCwFidhxkFzlYGJJYHeRvKb8apXyDdpellIYYYSkXY26+CGH6yhE3b7YcS1oPx80GLwsxisW8dl682OJoYY/ED/22SdCx/i4GtLUqzR+o7CsRPQNB3O3DBw6VNUvPDH0kyYprmRrlouDYdfrRsH16qhde4Hb+lD3DWwGuXwV+xA0BIw4gveNhVdhTN4Xrb28JnhnN+F3rEbcAGzebsncpE4s8Gkl9DqWmWstliZByMvCGqRGjy3eYSa7rVL0VqlipjmHjhrK3A7DmKN++FyhlLLgTl9DUZZJfRg8gbD8oM1bYdB8+PE5fcrk1kMCw4lMCX9Y0g80rv2wqHWpc3fOPSmbVmvOJwjGmcIx4GE4x2fLEMgYN37cxHytqFKLfLBkaJbsBzMF/hG+WXdM2ZAfi8bK5UIStij/U2h2ApuWNAauuC27kXMKEU4TvskHTvjMG596R2HFHmRoQl0TMyoaMgylDf86smv4v4xfGC7X4Fd2Y6Yrcn9NLS3F36Tw1wYKviARqH4JvLEX8Xt2rUL77//fvpvI0M9/dM//VP86le/wl/8xV+gvLwcf+fv/B38zu/8Do4fP/6Y5lbxOOFcIBwDGis2lNRSXnARObdTOhO1sqwmDJT7HpAvDD0xJKidqchv7ngsAufaCfDpDF8Y0wfrwJuydD3VghKLJTC7quHUkCbFkRQ7GnR012tgX//f3gsv/r9h7HsD7pnfetVZmYk//S/h8rQP0vIFwHf2ubj6/2fvvYPjStPz3uc7oSNyBpFBAsyZM8PhZM7Mzoy0QbsrXV1bV3L56i9ZklWSbMsq26Uq26pVqSzLcnlXpXJtSbZK67V17bXWm3cnL4cTyGHOBECCyDl2OuG79X6nG+gGugEGgGg03t9UD4juxgndJ33Ped/n6RfoGiUxxrujSCLI0zsEykM2vnNBx9FWgdpSEl40fHhbwvaq7RVkIEzJTt8+58Vw15b4ITpfwunbLqbmF0WlsD+AZ3a+Ar8mEbeh5r+nKg5j+AYSPRcWIoZVssGeE5AVjUqUUR+FJvH8LqnalSiiO0VdiURnHeBcOQdj7Crspt1w257EJz0CIzOL60PC0XM7qxB0k58FXbj7wzA6n4R965PFeZOIsf0QECqB9f431TP6S78E3+FXkTj34wxxhkx6jY5jSHz0XSWaEL5nfx5ydgLuaLJNSk3AhHnoZdimD0Y8qsQg23Yw0XYSH3XrGd/jztoj6KyUCydBLVgEs+0ArPM/yRDZKH3JPHRSvb4wm6omuJTAlN7yROlNB17MqKaxbRdjc0J5C6V/lk2VwP5mibD/wZVV8rhx+m/AuXVm8bMUGoy9z0KvbYEo8AtVMxyGffgzsD/9ARBL9gYSReXQ9z4LI1g41ZHM+mEEw4h0Po/TXcDE3OJ+GPKH8FznS/CHueJjJWwzCOPo67A//aFqUV2grBbajmMwqIqSYR4RPVSMiChSYQgz0dS1g0RJUOBE53b4g1ydyhQWeT8CIyGmrq5u2fPT09P4+te/jm984xs4efKkeu4v//IvsXv3bnz44Yc4fvz4Biwts5FMRVTNhzJrXSA5uBNp7QubnaDhjfDmEvraCTPJsmO6E5/Nj6dQkK4D5961TFGGICPIMz+A78QXF9pg4raOD7uWn/SvD2moKHJRdeAk5MW3YEgbTten0A6+4vmYROfUxYTUdPX8nh3HcHMohM8eBgYnJbpGMy/4qTLlp7c0vLZfqiooEoJeOyDUhQj9ns7dMa/i4vOHaTqaSio60yMzRBmCqjPo7ylym4gmAH90HNbSChPXUZUf5vEvIL7vNcBJIOREEL72Pl5pfQJzCCNhCxT7HfhnB2DenQb2HYHzzlVo7cdwuQ9JUQYZPjTvXRd4eU8YgcOvKuGFqpPcmVGYh19NildSVT2ohCSqfHjmF4FT/10Zclo3PoTZ+YRqV5LxqGpFUma9Xeeh17er709rPQBnoAtaSaWKriYhRZg+JcyQf46591n1XdjXPkD86M/jg1vLB1k3hnWUFzloSm7ubmQG1sV3llU+kVeOdel9mAdegEbroqpmgjA7j0G27oM7O67aIshLh9ofVPR8koglcOrG8u/x3jhQGqQKKglNe7D7ynJ2HA4ZJ2c86cK+/B604p+DKKlEITMXlThzrwS7dn0ORZgDyNw9WIJJO4R7fQEcbHIRDvK9emZlojEb53opIS/z+BWJA+/fFHhxl41wMO8vkTcMy9bwcW859u79AkLurLrWkqEyjCWCmBj0YV+jDX96Dy7DPATzUQcf3RaYWWLlR79/dFvi6R10vGcRlSkc8v6oeevWLWzbtg2BQABPP/00vvKVr6C5uRlnz56FZVl45ZVXFt67a9cu9drp06dXFGao7YkeKWZmVnDaZDYNFEFMl1hFacUxNLBTFFDFDFU06MLFvLWGJ6OFipmNS2Z6HPslbQ9O75XsLzqWF7UcKlZeK90jXvJRNq4Nanhme4N6VVhxyKFuT2Qgb5JgsYpXRtKEVGs7QPdh4ToOrg1m/86o8KFv3MUXj3mv3x5ePphPcXNQYlu5hrIwYDkCIzn8cqn9ilpnuoYlnmuPwr52MefnQmk2/o7jsF0D7tQdYGoYxvnvoIyqL6i9iPYj6cLRDZhNO6nzCAlXw93x7ANgqtIhI25/sBwwDbi3zyoxzB3qUe1VyiMmVRETj8Lc+xysmlbIWARychjW5LDn+UJiC92NVSadQlXDkDBj1LUicfYHXkUcTYvaDqjai36n9ZkcglvZCK1iG+5M5xZl6fuoCicQpD4xK6FEj6zfz/TIMjNL8u9REd1U0p+D4SmVmp2VW0NUOSNQFHwwI0RniXFzOvbdy0qUEtraHBvy8VxJ29boDD2CMLQgTKMacWvxc97bwHdQmdUhQXxgMvu2QuJMLAGE8/QeRT7sl9Q2OzYv8G53CIYegqkD8SEstFjvrJconKsuZqNIOBom57OfRCnhkl7nTCamkMjr20pPPfUU/uqv/go/+MEP8Od//ufo6enBc889h9nZWQwNDcHn86GsLNM7hPxl6LWVIHGHWp9Sj6ampnVek83Ph7dcfOdTF3dH89ccdmJOqmqZ9EhjSYM/ispeo4FKPkDj0KDhYm4NhZmFu/wbmKTwWPZLSjBaYR1lxFM5XNvFXCL34TFCgR4kyzQ9ndljTyLC9OiCKKNIzU8IRFcIEJiJaeq7pQeJKrlIxWhTW056a06uQWwFef4KR1Wd5EJVsUhH+ezJSNpFPq0H/V0y+YmEO0GpSMn55xIdUlU70u+HcGwvsj4FpViltSnRa8K1gfp25Qe1AAktNO9kcoqqh0sth8rbTiyqWvS+1O/J71Hz+SF9IcxZue8/0ABMpsS31VLJHmLfmI3JFb+bBz6auqt8j5RUtfB5PTr5eK4kESZ9cE3VYOnbYTZvJIZZSnqLaDZiVv5e6+TDfhmJy4zPMn0/pJ/kycYwj8pqx3M+3jOFRl4LM2+88QZ+4Rd+AQcOHFDGvt/73vcwNTWF//E//scjTff3f//3VStU6nHv3r01W+ZChE7AVHpP45/zd8nzIj9PuBPzQPGSm+MkzNBd7UIjYDiYSxhrXjEjNzAy+7HslyTQrZCoo5V6MUlCF6gK575yLw9J6JoE7p0G/CvcVqUEn5RpLIDSFW7t1BS7KgmaHpXFnlhAGmNdGdBQQd4H3vtKqOAkmZBEdylXCgCiQpC5BBB1TBVdnXMxS6shNR9iMUArWSEi1hdULVqEoUk1/1yUhgS0mUm4um/FaZJ/DBlxousCtFDu6pN07yPp2p4x7wrfo4zMAZEpVAVzq2FlYa/6TJF2nNAadkLvfBJaQ0dqKR+q6q6yKPeXo0TkBy3uoJapFSJ8tfLaxeq3NSAfz5XBtK+hvRY40Ox59hD0ea60TTJMClMXK+5/4UD+Xh7nw35JHh+5oH2Qzk8M86j4Vjme+/K+74NhHoxNdeik6pjOzk7cvn1b+c4kEgkl1KQzPDyc1ZMmHb/fj5KSkowHk5v+CW/wt7eRWieoNQJ5R8KWKiq7eMkYmZJL0gdchcJaV8wgDypmHsd+SYk6ZCKb9bVgkfIJSXlbNVVqypg3G3spabrnrPq3NPzQqrLfsdTqd8DSPLWQKnAONLo5Ly6qSzWcuwv1qCoGdm0DjncIJa7QAILSlZ7cLnCgWSjj36Epqdra2qqzL2NNqSecdNYLfHTXD739cPbWLN2Avq0Df/epwA+oyytUApH0UlmKsf0QbCPsGeIaErvrs4tX5J8S9EnI2DScy5ehN+3xRLGlCKFSkOyJKWBuXIkfIimOLVvMxl1euxgVt9y9Cn07rU8WKF2ruEINDMgceFs4lnOwvq+B2q2SxwdKadn1tOczRL42M6Mq7Yh+p/SqjOhsZSI9D2f0HhIX34F17TTcmTFlzJtOZbFnhpx13k0C4cCDKTOUWmW0H8quxmm6SqASD+hZs9nOlfRdHm2x8XN757DPuYS20Xdx2LyBL+ydx6Fm2ubz88YBk1/Q8aujNvvxuLrYhS+Pt6N82C+DPu84nw06L/hNbilkHh2f7qCxIvt21lQBlRLJMIXEphJm5ubm0NXVhfr6ehw9ehSmaeLNN99ceP3GjRvo7e1VXjTM2tE/KVEepju8AtXFUN4bciFZJT8YTvps0HJulYqZmJ2ZMrPZPWYeBxSHrVU1wtj9dEbMolZRD/PYG9DSqmn8posXd8uM+HW6GH2mw0XIsIDeq+o5Bz41Pa1+++KAmQbJjbuUePCTy9583r1GFV0ST7W78KcN1mmbfXGXRMIRytyXHlSNQsICGfh2j3hmsZ/2SFwbkEp8/NEloHuYBBuBPXU2Omrshbu/9KO5wsUTLQ6EE1cCzo46gTG7CObhV4DAYrqQEliOvg7LWFxJFzrMgyfVZ7KA4YOx4wi0ykbIrjMwOp+Ae/UUWiqBfducDAGrvkzimU6oaG7yPMHYeUjDhHnkM0roWJh3sFg9J+l7uPg95c/jJizlkaLVtCyKSCQcteyF3tipxA+1jGP3oJVWq+VIF15FeR18h17x/GkCxTCPvQ5f7xm80B7J+B5JLDmxw0VJunk2xWAXlyPx4bfhkCfOUI9KPkp89H+gF1VACy5uG9ROZH36Y1if/gjuYBec3qtInP47OHcuZYgzdMx8frdAZVGmCHekTaCq6OGOoSSa0XdG4tHCc+FS+J74mRWriAoFE3E0mWNwTv9PtS26Q92QNz6A+/G30BKaQtC/qS5rmA3C7zOwo5ZS9tyM6o7Gcokn2gV0HvCtiCFsPNMp1fF+4TnNOx80V0qYXLrGrAGGLtXNqNbqxcsr+km/728GggEumWEKCyHXeYRN1S0kpjz//PMIBoNqQE+Do/vhn/yTf4LPfe5zaGlpwcDAAP7gD/4A58+fx9WrV1FdXY1f+7VfU+1N5ENDdwx+8zd/U/3dBx988EDLSMZp1KdLJaH5cEcwn6Dv639/IlWpeHOVUCZcF3uBl/YKVCXbLQgr2d5E5cEbwZluV5mgHmtP85eBhHXmB2qQp0r8C4jpuIGLoyV4pWUMJf61uYC0znwfxq7jMJr3IB9Yz/1Suq7nP0QeKpoO4QvkFPAiEQuWK5QfCF1r+gzp+awkTWmjvnJ80i3x3PYENDumqo6ossE2grjYb6Jzm8BMBKgukrg2RC9L7Kj1zH2puCFhAed7NRxpF3j/mlQXt8/sEnjzcvZD8/YaqtiRiMzMoiSswf70R5AlNbDq9sAWBnQ4MEdvQ4zchu+Jz2JKlqi7v9SLrWvCS9CgyGmhKVHk9mQYFSEXYV8cVsRCSVCqWGoSQtR+Q+sqJZyBW14s867jKlIaB1/H6bs+PN3uwna9aG0a4NAdrvO9JvY2ugjGRoFQOTA9pEx79fZDC35PdGxxui9Aq2uDVt0CJObVFVfio++o9CWtssGbN4lfNPiOzqk4amnb3udLJrjxeeiNO9Vy0YfpTo+p+ZBIkWrdcsl3xbGR0IJIwIQrJXyahM8nVGVUCkplSnz83Qz/mwUCRfA98YZKZaJtx+6+oBK3suF7+gvLWrcicVcZNZOQSttQ2P/gaUxLIXFIKvPjpBExGSCvM/lwrrTnZ2F/+L8zfZzSI+qPvAYjlKaEMUwWEpEo5PkfAsc+B8v2rmEMXagqRNw4DWPHIRjhzSF0bsR+ac/PwP7ku8CuZ2EV1apjmyFcmMM3gIl+aPtehBla/2MSU9hYkXk4l34McehnEXd02I5QYo1fdyAvfA/63ldghtn+lykc1k1qHB8fxy/+4i/irbfeUkIMpSu1t7fjV3/1V1FeXo4/+ZM/WXUafX19+Ht/7++paZEQ8+yzz6oobPo38ad/+qfq4vbLX/6ycqgnH5qvfe1r67VKWxIyWqQBHbVTEGUh727z7SG5IMyMTEsVCUvvO9wKdXf+cUIDvKEpoGLptTgNnEl3LMSKGd0TYyiZaa2EGeXhsYGtTI8TavdIrzhYiVAoRy+K39uu4jMS47PA/z5PO0lmu0vKB+P0LYnXDwrcGZFqgN4ztnwfuTdGlS3ednxvPLdefmcM6KjXEPz0f0Ic/4IX7zw/DXPwFpYuKYlPQ0PFaGu1ceq2gZmoCpRPPhZpKBc41uaDGXLgjvcp4YaqP+iRiQAoJnp2AhZMjM4IfPv80jujnuDQUC5hFJXBlA6c3mtwJwbgjg8sWx9pxVSli15UDmekV5kp0/vpsQzHhl5aCXd+SlVKkBmwOzG4/G2j9xaEGUrZIqihLHc+U/J4kU2UIci8OGnyTO2RJP7kwum7CW1PpjATWlbF8ejHSEEtWyv4JRUqC4Jqttfmp3K+xjDpCDumou7x9l+pC+GlF8Nuw3ZgkwgzG4E7M+EdLy/8SJ13Uuee1JlLuFvjWoJZZ8iOYGoc8p3/ivQrrIUrJLoZxrlMTAGxbsLMb//2b6u7kdRatHv37oXnSaz5nd/5nfsSZr75zW+u+DpFaH/1q19VD2Z9mI0ttnAQJLI1VUoV9bqnkYyAgZ/ekMqQlEr0L/ZSlC8NRB6fODMT9RIBlrYxqQN6Mta20KAKCKrhiNhrG5m9kea/m5XV2smSRR+rJggkHCBA6dS65+V0X/NbSCnK9WYblZXeRcxKKSQkFlEJD1WiyBXFOUpG8i6JVqu1pHVQfieUyrTSdkUVRqmJrbb9pdZXrrLu6UlZ90v6F5X19bQPcIXlpEjrB6kMZR6Q1dotV/seGeZ+jp12Ybf1PjKr3cTh/ZBZC1a70ODtjCkw1k2Y+dGPfoQf/vCHaGxszHi+o6MDd+/eXa/ZMmtMKraXBowp6ko9z4t3r3pVMmG/ZwxMx8+JOeDmoMSh1sc3KBmc8sxRqZpn2Z1VwlxexbDZoTGfX3cRWUsDYGoxKXCPmXQoXYzEA9p2VjIqdBwXcVJNqPjK1Jb1zpN3LH0fZMLbWefFLwshcbkXGJpZTA3QhERtKTA2BzxHHiyGN8+xWYlPe4DGCoGrfRJjM17VWc+IzGnqS8vsPvnzkLTc5NGSrUqAEqGCxfCRwa4usa3Uwd1RHSf3WAhrUfX6RKII79wQaK5wVBKVGB6EqKiHk/Qt0ck3x/BBzk3CGezyPEw0A8buZ+BqUu37YR/wVHsCmmtDCg33ZgI4d4cqfzToo7chq9tVO6EzPQrt0CvQwyXqs3Tjc3DO/ghaTTNsMwAnIeEvKvcWPVikjJOpxYziu52B2972afi81iSqeKIkqdkJ6HXtECWVaqCgWp7mJqFVN0HGIl5hii+oRBLbtqFRHDdpS6YPejJNS6qWNFd5zKjqumyiDlWT+bx6G0EmwVVNcEfuem2SZTVKtHFG7kJOj6rPLJsoI+PRZAWfDyItYYp5MFSlG32+2S7Y6VhfgEI8sw4Yfm+fbjmgzM/VuU9ocGKzwCffgZY0gmeyo5VWIdeQmM4T5CvGMI8KXQOoc7/ylHvS+7frwL75MTA96r3OMAXEul0dzs/PI5Slv3RiYkI5yjObg9mYVK1L5E2RQtMEDrVI3BomE1qgpXrx9eoSL1r7YMvju2M8mDQnTl/GhYGQbix4WhQaAWNthRmhbw1hxnUl5uLAtX6pfInIiHfnNqC2hATIzG0oEnNwb8xF95iuxu4N5Y5qNyoKLn7uhpB47QAwFxc40yMxF/MqyHY3COxrlhid8QaQ1/uBIy2AIwVuDEoMT5OnAdBeI/DGQa9iZiqpJR5qBSrCEhPzmctDm/j+Jk3NZyZSjLZqFzt3PgXnyvvL1lNrPQBXN3HqmkR9yMS+NomDdbOqRcgauauqWcrqd+DLB7YjKkIQvZeU+EKGvOahl5WHidN/S7XukPhAz5EwYiVikN3nVIvSyV3bYSQicK6dgzszonxOmlsPouVADRyhw+66AHHnCszDb0CvbVM+NfaNj1TJi1bbBt+zP6+Enh9fM5THw2s7TW/e1M7Ud0Mtg1ZcCXP/C5C6AXt+WpkOix1Hoe8+AWHF1DI6PRdVZZxO8dbBErUcZNpLAo7WtBd6TSPkUA8sWh/Xhl7dDNG6F+70uPpbtY5kHHz4Vdhdny5ruTK2HwF8XkkeVRXpHUeVtw21U5HBMQktSpAhDx0SiZYIxM5YH5w7l9V6KfPptgNq8LKWCUpbBan7IFoOQN65sOw1rfM4XBZmmPtA+APQnv4ytNgs7CvvAbPjEIEi6G2HgOf/PtzNlY3x2FGm7fUdwOCtZa9Rup3JPk/MGuAYfujHfw5aYh7OzY+VF5wWLoW5/RBcXxiOEVi/gSzDbADrtj0/99xz+K//9b/i3/ybf6N+p0G667r44z/+Y7z00kvrNVtmHSpmUm1M6VCFwb7MYihFTQkwMAnluVGVxYOOjDev3JMqrcRzWX808cayPX8PGiwvhYSZQlbTqWKGPGbWDE1fpY2lMJiOAm9d9sx3iZgFfHxbornSE0RS1TORqI1TNwWmoouf8a1hHb3jwMm9zoI4Q9UxAxOaauNLQdMcmfHSPcpDrkpPIqsaWwq8dcVrAUxx4a5UkfRkXE3FODSVgIzgeIOFuzMBdI37VGVPbbGLvbUxhCAxEw2recQsDXOVLfAdCMO4c0ZVi1BFgd18BNHieviFX72vo2YOpi09c9tkix/Nhwxs3eEeBA+9gsRtz8yWKn6o+sOlKpUk7vAduCO9MJ/4GUgzoLwFZFUT9Mgk7LPfX2xvoucvvgk07YXWdlBFSnuv2CrBiKpfUigPm6Ee+I69rtoR1WepCZW8RKbAC/OOR+CO9alEKVUtQfNIxFUrn3XuJwstRjRv+8bHXhVL5xOQ5AtDm3VZFawLb0MmE50UZB58+5xKVFqYz1A3EsN3VJKTahScHFJVQ3bLEcTCNcqVJzVUo9arxIW3FiqVVKvY7U8hymqViJR+DLKu/BTu6L3F+fTfRGKoG77jn1epWMyDISlZbVsHZFE5ZM85ZQpNn6O2/ShkoPiRTZWZrYFqN5wegX3+x5ki6vkfQbQfhWhcbMFnluMKHXr7Qbil1cDdS14CZkkVtB3HIH1eNSLDPCp0rhWTg7CufZB5TTAxCINuztS1b+jyMcymEWZIgHn55Zdx5swZJBIJ/LN/9s9w5coVVTFz6tSp9Zots8bMRoGiB7gBSZUCfgPom5CoKlkuulDkb88I/UsiEgf2Nj2aMDMy4w2KlvnLJFNLCrmsnSKzJ2NrWC68BVqZ4pbEuZ5FUSYdElyociYVZU1teVPR5dtn3AZuDUrsa3JUW5PlaLh8L3vb0fm7Ei/v0/Ba86CqyDjf66pUgaWMzVLFDfDqXheO1IHoLPQz30V7RQOa63er+Gd9qh/i3DXI8m043PgcTnebaK8VeP+6CV2vx87Gz6DY7yBiabg5FsDcIPDqAYGmcgfBsB9Oz7kFUSYdEnPcqSFoL/0y3JunIKx4hiiz+EYX9vUP4Tt4EkqOEDrca6eyt5TcuwKtaRdclMB4+Ytw+65niDILxObgDHbjC0cO4O8+FdAcC4nui1k+SQnr2mkl4pAMY9a2wqG73Om+L0moxUi27geKK73Yq+hcpihDA/uyWljnfpxjHT9CbPfLiFkCc3ENN0YC6jv/zD6X9By4Vhx29/ms7WNyalh9nkgaDsvobIYos4BjKxGJUqYK0QNrPdHsBOzT/0u1q4ndz0E3TLhWDO7ts5DRGWhPfgEw+G49swqJOBw6fmVB9nyqkuEA3jdzodsx2B/8T6/ldP+LEJoBNz4P5/oHENJF4sjPwMepTMwjYjgxJKhtKQv2zU/gq9wG+Hg/ZQqHdRNm9u3bh5s3b+I//af/hOLiYszNzeFLX/oSfv3Xfx319fXrNVtmjSFT3coHuMalCpiKIql8Xw4teW064okyO2q9ioIbg1TpIlf091gNSoSiVqvgkhYUQiYi0Ioz01EKrWIm4WrK54cilh+ZLWD+S5Un414hRVaGpiXKwuRH4uDOeO4PtW9SQ2e9C9MEopbyzc05PxrUF138Pqzn/18MTuaed9+YxJE2mqeEfbfHe3KiH8ZEf8b75FgvqjroezJVexVNHzZwrn/5xcl8DNhXE4dm27BHcnt7uYPd0CubIHY+u2LikBI4ktuIcCy4lAiVA2dqFOLFz0NYUdjDPbnnPdwDc9t2PLW9CHKWPqAcHyZVwCTFECEduJNDuac52guj46jnT7Nk3hSpLCmNJdc6zo7DtV281128LKEuTDeCSbii9KgcKC+eqkZVuUGVRzmXcYzSr6yCFo/XA1UJRWlc9NlSZdfSN1hkjMbCDLMKdjx3CpuUKvkNRRsTCb8ZcKY9sdsdvA3QIw06gmsOHatZmGEeDeUBl+uGoWN5r4dLH/diMcy6sa6teaWlpfgX/+JfrOcsmHXEcT1z1JR56f1Ccb8kzJDXBrUspaCIbZpWfTkZqnrvoeeyVc2Mz0oMTQMtVciYxlLoPVmrZehOeiJe0Eo6ecwQkbWKzCaPmYdJs9lErCYB6gtvENA0mfMvqBAj9coSa6Pl7xWZf5elyMObd7oOtJIvktAWI0lXm7cGWBYQpCogscI0NQ1S+alKaBkLkn3+6sdqn6auq+nR+0XaMi+ft65ah6iCTvVy3ce81axzGcCqaRreB02P1N+kIDVr6XPLZ7T8mfSnVNpUrkXUF9tp7uN75OymB2S1727V75ZhVm+jLlRvujVj1ZZBPrIxa8BqFzmcfsgUGOsmzFy8eDHnyZBirpubm9kEOM+hqhbiQYUZEkroWEnVAR31i14wd8eApgoaqAo1biKj4DujXux2+kXSxJzE21e8AVffOPDK/uXGvkQ0QUarUN4gy1hIZCpcj5mA7gkz82skzIgt4DFD2zLFuZMPUjbqyrztzDA0bK+2MR0RONAMhHzkaOLFXV+9J1Fb4sDv8y5MqWLLzBFxTf5MKa3Bp7lorhToVq18y2muEpiYiCAeD6Kuvh323UtZ3yfqd6B/1jt20jJRMlIRhYtUCyUs0XN942QuTMtNlTQBPL1dQmvogHPrTNZpkpGtRZvTe38N48QXlcmvtvM4tJIqVZ1A+od77woE+bvo5qL5I/kLTI9mWUgBvaQK9rt/A+elX4ZGRrk5Klz0hk64ZhiX+oDOfaULqQvLJkl+LIYJ8+BJSM2EVt0Cd+RO9mnWNCNx5ruAEYC554Tyj0khI9MQxRVZ/07Np2IbfKbAK9tnYEsdNyeCmJjX4DeSIpA/qIx+nd6rOddn4d/UctV1Luv7tPp2iAI+Pq0XIhD2ts/KBuh1rd4AkFKxBm9Dzs9AcgUScx9Iw688pGS2qj9NhwhxtcxKqOO7pqtUPGorVDgW7L6bkHTOoNQrhnlU6HhOXpFUGbMU8jLi4z1TYKybMHPo0KGFwba6a7rkDoVpmvjFX/xF/MVf/IUSapj8I5Z4OGGGRBRKlLk3LtFR733nlNTkuDTwzYzdHpryfGIoRji1rZzpkggHgJ31ULG7twaBXQ3L50OJOkRplmrZVFR2Ifs3+HRXGaCuWTITCTMF7jFDEdUktIzPSdWaks6+Jk9kSVEWBp7uEMonJpWsRB5KFAVf7NegU4WRElwcPLFdx+mbMqMqhLREMv8NaDFVXCEvf4jOPSdUGtP8ksIkitoO+CTEeB+6E22orQhBa94Lt/dK5hsDRcpU9+IVb97X+iSe6RToHfe8c0gcooIXSkp7cY+ATzoYntEwOxdFWV27Mtul9JF0RE0LQKLHe99Qv7uGD+bxn4N9+wzsq+97VSn+ELQdT0CU18Ga8oQYZ24M5p5nYH3yvWV+K5SY5CQFHPftv4bx7C9Aq6hXhn0Z8y6thlbVgP951vvd0X0w9pyAfXlJypRuwNj7LKzpMciLbwN1O+DrOIrE1PAy3xy97YCK7ValQvQQGrS6Nri07knI18bYcUQZ9mZg+tXz8sL3EKSWGd3EkaZ9EDt3wkiKKBqtV8te1Yq01DeH/BZABsWp9QuE1fJQ8lMG/pBKehIG50k8KJS6ZD75s3DvXYN1KekzZPigN++BvvM49FCWEkqGWYIZCsPe+wLss99b1iqh7X0erp4l9YBZwNb9MJ/6nDJxty6+owR8GkAbrfshqlugB/m6nnl0XF8Ixv4XYX/6I28bSyE0GPtfUK9zbRtTSKzbVeG3vvUt/N7v/R7+6T/9p3jyySfVcx9//DH+5E/+BH/wB38A27bxz//5P8e//Jf/Ev/u3/279VoMZgMqZojqEuD6ADAfl+quffeIVC1O6X4yNMgN+YGuYYna0kUBh1JzDrd6LUxUVdMzIpUp69LSY0q9oWoBn5HFXyZKgypdXbAXKvRxUDvTvL1GpyXdKHjzX6I4KPDyPq9qhqLWSYzZUSdU1QkJNykSjo53r0kk0j4SSg96/5rEyX3aQve8cG1UJgbwyr4GdI8KzMaAsiDQWi3hn+2D9Feru/tyx24ViX2iUyiz34HJxbjsVFeOb/Iu9m8rQkLUYqTkIKoPtcEcvAphx2FVtiFW3ADXCSlvJorSJgGGRBna11KQANpNeoXl4lAT7VvAjBuCJgXiO15FUXwE5shNSE2HVbsbk6IcZSKI0MGX4Qx1qeWwL/wEmJ1YnCilIFx5F9r+l2BUbYNbuQ2CzH/nppSBrTs5DDkzqgQHqhJxZyZgSgt2ZYOqcoF0oHccg04R3AO3VFmPtm07BJnkOg4OVwED5NVju9DLG+A7/gU4fde8xJ3SGlWhYlm2J8rQZz47qvyQfDRAH73n+bVQXHbTbvWTPGgollq1tUgXxo6jkNs64fRdp5kokYjMmM3SauUJA0pwq2xQseA2RY8nE53oDrC4cw66E4O24wjtJOppLVQC8+hrSmgijxxlzty4S92B19KFGVqm1v3Qaprh3L2m/E+02la1bOnvYx4Ax1WJWjK9WspOwOk+r7yenNYD8PnW0BSdKUgScQtTogwVx3/O84WaHoYMlkJv2qWOlyFuxVkRjYzSr34AOZ1WApqIKUNWjUStYBg6XVMwzCPgOi5649WoO/pFGCM3oc+PwwlXwq7pRF88hCa64OHDPVNArNtR8w//8A/xZ3/2Z3jttdcWntu/fz8aGxvxr/7Vv1IiTTgcxu/+7u+yMJPHFTPiPmwfslFV7FUMkOhSXSwwOe9VJKRDQsu2MomuYSAS9wbIV/o8Aack6F0U0aDy4rRn2ErTXFoxk81fhqA72cIXKvj2UzIAXsuKmZSxa6ET9gvsqJVoqxZqO9WytMr1T2SKMimoKuZqHxn1SoT8GjQnDvfCjxHQNOxtOwy3pAz63Bjcn15SO5B24ssQB19G1NZxocvF+JxAQwXQVOm1RlFSGVXQUFx268GT6hqD5n3mnh+mXo1tZc/B1CTGZnVQgQht8890SGV8XRES+KQr+0beNyGwt0HDk21UryNwrlegbyKIokALassaIaXAwKCmBNg9jkRnTSNQWg9EJjNFmTTcW59AK/1Z6HueVeJH4tLbcBIxVUmjUVuAFVfR1FTFoFVtg6BWk+p2OD2fwrl7RbU+GarVRyiTYTk5rFp/WjufQKvuhzYXQ+KDvwOKq6AffQ06VUPoJhLvfiOjvYlEEPvSu6oNwdj9jIrHpgG7RSkrs+MwD78K89DLSr2kFj174Dbs0Xsw6H3KeLcf9k//VomRWss+GDufgrQTsN7//7KaD5OgQxUZqqQ6CYkz9HBrW72qHBKgsqDR3/gCXluY60LkeB9zf2iUBpOjhU3evQR9WyfAwgyzCpYjcOommecX43DzQVRU2eomx6c3NCWgf2afBNd85EYk5uGmizJpUEKaqGyEHmbxmXk0Eq6B8/fI0a4EtaVHUVzuYDahY/hWcoxQJjk7jSko1k2YuXTpElpaWpY9T8/Ra6l2p8HBzNJ2Jn+IWp5Z72omebnamZoqJW4OAHdNqdqNKrKIKNTaRD4z5+5IFAe8FJmdbYuvl4W8+O17YxJVxYvLQcbCkQTQVpN9/upOu58iVAobisyeT6yNMCOowsh1VDvZw3znmw1aR6pYyUbccjE6m/tvJ+ZJB0i2aqb8jFwXsuusEjMXCm5pjG/FoReVQNpSRXAT/RPeY2kFWFuNd0genvEUIWpNurskHYpETlcKfNwj8PIeV/07F9G4hM+ZghWuUIIQQb5Mc7HMFR+bAbZXCS96OJtnTAqqJHFtVa0iSMxK9n3LySE4Szxk5Mw4ZE0rdCcOmxQlYnoU9pLpu1MjMK24EjAcSkIhZsfgvPM3XjT2wZPLPGeoRSjlDWFnibwlPxvymVn4fbQPGOqGneY1o3BsuHcuAU27IGLzuROhqIxIpf0sR7vPdkllJsqGoo+MG51f4UUHktJ2sETFZ5glkPhCwjhBovXS2+7zMRelRby/5oKqInNCx8otcpOHWV8SlmeRT/8fmhYYWjJs9V5nmMJh3eILdu3ahT/6oz9CIrHoPWBZlnqOXiP6+/tRW1u7XovAPCJ0J/1h2phSNFcBlcVeyxL5xWQb7JOAQ21K1FZC8dlLU5job6hSpm9i0auIIG8amlzWRCYpvUjVrSDM6GvYykSOzMQWaGdaDYofT/eboQCK9Ehy9VpyMxVL2+XSqioUaeXcAV+mMXDSpkZV7YTTXgv7cl9skFBJAgLtm8ZijJQ36yX7q2rNuncHmpCZ60OVPGl/Sq+pxCg3aa6aCyUuaN62Qv9eQcAT/jDc2QlIXVfVa7nfF1RtVd4K0D4rkp9ZCdC0L3v6R7KSZvFDCS9+mEq4ybxTq1qm1D9o2TP3F+ELesempWX3K3yPzMYhTN+K34vg74m5D9KP58TSMDoyAGdyIwLpx/Qlx086nrIIzawBaaf1h3qdYTYb63YF89WvfhWf//znVevSgQMH1HNUKeM4Dr7zne+o37u7u/GP/tE/Wq9FYNaglelRhBlKX9rbuPr7qBLmUItUF0bkGbP8daB/ktKaPKGHGJqSKA1mT2tCZDppWFr4JpDkMWO7VHot4NMf8c5B6kKKhJkCb7eIJlwkbC+imVr1SDAJ+eRCzLGua9heK6HDwfZaIG57m1TQJzA8JWGYOoqTAiKlwIjKbbB2PIOEHkbMEgiaEj5rFkb3Ryp+2hrtR7CkFjtqdZSFpZoOzZsqdkgUmY/RvAWm58nAV6KhQsOl/uzL3lnrwNQ1PNXuqmWvLyOPHE3tq7TP+k2qqPHarfymhN60DRoc7NymK0Pu1mqhKnFo16E1uD0s0VEnoZNvC5nrlVbBzZWMtK1DCSIiMg0ZKoVW0+p5rCzF8EEUlcGk6piEA53Mckd7s66P3rIPgj7p8QHEQ9WInfgHavnoM/Q78xCwYT73C7BunQeGbqm/IRNjvaEDqN0O4fN7FXK0zZoBOHcvQavcljEPbVsHNDI4VuVM1JPuV74S7mCXMudVgpDjqO/RaD/kJZSR74w/pKqDbDLvXZKgRAlmMhH15k2DEn9IvV8sEZJIKI4mqAJRzUL5apG4lu5ntPDeRMybZiwC4Qso0YqmyaRBIl9xBZzGg0iEqhF3hDoOmtP9MMbvwNH963dhwxQMpuaivlSgvFhT1bx0jKfjKe2r5IlHxx8mN1q4DLKoHFbLUSQCFeoaJEj74cQd6NEJSIMbwZhHx69LdXOX/P2WQs/T6wxTSKzb9cuJEyfQ09ODv/mbv8HNmzfVc7/wC7+Av//3/z6Ki73R9S//8i+v1+yZNYAuUOiu/uOgNJT77hS1QdGgs3dMorJYwHakSnLKGpNN4y7yx9C0ZXfNC7WVKRWZ7dMfsdIleetBtamgcKuNyJD68j1ve0pB4siJnQLlIXdBnAkajmq1e+uaBttZvBG4b5uLhmL6rD3xygwVYXbv6zh9S2I62dVECkBlUTGe3PsZyBtvA0nxovGF/xe3h4Hbg4sJTrRtH2kT6BqUmJwDDrYI1JdJHO8APrrtCUIp6Pmmah1/p8KEBF7f66VEfdJFHjSZFyxPdwoYmgNrbhbdc1VoqpUoDwuVHkXCDUHC0NE2Ab87B4vipWmqR16HeeRVWOd+klE9RSa8Ztt+JD7434AVAQIh+J74WViRGcj0pCeKtKa/N/yQl971nnru/4K+/Qicrk+XiTIoqlDzju59HaduGEqwSn2GTeUh7C8bhXnvE/j2nECCvoixbmX4azz/iyqKWvbfWJygLwjj8KtwjMBCOagkNSQ6A+vqqcX0KIrzJm+Z/S9Cr6xXFTNUVWPuPqESRuTMWNp6V8Pc/0KGWS8JKPbdK3B6Lix+QaYP5sGXoZXVem2BdCyS3nd66mZmCtiOWmB3I213i8c9GZuHdfk9uOOLTs4iXKY+S/KyYTzMcBjxQ5/DqVsaZtJMr6uLO/Dkvk6EgnwLlVmdQNCHQ60SZ3skrvYtPk8t1XTsNA0e8K2E9PkQO/h5tR+mpww2lO3BoU4gFGB5lHl0gkETT+9w8N4NocYkC8/7gBMdUr3OMIXEurUyESTAPP/88/jMZz6DF198EfX19Xj77bfx7W9/ez1ny6wRqTtIGw0NmsgE+O4Y+XpI9Cajt2uSEdtLIW8LESz2PDAKHBIPiNnEGlwEbYFWJsd1VcpX7+K4e6Ftj9KW5uMiwxzyg1uLogxBY/BL/Tpmoml+R1GJDzNEGQ/ydDl7x4Wz60X1u37yV5SgSPHv6Zf8ZDD88W2JnfVCeR7QQCFma7g76iU4kfCyt1GoWOyKIg3DUw6+eMz7W+rmOXfHzRBlCLq7RAKM5fow5m/GRNREJCFw+d6iKEPQun10WyJhFAPJeFgVI9t9UYkRFF1N8dHmoZPQ69vg9N2C/swX1PuMAyeVoa/euFP5wND7jD3PwNz7nErNMZXXB4CdzyifHfKnMY98RhnwGh3H1L+VJwgJEkd/Du/1hNJEGY97kzpuz1fBNfywb52FsfdJaLtOwHjpl1TkdYYooz7MKOwz34dI8zegtkaLojbTI72lVDGvVOmSqkgh7xKKX04XZdRbp0dhXflphrcJpTFRClCGamYlYJ39oddGmSQah0r2WhrNTuJc3/hie6akv73+UYYoo56fn1LLvuBjxGAu6niizJI7qKOzGj69C0RjhXv8YtaOaNzBpXuuOianQ6l6H9yUSDgsLKxEzDbw3o1MUYbon9JwbUBDLLa84pJhHhQ7Mg//zbfxYv0Qnm+L4HBDTP2k33033oEd4XMjU1is25mH2pS++MUvqvYlGlgvNRSlliYmv6EBo5kn1ybUrkFR2jcH6aeX3JR+tzkFtQG4M2PQqheNPwu9T96nu5hbAwNgZU5KFLBpXzQhcHso+51Qap+hdrniIHW7eAKOzBGZemVAQ1nYQsBvKhPJqRzXBiPTVOFFjTreheyNgezzJrFkfM7brmkZuoaotQk4dcOLm6c2v2tx730hn466UnKt1JR4RH5L2aCBKy3btdEAjrUDF3tz3wGm9LT9e5+DHO6BnJ2EnBiANTHgtecYPk9sSLa4+Rq2K1NezfQh0Xdjwe9FGfKSAJPwRswyMgsc/xL0QAjO9dOQQ11w+m9CJKs/1OskUUXnoO16EXEr+32CrjED7S17YF74Lozth2C07IY9Pwt552L2lXEsuGQ2HPYqM7147uzrbnedg1Zeq9qGyLAyI/o1DTI3hhKawqrFyb6dWfmz+EYXznAPtPZD6lca9JGInI1r/dSyJtSdP6rAcYdzJA3NT3utTdzSpEjYJMpk/z4Hp4TXUvHYl4rZbFiOhr6J7NsRGaRTS2oRb0g5IUGGbmhkgwIdOuo0TrViHh07ATlyF8bIXZSaPpT5QpCJiLoRovbeHUcA8LmRKRzWrWLmt37rt9DW1oaRkRGEQiFcvnwZ7777Lo4dO4Z33nlnvWbLrBHULkQDinyomCHIk4MihumO/2zUixpOhwaEFN3o3LmivFJEWTW2ClQ1syYVMwutTIV7x5m2aRJgcjEb8y7UXVdiJq6teFHqJlOZskVqp5M+P0odyznN2KLh8Gzavyl9jH5PVbrQ7ynByMox6E9BF84VIc+LaemdzaUDEddfAr28Bm4y7UgRj6iqjYUqKtvyPFoIEtdTPjSO5b0vKcqkIuu1YNj72+h0xvP0SNUNiegMpGuv+J25wvTEFdteNSVJvTznqVWSkrJmJ3O/LzoLmVqH9IqabFje6+TDQ3+Xc5qURpUUgnIJCKnvZqF6SYmhud/LFTOLxFZJ4bCT+yXDrMRK5wEikuBWppWgc0Yu6LhG1c0M88jQNUcKEmPoOiN5LvaeK9wbiczWZN2EmdOnT+Nf/+t/jaqqKuXZoOs6nn32WXzlK1/BP/7H/3i9ZsusEanBZr4IM8T2Gigj1sOtFKOd5s0wNwHr0juwb56BOzcOra59sfpjywgza7C+6ea/BQqFGKUED6pUoBa5yjQrIvJgIciItyKUW/UoCXpm1UR62hH5IZEvDfkUpEhVndGUS1a4sVMSWhRPKG2M/k1FhmR+TctJpr4ETVskA7lp/1wp2ZzWcTpGgxDPQC8XND99fhzO6D1oxRW530iVJanthAxv05ORliCKy+DOjnrvKa7KPc3iyhWnQ+tIkdtqvklTaknpSiukR4kSb35kxCvKk8l/QoNWXgetskGZ/6qnyBA41cK3Wux16m9I+KW/ywHNI1UdWlGU+8sho/OFbktaL1qnXOuT5m+z1Qn6V0gCE7S98ICQWR3aTlbqdi5aYTtjPB+zXJB3GaflMGvC0hS+B32dYTYZ6ybMUKtSyuSXxJmBAa93vqWlBTduLPEFYPJWmKETbL5Ag53GCpERp03NJpSYQnG8+vbDymBUK849aCpEQoaDOcvI1a1x/6QGqOl3KAqMkF8qv5YntwvsaRSqTaiqBHh2p0BbjSesECQmN1eJZRGqKfY1AH4vt1oJB+01Es/sFGiqFEqoaasRyh+moxYwRVJEEVHsbch+sU/ToHmTTw0NFujvi3xI+sp4ST4HmgWOtQvsb3JhJK96fZrMaYJdVSzh04B9tVGcvwPsyTFvmh8lNblkjjveDxEuBXIYZxut+2Gb3hW5E5uH3rIn6/toGsJfBJz5AZxrH0Jv3pNDQRLQWw8Arp01kY3YVZuA0X9Redm4yQhrM1wEbfvR7H/gC0IrWfxQ9NpW6K37lU+OKK5UIoe5+2kY9Og4Cs2XnLHph1aVPUZOq2kBku+jtiejM2nysxTdzGijpO8uV7Ld/iZqY/I+E3X8atyZ9X1kukzpTIyHT3NRWZz9YNdSRa9zmzSzOpRi2JajsLY8LOHjVKYVoXNn+g2IdOi852fzZGYNkOR9l8OaQFS3QBoszDCFxboJM/v27cOFCxfUv5966in88R//MU6dOqWqaNrb29drtswaGv/mW8VMNuTUiOe/UNMMYfqWRdVuBSii0pUCEfsR1z352RVyKxMJLtUlwNV+ibPdEj2jwI0B4Kc3pIptT7/bTgPq53fKDMGAnqOY6rB/sZrGpztoqdaUATC12lF/Pfm5UFJSS7WAfuM99T757n9DaVjicCvNZ3Ga5Gnz1A7PmJcEmCd3CCXmhIPecpGvUs8I1PRuD7koDWvJVCZPQCWBiQak6bJHXZnEE+0aDNgoGb+GHZVxJGyp5pPUkxS0bs/tEvC51ILkDWgTd67Ad/QzKo1o8YPTobcfhFbbBve9/6aeci6+Db2hU0VhL1TR0MVSeR3MQ6/A1pJVMMO3VHy2fuT1zCoXfwj6oVchfQHon3wLz7XMorJIZghGu2otNIkB6MGwmo+RFGbU6xXbIDqe9Cp3UvMuroRx7GegpV+sUTWKpqmUKaf3Cpy+Gyp5iSK3ySR8YXqBsBJrlAiz8GkKtc7GziehpXm8aCVVMPY9r9ZrYd7hUvie/NmM6pawX+ClPWJB8FOLo3vJW+nm5cIwoG8/BL1xV4aARUKRefAlCIrzZhQ+w8Wxdk1VpqWgj6y5Cti1TSCQXsLGMDkI+HXs3EYieKZmXFsqcXwHHTtX6RPd4uhC4ukOoSo604/ZVNVMQr8/3y8emU2BGQrB2PU0RG1bxnlZ1LVD33UcZpD9ZZjCQshUM/wa88Mf/hDz8/P40pe+hNu3b+Ozn/2sis2urKzEf//v/x0nT55EvjAzM4PS0lJMT0+jpIRjSYl7YxIf3pZ4ppMGEvlb0mv3XFAeEnrbfmxVyOzyo8FyPFU/hYbiFYxE7gPr7I9UFYHRug+FuF8mLBfn7kAle2XjtYMCJUFvex+flbjcJ7G/wfWuB6RnwntrmO6o6the571vPmrjrataViNEuqP4fKcNMzEDGSrFjSEd5SGgJCxg2d6FLA3UKQaSfs5EgJ5RqZKYfnIp+6G5ow7YWU+pIi58po5LNyUO7PS8NShliaZjaBK3+4F2GqjGxoCiUszGDDU/TffmTYMRtT6DEi2VLirkmPKIkUXVuDIawN6qCDTX8rxkTB+mbT+uj/hwrDGO6FwE4bAPzrUPIKqboJfXeZVWug6XzHFvfAzf4Vc83xZ/CHJ2wjP+bTu80IYlhQ73zgXo1U3QKpuAyBSsQBli0QRcM6REsoAzB01IuI4N5/qH0Pe/CCNUDDcWgX37LMT2oxDkEWOlWp18sEfvwFdRv9CS5U6PIfHh32X9LI2dTynBh6rx3Ng8Ep98X6VLaeESz8/GMOHOTcLpvgjfE69nGPAq/xryfqF5Cw3C589p0Bu3vGQmR3riHmkH5PuzFGlbysBcfW5kqOwLKsE5X8iHc+VsVKqkK/IZqy4Wys+CtuXBKS+anAaLRcl9mGFyMR91cPq2wDMdlF5HRuresZNE8e5hgZZaEs03x42ejdgvyT/rnSsS7bVARXhxP+wbl4jbEsfaBEKBzfH5MfmLFZmH03MZ+vYDEGQEbFsQhqkqadyeT6G1HIIZzt3WzDCbjXXL3HnttdcW/r1jxw5cv34dExMTKC8vz0hnYvK3YiY1cMtXqI3JnRrNaFvYqiXZft3BZMx8ZGFGNYYXcCpT3Ba4lyOJgxie8nrnyfyXkopGpoE3p5fvBGOzlKgDBHwCcUvkTKcg096EqyFUVqUGlN0jMtkmKLMKLjTYfGo7cHsk9zJSlc/2WoE3r2p4ZR/QFwX6zmef5rZqwOzuhbvnAM70eK1S2d5H6U5HW2k/msDArB83hzTcHFrezkTHhP2NPvywO4Av75uGO96v2p+yNY+4sxMw6tvhxCJweq967x25u+x9TmwOoqwWFkV0N++Cn6Ktkyyt3dJS26aTgDvYBfTfzPoZOR1PKGGG7js4965nfY96X+9V6PXtSjxCIgZEpmFffDvreyk5KV14Uf41VB1zH/4vfpPuIK/6NnXBSQ8mN1HLEzKpkuzmYLZteUMWi9lkWK7A5DzwnfNJ1X0B7/q0irzCuFAtJ3QuoevEa/3029L9UKjPl2EeGTL577sMp+9y9tcbdqm0RIYpFB7rsLuiooJFmc0Ula2MRfP4+6K4XbqzHE6rad+iFPkcTMTWYECn6QXdykR39VaqEaQ7fYRMa+fLBsVQLwTqrJI+kQoxWm3QSPOjO7ZU+LFS0hNVxSxMe5V6R/Xexka1zitNM2ELSnpW/ikrrbdM//zSVywbVEmi3mdDrpR4ZCUgaObhUsj0tIVs86fqndSCpNKUsk4zGRkiJeRK6U12fCFBacXp3c/rzGMhffvPBlUlMcxqOKsIByzwrUxilfs3q50eGOa+4PMys8VYt4oZZnNDA9R8bxGmFgO6hc+JJUCxaaNvNqDGq4+ipak0q00uzFi2F/WuWnqWtOEZ2qLJbjZqS733U5sJVa8MTUkcbPZSkeiDnYtKfHALqCtd9F+iqhkvDcareCFD1/m4xL1xTz/wmQKxhFQ9+TUlEsPTZD5Md2Pp7ySicYGJeanaMnpGJAIGsK3M+3dRAGis8JZncl5icJLMir00kdcOCNXmQ5UYZUHgaLs32KD5XB8Eukc8DxnTtqBpEvUlLrrHNHTWSTSWJNSydU360TsGNJQ70J0I7BtnUL3jBbVeu+qBXdTOJB3E4Mc7N3yqoErXXBxtoFYb6skJA7H5rJ+lVloNl8RTI6C8UpzpUYg9z0JWeEZ+YnoA8tI76jWpGzDqt0P4fJ7XUVUTZMcJOMKAaUchL/xIVcksJDBohkpekvFZ6E9+ATq1FQkBe3II8sr7Cya+VNWi1bXBHbkLUVyhjHnpOXdqGO5YP7TKRoiUTwz511Aykj+k2pnIcFfGorC7znrVNGZgURyyvdYpsVqSE7PmFCU/cmoJI+Nr2v/mY97+RsUOvjw/bzH5gc+Qahui88ET7Z6QQIee28NeNVaqpZXJDhmbE9SWSf5OPkOo9qa+cS9BMJ+CI5jNi0idl3efgE7nb8eG1E04o3eB66fZf40pONbNY2YzkQ998/nGh7dczEY9k8q89peZm4KeB34oG81UzMClsRKcbB5HWeDhhRX72mlopVUwydh0k+2X5OMxFaHSaqlaHSgGe+c2SvHK9PMYnpJ47/rywx6ZGJLxLhm2EpG4VBfrQ9NkvivVnfiGcs/Y0BBAMJkOFo1aGJ3TlLEw+cPMxbx2qLZqAcd11HTfuabhmXZKGKBrDIHuYYmhKe/itb1GKEPikRlKsgA+7pJ4db8nxFCbVO+4VJ4w1aU0fzLvlap8fDrqXRzvafBakWi9Z6KeGEPrHfJJGNEpaFfeAoLFsPe+AtOJQg7eBoa7vFFIw27IyiY4egD6e3/lfRDP/zJMNwY5Ow7n7hUlSlDktNGyD3EtBB1RyE9/DG3nU8rfxb7w1rLPkgx0jV1PwTr7Q+WVYh54CTEthP4JiZ5xXYlCrRUOGqsEgm5Exd1T9RtFWTsthzGV8OHGgEQkIZQnD61PUM7BCAZhGN79BCs6C528Z3qvwB0fUqlKlBIlSqqVUKaFvG3Gjc5BzoxCRmbhDHarO2xaVYMSb0SwxPOTUdUzNpyZUdXI4PRcgoxMK0NfSo2itkky/EU8Audusi3L54fRegBa2dZJTcqHc+V81MXYnBdpT/slxcqXBoHWGqGqn6qLJHyszjD3kRwajXutptcHXExHvGPmzm0aiv10h8NFmFTyTcBG7JckhlJLr4TAnVHvnFse9s6PAhK1ZXncB89sGhKxuLrO0OIzyutt4bzcdhBuoFh51fkCfIOEKRw2x1mHeexQ20O+3/GQc5MZqSpbmRK/DV24GJz3P5IwQ4P1zdjKRFUy5AlzpW/xORJISNR4cbdQkdgpysISL+wRuNQrMTGXirv2fFtSogxBosxHXd57UlyPAnfHJF7Yvfg+ITTYUuDsLZkx74FJSq3QoMFVv8/PU9edwNtXUj4zHmd7pKrIOdgscKbHS7rQ4aBvXKB/MtOvhky5T+4BRme9fbSxnEwYBT64mTnv4WmJQy0CjWWl6kKGvFP8bgT22e8BsfQVOgWUVMN38GU4VC3lujBlHO6diyq9KAVNIzHYBd8TPwP4i2G7LtxgMQx6//4XYN+5rIQcqjqh2GeqRKELdjk/rf6eRJn3b9Id1cWL9Yv9OrrHKfkqBH161PseS+rQOypwaVB9sgvr0zcp8ezOMOqo5CmJbiWQ+Pi7GZ5I9sURaHXtMDrS4qylhN17FXJiaOEpZ35KiTSUorTwfVM7VWQW1pX309Z7Bu7oPRgHXwKis0h89H8WK8rI9/f8T6A1dMLofAJaWmIUs37owkHCMXC+K3Ob75/0zOqFiqfP85MXs+Houo7ZuMSpG564QMzFBEZmpIqyb65kYWElhHTU8fz6wJL9cELi+bTzI8M8EpqAGO+DdTnLeXnf85DVrRu6eAyz1vCZh8kKJYjkcysTiQcUk50Rv7uFoYKQioCFgblHvHOgGV66ziaDfFHSRZkUVJlxpluqVqIUflNDTYlQAsgbhwRe2S+wtwkIJytgUkxGkCHKpKA7gyQCxS2vid6SGs7fyb5cZ3vojqy3I5VVAFf7MkWZFMPTUAbCJAaRU1AkQQNNkdX34Eqfi0NN3rybqwU+7cle9EiR3VbyEK8d/oxKRcoQZVJQNcn0KMzn/x5iR/8vlXyQLsosQNUxNz6CgA29eTdMTYN9+V3Ytz+FXtcG8+BJJYjIyWFYn3xXTYfQT/6KEopIQFqKEl3GJcShz6jfnYa9uDxoZv0eP+0B5qJeP7kTnYV98+OsRtXuULeXbJT627mJDFFmgUQUzt3LcC1vGiIRgX39w5wisH39o6xtfi59rpTOxDwWaH+6eFfm3N/idh6fuJi8gczY6diZbUuiND5KuWNyY0kd1weWP0++Z/S5po7VDPMoGFY053mZntctPvcyhQULM8yK5r95C1UB0GDKz/4yKSqDFqbjJmYT+pYz/53KbnOymIyUZZVCfmpz8h46tfWkYdkuesdyd3n2TXiGuSmhhjxtskHzTc2bLvQH0ipglkLVPTu3AUVhr08/F/1TGsrCi0aouRKh6AI5Qv67tduBUDkw1JV7ogPX4UJDuDTktenkQE6NqBhpESpWIgUJFpJEkltnYF14C/aVn8Kd9EQQlzxlXvx/4Dqual/Kxd0JHW4RxUcFMGP5sg6UCGpZsRzvexKOA3c8y6ggte4jvd5P14EzcDvn+5zhO0qgUetGPjI5Esm0ogq4E7nn54zey/kas7aQaJnL9Jr2BUpeY5jVIJGbtqVskBA8k9sznKH8vrnc50dqqWVhi1kL1Hk5181CuvlDrzNMAcHCDJMzdSafW5nc+RnP5dbP7QMpKoMJmJqL25OLkb4PitikcdmrGh4/4DWifIDJiTVcB5Uatcr6PMj81HtjCeWRsvKHlHYqIKO9VSd6P0vheX6s9m6x8HqqoeB+WeHd6ULbiuu9Nt8etbMx+UE+Bwky+cNqmwnv0SvDuxmTF/CGyBQY7DHDLMMlT4Y8F2ZkdAYiEMrvOO8NaGfaVhTD3ZkgdlfOI2A8RF7lJk1lomQN2hSyWZnTa9m8QKMJL72J/o6SJdINgn2GhrZqqXxiskEpFKbuGf0GfN6+ki3Gl6ZLyR8v7xMwhVSpTXc8O5VltFQJnOmSCOqUCCVwczj7+5oqXIwnO5JovkEfsKPGRWO555VAazE+J3D2rkDQDyTaj8KEAX3bTsjbn2SfaONuOFLH/zkLfHnvttybR0U9pGZ4/k5FFV4y0sxYlncKaGXVwLt/A/HSL2N7lYOx2ewHlPZqB8bsIGwrjmIjDk0Es1ZEFAfoe/T8QyiVQatuVH3m2aD0BrW8mg69oRPuaB/0bTvU8hPkfWP3XYde2wYEPONele5g+qAVV6n3qtQpx1IVN+7MOLTqppzzo2VhHg/kA6Vr3r67lJCfthElbW7EojGbCDp2kjF8VZGLfdXzMODCFRq6p0O4OqCjaGv4eT80FUW0j2U/P5IJsKlt+VwRZi0g7zZKP7So/HcJlJSYTEtkmEKBbwowy6AEGCKfW5loYCX87C+zlPqiuEpEuPmwVTM06N6EHjMkgBxuXT4Y0zXgWLtQkbrpRsGDkxLvXJX4/nmJH5yXOH9HqhSmdEpCyZjsJdDFPCVPfPcc1N/74eJo2/J5k+BD8x6elHjzssTpbmAXpQsl05nTaarwBgrhADCbILFFoq3SzbqeNI0Lvd6hm9KdTu62lUj01nUdP7ik4SdXNRXX/cZ+V5Wb/7C7HN+74keiql2lGSyjogGiuBL/57z3qzRMlXiwDMMHY+dTgCtg37uORCIKY/cJT8BY+rl3HIVLfkUk9L7916gqEagsWr4+ZUGJ+jKxkOxk3LuIIy3L30ea2bF2IBz0Dkp6MAyj4wnvgm3pvJt2Q6Zitel7KCqH7+hnIGPzsC68rVqunJG7MHefgNa0G5ruedq4vhDMo29AlNXAuvGRep914xNo5XXKQ8fofDL7/Fr3Q/gevkqNeTBMYa+4vxUF+bKGWZ3ioMArHVEc8t2COPc9OB/+L8iP/w7bI+fwhX3zMLSHuLGxhTDg4GALsp5zj7QtHqsZ5lGQ/iDMvc8uF9uFUM/T6wxTSHDFDLOMlCdGvlbMSNeBjM6rWFwmE7pL1VAUR/dUCJ3lVDXzgHet9M1ZMWOoKhOJ8rDAzUESWbz467YaocSOdChq96c3Fj8Xqs7oHvF65p/bRRUwycYa6Yk95F/TPepFZzdWCNSVQQk5qaoOKpQxNImTe4UyBSZPG6rS2V4jEElIjCX9byh+nmK2KdGJkivIb4b2MUqDIrGHXqfo7K4RSmnSsKfRRWOli1sjApYt0FDmoLFSg+NqqC+TmE8ArVUO7o4KXB7QMw2CB0iccbGjhkQ2Uy3rm7dCeH736whHBiAHb3ntN427IUqroUsLVcUBbCun9iMNoqIeZkU9nHvXlJGuEifqt8NJJICSIohAEbSJQciGHfAd/zycvptwp0ZUFZvevAfwh5RASCKHMEz4nDkc3x7G+KyDrjEvLru9ykF1MRBw5mBXNUPaMRiNO1Af6cLLOxpwayKAuYSGyqCN9vIYgvPjcEJN0JNx2VII+J76LJyBbrgT/RAUl928Ry1bOkJKxC+8nWHQS1U+lKjke/rnFp7TBWAP3ILTe3Xxj60Y7K5zKpZb334YvuNfgDPUpSpnBCVQteyDVlQO4eO4zseGJANtiWd2CuUDpeKyQ96+GY1LJOI2fP7lBtIMk45lxSGGbyt/rAUcC+6dSyqdzb/zSZJvNnIR8xov/UxTJvrkj0ZeaxVFUEJ7NO7ADrgwksdqhnlYpO145/rjn4NN1yNz0xBFpTCadsOJR70LHt7MmAKCN2cmtzCTrzceI7OeH0WQK2aysa04hr65gGpp2lnxgI71KjJ58wkzhM8Q6sLwie2eGS9tv1paexJB6UwkqmRjKuIZBVNrEjE4BVy4K1WU9sHmReuSH1zI/HtKZTp1UypxZk8TUF8OzMeAt656hjHHOwTujUu0VQMfdkmMzQKfPURtTUJVgtAydQ1DJUVVl0glKFEc9oe3NLy0C3iy1YULCU1o+PY5eo+LJ7cLJRQJKXBtKPuOemdcU9U16fv1T26F8PLuNoQrvNYbOXgd7sU3gY5jOLFjL4TrANF52Gd/AASLYFDljOGDOzOGxAffUvH02tGf8QSJkgokTn8bSGjQX/gCDNeC1A1Y3ReB3ivwPfU5mIdepiWHc/cStJ6LqG09iJomlWkMbfgWnPPn4DTtgq7uiEklhODTHyKkmzhY0wbXXwR9ehyyqxeObkI//nnAKIUbmVFVNtRSpR04CaOuVfnZWDc/Acb7YR75DBDyMtIdMgnOlppELZu3zqq4b2H6lABFQlQ2nLtXoDftghYqgWg7ADTtJkMmCB54bEgq0/m7dGdeYlu5J8BSSyGJrbQ/Ve3TkKUojWEy0BNRJHouZH3NHbkDY8fhx75Mm4mYreHCXbq5INFQ4e2HZPr7/nWJgKnh5B4HfHhkHhVhW7DPv+md/9sPQqtsgozNInHmB+omonHiywC4aoYpHPiwyeQUZvK1lcmlRCaqWydPCCZr1Ux1MJGsmok8kBmmUMKMC+m6EEuSijYL5BVD5dTZsF1vEJeLsRmJ6hKqUHFVhDVB1TT0oL75mtJMUabY9LxqUtO+eHf5NFO+N6UhgRsD3i/fOZ8tCluqihhieNoro3/7Ov0/c2VGZwQcVyiB6JU9uROhCGrPCvqEupuZYnDCwY6RN1WFy8IyjvdD39YJaRhwppLmNtE52FdPZa5LdBbCtWFffAu+p7+wkGjkvPsNVTmUDok5RlkNnMjMQqKRe+cCQI9kpZF6bmIIeksCWrgUTir5iAyoB2+qNZfpCQxWckWoam7Oi7hyL76FpR+BOzEIvbpJbcfuSJYvJfW+qSFIx1LCjEp3yGZSpFbcXehxV5VGWVqamMeD13JI+wBwb0l6mUPans3eFsx9QMeSFdp25fwUUFzxWBdpMzE1nzzvOcDd0eXpaLbDPk/MGpA6L9sJOHTjZSl0MwfeTRiGKQQ258iLWfdEprxuZZqfgqBWiU0qHDwO6sIxRG0do9EHLOlP+YVswnam+4FEqiVFNBmQiEHQpuVfIltTxayfepHSmLW8NqqVSM1P/f0KX0fQzP7vpZCZcEquWG0XMA2Auo8y50Miw5InSeTUdLgkyPlX8EshUSI1UxLxVjBZVWa66n0mhLmCiOoLQKamSUZ/q7XaqYmLrN42C/NOrYMQEIHclXXCDCwaiK8wvcX1ZTYa2qbvZxNhmBVZbX9n8XVFAubK571cN0cY5oFY7YC+2n7MMJsM3qKZrBUz2ioD2I3EnZ2EFuLe75Uo9jnw6w4GZgOoCT2AmW9q8EkVC2kGqoUCmee21QAN5Z6XTNzyLiBJhLzaL1GVvPGiaxq210qUhyTqyr33kRRCwkpJkNomFqfpN6RKgyFfm6WQ98VMskKH2plaq4GOGmrHEIgn9zMSWqTjJYKMzniCC/lltFZYKgEpbgvlEUPzNoWL2yMCfl3iSx0jsPRKVBZpqC6hUnKhqnZofaYjdBdTqoSa9EoW0iCqKoKYKfmSklT8poQ5eht6cQkwPwtDJiBLq+GqyqksMVN121UiknnwJfWBGPueg1O2DQkRQNyS6nP0aw7EnU8hisvVn2g+H9CyB7LzCehkCJyssiExiHrHdTuu0qSoUkf5w4RKYDTu8oyKqa1ON1XFjZydUG1VhDSDKm0pww8mbSW1qobkPwX0xp2qOsho3eddxNHdN6HBGbgFrapxQcRRIk1xBfTaVpU2pfYBmvf0KNyR3kWhKYl0bNX+BOpzJ2HJF/QEY06KW/d9mB50V34p1MrIaTDM/SB1H0RlI9ymfbDCNeq6h6qEfdYsxM2fLvOqYjKh82BlGDjY4kITArYj4TMFZiMSvROUQsjmycyjIw0/RKgEMjKz7DW6RqD9mGEKCRZmmKypTDTAyscBhqR2AvKLqMwd6ct4A/DKoIX+OT8O1szefztT8u6Dau9A4UFtTjvrgRuDUiUapYZwYT+UiaFPDeq8NadkpKKQwNtXpBJRvL8H9jUJvLJf4ieXvOfIy+ZEp8B718iUdHFeNHh8aofAx7e9uYzOAMfaBLpGJa4PLJoH0/uOd2go8jv48SXvNuPnD7mYtUx8eINMFZPVMQLorBfK88Z9+6+89p1n/288ud3EubveNNMHqCd2CtwZXvwWaRsgv5tbQ1K1ZhEkCj3R3oGygAPtvf/izefFX4Z58GVljqtaeFJ/X1yhfBesj78NJ0p53Qbk838fl/oE7o7TfLx5lQQ1nOh4EppmwbQSKgEJlQ3QpkZhX3nPa0lSH6YJbfczcEqqIAa7IBMxuNE5+A69AuvSu5Czi30qWk0LjD3PQAt6gyXd54do2atEEzk9mpnUcOAlOIZ/oRxUBkIwOo7Cuvz+oiik6TC2H4JW2bD4p4EQzIMnYV35KeTtTxfnTUbIB09CpKU/uIkYnP5bcG6fXRSw/CH4Dp4ESqu8lkBmXTB1F8/s1NX+RlVoKSjt7Il2geBK5WYMk0QPFSG+92Vc6AX6ehbLO8rDZTh+4Gehmy6XlK+Arrk4tl3g9C1Necukjv8tlRKHmgF/tvhBhnlAzHARnIOvwDr7Pa+tKYUvAOPgy9DDLKAyhQWfd5hlUOJFvvrLpAZrZELKrExVMIG4o2Mydv/668KAskBbmRzHVQkSZLabfl+dkl3euy4RT+uLtxyBUzcWRRn1965nCByzhEpX2t9E3jIC1/u9yOwjbZ7wc7Rd4GCLlxB1vAPYuQ34uaMC43NUmeMlQaWgO/9kmGi5iztdXOp4/5qXdJGC/ub6ADA8A+gnf8V7Tg/iYq+LoanM9ZyYAz667aKlVlfz3t8s8EynQO+oRG1ZpiHwB7ekMlRFUVL0sKNw+m8o415j55PQ2w7APPCiiqF2B7uhP/kF9T7xxOu4OUyiTOZphC7S37suYEtdtR3aWhEQj8G58OaiKKM+TAvu5Xcg7ATssX5oJZUw2g/AuvBmhiij1nPkLuzuC7CpOoV8DWwb7mgf9G07VPUOLaPR+QTMw6/CoWWkapckIhGDde4ni6KMmqCjjH/l3MTCUyQMWVdOQU4OZc57YhD29Q/gJj1m1HunhuHc/DizqigeQeLM91UsN7N+JBwD1/ulGhRSahrtbxSTfaBZ4OaQi2g0S6UXwywhFrNxpQ/om8w8fk3OA6duCSTsQrw1sXY4UsP7N0RSlFmEzgck/sdTPfEM8wjMR22cGSnB3L4vwN77Kty2Y+rn3L7P4+xwCSLRwrxWZbYuXDHDLIMGa/mayERGoZTGpMw6mRUp8dkwhIvhiB8VQfvB+nlXMEXczEQSnliSa7uni/LioCfg3BnN7QV7rU/iqR1kBqxhcl6ib0Kgb4KMdr0KmLtjJN5476Uql5FpSmWSuNaffXok+FB89hePefO8MyZVW1I2rvcDNcW6OnhbrkC/54G7jKl5oSoKRqY9Y+GU6XFNKTJar2h+3SMS+5/8eTjTQ8pUl4QQelAJMbUPOfeue6KK4YNZ26rao6xABbpuZz9QRBIkdgkY0oReWQrn+kfpNr6Z695zAfqe52BfeQfG7hOQ80nX5SW4A7dhtO6nW7EQ8Qis7vOe2GKYEKFSJfSk/tataVZmwmr6A10ZlT/p2F3nIYorVSUOCTNycjD7vMf6vbt1pl+1L9lpFTWZb3TgDN+BRslNzLqQcGibl+qR2t9of6F2Q7pr31knOKODWRU6dt6dyC6+kNhALaSc+5gbupmRrX2X6BqlVmAXfr5MYx4RumHVOybROxZCwAwh6GtEdHaxlbWzXsMKrngMs+nI0+E3s+HCTB5UzNDdbLvngmqFoKYTaq9xZ0Yhwp53BbMy1LpSGrAxPP8AV0fkAZL0zyhEqOokvd1oKdPRxYQl8mnJxVycpuVd1HsDQg+qcCFxJ93/gloD6TkaNK6UCDU9Lz1zYs2L7l7pgpg8WdRyrnJTkpajPhknvLDsMbnMXJgGIpSioZdWLaQdEdTXLWfGFitd7ASE9GZKyVArJULN0mcZDlN5CzCfQz0iIl65j+ohXymqXbqQKcGQhJZUBYxtqWVMF3RSlTAuvZa2PssmSfN0kh9iejVPNpKGyeQHlEs8Uq9Te1UuRY95ZChefun+lr4Pprc3MUwuyBNlpd00GmePlJWYS54rs0HnhZXODQxzv6Qfz+l6Ztn1FR/vmQKDhRkmL4UZagewbp5RkbvO3Suwb3wC585lddNdlFZv7MJtIsr9FiZiprrL/EAVM2mtIIUE+bQsTVtKpyzkfU5UMUbGvbkoDpCA4l2YrpS0lJ4iIyBVNU7OeYcFJZWrwQJFcy8uE1BJpqbJr6Yo4E1LLecq+ykJMFczO3NQHBSqoiWd0iBNS8KdnYIoWoyIFUXlEGW1i2lJVDGSbHczNLli8gbNB3NzEIYBpE1zGSS0CgkRLlsQBrMiNAjDXEyHSiUvFVdCJ2Phln2Lby2uVD81qqZZIfJWGQynEqGSxsI5SVbpCV33ljUHWllNXvpzFQqp5LTUvlBV7PnLEPRKvrbhMvmFqYsF7zXafmg7ou0pRcjP+/BKqOP7wr+9z4+q1wg6L3AqE7MW+FY5nvPxnik0uJWJySrMBDa4BNUZ7FIDJr11P2R0Du5Qt6ri0GpauY3pAagIkMAiMBLxobE4R91xtooZqnIoQEI+iZ31AhfvLb/bRwILiSCErmtorZa4PbRo0pvOngaBcPLC3dToolRibHb5hfy2crmQbkYXGLsbBD5KmgGnQ0JQfRlwbcD7va1GoL3SQkdFFPpUH4QVh9vcgEmnGK4RgN9wVDuRqUs0VQD3Fq1SFqgoIq+ozGUiUYoe6d41NDhprxHAnU+hOQ5E0y5ode3Kv0XOjKsWH61xp1e1lojDSQoYZmwCHTWVuD60/AqczJTDfgkj4SAxMgqjZS/swVtZe8P09oOwL70Ls2UvSJkiMShblYve0AHX9Ex9pT8EY8cxaGVVSsR1xweUea/vmS/BodS2ksrFv6tvh3PnUtaUKWUAnEp48wWgVW5T01qKVt0MkRSn6KcyE/70R8s/dN1QRsXM+kFJY02VEs2Vmqpcm49LNFcJZWQ9NiNhanSrnq/WmZWh9K7OWon6cAzBxAS02VHIolIkwjW4ORlaUcBnvHbY5goXOysjMGeGIOKzcOtrMW+UYSIe4AEzsyaYmoOaUmoHX359VVtKyZN0vOedlSkceGtmlqFiIzfwboe0E3An+qFVNiozWrqrLdoPqUGdSN3dZu4Lv+EiZFA7k/++hBl1p5+qEQq0YoYEl4ZKiZgN3B5aNOGlO37Hd4iMu4BUEfLsToGPuxb9YqhC5UCTQFFgMb2pKCjwRLuGsz0uRmYW/76+TOJgi4bzd7yZ/N2nwBuHJPY3CRXNnSr1pgtcSm+iRKgbSYuTXdVxHAj2wjnz/sL0tLvnUFNWC/3AS7Df+qb3nBPDvqYgXEmeG4vrSfHZR9o0SNWmoy1U+TyxXeBccnkIusN5pF2oahmn+4J6Tm7rUGKGde7HC0IKTYWqRMwjryLx0/9PPed+8h3seP5XkHBc9IxqCw4yZWHg+HaqpnHg+EuBuT5IswL6wVfhXH1vMVmBRJbdz6joa6OuFe7UENzYvJeMdPl9yOlkdBQEtPp2ZfCrJZORDMOAW1EL6/xbmUbBNz6Bsf95OJq5mMrkD8E8+ppKekLKmFc3lbhCItDC5+sLwNz3PKwr73ueMqnnq5th7jkBYfoXnhNlNTB2Pw375ieLRtmBIvgOvsQxu+uMz3DQUWcos+7FVj6ptuXndwsEA3yOYFbHHzCwt2oa1tnvLx4XqHpGN3D06OuQBlXF8SVyLgzNwdGKcdgkUCdFb9rzykLFqDryOnR/yUYvIlMAhIIGjrRKdd0ynNZBXFcGHGrREApwZRtTWPBZh8mAvBGoZ3MjW5ncqRE1Yk5vWfIEAz4APwzlAUv5zNAY+74+QorMLlCPGaIoILCrXqqqFPKmoJJruttOz6cTTQjcHpYqClsmbU2oK+femMTglMCOukUvlfN3pUpkIt8V2n+oOoY0xE+7JQ5TUtM28vuRuDlMAonEK/uESnuiahra18iQeEedgGlKGJYnuNhXFkWZjDSge9ehn/wHELNjiIkgPrwtVRn5Mzs9zxdan8k5iVPXJZ7dpePkHge6psGWArcGJXZuE0pSom2BlvXqPYlDrQLF5fXA5CCFYCNx/q1l1S0qYen2WZgnvugNZEw/3LFu7K9rwM76gPosaV38mgN0fwy97RCGYkXQgy2omRuAPdID48gbykdGyVq6CefeNVBRj1O7A/HZWYTCfjVvc+cTSgihKjlh+ODOTcG6egr63udhBMOwE3HInovL0ptogG5feg++Z75Il3TqGd30wymtge/YGwAlK9EX6QsqQUjzZVbfiUAYxoGXPP8a8rMxfKpCJl2UITTTD9GwE1p1kyc0kZhJFTcBtgtdb2K2gVM300WZ5PMW8EmXxPEdnljKMCthR+bgXHkvQ5RRODbscz+G+dTn1TGOyY5OaXrnf7ysElFGZmFd/wjO3ufgC6T1hjHMQzAXdfHBTao+hrpGSl3jjM9KnL4lcaJDoijIYjxTOLAww2RABz2qIthIYYbiaikOe8FPgnnkdqb+uSCm4gbKA/chuOiGMlouZPw+DeqSO4fni+266B7xkpIGJpe33xQHKXaaRBZPYKG46h8oD9vl76UB5DtXJV4/KFT6kWdUuvx9PkPi2U4g7AOc3js5l132XQUaduFbN2vwyj7PDI8eFFG6FJpX0a0LcPYcwie3PFPhexPL30ctW0f3PA957T3l65QrxcgdugNj+2HMOAEUmYBz9ZRaFyPLycStakF5cRgBLQHn6lXIsT7YA7eWfz5zEzD2V+On/VX4TNMAMDcB6+wPs85fs6nqKwzNiiExcDvXJwR3rA9aWjWMTt5JyZSm1SDR5X4GZMprJkgGJ8lWKOaxQAJMutlvOrQf5EozY5h0hJOApJtA2SABNzYHhLnqIxcutZvmuoEzdg+aMlNnYYZ5NCi2fiYqk7Hsy69d7ts/kWE2CSwzMhmkEms2SpiRrqMGhqIot7km82CU+m3lu9A3e38XSdQ+Vqhx2fcLdQCR4LLSfpIqKEmF+uScVtpAcaVEKBpwUl++8l9OLLmLm46VWDD/zeZ/k7GctGyNjWpZV1sfV+gQVEkST6YdZYMEG/KBobuk5FScIwJbvTURUxVGcC1IGujkXJ+4SnoiXyvysFkJrzUrtRy5P/gV14HZ1FDK2UqwMMPcF6tUha54zGLU8X2FV9W1HMM8Ks4q1zic/sUUGlwxw2SQip7bKOM2OTvpDfxWSD1hHgxqWakMJpQws69qbvV2JhJmCriVKYXrem171HK0zCTX1FBXKjE0JbFrG9Bc6UkQk3PAmR6gutgzjyT/k5RRNpnwHmzxBoY0udM3gOm4Zyp8opPalqjlSGI0zYcmnfoygd4xiSI/0FDVDNl3Pev7yN/E1Qw1TSXkaLkvTsiEVx/thSirQHWxjt5x4Giri/oiupsp0DXhV4bD1K8tZofhTgzCbNqlPGWyzjtUolKZwmFah2Qykh2Hvvc5aFQ54tqwbnwCzIxBL63EzEwCRaUmtIptcKZHlaeLVtWg5k0mu9SKpFXUw9ICGJsFRNMK+72qZEl+2OQ9VVwBOTuhpqdSmBwLzvBdIB5RJr7ZcGIRT83yB7wqmhy4FI2tWplMaGw2nleEV9CXjWRbIsOsCh1PyMhcVXbkSGxjckIG6zmlFzov6FzxzDw6dP1E16x0rXOgwUKJaWHGMnGx31TXb2zSzRQam2qT/qM/+iP8/u//Pn7rt34L/+E//Af1XCwWw+/+7u/im9/8JuLxOF577TV87WtfQ21t7UYv7uaumNmgWip3ZtS7WEpF4TJrQk0ogaH5AIbmfclB+QroekG3MpGP0nwc6Bkh4cU78ZMHDCUy+c1F0YTEitfLBMbngE/veGa9jRVQLUlCAsFkKhOZBL9+0Cu5Ja+ZuRhQEgSO7BBKvBmekegeBg40AvubNLx9hfKNMqGYVorI/ijZndN4oEINDOR8mtudQkDvPI7hiA9X+4Hnd7rYvU3gct/y9Wyt9pbNHe8HolHs63gORxvm4Yz0AnduUS8OOht3Y+eBWsREGPK9NxfmQRHZ5GezFH3nkxhJFCEkYgiYEtqhV5QRr9N7DXbPJZWMZHY+oQQUSo8KX/2hao3T9z6jLuRlbA7O8B1VbqTXtUFsPwQRLsf3L5jq4ov+Rqttgzvcs2zexo4jSkVT6WyhEui7jqvKHWpbonUkHxiz4ygkCbuhzBYENzILl/x5+m4o0VGrbYWobYO2pFXBpbvA0VnYdy6rz54q9wyK4Q4VQTO5LD8foG26pQq4O7b8tV0N5HHEqUzM6jgmJbsdhX399LLXRP12SJ39ZVaCPLpQ2QSM31v2mtbxJISfj5fMo+MTDl7ssFGuzcK5652Xi4tK0dyxH5NOEXzkibi5hrIMsyKbZmv+5JNP8Bd/8Rc4cOBAxvO//du/je9+97v427/9W5SWluI3fuM38KUvfQmnTpH3AbPpWpnorjqlMHHb6JpS4rNR4rNwdbwIdeGJlT9fiswu0LhsYjYGvHXZq5ZJMTwt0VEH7GmkO+7eh0P/P9PjZlS4kIcF+cQ8t2vxOU2TGJ3WlPFoCuXlMi7xdKdAdZHEpz1Azxiwt0ni+T0Cl3olJuY8818Se3Y3ioy+0rgIQex/HVrveYih26ptR5RUwdl+HIlAGabHvHlQddC8+U8AAQAASURBVFlDhQGfCVzrlyoGmyoGaF0aKwV0uCryGjPjCHQcgX32+5CRmYX5KPGlrA7B/S/Apo2Cep4oxWjnk3AGbsEhHxcy4A2XwWg/qAQPzRL48Y0gXtltoxgRJE7/3UJbEVXAuKP3oG8/DLGtE3JmzBOhhAabzHrJvyaJnaygMQ+9gqIiiUP1MdUXprfugwgWwem/4bVtBYu958pq4Vw5BbTug1bZoLxgEp98V71HzZs+jvEB6E27gIrFihknMqu8cJRAlXpuZkyZKPuOvQ4teWfctW3I8X5YF99Z/Hxmx5EY7IZ58CW4NU3QknHyzMZB+V876jSE/BJdw945K+gDOuuFqmTz+7lDm1kdn8/EfGU7xG4/9J4zSjRWhuaN+yDrOuEK3+a5QN4ALBGASal6fdc83zPbUucH0fEk7OJahFQfK8M8GkI4KEsMwLrw9sJz6jpjsAdlB1+CE6ZzPW9rTOGwKbbmubk5/NIv/RL+83/+z/i3//bfLjw/PT2Nr3/96/jGN76BkydPquf+8i//Ert378aHH36I48ePb+BSb042UpiRiQhkdA4apcMwawqNuVtLo7g4Woxzw8U4WDOrWmCyoukqsrwQSdgS53syRZkUt4aAtprFVggSPrK1HVG1DYkze7a5ME0dlqPhXM/yRmh65myPxEt7aBoSB5uBS/3ATERiX6NQlTqk/ozPSLx5SapUpdf2e+4xUQt473oIzRVPoe3gQQghMRkzcaPPj8piiuwGrvQDCXixwTUlwPEOoYQe0lZ6xyV+ckni1f0aaDbaS78M++7VDFFmAYqpnhmH+cIvAVODEI6FxMff8WKi9z6rRBUatNhd5wF/EFX7XoCUIQRFDPbVD7J6vThd5+Gra1P/1l/4e3DHejNEmYXPaG4S7shdPLNjN+SH34Z+7A0kPv6uam8ydx73jKgTUTh9N4G7V2HsfUZdoPme+pwXVZ0UZTLmTalVDZ2LT8xNZYgyC1D1Tu9VyI5j0MloPD4Pi9YnyzdJiVC+4s/dt4Ews35YrqbMtCuLgAPNFPXunbeoAu7mIPDCbjLnZmWfWZnZqIv3b/lg6m3Y3VmHoOGobevmeBCj1wRe3S9yecMzJKxLge9dCmJvwyG0PbELGlzEXQOXhgOIjABPq7Qc3g+ZR8O0Y0jQDZllSNh0Xn7qs6TGb8CSMcwWFmZ+/dd/HT/7sz+LV155JUOYOXv2LCzLUs+n2LVrF5qbm3H69Omcwgy1PNEjxcxMlsHKFoUucGnArq1zyYqULgRFzKbhTo4qBYF7u9fPBLizfB63JsMYjvjxRN00qkJW1rSZjTA+fBz7JW3fwytMlipnSkMCCcvF3THPQyYb98aB9moNpgnEyI4kh8cLpcekxE66kO0b91qi3r+xXMghf5nDrd6/L/Z6Vih3xnXcGc+MYI5OAHsbPbGHjFCpSobaOrzlzSQSB0p3vQJhJSCHbuZe8f7rcMvrgOJKiBGv1YgEE3pkTnBaCTeEIW1Yy+KqU0i4U6MQJ74ETbqw+3MlKAHOYBeMmhZY5XVKqCFjXxJSsokpypiaoqyTLUw5pznSC620Gq7rqMqfnO8b6oHWvFd5yajY61yCJO0PW9AMNB/PlZGE56k0MkMP+cDmwAxDWI7AfNzbfk7fDWatrCzJ047qfNgvqeKTuNKv4Ur/8g+KTbiZNTOZXuG8rAIDMi+RGGZTk/c1v+Qd8+mnn+IrX/nKsteGhobg8/lQVpZpGEn+MvRaLmha1PaUejQ1Na3Lsm9GLEeuq/EveZdY1z9Ucbg29YumuW24E/1eG9MKppzMo1EbTuBI7TR8mov3+8oxHc+izVLP7gZ4zOTDfplKWvLI/7t98hFfX/+5i/ufzhKh9vEg8+bTzEfyYZ9kGCYT3i8ZhmEKk7wWZu7du6eMfv/mb/4GgcDaGYmRgTC1QaUeNB/Gg+7ur2cbk9N/EzIyDa28Du5Ir2fGSUOe2Bzk3JTy0WDWl5DpYl/1LAKGi0ujRUvECM9jRm5AXPbj2C+pTYnafnJRV+YJCT5TQ0uVUNVjZKJLbUL0IJNgmkZTJRAwvVuCQdOrMssGtSuZxqIXTUN57nk3VwlEYtSi6fnD5KKhXEIn9+Hk+gRyhF/QMoUoUOj6TyApWaiuI/fMG3bChQPnk++pBCVlAFzdAvvAG7AOfx5O57PK60WZAiuzPcDRTJWMRGKqsfMpmAdPwtz3fDJ1CdBKayA/+J9whQZ9246cs9brt8PWA8DgbeU5k8sASSVCUUy2L6AMqlPzyTrN6mZvGTR95XnXtQO+5N1y+kmVMzkTobaemWU+nitpm6aWvWyQ10xqf2OYlTB1iZAfKA0Bh1q84/uxdoHqEm/7Ks7jPqZ82C8rinK/Rp/pRgVIMIWFoPM9BYJkw/R5rzNMAZHXh05qVRoZGcGRI0dU8gc93n33XfzH//gf1b+pMiaRSGBqairj74aHh1FXV5dzun6/HyUlJRkPJk2YWaetgtpjSIwhDxmtphladRPcwW44o3fh9F73DrI0MGPWHbrwbCmJYCTix0xCz4uKmcexX5Kx76FWz5diKTvqPJElBaUkkckvlWR/dFviw1ueYe9TOwS210L5yxCm5uJwa/aR4pFWAUE9SQAu3fVMfpW3zBK2lXkDTvKgSWhCLQeJP8uXn9qYNPQlO4h8sHG0XWStSznYTKlQnnjkvv3XMBo6lLiyFBJbtJIqyHf+m/JdIeHFOf4LuFH2HH7cV4cfdFfi1GwHpnZ9Ftj7AiYSYaWdRGQAxr7nYbQdVAKrdeEtVQ2nDH2f/CzclIDz7n9T8dUq0nrpvMNl0GpaId/9a285JWB0HFu+MkKDsfsEnO6LMPc9BxEogtH5ZNYLNm1bhyfepKCI7oosvlX+EPTmPdCpH42gRKk9z2T5JOE979969dL5eK40NBcHW5Zv8fTMkTaBgMG9TMzqFAc1nOgAttcK3Bryju8XeyWqioEX9wgYucOgN5x82C/p5sDexuzXFnTeY38ZZi2wjACMPSeyvkbXBPQ6wxQSeX1v6eWXX8alS5cynvuH//AfKh+Z3/u931Plm6Zp4s0338SXv/xl9fqNGzfQ29uLp59+eoOWenOznhUzKc8IQV4W9LNiG7REHM6dK+ouubZtB4SW11phQVEZtKAJiaF5P0r9FPHjIZQwY6tYaVGA8VgUZU3Gjl3DEsPTntixa5tQQowvLS6bRnokyJCHS4rRGeqtl3hl/+L7XAhUhCVe2itwY8CLyy4NAp3byIxXqst7uoNI8gwFxpAZ8J1RicEpb1+jgUFFmExNgf4JYHxWqoFBfZl395a8Z8ismCp9qKKH/DVkcj2k0FDsl3h5n8DNQakMi8MBYGe9UHHW5NeixM4iqkQT0I++4cVVD3Wp6GnRuNsz2yZBZM8zyo8lAR8+6fdlGB9PR4D3ugN4dqeE67p4tTOOwPyoqmCxL7+3+AHZCTjJqGmqoqGKGuim6hEz9z8Pd2Io6flCcdnbvaoXKSDKWwBrBsJJACWVMI+9ro4LVEknSiphtOyFm4hD3/UUtEBIbZe248L35GdVehOlMdGdM71ptxJY0ovA9FAxsPc5aJNDcPque3HZNa3Q69sXEpnU1y0p5ErCPPwKnP5byiiZqoH0bR3KDDtXlQbzeBHSRX2pQOkegRuDLuZjQkXdUyoTRWXT/sgwq5FIOJiYE/j0jsy4/rnWD0TjEntzF+QxSahak25U0PmMzpNURdNUKWC5ErbtqBuoDPMoqNtOph/mU59duLZQ5+XWfZCOra4fGKaQyOujZnFxMfbt25fxXDgcRmVl5cLzv/qrv4rf+Z3fQUVFhbpr8Ju/+ZtKlOFEpoeDLkz8xvoJMzRITHnIqDF/XRu0smolBnBJ4uOFBpplfgtDc37srIhkpDIpqGomVwnpJoYG9UUBYF8TCTLe52AmI7LTIdEmXZRJQcIIRVMfbSNhhSpqBH58iUyDJY62e9Oj96REHRKBTnRKNVz8sMvFyIzAG4e8Fil6bioi8YML3gUuJS7tqgdmosDHXRJhP9BA2obmmS3Snd2qYokntwtUl3oGiz+5DIT9FM3teeTQ/M/fkRicBl4/oGGw8Q201hqwb30EOXADYt8L0Pa/5K3M6B3YP/3vEDufhtHYCb2iEfOOmTWNijh/V+DFnQ6MgRvQa9uROPP9rO+jyGxsPwzz2BvKR8q5exVO93lode3Q2w+qyy135A7smx+rqhXj8HNqwI14FImP/g8QLIax/bC6ICOBJPHJ99UBg9KYhG7Cic7BvfpTOLOT0LcfhN5xVAku1p1LwPQozKOvAyTIpIszoWKIigbPeNwfhLbEy4rSn+wr76vtX69rg6htAaLzsC6+rT5YrawWIm2azMZgSw0/uAjsb5Q40uIJlT4dKhltcFbg1b0ya1Uaw6QTtwUu5egAujNGwjp73a1EwhEqddBvSjRWeKLMbBT46Q2pBJsXdusozusRBrMZ0KwY7E9/rK4FjB2HAaqIjc3DOvemMv81nqGb8oV3ncpsXTb9YfNP//RPoWmaqpghl/rXXnsNX/va1zZ6sTa1MEODwbVGxiOQkVmvzSANEmdEcIVmZWZdqQhY6JoKqYQK6rlXJFtQYBemMJNC1zwPmWw4rkT/RG6zVxJtqIqFKl5IfKF3UrXKm5ezJzNVlWiYjUqMznrPff/88vcNTknUlwG1pcC5u3IhmpsigNMZmxVwJSWKUI+Nq4Sh6SiUuLOUSEyiNOAHnCjkhJdiJC+/u6xIX4zegVO3A8Lnx+hw7vWmaiDb1SBun4Ne1QzE0wS9JbjTozAoGSkys1At5w51q0fG+8YHlDhD1SvO2ID3ZHQ2sxInRTKdQVBFVzIRyuk6t3ze4/3Qs3jQ6MEVYlYo/YHEIcdVXljLsGJ0uyD33zOPhfmYZyp9qQ/qsZRUChrDrASd8yjsIBczES+hj8nO5Nzi+a1rOPM1Oifa+dsJxmwipJU8L9ONk6sfLH+dztvhjW+xZZgtK8y88847Gb+TKfBXv/pV9WAeHbqoXY9UJndy2IvCLuIo7HyixG+Bajmm4gaqU9HZSWGGDIC36mUprfdKlWN0hz712awWIpYu/tDfxXMMHGl+tP+Rz8pK807tn1Qdk0tYSkGV5Hd6gLLdGgRVn8Tms75PmkElcFM1SSC9nWsJJKQutPSs0nYoUma5mg5h+nJnGpGxrtAX/70SyWouqRZEV7HZWef9MNV3qUqxh32deSyY+spHpdX2CYZJmbGvBLW4MrnxrVKVxl3pzJrA52Vmi8GHTmYB8hRJVQGsNe7UsBeFzQfRvCJkuMoHZSpuZnrMEBtgAJwvaJrAjrrcA0Dyjwn4vNdJRKE0mGxQskdKSPEbLtprVk5luj0M/OSM16efi7Yaar1y0TfhRduTf002qJ0jYADdFhBx/BDN+3NOUyMTXGtemQRXFmu5gpHQVO7C0DwxRPmuVDXmmKDu+cvQPwNhVRGTC6N5N7SQVzWnWoVyVGmRSfGCcOMLQq/PlbYkoFU9RHysL6hMhbNOMVTCrZZ5Ankn5RIuyWtmPW4sMIUHVYhWFGUXZ2gbosQmJjfko5ZLBK0rkwvG8wzzSBiBrKEFC9cLWzAtkSlsWJhhFiBRhljrC1uqvJBzkxBhTlzKN2gAHjYdTMfSRjraYsXMVqbID+zJYgBJ7Ub0SOHXHRW1ulTQpDuu5BuTSqfwmTpaawQqswwGDjQL5TXjukBNLYmjUkW4LqU8LJVZ8MSchoFJJUHgqe3LPTXogvmZDgkDNPgAfkL+2hSDXd26bJqi5QDcQAmEP+SlLGkWnt6+3EK1WPnyCMgrXtWidfmnnsHv0osmoanobJsiulNPhcugN3Yumzd5zojS6rQPMwzz0MvL74L5QzD3PqNEHrV+pg96+4EF8ScdY9+zcFMR2A8AmQqT8e8yYcj0qWWiz4fZeHymxDOdctmgkPaBJ7dLhIJc6sCsTjig41i7pvxQ0qHt6kQnpXtxL85KGMnz3lJTdBK0DrVoCAVYIWUeHTMchn7w5eXnZcMH/cDLMENbLy2RKWyEpDKJLc7MzAxKS0sxPT2dF3GgGwV5YPzggsSBZhoArl0TizvWB7vnIvTth1VLA5Nf3JoMYd7S8WrrxEKsuX3+TTUY1WuXD+S30n6ZsD0D34FJqXrmGyqEuvBc2u5jWTaito6xGc+boCzsGfkWZ4kMnYtKzCeAwUkJ0wAaygXitsTYLCUvCSQsiVBAwKdJ5R/TPylVixMlMpFYJJMeN3MxMgIWqCkGLNvF5LyL8TnvTmZVqQZTSExGvZ4rOsqPzkjsrI5Di8+p2HqpaTBqW+EYQfhDgUURNR6BJXwqnWlo0kXU8hKhKAUqgDjcySHI2QmIkipoZXWA6wmv7sSgEmmoisYx/DADmeIIec2QWZ9KhZLS27Z8AWihzO/WJUEwPq+8ZyiBQSuvhSiugpalj9yhac5Pwx3rB/xB6DXNcM0gDP/D3UWj0yElQbmTI8rDxlvHGogARYRv1ca+/NoniVjMhi0FRqddZZRdWUTnLA3hEA8GmQdjLupiYh6YmAWKgkBNKaV7OfCvVwpCAe2X0ZgDy9UwNO35mVWVCFXBme28xzAPi2VZEIkYnKnkebm4EnpZDaQvoJJ5GaaQ2DxnHmbdSZkmrnXFTGrAxqJMflJkOhie96t0E3UXmluZFvAZQlW+rGYCaZoG6PqAxItF95nsUAUNDQBqS9PfJ5Tpb+rf6T9Ls4ikxUvm4/PpalDamFZ8QtSl6RP15fT+IBAKAuXVWU8CwjAhjFJQFT89ipcNdE1owSwtRBRfmSbiZSvFTAkwWnqFTLb3GSZglEELp5Ul5UCnaYZKoFc3rUkZKIkvSlxSVUDbH2FKzHoSoB49tS+xEMM8GkVBTR2Pm6vSn+VL4/shGNDpjIISVUzIYgyzPijxxTRhhPm8zBQ+3MrErKswQ9UX7swYREnl2k2UWVOolYkMgOes5MWo0FSP01ZvZWIYhmEYhmEYhnkcsDDDLBNm1tL81xnp9dKYWJjJW1K99HMJ74tXLRvkM8PCDMMwDMMwDMMwzLrDwgyTIcyQkZu+1M3tIZGJCNzhHmilNYtJP0zeYWoShnAxZ6UpcroBya1MDMMwDMMwDMMw6w6PlpkMo9NHaWOSZM7VfxMyOgth+OFGpgFdh8gVqcvkBVQgEzRczCUWDwdKSOOKGYZhGIZhGIZhmHWHhRkmo2LmYduYpGPDvvkRpJVQ0bjSoZ+l0CobIHQ2aNwM7UypVqaFihk7sZGLxDAMwzAMwzAMsyVgYYZZIP4IwowzeBsyHoXeug/ClxmTy+Q/VDEzHElLzaKKGYuFGYZhGIZhGIZhmPWGPWaYjIqZh2llknYc7vAdaBX1LMpsUoKmg7ijw3KT/kK6yRUzDMMwDMMwDMMwjwEWZphHbmVyR++RPANRXrcei8U8BgK6q35GkgbAnscMCzMMwzAMwzAMwzDrDQszTEYr04NWzEhIFYktiqs4eakAIrPnU8lM5DHDrUwMwzAMwzAMwzDrDgszzAJx6yGEmelxIBGDKKtZr8ViHlNktiYkIlbykGCYXDHDMAzDMAzDMAzzGGBhhlE4roTjPrgwQ21Mwh+ECBSt16Ixjyky26+7C61MyvzXsSCl3OhFYxiGYRiGYRiGKWhYmGEWqmUI03hA09+pIYjSGjWwZzY3Ad1BxE55zJgAiTKOvdGLxTAMwzAMwzAMU9CwMMMs+MsQvgeomHFHegEBiNKqdVsu5vHhN1zMJ9IqZghuZ2IYhmEYhmEYhllXWJhhHqpiRjo2HIrILq1m098CSmZKVcykhBmOzGYYhmEYhmEYhllfWJhhMoUZ/T6TmHqvAq4DUdGw7svGPB4ChgvL1ZBwhNfKRHAyE8MwDMMwDMMwzLrCpQ7MQiuTJgCd/pcFqpwgo18Zm4eMzUHOTUGra4cwfY99WZn1wa97kdlUNVNqcMUMwzAMwzAMwzDM44CFGUYRtyR8Rm6TX/vqaUgrBuEPqTYXrbETWlH5415MZp0rZghKZioNcsUMwzAMwzAMwzDM44CFGWahYiZXG5Nz74aqnNBbD0D4/I970ZjHhKlJCEhELQ0I64DQIK34Ri8WwzAMwzAMwzBMQcMeM8yCx0w241+ZiMId74dWuY1FmQKHIs+paoZamQT9YpgACzMMwzAMwzAMwzDrCgszzKIwk6Vixh0fUCN2UVazEYvFPGb8lMxkeRuCMHyqfY1hGIZhGIZhGIZZP1iYYRSxXMLMxAC0cBmEdh9xTUxBCDPzSWGGKma4lYlhGIZhGIZhGGZ9YWGGWRBmlpr/ykQMMjILFFds1GIxjxm/4ahWJgVFZrMwwzAMwzAMwzAMs66wMMPAciQcN4swMzumfopQycYsGPPYCeguEo6mtgeumGEYhmEYhmEYhll/WJhhEEsmIvuXCDPuzAREIARBJrDMlsCfiswmA2A2/2UYhmEYhmEYhll3WJhhVBsTsbRixp0dhwhytcxWq5ghlM+MMv9lYYZhGIZhGIZhGGY9YWGGQTSxXJhRA/J4FAgWbdhyMRtj/isgVTKTUB4zCUgpN3qxGIZhGIZhGIZhChYWZhhVMaMJQE/bGuTcpPopgsUbt2DMY0eItMhs1cImlTjDMAzDMAzDMAzDrA8szDCIJST8Jg3KxcJz7vyUamVRD2bL+cyoVibTr36XiehGLxLDMAzDMAzDMEzBwsIMg2i2qOz5aYhAWFVQMFvPZ0a1MplJUY6FGYZhGIZhGIZhmHWDhRlGecz49MXfJf2XFGaYrUfAcDBvUysTV8wwDMMwDMMwDMOsNyzMMCouO6NiJhYBHJuNf7co5DGTcDTYgvrbNEgygWYYhmEYhmEYhmHWBRZmtjiUuBNJAIE0KxkZmVY/uWJmaxI0vMjsiG0onxmumGEYhmEYhmEYhlk/WJjZ4sRtwHGBAAXwJHHnpgGfH0JfYjzDbJlWJmIukfSZ4YoZhmEYhmEYhmGYdYOFmS1OJO79pFSm9IoZ4edqma2KqUnowsWciszmihmGYRiGYRiGYZj1hIWZLc58UphJVcwo49/IDIQ/tKHLxWwclMRF7UxzCWpl8rHHDMMwDMMwDMMwzDrCwswWhypmdA0wUltCbJ6NfxkEDUdVzAhfADIe2ejFYRiGYRiGYRiGKVhYmNnizMclghS+Q2USVDEznzL+ZWFmKxMwXMyTx4wvCMQjkK5nCMwwDMMwDMMwDMOsLSzMbHGolSndX8adnwJ8AQhd38jFYvKgYibm6LANr6VNxuc3epEYhmEYhmEYhmEKEhZmtjjzscxEJqqY4ZhsJmQmk5lEifdEdG5jF4hhGIZhGIZhGKZAYWFmC+O6EnMxIOT3fpfS9RKZuI1pyxNSkdkS09IT6SR5DzEMwzAMwzAMwzBrDgszW5i5OA29gZAv+cT8DOBKNv5llCE0JTPNWj7A8EHGuGKGYRiGYRiGYRhmPWBhZgszkwzbSVXMuPOTKitZ+LmVifGqZqbjhpfMxK1MDMMwDMMwDMMwW0+Y+fM//3McOHAAJSUl6vH000/j+9///sLrsVgMv/7rv47KykoUFRXhy1/+MoaHhzd0mTcTM1HA1AGfkUxkmp1UbUxC835ntjbkMzOTMIBA2DOFZtYEKSUicYnpiMRsVCJuUd1adug1eg+9l/6G/jYblu2q903MScyoaXKKFlPY0DY+k9zmadu3HN7mmQeHtpuFY2eEj50PSiTuqvNT6txj8efHMAzz0BjIYxobG/FHf/RH6OjoUAOS//Jf/gu+8IUv4Ny5c9i7dy9++7d/G9/97nfxt3/7tygtLcVv/MZv4Etf+hJOnTq10Yu+KaCT6IK/DCTc2XFopdUbvVhMnhA2bcSdIOKhcvjGujd6cQoCy5YYngbO3ZGIWd5zlUXAse1ASTBTEKXBwpluibFZ73cy6T7UIlBbJhfE1FTk/a0hoHtYgsamlHzfXAnsbZQIB1hkZQqP+ZjE5XvAvQkSK73Wy+21wI5a3uaZ+4eOnV3DwO2hxWNnYwWwr0miiLejVZmLSVy4CwxMejcMDB3YWQ80V/HnxzAMU3AVM5/73OfwMz/zM0qY6ezsxB/+4R+qypgPP/wQ09PT+PrXv45//+//PU6ePImjR4/iL//yL/HBBx+o15nVmY6k+ctQq4ptAaFkCg+z5Sn2eclMU3o1YMUgE/GNXqRNz+Q8cPrWoihDjM8B71yRapCQgv79ztVFUYagv/nwNt2ZXHwuYbm4MSBxaxBqYEHQQPXuGHC2h6ps+O4lU1jQNk3bdu+4t60TtO3fHKSHRMLmbZ5ZHaoyJEHmxkDmsfPeOJQgThWKzMqizOmbEgOTi8/ZDnClD+gb9yqRGIZhmAISZtJxHAff/OY3MT8/r1qazp49C8uy8Morryy8Z9euXWhubsbp06c3dFk3y517amUqDnq/uzPjnr8MG/8ySfy6C5/uYkKWqd8ltzM9EtSWdLE3+8V+3AZGZxZ/J/ElXbxJh6YRS7Y/xSyBnpHs76PKnITNdy2ZwoK2adq2s9E94u0TDLMatJ1QtUw26Fgcz3H8ZTyiCWAq6VO4lOsDEtEE74cMwzAF1cpEXLp0SQkx5CdD1TLf+ta3sGfPHpw/fx4+nw9lZd6gMUVtbS2GhoZWnGY8HlePFDMzaSOiLcJEMv24JCXMTI1AhIohNH1Dl4vJH6isu8RnY8ImM2gBd24SWnntus2v0PdLuoE4tULq+PC0RGu1dzE7Mi1XrHRzkzcjLccLUstFJAGUsZc3U0D7ZGSFwj3aFyz7cS4Ns1lJOIuVMtmYjQHleXqfKh/2SzoP5YLOS45XcMswDMMUUsXMzp07lQjz0Ucf4dd+7dfwD/7BP8DVq1cfaZpf+cpXlCdN6tHU1IStxvis1w9MrUzSdSDnJiDCmSIXwxT7bEzGfZChEsjp0XWdV6HvlyR0BZOeTtlIiaREqpItG+Q1Q9MijFWO4P68l96ZfCYf90m/ufLrdF5jmNVY7dgZTLV55yH5sF+m/AmzQecn8n1iGIZhHoy8P3RSVcyOHTuUhwydjA4ePIg/+7M/Q11dHRKJBKamMtsrKJWJXluJ3//931ceNanHvXv3sNUYm5VqICiEgJwaUbfgRVH5Ri8Wk2eU+S24UmA82Ap3an0Tzwp9vwz6BHZvy17e7ZlOLr62rVwsiC9L2bVNKHGG8BkS1TlsoYoCqw9iGWaz7ZO0TYdzDAprSrx9gmFWw29I1OW4F0U3rIJ5fOzMh/2yOED7WvbXmioAn8n7IcMwTMEJM0txXVeVcJJQY5om3nzzzYXXbty4gd7eXtX6tBJ+v38hgjv12ErYjlQ91GUh73d3YgAiEIbwBTZ60Zg8I2w68OsOhvQGyPlpSGv9DIC3wn65rRxoq8l8ju4sPtMpFo24k3drn9splt11bKkGmqo8QVW9z6/haLtAaXJfTr+beaJTcDIGU3D7JG3Tz+wUy+7Y0z5wpF0g6Nt0lzXMBhDwaTjcKlC+pNWTjr20fRUtScnLJ/JhvwyaEs/uEsvE/6piYG8T3Tzg/ZBhGOZByetCd7or8MYbbyhD39nZWXzjG9/AO++8gx/+8IeqfPNXf/VX8Tu/8zuoqKhQJ6bf/M3fVKLM8ePHN3rR85rBKa8Xn06gNNAmfxmtunmjF4vJQ2j8XxGwMBirxF4S8cYHoNe1bfRibVoCPoEDzV6kKBknmrrXtkQVMLq2OBCgf1eXSLx2UGA26vXs08CT3pcelU0U00C1E4halJTh3e2lRz4PLBjmUSgNCbyw2/ObIR8lqg6jCgeOymYeVOR7uhOIJTxPGT523j+GoaE04OKlPQLzcc8MmM5RVEXDNwQYhmEKUJgZGRnBr/zKr2BwcFAJMQcOHFCizKuvvqpe/9M//VNomoYvf/nLqormtddew9e+9rWNXuy8p29ceheyPgGnv9dLYyqt3ujFYvKUqlACg/MBjIe2o2bkLgszjwgJK3TxupKPDKFpQrVs5GrbSIcGpOGAJ7YyzFaABn90HmOYRyHs946zlXzsfChxpvg+zmUMwzBMAQgzX//611d8PRAI4Ktf/ap6MPdHJC7RPwm0VQPStuAM90ArrYbQ2TGRyU6pz0bYtNGt7UXVyPch7QSEkcfOiAzDMAzDMAzDMJsIbgLdYlwfkCqNoL4McO5do0gmiMqGjV4sJs/bmRqKYhh2KzEuKuH03djoRWIYhmEYhmEYhikYWJjZQgxPS3QNA02VgJi4B3esD1pNK4SRx/EDTF5QE0qgxGfhfPhFzHddg4zObfQiMQzDMAzDMAzDFAQszGwBXClxZ1Ti1A2J8pCLurmrcO5chlZey94yzH1XzXRWzMPWfPhp8DX0nz0LZ3psoxeLYRiGYRiGYRhm05PXHjOPCyml+jkzM7Pi+2ZjGi72+zEf1+D9xVo5z6/11HJPKTjVg3vSgPR3AE4IGIyt0VyZrUCJdDCmVeK09hxwjZ5x1fM7KqPYXuvc1zSKi4sX4p7XYr9kGObRuZ/9kvdJhnm88H7JMPnF/V7DMszDwMIMCS6zs+pnU1PTiu977cu/hl/9J/9pHZbA28G9U+v64XcjGDfq1XxcystOrPMMmYLEEBHYeijjuZ+eu4uj//e+hQvElZienlbx9mu1XzIM8+jcz37J+yTDPF54v2SY/OJ+r2EZ5mEQ8n5GUgWO67oYGBhYcxWU7l7QifLevXubeicuhPUohHUolPW43/1s6X5ZCOueDq9P/lJI63K/63M/++V6nSsflkL7ntYL/pw272e0GfbLfP3s8hn+zDbvZ5Yv5z+mMOGKGTLa0TQ0Njau2/TpAFIIB95CWI9CWIdCWo+H2S8Lbd15ffKXQlqXtVif9T5XPiyF9j2tF/w5FeZnlC/75Wb87DYa/sweHP7MmEKGzX8ZhmEYhmEYhmEYhmE2CBZmGIZhGIZhGIZhGIZhNggWZtYRv9+PP/iDP1A/NzOFsB6FsA6FtB4PQ6GtO69P/lJI61KI61Po67XW8Oe0OvwZPTz82T04/Jk9OPyZMVsBNv9lGIZhGIZhGIZhGIbZILhihmEYhmEYhmEYhmEYZoNgYYZhGIZhGIZhGIZhGGaDYGGGYRiGYRiGYRiGYRhmg2BhhmEYhmEYhmEYhmEYZoNgYQYA+R/PzMyonwzD5Ae8XzJMfsH7JMPkH7xfMgzDFAYszACYnZ1FaWmp+skwTH7A+yXD5Be8TzJM/sH7JcMwTGHAwgzDMAzDMAzDMAzDMMwGwcIMwzAMwzAMwzAMwzDMBsHCDMMwDMMwDMMwDMMwzAbBwgzDMAzDMAzDMAzDMMwGYWzUjBnmcSHjUUgrRtEFgOmH8IcghHioaTmOAxGbA6wEoAnA8EELlTz8srmOWj5YcUA3ADMAzefPMl+JmAVYDqBrQMAETGP5OkjH9qZnJwDDhPAFIQzzoZePYRgmH3Gj895xzrHUcZiO7Zo/uNGLxWwyHFcillj93Mpkx4nOQ9gJSMeCMHxwzABMf2CjF4thGGZTwsIMU7BI6ULOTsC6+C7k/JT3pD8Ec+8z0MrrH1iwcGMRYGoYiesfAvGIek6Ey2Duew6yuBy6/mDTk4kYnIHbsLs+BWzLm155Pcx9z2aIPTFL4vaQxM1Buoj0nqsvA460ASH/4gWkG4/A6ToPp+8GKT6AENDq2mF2PgERCD/QsjEMw+QrbmQG9s0zcIfv0JEU0HToDZ1A635ooeKNXjxmkxBL0HlV4tYQ4CaTphsrgIMtmedWJjvu/DSca6fhjvd7T+gG9Ja9cBp2Quf9kGEY5oHhViamYJHROSQ+/u6iKEPEI7A+/XHmc/dLdAbWhbcWRBk1j/kpJM58H4Lu3j7IskkJZ7QX9o2PFkQZ9fzkIKwz34cbm1+4m9c9LHGtf1GUIQangFM36E6fdzUpbQv27U/h3LvmiTLeTOAOdsG6cgpuIvbg68swDJOPosyVn8Id7vFEGfWko459Ts8FJVAzzGrQuZVEmRuDi6IM0TcBfHRLIm6lPcksw4nMwDr/5qIoo5604XRfgEs3nKzF6xqGYRjm/mBhhilIlPAx2KUuFLJBIoakMvj7hIQSu+t89hfpYmSwS7U53ffyxSOwb53N/lp0DnLOE46ofenGQPZpTEWAaHIVZCIKt/9m9mUfuwdQKxfDMMxmx7bgTgxmfcnpv+W1hTLMKlD7ElXKZGNsbvHcyuQgFoGcm8z6knP3MkSCBVKGYZgHhYUZpjBxHMjJ4ZwvuzPjGZUqq0/Phjs7kfNlOTMKQV4HD7B86ZU3y6c3pn7aDmCnVcosZSalt5DnDXno5Joe+c4wW0KQpAfDFCqSPL5yvugCfKeeuQ/IUya9UmYp86zvrUguUUZhJyDs7DfFGIZhmNywMMMUJpoGEc5tyiuCRZCafv/TExpEMLdPiwgUQ5J57wMsH1bwpBFJjxkyI1zJpzjkS/5jFb8cYS43FGYKj0u9EqdvsjDDFC5kaL4iBlvnMatD59aVCKbOrUzOa6jcL9L1zQNcXzEMwzAKFmaYgkRoGvSm3TlfN7Yfhua7/+QAMpQ0Wg/kmhv0pl3QH0CYEf4g9JY92V/UTYjSKvVPSohorsz+NnotnNJbKM2pYlv2eRWVQzzAujKbl0jCezBMweILQIRKs76kVTV4CU0Mswp0/myoyP4anVdZmFkFunmU47pC27YdLt8MYhiGeWBYmGEKFqpiMQ+eVIkdi08K6DuOQCutfvDplVZBbzuYWcKiGzD2P6/Snh5oWpQi0rRHpSZl4AvA98QbCylKhi6wv0mgZsk4hC4an98tFpIjKGLb2PccRElV5nzCpTAPv6IiwpnCx3UzTaIZptCgxDrz8MsLVYUpRGk1jF0noK10J59hklAk9qEWgaqi5aLMc7sEgj5OZVoJPVwK39HXll37aJXbYLQfhsHR9QzDMA+MkGxIgJmZGZSWlmJ6eholJbnbX5jNhySvmUQEMjKjRq0kVFAp/INGZadQiR9WHHJuWpXqimAxpC8A/SErUtxEHEhEveUz/UqQUY8l/UuUEEFGwPMxwG96wky2OE/ykiFjYfJhEH6aVmjTijK8Xz447193MRsFfuYwa+5MYe+TFNWrjp2xiDoOw+dXog3DPAh0biWjX/KUofOq99hcosxG7pfO/AwQn1fXHnR9RRVrHJXNMAzzcHAzNlPQiKR4AnqsARqJHPQoKl+b6fn8akCBorIV3+c3hRJkSkOrt0jRAyU5+p+YgoaqZVYytGSYQkGjQSA9GOYRSJ1by3JbyDEroJOX3wp+fgzDMMz9w7dVGYZhCqiViR4MwzAMwzAMw2weuGKGyTuk60ImotRnpzxc2LiWYe4PqpbhihlmK6C6sBNRT4nUdK9SkGGYx74fUvu0d72mr56axjAMw+SEhRkmr5Cxedh9N+DcvQLYCWXoaO58CqK44qF9YRhmq8CtTMxWgPwsnJG7sLvPA7F55W1hdByDKK/32kMZhll3yHPPGbgN584lIBFT12nGzqeglVRBmBxrxTAM86BwKxOTVxfbiUvvwuk6p0QZ9dz0KBIffwfuzNhGLx7DbAphhlOZmEJGWgnYPRdgXz2lRBn13Pw0rPNvwh3qhnSdjV5Ehil4ZCIG+9qHcG5+okQZ9dzsBKwz34c7MbDRi8cwDLMpYWGGyRtkdA5yYjDra/a100q4YRgmN6lqGZfD9pgCRVoxOHevZn3NvnWGzxMM8xig9iV3uCfra9b1D+EmRVOGYRjm/mFhhskbVrrLIucmIR3rsS4Pw2w2Usa/bADMFCoyMkv/z/4iVVpa8ce9SAyz5XBnxnO/SKJMsuqZYRiGuX9YmGHyB3MFk1+hQQjxOJeGYTYdzkLFzEYvCcOsD6t6jWl8WcMw640wV/FyEvrjWhSGYZiCga9gmLxBq6yns3n21+q3Aya7/TPMSqQqZdhnhilY/CEgx6BQmcRzih/DrDuiuFyloWVDq2qAYBNuhmGYB4aFGSZvoLhT88ALy58PlcDYcQTC4BAxhlkptnTBY4aFGaZAEYEQfIdfXT4oNP0wD7zIcb0M8xgQvhDMQy8DSyuZA2EYu0+sXlHDMAzDLINHukzeIHQTWnUzfM/+PJzhO0B8HlpVk7oLqgXCG714DJPXpPv9cisTU6gIoQGl1fA982W4Y33Kf0yU1UIrr4UWLNroxWOYLYHQdWgV29T1mjvSCxmZgVa5DaKkivdDhmGYh4SFGSbv/AOEUQqt/eBGLwrDbCrS25e4lYkpZISmQYSKoTXv3uhFYZgtLc5QRbPWum+jF4VhGKYg4FYmhmGYAiC9SoYrZhiGYRiGYRhm88AVM0xeYjlS+WSYOoVs5E5jknYC0nUhTJ9X4p6DaMJVrR4Bk6anPbKXh7TiKiVqpT5q13WAeEylhGh+z/eAlpWWWd3xNXzqOYfiXa0YlQtBD+Zu2bISFhzHha4JmH5f7vlaCS+q0jChrbR8iShg29772DBz05NeJcMeM8xWwI5HAcc7hhl8DGMeEjuRPGdqGoxAaKMXZ9PhxCKA68DVfTD97C3DrN/xXtgWJB3vk9fUDFNosDDD5BVxS2JqHrg+KBG3gLpSoL0WCPvJW2BRoJHxKNzpETh3LkPaFrTaVujbtkMLFmdMbz4mMTID9Ix4VQQNFUBTpURR4OGit93oHNzhO3AGu9RFnN68B1p5PbQlF3Pu/DSc/lvKA4Has/Tm3ar3Wj03es8TknY+BV3T4d67Dndy0EsTadkLES6HFlpcDyuRQNTScXtIYGzeRMgnsavORrHfgT+4eBHkksATnYVNnwn5LgRLYLTtB4LFC8KQtw7zQGwO9p1LkNFZiKJyGK37IP1h6Hyy27SkV8mkYrMZphCxI/MQ8Tm4qWNYcQXcln1wfEGYPLBm7pNELAbDisClc+bsOESgCE7rfriBYpgh9rVbDScyC0RnvOuweARaWTXc5r2wzBD8LNAwa4Qdm4Oga/6eS5CRaYhQGZw2umYNwgiwnxFTWLAww+QNCVviWr/EraHF56YjQNeIxMm9AqWhRVHGun4a7lDPwvuc2XE4vVfge+pz0EIl6rm5mMQnXRJjs4vTm5wnkUbi+d14YHGGRBnrk++pgUAKe2oEoqIePkoDoRhXet/cFBKffJeu+rzlpecmhzzxqHEXnO7zkCVV8EEi8eG3qWRm8X3jA9CbdkO27oOeXI+ZmIZ3rgm40lve6YjA4JTAgUaJtqo4fAE/XKrEmRyCdf7NBRdYOTuBxMgdGPueA2paoZk+OIk45Hgf7Cs/XVgH9b6hbpWw4FQ2QtezR2Ay+Q1XzDBbASsWgRi/B+vqqcxj2GAXzMOvwtJNmKa5ocvIbA70uXEkPv0RlbIubEfuaC+Mncdh1bbDDPKNilzY0TnIgVtwus4tPOfMTsDpvw3z2BuAv3ZDl48pDOx4HJgcgXXx7YXn1H463A3jwEuwK6h6hkVApnBgjxkmb4gmkCHKpLAd4MIdqYQbwo3OZogyCyRisLsuQFJpO6Aqb9JFmRTzcU+ccR5g9EotSE7fjQxRZuG1iUG4M+Pesllx2N3nF0SZdKjSRkVL+kMwdz8N+8bHC6JMOs69a6pck4hGEzjTo2X1DLnUpyPhJrXV2BysK6cyo3mS2NdOA9S2RGZ9Vgz29Q+zrKCEdfUDiNjc/XwcTB7CHjPMVkB3rBWOYaegJSIbsVjMJsOZn4FN4l5SlEnHvvkxdCe+Icu1WdAcK0OUWcB1YF/7AE5kZiMWiykwNDvq7adZoO1Ms5dfazPMZoaFGSZvGJ7OPZocngEsT2+BO9CV833uUJfyf7FsF3fGck+vd5yEoAeomEnE4Azczvmyc+86JHnKJGKeAJNr+YbvQG/oVO1N7sRg7umN9amflqNhxtNUlkFrNzWfvKgkISgpviyfmK3KjNXfxOY9T4Zs0HuoHYrZlHAqE7MVUOI4HWuzQcc38thimNWw41lvtCikCzcy/biXaFPhTo3mfI0qGlI3lxjmUZCJuOf/lA0rDpnlJijDbGZYmGEKl3ysGshS0VLQ82UeG+kFYFwxwzAM8wjwMZRhGIZ5zLAww+QNtaW5K1hqSwAz2bWjbdue831a3XaVlGQaGlqrc0+vqQII+jKvvKiqxJ2dVA9JKQPp+ALQt+3IOT29aReEpqv3abUt2Zetol6ZAGsllQu/55xeVaP6aeouSnK0udPalYWTuzAZB/tyvFE3IAKekaH6qeewliKPnBVSnJhN1MrEFTNMgSLI4J2Otdmg4xsfw5j7wfB721I2hAatqPRxL9Gmgox+c0Fm3DKZOskwj4IKxTD9qtKcfBDNgyfVT72hQ133qtcZpoBgYYbJGwI+oKNu+fOGDhxsFfAZntBCyUtaXdvyN/oCMLYfhEgKD2VhoCrLdVfIT0lPAnoyNls6jjLnTXz8HSQ++F/e45PvqOfoNYLirfXGnRDB5Q7wZP6rFSfFFtMPo/2wJ5Skobfuh1bdjMQn31MGvYmPvwe9/RCgLzepVOa/hvd8MOjDsTYX2RLD9zc68GnJtqRAEcy9z3geNks/v11PL4g20gzA2HV8+cSEgLnnBCQ73BdGKxPf7WUKFEc3Yex+Oscx7Fm4uQRqhklDD5fA2EPnzOWXwUbnk3A0FvhWwtVN6HStsxRNh7H7BPS0ZEmGeVhcIwDfsTcgpQvrwtuwLrylfkop4Tv6hnqdYQoJIWnr3uLMzMygtLQU09PTKCnxknCYDY7LHpCI26m4bJEzLpuioaHisltURcvSuGxKZhpVcdlSDVYbVVy2yEhkUilKH3xruQmg0OA78UVoRWVZ4rJvqwuQ+4rLLq6AXtUA6+I7/z97/x0dyZXed+PfW6kTcg6DjMmDyTOcRHKYwwZukt71K2tXtizZsiXZlnx8JP9h+9XaWss6R7ItS7KPpd96lbyypF1pl7vLnDnkkJNzAgZhAnIGOlS4v/M81Wh0A93AkDMkwtzPIc6wb1VX7Kq69dzn+X6Rsfj8Uhjr98Ib7GE3Jor86/Wb2b46wy7bthFNaLjWKzE4pSXtsuUd2GXnw2jaumLtstV1+dHoGZR4/5p/O99aL7C+5uNZwisUy/ma9GJTcG+3s/se6X7N3MP06hZ40+P+c0BlzSju1C47MQ2na9YuW2/cAi9YsKLsspfqupxnl11YDr2B7LKDCCyjvoRi5eLFp+FcfB9e33zDD62qmQca0/u3CsVKR9llK5YVAVOgsggoyffLMUwd0LKki4hACHpFA5cDkWOSMCzOapkLBWDygkBVkWSZlaCZuTwS7KVOWTZnBmojC26xYZ9fpsTZOnkQDZuh1bRyoIjKprKhRQqBlh2c/ULLsY+/MH/xE0Pcbu5+FhrNJ3ToofmdQbJ+JffXtjobrmtD1wTMgDXv8uWXEcrY2XjAF0szzKwvKBqtIxSBQdtIAn00n0oHXfHMZMkYmtKYUaxiSIj9yodwDQt6ZSMHZSg4Q5mIdJPXS2tVOZPijrCCQSAYhLZ+ny98r+vQg2HkKJRTzIGzYugvUsymAh71JQIhqKtPcc9IxLMGZQivtwNo2Q6owIxiFaECM4pliakL3EnviAMyd7C8kJW9ak86NuRYbncBb7Sf5xHW7MZwQOYOAhmarnMAhOy9ZS7rSCnhDXTDXL930eWZlon5hU9Z1mtaNPPi87EujQrIrBZmdGV0jcqaKDKjMmYUqw92liOcBNybV+bPkMvBQ6HIgWFZAP0pPhYUzOJ/l3pDFKuPxZxCybVJoVhFKI0ZxX0NZcKkdGN0kzNwWJQ3qVND5UAz2TJ3sRLAzB0AEZHZUimF4m4yZigZjBLHlPivYrWSHhTXKpugN2+DRlkyM+QSN1coFArFyiKpt/ixpysUKwzVg1HcFVRGJGOTrJEiJ4chCiugFVdyrXa6JswdL48yWOLTcPu6gPgktLI61mjRkq5C6XWniEfh9l7niLpWUQ9BpTmuA7evk0dNtYpGaJECCHIbSv9uIsYaK/xdIaA3bIFWUA6RVwhv6DbPY9ZvgpwchVZaA5F24ycNA0k6M/2dlK4DvboJ0gxh2Ing5rDk0qs1pQL5mICcGoPX3w0UlHLdunv12Pwd1nR4hVU43uGx+PGaEoGgKREwP3rMlOSi+FyM9EGO9UPklfD2S02DpPMzNghRWAZB++R59+ycKZYHFIzhwIxQpUyKVYwVgmjaBrO62b+HTY2yGDwJtjqU2q6yABUfAWdqAt7oAORYLxAugl6+hsX3TVUesSh2bBo6Za71d7G+nSiuYp0ZLuVWKO4FZgCioAxyfHDeJFFYrspWFasOFZhRfGw4EDA+iMSxH3NAxOci3yitPc9yQOUjLc+1uawnXSTX7b4IES6Euftp1nchvNg0vNvX4Fz5cHa+G5f45m20bIfbftJv6zrPHQVr6yMQyVRbmYjBuXoc3o1Lqe9qRZXwJkfgXTs+u7yei9Cqm6FVz1pze9MTcM6/A2/YD9746zjLgr15tZtxtdcPHm0snWDleDk+lJrP3PIgZFULvN722R02LMi2J/BuVxiDk37ThRsSe1oEqou8jxycIcHfxIc/BOy0VH7dgLn1sC/OR4LAI8UwjAASZ9+4J+dMsbxcmShbhmJr6Q5NCsVqwiVnudJaJN7/PuD5rnm4cdm/h+1+BtqcQLxCkQtnYhTOsR+yblGq7aoOfedTsKWASRo0iqwkYlHoY/1InH6NS7JT12EwAmvX0xmmCQrFx4X6/Wbbw36fenIk1U7aYuaWh1LvBQrFakGVMik+NpTZkjj5StoLfhI77tvZxaMfcXlR2GfenN8+PQbn2glIJ7meRDQjKJOab3yQgyZa2ZrZtpFeuL3tHEQivInhjKAMZYnQfrCI2By82x0s0Jv6PNCdEZSZgQSCLWeSRYYfXm/D7b6UEZQh7PPvcHCIXJ7M7Y+z4G9i5xdwpLcMg5OZl+GH7eRI9dEyV2gf6MGVEZThjXNgn38XRmMbf6R/7Qvv3rNzplg+eFKqjBnFqkdPJO91M0GZ9HvYubc4q1GhWAxnegru+TczgjKM58I99QqEay/Vpq0IDCfuD6LNNXaNTcG59D7c6MRSbZpiFUEOp/bFI2xtb+79DIy2h/1/Nx3kdpquUKwmVMaM4uND5USJ7C/ylF5O2SnknpRh50ydIAoKkGhvIASRpgfglxFlf6P0brdDtu6AMPLh3krLOpkD2adSSjvZVM/gdJ2HXtUCaVicRZMO2Wx7t67lXl73BT9dkkqkei7mnq/nErbXlaLMiiFx63KWAyLhdp7l/yWh34moxEtnfKeobPSPAQUfIZNaJuJcOpUVOkdcjiX8fz/COVOsrFImypZRGTOK1QwFoWHHsk+bGJ4fnFYosuEmuLw3K06Cy4IRyf+0t2rFwNfa3OBoEm/oJoy5gz8KxcfBjkMO34b9wfOAZrChBqJTgOfcmTiwQrHCUIEZxcdGLvbgTXtokzORc47KgG75DZoOvX4TZ3CkAgE5Otv+yrzUyIxcaD4nkRHsmWmTkBDwIOfexHUDcgEXD0mdfHrjpbKthTr8TgKWnnwbthcYaUuunzIacgVliLj9EV11cnSQMqaTiPFHOGeKFSr+qzJmFKsZZ5FMBqnuYYo7YBGF9AWf94r5fam5qL6E4l5fpxSMmTsAqX5nilWGKmVSfGwECfLmEovVTQgrMFtmc+Ll2aDMTLpw51k4PRcgXf/Gym5IudaVVwyh+yK8ekV9zvm04mp4c0TCtNI1bKtN26RXNswrf1povVpZLaQVYv0CEtLNOV95PXpGLThSh1ZSteB8hKEvnBFTUfjRSpn4WOdyI6FzRPtPDzUSSruDc6ZY4eK/KmNGsUoRYcpiyHEPo4xAJQapuBPombjAb0VTbokLohWW5Z5IfcNkf02huCtIzJ2cTbNBg43UP1coVhEqMKP42AgrxI5G2TDW7gSSIowyOpUh2pUOi9ImpmetqYuzB0mMjftTmTUkUEuBmvkbpPnuRzevzLZpOgwugTLZcUirbMy4kXuDN31NmmwdNDMIvXYddMOAFgjBaNqWPfhBbkalNbjaC7zXHYa+dnfWBwkHl/L97Y4EBLY1ZH+5KMsHwh/13cIKw2jdlXWSvmYDPHKqov3t64S+Zv2i50yx8qAsGVXKpFjtSHLDq1uXdZrRshNSvRAq7gQabFm7N+skUbuenZkUC2AFUwNNc6FycuXMpLgnaBr0Jl8jcS7U3+fgjEKxilCBGcXHhoIdVIpkbD7kj5DwaGYBzG2PQqtuhUjeML3pBcS5qLQmKepLgRdr68PQW3b4o1lJOzxr72ehFcyOzmi0jh2PQ6/bmAqUUNaL9cBn4U2Opsp1KNvF2vd53qbUd0P5PJ9Ws9YPnggBt78b1t7PsOXqzJutVtkEa++zGZ0LLxDxt4XFhSk1QeflWLufxvlBvxZ9aBKY1PJYnEwrTmbO6PQisZG3mbZ9huKIxMMbBUqSovJktb2hBtjbIjhw85HOhU7b0srHPrW/wQgLpNE2zogWszhyzTpuX+icKVYeVBpHP19VyqRY1UTHoTe0wVi/LxVIJuc+Y+thiNJaiLlirgpFFgzL4t+Lvv0JiJnsmEAYYv1+6M07YIbUIMVCUF/K2LAPeuvOlEU9DZqZO58ESJdPobgXJGKcCW9sPgiRdGCiQVx676D2eeLdCsUKR8gZu5r7mPHxcRQWFmJsbAwFBbMvzoqPKMjItRQaxJysC3e4FzbZOGdDaLAOfQUap6cnl+V5kCRQKyXrxYjkQ38uHmm5sJCt5OCHFoxAei4L2PJ3KUsmR6oyOTzNaNXQPDSvR/swo19gmDltVz0SBUyWX1EAibJpbEci4foJ9gET0DXBrgQiWVMijSD0QPZtmY5LP9uBYimmhK5r9/xc3GnbckJdlx+No1c9jEf935/jAo9uUXF3xeq7Jr3xISTe+1uITQdhFFdxMJJ6MV5fB9xrJ/3niRqtV3wE7OkpCNKxo6dwIAjDWFnyi0t5XbpuAiKWNBSgQa20wSeF4m7xJkeQePe70KqaoddvZEkD6ZL76UV2U7UOfllZsytWFSvr6aNYtiz0Ys+aAJSdEZuaN02rXTvPBUhQoCCZzbEQmkl6ApnpxpTxcSffFYYBYeRlLo/24Q5KiLRg5vcI0xAw51xNemhxRwcvOonA2ADc/i4eDRDVLZDBiK+Jcw/PxZ22KVYuHGGnhK9k9oxCsRphN79IEeSFdzFXBphKK3IF8hWKudC4JLkvieFbnE1K5cZ6ZSOkyOMsVMXi6LoFRD5+f0WhWEwyQRRVcBCG/jKmFVWq+71i1aGGVBWfOJTJYu16mtMPM9rL62C27JjvonSfQE5VlElkn34NnqbDHbzBIwNuXyfkYs4jCsUcZrKuKINAlTIpVisUUDZ3JstP6tYCB38CCNZDFFfB3HQgZ5akQjEXOTWKxHt/B6f9Frzm3XBdh5/B3kgvZ+4qFIolxgzA3PwgREEpkJ8PbDrE/4qCMpibD6nAjGLVsaRvxN/85jfx3e9+F5cuXUIoFMKBAwfwW7/1W1i/flacNBaL4Vd/9Vfxne98B/F4HE899RT+4A/+AJWVlal5uru78Qu/8At4/fXXkZeXh69//eu87JWWjrqUUOmQjEcho5N+Bksg4ltUUxuNKHE2STij5Cj13fg0ZGya/6VsFZpX8nepLepnggRCMHc95ZcPJWIQlHViWDzK7432AYk4Z9Z4VgiaHYek7Bo7DkEp6abFaqYyNgHYCW7zjCDi0sRUQsBxJPLDGixhw/TikNEJ1pnhUVVyGvIcyOlxdoLy2wwIKnki2z0qecorhNRoPttvS2oWuLqFuAxgIuqxbkckKGAKF7Y0/DaNtGDAbQlukzA0f76gnPbXS5o3VFIVyodL67VteFNjfvlUMAxj97MQLq13FKhu4TZXCt5ej7bZCiYzgATgxP39oBGEQARaZH7KsDNNxy3GmThaMAxphmAYOmR8io+pf34i8Cjww+ec2vJ5PXqWc6tYeRozXNqx1BujUHyCsM7Yzif4+YLJQYjt21ms/U6yJRUKgkqe7bgDa99z/MyUk/1AWS1ETSsSegABKvVNaloocuNMTQLxKXikBUJ9CCMAI6yuQ8W9gd4rEjBYB5H1ZKKTwKbD3GdNeBqs2BQP/ioUq4UljVy8+eab+Gf/7J9hz549cBwH/+bf/Bs8+eSTuHDhAiIR/0L7l//yX+KHP/wh/uqv/opraH/xF38RX/rSl/Duu+/ydNd18ZnPfAZVVVU4cuQIbt++ja997WswTRO/+Zu/uZS7t2IgzRT7zBuQI31+g27C3PEYnCvH2E56BgqImNsfz6jnpOCBfeKlVECD5ysog7FuN+yTrwKunUo5NFq2wz71qh9kcG0W7CW3JfvDF9jKWVQ1w6jfiATNkyboRU5KRvN22MdemG2rWYexil1497ofLa8tcrGrqB+Jc2+k1knr0Rs2Qato4G30mwT0pm3Qqe3ky9xk7nkGcmIE9uUP/GAUz6fBWL8XE8EmvJNcx1NbHLQPa7hwS0DCT3MmOZi9TUBpxMa7V/103i+1TcG7fhruzcuzB9mwYG55EG73hZQQr3Xgi3CunYTX7zsm+Y1BmNsfg911AbLvOqBbsA48B+f826nvMcE8WCQmTKMISdzpCTinXwOS54wr5imItf1J2O2ngP4uoGkbrJpWOKdemXfOxNZHsgZ7FCsDCsZwxowqZVLcB7oD9slX/EB1EhKKN9sOq3uY4o4DM2YoAPvsm5A0OJSEBlHo2eqZ4eRTXpELZ3wYzsmXUmXq3HsqXQOQ/lNYBbUU9wDbg6V5/D6R7u5KQtMWBWtsDVBJM4pVxJKWMr3wwgv4mZ/5GWzevBnbtm3D//7f/5uzX44fP87TScjsj//4j/E7v/M7ePTRR7Fr1y5861vf4gDM+++/z/O89NJLHMj5sz/7M2zfvh3PPPMMvvGNb+D3f//3kUgklnL3VgTSScC5+P5sUIaCDQ2b4HaczgjK8LxTY37ZzfSE/zk+7XeO017wuX18kL9PQl2pttE+Fusi++mZwAkFGpyO0zA2+JaVZtNW2MdfmqeyThbP7u0O6M3bZ9tuXUHRRDvK8v030LbyKcgzr6QFZXitcLvOcxaQ76Tkv7G6Hac4q0ZUNABsuy3gXHp/NijD83ncVm6OI2wBtSXAZFzD+Vt6RjYC2RK/164h4Zkgbd+HNgBysDszKEM4CdinX4fe6Nv+kfOUe+taZlCGoFG84y/BbN7GH40dj8K5diIzKEPEJpE48RJn3xD29DSc8++kgjLp58w5/QqMdQ/4x3jNOj6H2c6Zc+EdODQaoViR0M9XJCMzKjCjWK2402Mc4E8PyhBybADOpSNw1T1McQeQHbZz+YOMoAy3U4nxyVcg3PiSbdtKwJmagHP8hfnagUM3uI9lx5VbjuIeoEvYZ9/ICMoQcmKYg6oqeqpYbSwrjRkKxBAlJSX8LwVobNvG448/nppnw4YNqK+vx3vvvcef6d+2traM0iYqdyKV+vPnz2ddD5VE0fT0v/sVSgX3KJMiDa2wYn4gYGZ+ujnafodFxmPzbpYzsC1zUWVm20APtNKazLbe69AKyyGKK+FNDM8JrMzi3rgEvaI+czt7zmBDaRQVBYAx0J7zbdTtPAu9YUtGm9N5FkbzNrZ7dDvPZf0eb1/nWWytTWBztYMLt3JfLh39Ek9s9FBmTsDJtTzpwRvr55FdvbyO9yn7Btt8LERhBTQrPE/wLAWViiVfQoSbgBy+lX21dI6cZJCSysQWOmcz8y0B6rq8hxkzS70xilXBsrwmE/F5geUZvMGbEEt4D1OsHISdgNffnXUaBWfYGXKZshyuSw6M5jhG8tZVdR0q7g2ODTmWOeCYHoxP9W0VilXCsgnMeJ6Hf/Ev/gUOHjyILVv8l+je3l5YloWiokwrNArC0LSZedKDMjPTZ6Zlg/RnqCxq5q+urg73La4zv81LWkHnYMZmWjqLjCjNWw55mnrzh/k9DyJcMG8ENINsN99EDJYuESCL6Wj2YAOvgoIXhjm/TWis9UIaOjm/G5tEWHfIURrTC9z/J+IaNEh+KaZsloW2xRcrI82Y3AK/dCwEpeR7zoLpD6ltX0QsWNoJoLiaX2oWnG8JRYfVdXl3sODvjMaMiswoVus1udgLs5PlmaZQzIUHgRa4UcamsVxZDtelF53vspnRr3MX7kcqFHfCYn1SZZShWG0sm8AMac2cO3eORX4/aX7913+ds3Nm/np6enDfQrbM2pxcQPrMNRHZmbFZJhu73DMJcDRjseXqJgdIvLFBaAVluZfHgsKZnShy4dB0DVURG15FS+5NyS+ZN/ql5Zdwx4wFU+n/c323oAyjcQuOCxSHc3fiyiIuEg7tr1hwebReOT3hiyMvYFdNx4KOCcixio5Rru0jZxKCBJIXPGchYOQ2EFzAIlsICFrOEqGuy7uDf8tKY0axyq9JFo7POVEDzNz3S4Viwb5PGmRGsFxZDtelnqY1mPXY3qdum4p7y2Iue8JSLnyK1cWyCMyQoO/zzz/Prkpr1iS1QAAW9CWdmNHR0Yz5+/r6eNrMPPR57vSZadkIBAIoKCjI+LtfoRd2vW5WC4bwBrqhVWUPdGhltWxfx1jBWe2WufNVt3DpUjqkL+OSoG16G+nZ0HyTIxChSM5ONwkHOz3J0h8huARJr9uESPubqO56EXpsjF2f5lpy+9/dwSK7Gett2QGbtHVG+2BQmRN16OciNOj1m3HmpoHjXQY21WZ/2yUB4PoyDS+cE2gfz4PRujPrfOwaEipgByan5zKXUmWDjgG7i0yNwp0Y5mOUdb78UoACLlwvb0FUr82+3rI6yOT+kUuVVlqbdTatZi08Y+kecuq6vHeuTMouW7Fqr0nDZOH4bOi1a+Epu2zFHeAZFvQ1G7JOE0UVs/2cZciyuC6pj8IaffMRjVshlY2x4h4gDQNaRWPWaVplE/dpFYrVxJIGZigDgoIy3/ve9/Daa6+hqakpYzqJ/ZK70quvkpOPz+XLl1kgeP/+/fyZ/j179iz6+/tT87z88sv8oNq0KfsLrWIWoRswmtp8Udrk6JF78yr0mlbodRtmAxZCQKtshrHxYMqaTiMHoc2HoFU1z2ZrUDCjbiP06lZejj+jDr1xCwdxvNtJvRTdgN60lW+4bvsJbkpcfA/mric5EyaFYcJYu9u3ub7lL89Yt4cttp0zr7EuCosNXzsO++xbMLY8ODsKZoVgtD3M7guYGPLbAmG23SPRY24jC2qhsfVqelCH/t/c+STaxyIoCPu7F9ZtHGz1EEx7DhSEgMMbPBjSLxE61QXISDGMzYcyOnaioBTWzifgdJziz/LWFYi8Yt639DIr2nc6BolLvoaSe+YNaNWtGeeHD2nZGt4PkUyNMIMh6C07IdZszDhnoqoFxsYDcE/4jlZ0zIxNB/iBlnHO1qxncWVjoYwaxcrJmFnqjVEoPiGoYJTur+TW5//ak8+YNRvYcU9bIHNQoZhBc23oDZt58GX22SqgldfDpH5DtjJvxSyeB3P7ExDkwjSDbkA07+D+n55YvqVgipWFsX4PtJrWtD6r4M/k/qp6O4rVhpBz60M+Rf7pP/2n+Iu/+Av83d/9HdavX59qp5rZUMjPBPiFX/gF/OhHP2LHJgq2/NIv/RK3kzPTjF02uTHV1NTgP//n/8y6Mj/90z+Nf/SP/tEd22WTcBqtk1JCl8WI4BJAnRASAmYtF8NkHRT+aaS1UaCDgjHzvkviXFQqRLWelLlBWRzSY3FgruNOtnmJOATp0lCHx7QgjRBXO3HgxHX8Mhor7GvY2DPzBfzyG9JIoflIo0a6SHzww6z7odWuhdG41V8vfzcPID0ZN+GnEZgWvEAEGm0vrUPX4fZ1ckBEUEYLabrQPlFHjVJxSSBw4AaXZWnFFfCmJpAoqIENk58RpjsN/cq70Bu3YjJcza8JpHtjmh402n9aBy3LMCGtCDtZ8b5Qmo0RgDA0CNovbkuWLZlBgDo1vH0GW5KjsBwaHV86F7oJqRuwr3wIg6zEq5tT+2/HoxA2zUfH3eBMGoP+TZ0fOrchuI4NjYSAXRvCsHiU2Uhm3ywX1HX50XjlrB80DJjArRHgud3LIiFSsYpYDtekNzmKxOnXYG5/DIKeB8lnDN3enRMvw9r9JLRI4ZJsm2LlQL8jEvlFfjEE6RIln6305yViEPCgU+bMCmAprktvfAj26DC08lpf6Jc0ZUzqm5jwzr4Bc/NBaGH13FbcHd7ECBLHX4LR9iA0kk+g+z1fo1E4596EtetpaDkytxSKlciSFoH+4R/+If97+PDhjHayxCYbbeJ3f/d3oWkavvzlL7MSPTku/cEf/EFqXl3XuQyKAjiUPROJRPD1r38dv/Ebv/Ep783Kz5yZW1PNsek7SOcV9LI/R1zXb8/UK9FD9HOLzJ9vzjqEHvHTZDO+bKba7At+Nkk2OCOndRe09PpnEtFNg19XDdrX/JQgr9t+kjN9UlHKUD7cjmPsGjUDSdnRPFZsAnr7bGmUTKZFF26vgUivWc9WFsTrnQMFYua1+S8WHpU9nZrNGJuLqMksOTMpuJIlwDL3/Bj0OS07Rr3Cr3zoxVRpzChWOyx4PjkC+52/zj4DBbkVikXgwadEFPbR5zMtn3UD5tZHgAW04hSAF5uCYWqw3/m/GUYP1I+kLN15Rg8KxceBBlXjk3CO/Tj7dOXKpFhlLGlg5k6SdYLBIH7/93+f/3LR0NDAWTWK1YtHDgmU9cGBj3v71klCuy6n4yZFOihzZWo0Iygzg9tzEebWw3ApmJS0Df9E0U2IwrLsdoGaPiv+q1CkuzIt9bYoFArFMobukc7VY5lBGcJ1YJ97C9b+LyzVpq0ItGDYz1ye475J5gZu1wUYGx5Ysm1TrCYWK01VpauK1YWSTVfkxE0kIBLTXKpEGReeGYQRmJ/d4XF5Tty3KeWSpyBnjnD5DJUjUUYNuSrRSCaVKXGbX7ZE6cJcykQP95kyKCqrSmuTngPn+ItJ22sL5qaDHCDJBundiDmZKtFoArarcUaBZUiEQybc6YnkyCqVNwWgh/Nhn3+Ho+968zZ4Q7dyH5fe69Ar6mc1dGi9a9ZjfFpCCAeW5vFIUtTWYLsCmpBJW28XIpYsDaPjQ+mYRgCaTWVVCc5a8igQYxrJ8iZK2TR49MkzTOjck5wpZdLh2Q48KeCNDfnBJCMIDwIJT2MXKV0Hb4spHH9fuSTN4v11KQbF6ceOvzw6rkEl1reSofHJGfFflTGjWK2wQHwoD9r2p5EwInyvM+heFx+Fd/pl36FOoVgMOwY52g99/5f8TFcukTBYc8498aKfmRVawAHsPof7YyW10DcegKAyaSoDp5Jt3YT75v8B5J6l3kTFaoDcS+mdonUv7OJ6OJ6AoUmYI92Q7R8s6G6qUKxEVGBGkRUKXHidZ+HevOIHSEhsq6oZHpUJpZU8kf6Jc+0EvN4O/20wKcKola+BfeJl1prhtobN0IoqYZ98xQ+G6CYLAou8IjinX/cXRsGH5u2sgeKce8tvMy0YjW0s9OW2n+LggjQDLPzo9XVmbrQVhNG0FcLwf9aOY2MiquHD6wbGkjp0IQvY1eiiqO8SRPcZ3g5zx+OwT7+WWoygsqkFsmEoaJTuHkX6NJNGCV4+5xcEPbpJYGJC4EwPELf9N+SSPGBXk4lw14fwku5S3KGRHuxrJ1LpmOQ2Yqzbi8SZ1wHSlqHdOvQV4NZVJLrO+4EUCN5mjPTB6T6fOj+isglO4x68ciUMOxmY+dymKNzrp+DeuuafCxL6JWHnxi1IvP93fl04Zd6s2QCnoQ1GeH6pmWJloOyyFfcD0vXg7fkyztwAuoc0znzQBNBaWYR1+74Cz5lSpZmKxXEdGA9+lQd5ZPe5tOdoI8xdTwNTY0u9hcsaaQRgbngA9oV3gcFuv5EGlhq3wnjw/wGc2FJvomIVQIO63r6fxMVbAtfPa/5rhgAay5qwcW8jRCC35b1CsRJR/RfFPJx4DF7HKT8rZSZNVUp4t9vhXHwPbtRP/fWik/yZ2lNvgp4Lt/s8B2ooAJBqu34G3tBNaFVJ5y3XZl0XOT4ErbwuuWIb7pUPObU4ZYdqJ+BcPc46NFTSQ2g0Wlq2hjNJRFElRH4J9IYtvpNCmhNALKHhjYsiFZQhogngnSsC0YqNHPTRq5rg3kjacCfxJkegldTkPD5kN+05CYjCchjrH4CxZj3yTF80eE0JEHcEPuygoMzsd4YnBd66JBFv9N3E6LvCc+Fcej+jRpZcpihIZLbs4M/6rqc5qOJ2nE4GZSgrqAne0A24nWcyzo+kY375LbRV+0Glg40xyKsf+sE1CsrwfB5/dtpPwdj8YOr8yO7zcK+fhk0ZPYoVb5etAjOK1YodyMOx6wJdyaAMQdmQV3o1XL4l4JlqBFWxOK6VB7fnAmTn6TnP0essKipVmfDChPJhn3plNihDuDZk+3G4ve3wAln09BSKj0g84eBMj0DHgB+Umbnf0+ezNwVPVyhWEyowo5iHZsfgJq2p5+IN9rDFNOMk4A3eyDofBRO0ivrMthuXoVc1Zrb1XGRrxXScrvPQa9ZmtnWeg167HtqG/Ry8cM6/A7fzLLSicra3lCQGefxFOJc+gDc1zm5dPYMenBz6cxf6g5A1GznbRU6OZkyjkiK25qPyoLmYQQ6MGLVr2ZrVG+mFffZNyN52tFZ42FgjcT77IeFAzcCEX/ak166D03k263zsFEFPICsIPRiBS5kyafjBpCvZVzJyGxXBKGdNlAbi8Prm6+QQFDjT5nQ85c1LfnmTYkWi7LIV9wNxR0ffeHZdgfYBDQlXdWsUiyPcBA9IZEOO9H46GnIrGSphnxjOOklePz3bT1Qo7oKEq6NnOPs9nTImbVdlzChWF6qUSTEPSR2ShYbc6YGcXwJJgrw5FyLnq/LTqNTcxVJtMg3xp0M6NHODIrEpzprRI0UckOFVRCfgdp7LXO3EEL+Weo6LgancP++RaQ1uRSlMTbKALgV2ZhChfDjXz8Dc9iiviwJB9Lqr1bRwqRQFnbyBbrbQ1qua/UBJbwdKa1xomonRBQ7L0ARQX1INITT/OOaAsnYE1bdT3Tv9zTu2mYJ76YjYJEyjaNGOEZ/nuctVjiYrW/t3JjKTFFcXc68thWKFE03QcyV7Z5xGUm01gKq4AyRpuC3wHPVIh65QOTPlwp3IHNDKYEa/TqG4S2wn6WqQgwRPVyhWDyowo5hPFuvrDJL21sJaxEo73To61TYn8j1Te7HY92ibqOQmOjnP1juDpPaL0DTkBTz05UgKCwcALT4FOTkOvW69n1lCmTKF5b4IMWm/nH2TM1vM+o2+YVMwgsTxFzNcHJzxIYiiChituyBdI6VjQyVT2cgL+q4FvA+kZTM36DJzWMgaPJEMUM2tTZl7DOdCGj3s7b3wecxmcb7ouVcsW2Z+ImJOaZNCsZoImAv/qEkIWKFYjBktulxowdCnti0rES0UQc6wFg08ZevHKRQfEUNf7H6vOjmK1YXK+VVkFXXTiquyTmN7ZiPp3kO6LznqsEkjxhvrz2wrr0tmn6S1VTbBG+jJaNOrW+DOEfalAAllpTgnX4Je0eg/+LNgNG6BFimEBg/NJbmzPzaURaHfOg/3dge/vZp7noXZdhgirxhyapTLlIyGzZyRY596jUu73NvX5ltr0vEa7YfnOBiPC0xFJdYl5XHmQi/JtSWAe+04r1evzSzXmt1Zk8WFKQjluS4fo3S84V5oZXXZ1xHKx7gX5pHjaS8AUVCWfT6y4J6THSNKqiF15WiyGjRm+PNSb5BC8QkQ0CUHuLNRVShhabmzIBSKGcg9SJQ3ZJ3G2aqW0ipaCBEu4HLrrNOqc5SCKxQfEUv3UJzDk4LaabpCsZpQgRnFPIxQBMbmQyyqO/dBbG5/FHrEz1jRkp/nZrCwGG/TNrjdF2bbCsuh129mnZlUW3EVCwS7JB6cRCtdw9o06dooWkUDuzoZa3fD2vd5SM2Auf2xeRkhWs1a1pvxFy4QHO3CAw1xVnBPZ2O1h6Jot2/3SOU8rsvbRUJ2tM30Z3/4Q3hTYzA27E1uVw3c/jSRuznIm5eRiHt456pAdSHQWD7nmGrAgXWANejvKwWjKPiV2t4ZzADMbY/A6TjFH51TL3M2Dh2rGUismI7HjBhy6ngG8+BseRInb/kjfe92haG3PTwveEafzc0Pwb54ZLYxvwTGpgdhhlVndKVCwbi0Sib+rFCsNnQhcGitRGROwmZRWGJnI+BABZcVi6MnpqCv2wMUVmROCOZB3/4ERGL+IIwCGY6cxs6nOEM3g5Ia6E1bM0wNFIqPS8CNY1+LRP6cn1lBCNxO0xWK1YSQJERwnzM+Po7CwkKMjY2hoKBgqTdnWVlmIxGFnB737aEDYeiR+ceHxHZBZUGkA0NBGhpp0jTI2CTrqIhQAVveSVLsp2BIPApBy6EHuhC+2C1ZUNMITCDEgRJus+MQkUKeT0sbmfEmRmB3X4BZt4HXKZ0EtLxieFOjkBRMIcttTYM7eBOJrgtw6ndi0g3AlUCh5cCc6INVXAKPNHI0jd2R7FOvZj0GbEtNWGE4p1/z9ykLoqIBZ/IPo3NwxjJbwtA1jE1LmIZfwhSQCRjuNLyJYQgzCBHOgyd0FtwlAWJB+xjK48CTRsd9ahQIRDCOfBQGJdtPUrCIjqUIhuFNT0LIZHlXIMSaIk6kHNMijKmYRNgSCJlAUE775zE6wRk1dIw9qfM588gBi89ZEEZ41gJ8OaCuy4/G9z70UF8KBE3gwk3gud0ClqHSfBWr65p0pibg3LwCr64N0YSG6QRl0AgEDQ9ax4fQmrbDDOcYYlUoknjjQ0gcfwn6tscgNMGaMvRspXJe7/J7MJq2QZ9xjFzmLMV16dxqZ4dHfd0DkE4cMh7lbGVJ7pqnXoa597PQ84s/lW1RrF7o/cIeG4RbXI+oDUzHKSgvEDQl9OEumGQAQu8JCsUqQeUaKnKi0ws7/RXNGVGag0ZBliwBG5BOShoCISC8+HwMpRLngKwY5Y1LSJDNNXekLICCGAQJBK9ZzxotFNTRLQvixN+imOYhbRYKANEIWcVhGIXlcGPTcM+8nntd5BDV9gg0KwCNSqzIbSALduUG9N6eTUB77YJAa6XEjqb0pDQKLgWhpWUipaYWlM7Z/whQWMYPJS0u8YOLEUp1QX1JKVqscVjv/I0/H5V0keYPjU4lhQwL934GJeXppWjJ81NcmbneiHp5WZWlTGmfFYpVRzwKXD8F7fopRMKFiNDzaeAmYE/7Ath1m+jmttRbqVju6AbrzLgf/gDQDL+vQ6XK9CzVdL+cSZETkVcESQ6Z73+P3Sp5wGd6jE0fBPVnlMaM4l5AQb+zr3OfNVJYhUjdOqD9CjDW65dr7/v8Um+hQnFPUYEZxYqDRmZSkLNRursRdaqSb6RaKI/LgFC7Hu7Nq5DSgV7VwjoynCVCy/I8zrjJuS47ASk9Xq5WWs0lVpRBlDFPyRqMiBLE5uj4UnT/rp1xPBfB86/i0Q2PYCAeRt90AJaW5nZA25ZIOx4zx0Bx39plz7oyLfEGKRSfAJR5mYJeBOkvnQWcdhSKFNKDsW4v7NOvAZ4DpDkzGuv2QCZUicRCuPEo9JZtcNtP+U6a9EfoBoyWHdy3UijuGjftfj7W6/9lTFfuX4rVhQrMKFK405P+iz49W5MZMDwCknzBm0kXdKfGISAhIVLzOdwGSCFghPPhui4EC+XS26LGgRDHcSDiU8mXR7/Nny9ZHpRqS0DGKLggIYXGaemubUMk/ACMXrcB3tBt6NsegW76egK0ifbV49Cb2rhjTiU/0HUOzji6Ab15qz+f5rd5FNyhYAs1Nm2D03EGxraHoSWDKB6VBZ17B8b6vRCeA0l/4SIYO54EaHulb/1NQskDdh4+6MwUwdu8BlhfOg057fK2uVYQphmAHZ2C4A6LgLQCME2TS8bIBYq3LxiCrlu+VSe1UanVrqdg6RbqHRv1xVOQCMI79BMQF94FmndAMwOQrgN54wLQupu1ReTUBJ8fM+KP+rlUApU8TnrqPPptlGZBekF0LlLixkKDvsxKmxQLMxOHUeK/itWMn8kgYDz2tdnnCQQcMwjv7e8AyWeCQrEgugn35mWYD38VwqFgH/VpfFFg2X4CWtmapd7CZY1G5emODePw34dwYqm+hNQsOOffgr7hwFJvomI1QCX+1B995O9DS0yn+rGeFYb7xp/nFKBWKFYqKjCjgBudAsYH4Fw7AUmjRqQnQ+K60+Nw2k+y1glpk+jN21jLxTn7pq87Ey6AbN7OFtPuiZd8DZNIEUTbw5Bj/bCvn+Ughsgrh7njEaDvOuyu877uTH4pi/nKcAHsD37IWR+iaj2MdTvg3LgK2XOeR2BEUSWcdXvhCQHvxAuAbUNbsw7WnqdZpDdx8yrg2JzNYq3dA3f4NhLtJ3kETKtqhtGyHbLzHBIkMOy5LBAsGtvgdJ6BR45MUkKr2whr28MsuOv0dfEx0SobYW15EE73RXhUMkXBi8Y2GFVNcLovwBvs4VRdcpCqbGzD+mrg4i3/eD63NQ7dnoR77pjvQmWY7MDk1W+Cd+UYJDlOmRb03c/AnbDhXP2QnZ0oHZiCTqJmLezz70CO3GZ9HX37kxDuBNwrH0BODHH5lmjcCm3zQ3BPvggnec70Xc9Ajg3Au3Y8dc5sOj95RRnnTOx4HN5IH9zrZ1LnTG/ZwWLC9rEfJ89ZMbB2F5BfBp3KqhTLHlXKpLgfoBdn68GfgHf7Khy+h/n3K7qH6fu/AE9TgRnF4pCejL5hH0B9lavHk32fCIzGNmhN2yBUgG9hjKBv6HDzEveJuF9XUAZj7S7oG/epfoPi3qAZsA59GV5/J/fRZ/qxevN2WAe/pDxsFKsO9Yu+z3Ep02Kwh8VvuWNCA0k1rVw7bJ953Regpc5wdALO+XfYQUkr8rVK6AbpnHuLbay1tbtT7kVe9wU4F9/zM0vo+b31QThXj8G58mGq7IgCDPaJFzkgJLY+6q937Q7YZ9+C7DieSouVo31wPngewnUgSms5Vk4dJ9pe0n/xy3YkvKFbSBz9AQchWEtGSuiVjbCPv+g7QVG6I7VVNCBx7MfwKKBDKe/Sg16+BokPf+QHaqiNMm5utyPx4Q95WiqLqLgKiaPPwxvo9t96Xcd3czr+IjaVTvA8m2vBQRmb5humSA2J9iZ4W2mbDcrooVyW6hZoiRjsD3/kB2UIOwaXgkPn34bRuoObRFkNZGwC7vEf+0EZIj4Nefl9OFePQ9v6mH/cW3fyefROv5pxztzzb/O+zJwzvXELb7Nz4V1fYJnmmxqFQ+e6vwv6A8/5bZMjsE++Ajl0g38jiuXNjIZ7hl22CswoViEkeO52nYNz4YgvJp+8X7E4+0APJN3/FYpFcD3b7+fQc26mjCk2BefS+/A6TsGz59QmKzIQcOBc+QDu1WOz/brxQe4PYXwI0lH9BsXd45GRx81r/K4xIyOQeve4dQ3uXNtVhWKFo3ow9zvUEaEHaxoU0KBMmWy4PRehVTVltl0/k1Lfp/Rf99bV2YmGwWU6Xm9H1uU5lz+AGQwBlU3sEoSRZNpJBhLe5fehNe8EqprZwUhODGeZzfPFeikrJr+Eb94zHXdCFFXAGx/M0KTRSmvhDd5kUeB5JGKc8aKV1ECrbPL3K13fYGa10Qme7ws7Xawvm/I7KslgTsZ8tM1UKpRfCrNuI5zLR7MWnHgjyRpacqOqb+N9z0rvVQh4fIy1wkrOlFnsnFGAJt3GPB3n2knobuZx4GDaTHmTYtkyE4RRdtmK1Y7mOXC7L2adRlmfhj1Hc0uhyIIWj/nPtyyQ25DwVGBmIchN0qPs3xz9OiRLzxWKu0Gjgc3OM1mn8bsHlyEqFKsHFZi537ETbEudAd3osgQgUm+AlKVCbkAzeC4kBTZMi+2rM6ho9oMhuaAgCdUpr90Nd+h2ztkoqCFIM4X0Zfr9cqNsUJYKlVZpBWXJjJVZqJ0ya9Kh8h0uN8q1vKFbELS8xebr74KQNuvHLDjfQA/0inoO3KRG6bLux20OGgk63unixnPnGx8GKhoh6Rwuds50C5KCX7lSKej7cwUPabn0G1GsGH0ZpTGjWM1I0t/K9et2sjzPFIps8LMt92+FBoAUufHGBnJPpGxplWmruAfwu0UuQfeZdw+FYhWhAjP3O9nSvhdLBScbxDkZIYLayCbRMDPnJXFGsnNeZBvYGWmh+SgQRG+cFDRaaD7D9IV66Uauz6kRp3IoY26by9/JuVqaRo4Nnjt/3zLWa80Gq/RF5qN9mNmfXOtlC+x4ZgAs1/Ji0/7xXwiaTh0lsgVdbL47aVMs24yZuW0KxapiofswoUqZFHfCYs+1xX5n9zvGIv26xfouCsUdsFjfdtG+r0KxwlB3zvsdM8BCvOmQzaFIOvfMgxTQ54yECBILpk4MtdPDOL1DM3STxWVzdYJEcRWkbsB9/++gl1bPebVMo7KZsz3ss2+z4G4u9OpWTq/lzJTKxoxpbn839DllWJTpstDytOoWeH1dcPuu87JzrnfNenZ2ckkQr3btAtvXDLfnEjwSJ67I3L5ZBLSSKt4Hco+iY5R9YQa0vEJg+Ba7TS1+zjwI3cipYk/fl3MED0nMj4M/ipURmFEaM4r7QLQ1V3CeRcsXe2FUKAjD8p9vuaaF8j/tLVpRaAUlOft1VP4tVWBLcS+gPmkwu5A0v3sokW7FKkMFZu5z9FAezC0PsiPQDM61YzC2PDT/hVzTYW46CKfzbNoCTBhbD8O5fs7/budZmJsOZYyWOGODMLcenp8hEgjD3HTAd2+isAHZZW9+cN42inA+zNadcM+8Djgx3/K5def8+fJLfc2YgRuc0k6ithQwSZGIQiaiHGyZgQVwpZc1SELOTFxyFJuEHBvk7dCyBEn0uo2+hWvXWbhvfB96/SbWuJk3X+tOeJQe7TlwTr7K7gW0zLkYmw/CpX2gY3L5CPSNB1hvJnNnBfStj8Ib9QWBvfZj0NseWfSc2R1nYG59ZH6HyrBgkJuWnvZSYwZhbn5Q2WavANJjMClXpiXaFoXik8TVrOz3MDMAs+0hQFMvhIrF8aDP6/swQuP+ip3+LFTMw9EM7jNk69cZG/dBOvN19hSKj4wZgkX3+7mZ6Lrpv1eYc/rGCsUKR8gZO4/7mPHxcRQWFmJsbAwFBQW4H/GmxuAN98Ib64MIF0JUNUMj0d6hm6wRQzbZWlkdO16Q84U3MQSNAiFltfCoPKb3OrypEWgF5RBltay14vZ3QU6PQSuqgCihNgcuicWRRXNxle8UZFhwey6wwCyNsnhF1RCuDbf3ul8GVVbH6xFOjN2FqCZcFFfy93m+Wx1c8qNVNECQI5OdgHv7mm+hTdkxFNBwHV98mLJUKpt4xJVKpzxah+fxfBR5l/Fpfx3JTBmeLzbpf5eCRtRmhXyx374OLgviNjMIJzoJScszLRhVrRCmzjXqrIdjBKDXNEPqFtzJMciBLsAKw6htotwYeORgMHQDCET8jB7dYKcm1sghG+yaVnhSwBvt9y20QwXQKxvYNlYO3YQc7QUixbxvdM4c0tEZ7wfySmGUr4GkflPaOUN5PTRynqK25DnTSqphR6dgWAE+H3RuKAil5crC+RRQ1+WdE7MlfnBcYvMaIGgCx68Dj20RKMlTjgWK1XVNuuQiJ3SYfA/rhjc16t/DSmvgCBM6HOhhdb9QLMzEtIOw4UHYUXgjt/n5Sn0f0oBz9CCito7CgpUxGr8U16VLfUahQ/eov9bJ7pFacTX391w9AEEOmmTsoFDcBR45hE5Nwozkwxu8AW9y2H/3KK2FPT0BkwZMqe+vUKwSVGBmmXQ2lyuShF81AelJ1lgRC+iifBI4k+Nw3v0rHpXhQI5u8o2ZnYKKymHu/gxntdh9XcC5NyGKamDufpKzBdxrJ+F1nubgj163HhA6W3tjepwDO8b2J3h5U5NTCJz5MWTTDpjVfqmTfbMdousMElufRjgv2bkYHoZWEPFT6XNgux7s2z3Qzr8CPPRVmMmyIfv8G8DATYiDPwmDUi/tGOwjf8OaN/r2x6GFC7iEzL34Przedhi7noLIK4Gnmfi7kxqXpTy73X/ppv//XtJI66ktDiJanN2nvFtX2A7cK6mFpmnwaHmv/QnPZz7yU/4IcyIK++2/4jZ9/3PQgnn8YuN+8ENusx74HHeslgPqurxzogmJ509IbKHAjAUc6wAe3SxQmq8CM4rVdU26o/2wj/4AoqgSxq6n/RF7z4Pz4fMsEm8d+CK0LBmLCkU6I5MeTl33sLt2CsG8EDRdB3WHY6PjuDySh6pSA7UlKyOpfEkCMwM9sE+8xC/I1IehvqHnunCP/h2bQFj7v6BemBV3jTc2iMT7f8f/r7c9zIPE3sQw3HNvcZu17zk251AoVguLKIEq7ldI6dwdvAH36nHOGuH01ObtrNsiAp/eKIjXk7RFlXLWRnqG0QFgoBv26ddmt3v0FrsYSUpPnki6QZHdXrJcKjXf1BgHRyio0zMeRvWmZxAc7oDz3vf89VauQ2zT07g1HsbGiMc1f6K8nKfZjoe447/whi3JQZAZRHwaeucxv4zkre9grk+S6O/C8cRa7KiIs7W4Xt4A59zbcCaGOEhE+jTm9kf9LKX8Ekwm/M4i8aNT84/PyJgN69oPZy2tPQ+60Hx3LHJzohpcOn+DN2BfOAJr77Op77rv/R0ytO4pcEMaNIqVrTEzp02hWFUkYjA2HUwGmf8v/0t6IHrjFi5VhaPcYBSLo2vAaEzDBzfzsbvJY81oCYFLI0XoGgJaalRQeyFoMIhKSSjj137r/3C2MukJUj/RG+v3jRUUiruFzDeSuGffzOyz8nT1O1OsLtRbmCKFZ5NNNmXI6HBvtcNtPwG9ZQfrp1CZj9N+ApIcgBo2J92RTBjJjBAnHvPtlkmrxPJrs71kJ1lSKY/lpwTH4zZcT/D7f8D0f35ObNq/uVIZUFLU0aXAAjkhNe8AurtpTGje9gqqOy2sgHnoJ+EKDd7b34Fo3c1vp8KOQZBuDIkPhwuglddxORIFd+TYADSyrNYE7++6Kh0/OBnG53ZshpvUpDENAy+eFPjsDgFB2jS0TCMP41GJgPBgeA6EJpBwTDieRNBwIRLT0KDBbd4GnH0T2iM/DZ2CP0LAppeF974LRPKwq2yKjL8hy+thn3kX+oHPQGO9BA125xl4ned9vRfXRr4hsaEqiL4h4OEtNjQ3zmLJN0aCON0DlJdYkLu/CE3a0PrbeTRBFpT6gsuGDrOoBl5sBCipgbn/OS5/0mo3wPNcGOv3cDmY1Aw4p16HXuKXlnnT46w1owdUjf1KFv/1VGBGsQqh+zkJvLs166Ct2Zx02zPgdJ+HQUFpdd9S3BESD28AXKkhbLrJZ6uJtWUBbKgBP9dzmhEoOLPWuXoM3roD0Bu2JZ0wTdjvH4HRXAnPsJSIpeLumRF6L1sDY/ODEK7DfWDn/Ns84KjEfxWrDVXKtEzSs5cSj8qVYpNwuy6wDgkFYvTGbazf63RdgJwcgSBdk+at/Abodp1jYV16+debt/sZKZ3nIaPj7IphNGzmF0X3+ikeVaF6ULdpFybcAK7clogmBEoiQEuVQEhOApffg4xHuVSJhHPl9Djc7vOctUPaJ3rtOtiaBfn2//E3OBiEtedznLbudl+EdBPQyurZ8Yg0bdzOc5CuA62qmZ2evJF+v4TJc7nUhzJVOBXyxmXeH72mBSirx62JAK4N+IKSzWUuKgoFrKHrcG9c8sV2a9dxgKNrNIDOYZ3jOptrXZSZ06ydQ3oy5Hqk1W2All8G93Y7vMFuCN2CXr+RBYHdG1dYt0dv3cEDSmZegd82chvCCkJr2g6NdV4uwRvt4+wkvWELRCACt/scp3VSKZVo2YmoWYxrtz0MT2uIBCTWVwtEtChEx/HZc9a4mTVu3I6TqXNm0MgyBNyOMxnnjByl5JX3U+dMb9gEaYagL1Gd+P1+XX4UJmMSPz4lsbXeL3f7oB14aKNAZaF6sVCsrmuSNAccLQgtMQW36yyXpiK/DHrDZnhmEIYbX1JtLMXKIBpzocsEDCc62/cJRjjzijJNowgiL7Qyxi6X4rqkrF7HCEPEJuB1nvEzlYuqYNZtgGMEYXpxLtFWKO4Gl7QahQ7NiWe8exgNW+AaAWjSha5K5hSriJXx1FF8osjxQdjHX+SyHoZsIhNTSJx6dXYonkR/6UF8/t2U34sgS8Sxfi7FSV9W4vY1mFsegpyegJwYgh0pwY1hgdM3+Vs838gUcH1A4uGNecgPRlhQWNt8iAMybveFpO2pCffmFQ6gWHueRYIyZM68zkEZHqkhsd0k7tgg3J6LMNseZhE/zrapXQfn0lF4w7dT84m6jVzSQ9s9gzPWDxG5iMiGpzA06evHDE3qKApLHGxthHber2V1RvuAokpEGh+hg8SHi4IyiWM/TpUS0ZGh9ZFQMolRkpuT33aLRYaNtbvhXj/NwRUTAomjP+DAFn83EIbuxJE48ULKkpy/S9bfjW1cpkTHF5EijCWCePMSnR5/TGpkSuDGMLCrTkO17UCMD/K8JFJskPMEiRbfboccH0LidgeMzYcg45M8T+qc7XgcTt0WyGPPwx0fhHvrKsxdTwFKwG/Zo+yyFfcLjhECBnvgJO/LDD2bbl2GvvNpoNAvOVUoFkLXNOgTI0ik9X34mdnfBWPjfgTKG1QXeQEcMwJ5+yq8qx/ONlJf8sZFGHs+65dRKxR3iUODgyO3YJ9+PfXukerHbnsETnENspu2KxQrk4+Vafitb30Lf/VXvoBoOtT27W9/+15sl+JTwpuegHP+ndmgDGUONrVx8CL9zc6o3wznygcZJrxGdQuci+/NX6iUsK98yNkvhFvbhjM356cbUqbwiU4Jp3EvYBgcsnGmp2Dv/jJuNjyDaxVPYHzLF+BueJjLqMyiCph7nmX9lPSgTIpElIMJ5E6EYITfUDOCMiSwSzbaaUGZ1CZPjSI01onSyOz+jU4L9I2DM1b8BQh4Fa2wghbK84FtdTbcrvOz+i7p+zbY42vxzKRhUlvvdS4Fo6wbYQTgXD6aCsrw8aSRpo5TqaBMOm7nWd++mzRuGnfhwxshPj2UtROy/Hp54uSNAJy6bRnfdS6+D6OmNX1v+VwayfPjN0nY59+FGUyzDiWHpwvvsGOXYnkzU7ZE15DSmFGsZjTXhneRBgjmQNmc59+Cm4gvxWYpVhi6Pc7PN+77UHowifonNdacyx9Ap9JsRU40NwF5NelCkI7nwr3wDlxP2WUr7h7TifnXadq7h4+Ec+Fdnq5QrCY+1nDAN7/5TfzP//k/57VXVFTg53/+5/H1r3/9Xmyb4tPAJkeficw2eqCScGw6FAGgkqfUZw2S9FOyBBGY+DQE1X4GwhiNm/NuqTOMTQO21GG17oY9NY7hNQfw3rVg2kulhcJQEAfrIjCotjS/FN6VtBGaOZD2gLn5kO8Q0E/aNGmbTNbeZF+dA733CurrmzE0NRuc6BjUUb1mHdB1Du7mx3BmogY3Lvrx+bVFcb9EagHXAirFom1KbV9vB8xN+1nQLD1oRFCWkLx2IufyuDwpXAAnUISEA+ytj6HUnAai42y1PYkIjt8KY8oLoEg3fc0f3hAb0o7zOeNzS/DnOeMMdM6pPX2d0xMZwSPFCsqYWdItUig+GViMPpfgIwXJ1f1KcQcIGqRJxGFseAAimMe/K2GF+bfltJ/ksmioEomcUJZyrqcMZUqzXiFyO1gqFHcCSRpkvHvMfX+h6ap0VXG/B2a6u7vR1OTbCqfT0NDA0xQrnTt8pbvHb36JvGq8d8GaN9I/FtVwaTQf22rsZDbAIitOWXrPnW8RvY0cKQYk/EsOSf0ox41R/SMcAJljHeLjHby07TvcMo3g5VeA8aFUW1Ewgoe3PIWoZ2XZ1WzrU6/uq4WZM6kyZhSrnkV/1+qHr7gzyFXIuXbCLxGeIRjhwR0l/LswAlJdaQqFQrEcSpkoM+bMmTPz2k+fPo3S0tJ7sV2KTwvT4tGiDIQOJN2WUtBbnpFWjuR5LFab017ZCvnOTfFpFAZypwQXULWP8ODd6sDgtJnzZbJzyEAcAS6RIlHfXGgVDfAGb/o6L+X1GdNIdJfdmHLgVq5Fz1imo0dTqQuj7yqcqo24MhhEYRg40BjFEy2jENJjlXgum8qCXlY3z+KbBIpBGUpCgyiuypgmJ0chCspybh+JB1MGS0izEbx+JCMow8SmYJ57CUV0vOnYp1ZqQJB9eHpqMZ3LubY9VmbpFa8zlJd53hXLEqUxo7hf4HvS3Gy/GagcxVCuTIrFkSaJ7F/MDMoQsSku6xWh7M91hY9eWLpgX0VQ1q5CcbdQ39UMQKtphbn9MZjbHuV/6TP3V+e+qygU92Ng5u/9vb+HX/7lX8brr78O13X577XXXsM//+f/HF/96lfv/VYqPjFINd/YdDAtywSwe87DpLa0ESOn+yKMdbszvuv2Xoex/oEsSxUw1+2G032BPxm3L2BL9fxURKqO2tUEGN3HAeEhtkBJN8UQ6HeGG5c4kDQ36MKYQXZOovIiTncni+uiitRkOTXGAQpRML9DQSVCsZJmDE7O7nNBSKKqkNylznAnrjzi4FD5LZRefh7BE98Djn6XLcXpWIn8zGVqJIxMZUGUZjnTVl7PI0wktJz44HkYLTvYXjJ1jG9cgtGyPetLB+n1kAgwjQYbMs7il9mg/dbifuBnBjpHzpySK2PdHjg9F9OPAMxNB2CTZXqqSfi/DdXBWjmBmbSEMWWXrViNeJoFbf3++RPIOW/Tg/A0FZhRLI7wvOQzNQuxSS5zUuRGOo7vYDUXTYfRshMacpQbKhQfgWlEYO5+huUJSADYPv0a/yuExu3TUgVQFauLj1XK9I1vfAOdnZ147LHHYBj+IjzPw9e+9jX85m/+5r3eRsUnjCgqh7XvOTidZ9mCWlCHJFwAc9/n4F4/69vTGRZEYTnMBz7vByqmxzjQwVHsvZ/x54tOQESKoTdt4TdFzqghK2Zpo6nEZmHdS/0WorZAadjB2tI4QhP9rK1CTkplYQoKZM/OyKfknMlBntftuQp9wwPsckQjXpQdopXXcVCGrFQ5SEK6KrFpmFse5uwZ9+Zlrh33olMwtz7K2TPk+ETbqVU3Q1Q2YWw8gCIqiRZ+pkxNsYA51AEvvxSGM41NJePAhy9mbBcdL3pIWLufhk0iyroJneyyiyvYBnvGXUqv28jBH/vDH/pfTMTgXPmQnZBI94a2kY6X1E1Y+59j+3GP3KKsEHd+RDgfTscZf3lpQZdsUM0tnSthBqA3tfkjDoM3+Lu0DXrzNj9oRZ1SakueM4+sLy+947fll0BvaMOgHUHpx43gKj41Utkxadn3Ki6jWI1EpYVQeT30fHo+nYagDMS8EuhNW+GaIcRhQIVmFIuSSx9vhkT009qSlcnEMKAZ7IRJpgsyHoVWUMb9KafjNDtbKRR3i6m7cNvPwuttn22UHvffpefBbN2n3NMUq4qP9Wu2LAt/+Zd/yQEaKl8KhUJoa2tjjRnFykOjdEAzAGPjgZRwIltAm0EYWw9Dk1RLrCE+MoCJYCUCzQcREA4MQ4N97IeArsPcsA/CMOEl4hzRhuvCeuBz/HooXQfe+3+DAsPEnqp18PIiHGRBZwc8TYO17/MskhsROkrCHoan54cBttUmEMorBHY8jnEniJfPGHhqax4iRVWAdOHpYfzNKR17W/KxZmtp0mlBR+Lo96E/8DkYpdX8puoaASTe+j+wHv4qRFktt92cCqMwFkVdmUB1oZ8xYpg6psajiOW3oHBbNQcynItHsr/sujbc4VvQdzwBQc4go31w3v5rGA9+FUbNWhbd5Tr22+1ZbMpfgLHnWZgNmyGFhoF4GJe7gYOtu2GS6wGNEpx5A0hMw9j+JDRKM+KTpucUwCQ9HG3Lg5BCh331A+ihAr+TRBlHugbn5lV4oSLOkBEuHTsT9o2r0OFC33gQ41FgNGHi1GVftPnJLRLK+HJ5k4rLqFImxSrHEgmcvBlA2Axgw6YHuXNOz6CjHSaK84G1pZSlGFrqzVQsd6gMe4Hn6LwSb0UGIlLIbjkuDR5VNUErqmQHR/vEy77LJpkNKBR3ielGYacHZdLwbrfDpIFGFYpXrCLuKsy4bt06/lOsDjRyUTIteKS2Pz0OYBzO2/+Xp8mKJtwoO4DT1/yMFk1YeKq+F4HSanY7crvOsf6JyCuCuWE/j6CQYrpWWAanx89WQcKF6D6DjEIdz+WUWLf7NMxQAfZV1+HKeAGuDxlwPSA/BGyvjqGg7xQQ2ggtrxhX232tlBdZ5ihT9f+DdqB8Rx6Cug2v+6Jvof32/52XVOtcOAKtdi3s3m6U1m+FfvJ5OGlOVDSWFgiE4ez4LI7fzsOuqnHIuZouaUjSkiHrccrCmWnrPgsZKoBWUAqZK2WabKp7u3FU7sYAHfIkg7EATnZaeLRxFEjaezvvfZf/Nfd8Bvqa9XCTpWIZ57CkmgNhtH/CCnDAh5wm5OgAnE4qUdsHL+n8NLdyzNV06JWNeOVqpsK97ao3/OWOsstW3C9YE73YXFmOrtEgfnTOYoe6kAVsrAEqzTHosQQQUoEZxSJIj7Nb3a7z8yZppP9GgzuK3FDWbX4pOzDN7YsY9ZvV80dxb0iTA5iPTGa2Kfc0xX0YmPmVX/kVzpCJRCL8/wvxO7/zO/di2xRLRbgg9b/aIz8NXdfhugLnTvlt+1qB4jwqOiqGiBfCPvUatA37YTSVwhm+DfvkKzC3HIIkkUYWgitOLU9vexhaKB82WVl3nvEf7lRys+kQZCIK/e3/i40Vzdi4/SF+xfRcF/qxH0HGJbBhLy9jUxXQOQCQeszB3X6GQDQK/Pgc0GwBFkV+hA5vZsSr5UEYjc1+jer4OPDBd+EZERjF1bBKauAO34RHQZntn4WRFK92BgaAMz+C5UxiV1MYsEkkOcLbmA1BAZj1eyA27INz8scw69ogXRtebyfcsX6Ymx+ENznMpVcUXKLgiUzaTRrVLXgw33+R/t4xf3l5AYkn2+iNOx827SBNfPinYJomW22LqVHoDZu5JIsDL3aMR7D0qhYOrlEWDmny2K//KWvMiJp1MMrreL1zz63jOJBv/JkfJJMSj2wGekeBizf9+YwcOpuK5Sr+67t+qY6xYlVihWAc+T9oadyGddt2UUIiHEdCXn0HuHkVOPDFpd5CxYpA+M/Mhi3wJob9ARQqi4OAXtMCqUS6Fsa1ORPX7TwDGZ3ifhz1o+jYwQwpTyvFPUEk5TL4/8OFfj88NuXb2fN0ZU6hWF0ISW9id8AjjzyC733veygqKuL/z7lAIVgIeCUxPj6OwsJCjI2NoaBgNihxP0EpqHJsAN7YAOuQaBWNHADwRvs4U0REinxBW02DHLrFoySs5VJK5UAevOFeyMlhiIJyaEUV8IZvQs8v4VRDrbAcXnEN4jKA3lEPk3GgPB8ojggEnEnIoR7I6CRne3j55RCuA5cyTOKT0ErXQOQVQqNyob4uwI5Bo3XmFUE4Ntx+aouzxgwFlLitr9PXnSEHplAehB332zyXXZtEIMLL4e9SW2UTRCDEQRevt4uPh1bVwAEPNx6D19/Jyu96KB/O6VezHj8qx3Jvd3B6NGWdkDAy6R+kMCxWkqdSMQqmsMo8bZ8ZhJwc4WNKjiIkEOzpFrTxfnZ0oocQ1WxTGZI3Pgg52s+uJDPix1QO5Y0OcAdTK62GJBPLjHNWDc8wgYEbs+esvAGaE2NdG9YPKijlcybNMGRvu99WWM7nrWc6D9WFEpb16dfwquvyzrk9IvHOZclB04Ap8NZFiR2NAi1VqnusWF3XpDs1BkcPwHRj8OhZRKLupG1RVAHHDEG349Aj+UuybYqVgxed9E0NKAgzMTzb9ymphn2rA+aatdAimdmjy5WluC7pOnQ1AwYNQA3d5IxpyjSigTipWTSsBk05WynuEm96nN1YjZpWyOlx/34fKfJ1F2+1s9EImZgoFKuFO37bIgembP+vWPnQaFHi2AuzYneF5bCKKpE4/gIHPVLoBsyth/2yJXp5JwHGvGI4x3+cEtKjKJ9HejW7P8OfKcXV23IYozEL71wR8KSffnG1z08/P7whH0ZvJ5freGYYwvXgnn0jpZpBwRIKEiQuH01tBgvgUi3zlQ9SbbQeFiem7evwU3sEBSq6L/L2pr5rBrlDxmLAM22hPLhjgxxESi2v6yy06lYYTW08IkRoD/4EZ6m4XZS2K2cdCDbuhzTM1Hpo/XrTNnZS4hRfIVggz7l8lDuADNVl16yFfeIlftCk1nv1OIy2h7iMy6PvFlfCKq9D4viLbOPpfzcIM68Y9tm3MgUKNd3f/+4Ls2VXdM52PQ2HgmoX3oF48O/BiI76y0sXPzQDsHY/A7uiCXjzz1PbWLf7aWhWyZ3/mBRLrjEz868a71WsRkhPzJgeROLES5n3MCvI9zBpqDImxR3gCX7ZYz29uc/RnU/CpQGSpdy+ZY4jTBgTA0icei1V9uV2n2dtHnP3U4BUgwKKu8fW82A2bfXfUZIamIxh+aYbep5SmFGsKtRz5z6Ho9Hn387omJjr9sA++2ZmUIZwHdgXjnCwgtBadsE59cp8dwPKUDn7OrxkiqFT3IB3r2rz7HujCeBEJyC2+BlYemUDvHOzQRk/pbiVAxopNINTjp20oMwMlPHj3rgMbceTQDACoc8GSxgr6Adh0oIyoHIn3cwIyqSOze1rHKEHOT5tPexba7oOzJ1PcDDG2HwI5rZH4FE2TjwKpFlmU7aMVlrDnTzK0vEGumeDMrSvWx6G034yIyiT3As4596CUeQvy9x4EM7F92aDMsn6befa8fmuEZ7L59Jo9M+PvyEOizGb8DtOprS59CzbOaNzbnlpD75ElJ2mvGlK71asFLts/lcou2zF6kR3p5MC83PuYYkYB6uFXMRtR6EghDev75N6jp5+Fbqb9ixUzMOUCXaknKvFI2OTcC69D6mrGmjF3WM4E/79Pj0oQzj+789wJpdq0xSKpc2Y+dKXvnTHC/3ud32RUsUKwLGTWiezCM3gjJiskBYLB1w0CM/JaSlJ5TnCiQMlNRiPSs4AyUbfuEBCBBEoq4M73JuhWCoKS7mUKh0W6+u9nnN3KDBj1a6F29DG/5/x3YoGuL0dmW0UDMoSlEktr/sCzNZdXD9tn3qVjwsv1wr5HZKZ4JVhwdh0AM7RH6S+S4EcCs5QaRNbaaevNxRBItd+SMllRtqa9VSYxP+fDqcKU2AmGzY9vESm20R8mi20gQL/3wXOmf/9tLaxAUB1UFecXTarzKjAjGIVQra8uQQhqVxzXgdeociGk/Cfb9mwE77ezAopZVoKeKAph6OVN3iTS5wUirtF8LWYPfhC1yi/ZygU92NghupXFauQbA/WHA/bjOmmmSEkmw1J0ZhQPrtmLLg4eoG0Aqz7kg5lvMwNFFDJDWex5CIZmCDBMDn3hq0bkHOXp5uQczOD0veB5hcUHkHmfHODG/QyIDJHiHh+suQU2vzRXQrqLOD6QAEU0rjJfn4WdouQtC00WpX+Xeoktaz1/12IbOsjm23FisqYof9RcRnFqmSxwMtizy+F4k5+JyrAtyAyscgLsboOFfcAucjvSKr+qeJ+Dcx861vf+mS3RLE0mAE/AyajdtP0AwrZAi9UI0Hz23GIAFlV+w4w89ANtmtGXzuKGvfnXH3QBExNsoij3rY+w9bamxyBWbuOnYxmcAe6YTZugUd23FnQSqr4Rk7L08rW8MhNanljgzzdTcvCIfFcrbgablqZUcbyyAp8YgRacQWL63ok8JttvvI1kCOZmS0khMd6L3nFLE5J60qtlx0hinJmJrEA4bl3oNc0+9k56YEgCujMPWdpkGBwRkCLnK+orf1FiINfXvCccYAsHbZQVxW8yx1vrsaMyphRrFJI9DEnFMxX9yvFnUC/E3q+zR2sSULPZ0VutMKy3BOpb0jXokJxlwgr6A9uZhvIFJo/XaFYRdyVxszAwADeeecd/qP/V6w8pBmC0bozo43civSmrVnn12vXwSM3I3oZpEBD3aas84nmnZB0M3UcBEQca4qzZ3lsq/OgD3X4JVJUflNUOTsxEeMgCzsJzUDOCaGC7J0mIaCv3Q370lF4vR3sIkVaM6l9He2DRstPu5FT4IaCKlk782TjXbMW3oV34Jx8FUbTNj94MRdyTipdAzddoDiczyLFklyihm7CWLs7PZ+BBYWN9b7997zdKKpgtyZEx2GP9MNYR9+dxb1xBUbztqzf1apbfNenNPQ1G+Bp/nZLco2q25D1u3rzdrhzhDONlp3waFsUK8Yue+ZfFZhRrEakbvJzKBtGyw64ugrMKBaHHLyM1l1Zp5HwPwn6KxaAnCXL6rJOMtbtgacrRybF3UNalXrjlqzTqH1Gy1KhuK8DM1NTU/iH//Aforq6Gg899BD/1dTU4Gd/9mcxPT1977dS8YmhWxZbL5ObD1lFEpShopfXw9jyIIvlMoEwjA37oVEGy+ANbvKuHWMhWrH+gD9Cwg5H+dC2HIZe3Qz36N/6bWdexPYGYEutixnX5fwQcGith8pIHDIp5Otd/QBG22GIxm1+1g5ty62rMLYehl6/ORUUsTtOwdzxOPQ16/1gDgczKmHt/QxciqonM2Kcnouwdj3NwQqOuNPyejtg7XkWWlVz6i2WrLS5raLBbxOC/5/abN5X4QdJEjFeB9t180o1XjatwyEBYILEfmvXwdzxJNzxQRgt26GXN8BLRGHufZado3hf+7rgGUF2TCK7asYwoTdsgdl2GM6l97hJXjnKFuTG9sdSwSiPdBQihTC3PZo6Z2znvW4vjIbN8Pq7Z8/Z+gegN7bB+fCH/ne7zvFnak8/Z3Su9apmyIu+Fg4t19h0kPUcNKUxs/LEf7lNRWYUq5DJEWjN22Gs2+tnEyYD4caWhyEqG6HHlFi5YnE06UGU1XH/IuM5una3P1ilXIUWRMam2ASBBnRmBrZoMIr6ZjS4pLmzhgUKxcdFSJcHF42NB2YHWoMR1nSkdqH6OYpVhpAfo/f+j//xP8Yrr7yC//7f/zsOHjzIbZQ188u//Mt44okn8Id/+IdYSYyPj7OGztjYGAoKkg/o+xBvatxPFxQCdn83tNq10OwExEybEYA+MQSNnIwgOSOGMjBcYUF3SB9GcokOlcNIz4NBbfTzEoKzRmTVWkqg4Xk04bEMCtUhG/ziTz9DAXvgFgdNBGuh+G0OZXlQNkxyHaTlQt8wDBMa677QtuiwocPQJDQuwaJt0WE7NoxgEJqT1FYRGhLXz8AoLGN3J1q+NzkKNzoJo3Ztcr1+ZolzuxNGZQO/4PJFQi5Ptg3TSAofJ6P5zvQ0zIDFDxBenm6S4QOFfGbbjAA0EtMhx5BkmwsJVw/C9Gw+xnRcPN2CNzUMkx9Ayf03ArzdfDxJX0YIHu2jZWuuDTHTZgRhaBpkYtp/WAlaL6WBkoBaLPUASxz5LsSez8G0LD4/dB69+BTcEy/D2vd5FgGW9LnnMpdaWfu/CK3g07fMVtflndPRJ3H8usRDG+i0Cxy9JtFUAWypU8Z7itV1TXrkvjfcC1GzEZozlbyHCdbkcq4eg1G3Hlr+p3+/UqwsvOgE5EgfvPIGaIloWj8nDK37NGfLaitE/HcprktvYoQH8WTrbhh21O/raRr3Q/SRW5zprC1UdqhQ3AHcP+/tgN64lfulItlnJSkFcj/Vq1ug5amyQ8V9qDGTzt/8zd/gr//6r3H48OFU27PPPotQKISf/MmfXHGBGYWPFklmzIwNchaLS39z5qFwhNj1LH7QXgldAE+sm4bZ/iqcZBYNRQG0qiaY6x+ASHZqnBuX4ZLl88X3MlK0UsVN+57jemW7/RS7DbmXj8zbNtoObdujnEEjqLTm1lXelrk4QnDGidt33a9xTs4nwoUQeUUQZWuAG5fgzGxu+va4vktDuguS9BJwB3oy3Buc4ipo+aVwu8/Pbl/ZGmibD3FQSEwO+y5MaRbXfHxrWjk7xW0/Ca28jrcJXecwT47XMBHf/UV0jEdQGxhD8OSfc/NM3or1wOfgvfPXqePCRz2vmNP4E2femFOLK2Bse4TTsu3Tb8Lc/oj/IvPB91PLm29B+Fpmm7K9XPb4ITw/KEOoUibFakUaAYhACM4b386coOkwdz5JaaBLtWmKlYTrwL56DDj75rx+jksDQZVNS7RhKwPpOb7+X8/FeX0JGSmCuf2xJdoyxWqCxjNpEDXx2p9kdmqor7/9MXhS3p0mh0KxzPhYv2cqV6qsTNMCSVJRUaFKmVYBIlke5FMAcArh7MiRbhh4YrPA420CgbwIrK2HYR36Cqx9X4F16MswNx2ECIZnl0cZHzOUbQf2fSVzhZr/MxTp+i2k57LvC+kb5c9XvS5V5sRseBzYm2blTsEYzYJXv5l1CKhWnDrreutB6C27IdOtsSnAk643098FrX4LUD+rr+NS5lDLDqBhe9r+mEDFWmDrs7PL4m2i1BQNLq1jJiizbg9Q2ugv/9Y1fyR34wF4CPDDRqv0p/ExadnDqfnu1mcwFA9iTcHssUlB82W05QOtuzmd2CaNGw7KFAA7nwGCVfzK7px/2xdq3v3ZzHMbLADW7/PnTz/ONWtpon9qSqqVuNoKgPsraZn3YsbtTKFYZZBHnnPhXf9DsDX5PCng7Evn/DuQC7jdKRQpKLM2NXhS4P+OqH9C0OAF2WUrFrbLnqFuf0a/jk0NlCuT4h5A3V0ywuBOzsz9nv6VkgdANU2VHCpWFx+rlOmxxx5DaWkp/uRP/gTBoP/SFo1G8fWvfx3Dw8Nc5nQnvPXWW/jt3/5tHD9+HLdv38b3vvc9fOELsy/jP/MzP4NvfztzVOypp57CCy+8kPpM6/ulX/ol/OAHP4Cmafjyl7+M//pf/yvy8pLaKCskPXs5pPUiEYeMTfp1+1YQgu6IJMBLnRd6sTeDXDJEttZebAoalduYIdjCQMzREEtIhAICQd2D6UX5u+QmxDo1gXzAiUGSuxBZQYfyfQcg12UdE1om1XlTaY8ubUgSAybnp3BBsgzI8bfDsVlPwCPbbLLjjk2xbTelzFIZkA0T03HA9STyghpM4cCBjqk4VQHNtCVg2tP+OqTk7bONCGzpz0dEAoAlbBhu3LfnptTJUB5c3YJwHb/TpmkQwTwW1vXnGwM0AyIUQUIL8/ImYxKmDoQsQBcOzOiYbwtO5U7BiJ+S6dr+OszkSLAwuWyJ10Hngc4HCyknMtrouJBoshedghYIQloh6JSHZMczzpmADjjT3CYCET6/Hr26J6LwSEOGgmgUpIpPgZ5xdFz4nLGomliydGR1Xd45V29LnOmWeHCD30n5sEOithjY3qjGkhSr65p0B2/CDhfDpFxDesbEo3wfpvtnImbD0l1oSS0vhSIXZF6QiLqw8sPJZ+Zs38fWLJiTg9DLs4vbLjeW4rp0bl2DW1oHc06/jrNzB0ZgleSrkkLFXeON9iGhh2Fp0r9OqZyJ3z0CSLgCljvtm3ooFPdzKdN/+S//BU8//TTWrFmDbdt8d5jTp09zkObFF1/8SCLC9H0SEv7Sl9KyHtKg9aRbdQcCmY4LP/VTP8VBnZdffhm2beMf/IN/gJ//+Z/HX/zFX3ycXbsv8abHYZ97G3KkN9XG4q+bD8Gm0hgKYCTtIyl1MHHpCDDaD6+qBc7aB/HuFYHxNDfnkjyBfS150C+/6bso7fkMTEzCPvmK3/nhZRWycJx99q3Z5Vc2sXht4tSrKXtoUVjBArqJs2/yTXkmi0Nv2AyHvpu0jOZAQ90mWI1b8aNLfrDw81sTGJwycLRDA8VweHkC2FxjoKk0D3jPFyfGgz+FW2MaTnZpqSyDzVUJtMp2JK5+mCoN0ilzhjRfOk7OplTqBosdO2YA3kk/ICkf+AouDwtc7efiEm6j4MyBtQYKgwWQHzzPbdZDPwn3yofweq/PHjwrxMfY7joHSYLCRhDW/s/BufAOW4Cnzk8oz5/v0lE+b14oH9aup2CffTOj7Cp1zjrPAb0dQKQIxrbH4J5+NWXVzXtXWMEC0ImTL7O4Jn+3uArmlgfv5qel+JSg3+2MIxNyG6IrFCufcDEsLw77FN3DxlLNJDhqtT0MJNRIvWJxpGHByqfR+Lfm9X2s7Y8D+Sq4txBaWT202DgSJ18Fkv06v30NLMqyVrW0inuBFoKlebBPvw5JxhdJSMPI2vYI4KmMbsXq4mMNp7a1teHq1av45je/ie3bt/Pff/pP/4nbNm/efMfLeeaZZ/Af/sN/wBe/+MWc81AgpqqqKvVXXFycmnbx4kXOnvmjP/ojPPDAAzh06BB+7/d+D9/5zndw69bsS6wiN25sCs7lDzI6JgRlcFBaOOmWpNqmRmGfeR3WJl/wWa47gCPXMoMyxPCkwIlOQLQ9wZ/NQBCJEy+lgjIEuR7Yp2eDPjxf8zbYJ15KBWV4PmojzZNkUIYgVyH71GupoExy64Ce85BDN3BoPRAKATFp4si12aAMzyWBczd1jMZ0YOujQEMbph0Dxzv1VFAmYAL1wRF4V2ZKg8Ajspwx034is8PhOvBOvwqNsn+MIJdO3Y6GcbU/U5fFdoG3L2tISF//QH/4/4XbcykzKEMkonwMTHI6oP3f/RSc9pMZQRnej+gkEidfgZm03Da3PgLnwpGMoEzGOUtaouubH4J75rVUUCbFWD+XB+jbHp/97kgv/zYoI0exvJlTyaQ0ZhSrF+nw/T89KMPNo/1wLr4PGVAddcUdIPScfR/71MuAciNcGDuKxPGXMoIyhDd4A27HaTZBUCjuGkP4A45pQRmCPlNQFaYqZVKsLj5WxgyVIB04cAA/93M/l9HuOA5PI/vse8Ubb7zB2jUUkHn00Uc5kENlVMR7772HoqIi7N69OzX/448/ziVNR48ezRnwicfj/JeeBnq/IuzErL3yHKiDwvoiVEaTDFBwXXGydjju6hjLISnUOyaQgAlzzSYOIqQHYChVWJI9E5X0zGxHYQU8WnZasIWyPTiAwC5LM/OVwxvrnyNwm7bN10+idHctntoYwDkW+M1+0z5/S8PBlhqI4hpc7Mqcp7nEhtlzOiPjgIR7KZCSHckORvr2R2Drebh4PbtYLgV+bo94aH7070OLR5HItTwnAY+yVgoroOk6nNsd2eejMi4KWFkhCF2HN5w9GCnTjqvQBLsuZZ1v6KbvTJG+zfTbaN1FxV34pFHX5ccnacKVwrfLXsotUqwGluU1acfmB5aTeIM9MJzZ/oBCkQvhLNT3mWB3QyQNEZYby+G65PLrtEG0dNzb12A1bgHg29krFB8bKuGfM+CYHowneQOFAvd7xswjjzzC2i5zofpWmnavoDIm0rF59dVX8Vu/9Vt48803OcvGdf3AQG9vLwdt0jEMAyUlJTwtF5TpQ/W4M391dSujjvgTIWVLnR1JNfzpYrvURsGA/FIk7IXf/ChLRFQ1+IGZNFgzZc4oi8gr9B/06W2B0DwBPvru3OVlbFt00rfTky4m4rl/3qRD40nB7tNT8czATMQkUcBs25J7vSI66mvwGBYvOxdjUQGhGX5gKSPjZ85+TI35LlkUlFpAzJK3KZQHucjDic9ZqAgyscDGEfOWI5O/kU8edV3ew8CMyphRrNZrMsfLYAoK+isUd9n3QWz5Glksh+tyQXFkGrxLG1BTKD4ui/ZtVWBGscr4WIEZ0guesWVNZ2hoCJHIvRtZ/+pXv4rPf/7zXDpFosDPP/88PvzwQ86iuRt+/dd/nYNIM389PT24byGBV8qIyQEFJOYGEDiwMjGEoJU7hZCmmBR/6DrPNtXpsAht0kp7Bm9skF2K5gVZ8orntE1Am9OWsd68YhbU9aSB0nBurYGisISu0R9QHM4MfIzGTci8ssz1To8vuF5ZUAE5NQ4tMYWCBQaJyvMkXKqtInckEufNgVZQBm98yHeZSnermgMfx6kxCJPO4wLng9YVHfXPZ86ZBEDLydgQPSkC/MmjrsuPD9+TMScws4Tbo1gdLMdrkoV+c07UAFOVUCjuAHquZThQZkImA8uV5XBdzu2bZWAs3G9RKO4UYQbuarpCsdL4SHfOGYFeCsqQY1K6EC9lsZw5c4ZLnD4pmpubUVZWhmvXrrEzFGnO9Pf3zyunomwempYL2u65IsL3K+RupK9ZD7fn4rxpVF7EdfxpQ+9aaQ2/BBIBYaOywETf+PyAQEOZh4CMwxvoBtbvhcgvmbVXpNRE12WRvVSWzOSI3+EmtfWkhSUFYTgIRH/JUVIqw+FgBN2M03RnUtu3dg86x4I41QU8vVXD5T5yaJq/35tqJWT3GU6RXLfpKXQNze5m57CBdU3boPd3pkbU3FvXYG4+lL1cSDegV7fAefevoZfUYGvz43jn6vwOn2UAZQUa3r4iUFcSQXPzNjgX35u/vKSejZZXBNd1oNdvgnv9zPzzQ44HM25N5K5U1Qwv3Q48/ZwlO6AyHgNKaoHhm/PXW70WklKI0netluzJP51rRV2Xd6kxM+cyVHbZilV5TRoWC5PP1QYh9JpW38VvSTZMsZKg34m+Zh3c7ux9H+5jLFOWxXUZiMyWm89Br98MlzT3lmTDFKsJcvnSyuv9d4k5aBUNkIYKACpWFx/pvjmTNkkv5vn5+RmplBQIITekP/uzP/vENvbGjRuclVNdXc2f9+/fj9HRUbbbnuG1116D53ksBqxYHCMQgt64BfqaDRmZM1p5HYz1e+F0nE62CL4JGpsOwibnHmq5ehS7myTWFM++AdLLYVOZhy1rAEmivVTS1NcNc9ujHCCYwWk/AbPtYe5gz5C49D47C5G7xux8p2DteByioCyjzdz5pB+YmMG0oG16EF5+GQdleB/g4uENHvLStCBJ2PdAq4c8wwYo2DF8G0ERx4PrPISTiSGOC1wZy4e+44nZrBY7Dne4F8bWR/xA0cz+hgth7HoW7qhfA0uBmyJ3CLsaXXZimqEwDBzeIHHpFokjA6e7NUzl10MnUd40kTx2Ftn1pK+3Q5GiW1eh166H3rAlY3SPjiUJ/rKrFW3eyZdgtOyEVrs27Q09/Zz5jlHuuTdgbDoAUdE0q79Dlt216/n77offT7XpdRtZaFkLqjrxFVHKlPZZacwoViuOMNktjjrrKeh+RffJ5u3QlOio4g6IeQHoDW38nMvo+5TVwdz6MKaV28uCOFoA5o7H2SUzhab7fYbadcidi6RQ3DmTbhDGhn088Jjq2woBraoFxvoHMOmq/qlidSHkTPrDR+D/+//+P/yrf/Wv7rpsaXJykrNfiB07duB3fud3WKOGNGLoj9bz5S9/mYM+7e3t+Nf/+l9jYmICZ8+eTY0WkOZMX18f/sf/+B8pu2wSA/4odtkknEbBJUoJLShYnmJvnxQyPo3E0R9C3/gAtFC+rzGiG/CovjqvBJobT7aZ8AwLVDAhqDbbsaGZJjsDiW1PIKGF4Xi+LbRpT0KeehnWrif8MijDhDMxBr2gFMKz/dpjw+LlkQAfC85ymwmn9zoMugFTjbJHbQG4iRg0QSYKpt9uWHBIpwUahENiMbTiAKRpwbU9JKTB2QKWLmHokicnXI1fVLnNAPTElL8f1EjfsyKwbZrPv/HTfJQRr5MAIGXmCAFJ22KGodlRf7/oIWFYcHUTJgkZ07ZQB4/2wwzDdgQ7t9K260LiZLeO3kwjEbTVOlhbHPX3g8uGTCTOkM14ZiaYcfBLtLf+enUDUrd4P02ZSB1jqZu8SZqTPGfcRtEmD4J0F2h/DRP90RBKIh40+pxsc/UAugYEmkui0JLL83QL7rEfwdrzGYhg7rKrT4r7+br8qJzu8tAzBOxt8X+/Z7olIgFg/zo1ZqlYXddkNGpDjg0iUJgP4czewygDIjE5zRmVoZAKzigWxp6egnf8R9D3fhYaP7/9vg/pxNn9N2GU1cCILN9ypqW+LqenE+zMFLCoH5berwsiHo1BC4YRCn06ZdCK1UticgJebyfMNc1sVjJzv+frtOMS9Ib1MCMLlLcqFCuMj5UDRgGS9HhOV1cXvve972HTpk148skn73g5x44dyxAL/pVf+RX+9+tf/zr+8A//kEujvv3tb3NWTE1NDS/7G9/4RkYK55//+Z/jF3/xF7m0idyYKJDz3/7bf/s4u3VfQuK+MjoO54SfBUNQNsqUXoi3LgQRs2dHjSjo8nDzNAr0OKIxF0EKnEyNQh75K1A3eKYrLNOtmttPwWjYAu/cm8glYRvb+WV8eLsMB8IXoLefRKL95Lx5SC3GOvBFXz+m5wK8LOnHhNB05G0+xPZ6/LmqGWZJFcSFI6l5aDtkKA+9LZ9FSb6APjqAy9EQrg1mduZby2ysD43ALK7gFISeIYHjN+hFlwKSmUHJR9Z5yA+HYLgx2Ee+ywEkGjGiWL574Kfw43MU1JrP2ZsGXCeA1v63oRWV++Vec4IyhHPke4jv+gpeupqpfbO/1UTZ5VdgbT6ExLt/neMIA9aeZ5E4+xrGt/89vJ2qdpo/IlhWbCF89P83Tzh4KQIzirvMmFnC7VEoPik0NwZ5/hXYWcTTdSpz3f5M2tNIociOsONcSu28kX0QT+54ClghgZmlQHdikEe/CzuLOYFRXA255d4ZgSju79+Z1/4B7PYPsk7XaihzUgVmFPd5YOa5555jvZl/8k/+CQdN9u7dC8uyMDg4yFkvv/ALv3BHyzl8+HBGgGcuL7744qLLoMyaj5Ido1icRKAIRzsjiNnzXZbe7Qrj0XUGXr9p4dnG3M5X6QhBqSpBGI1tXJPMWS+aDm/oxhwL6kVeJYXAIEqQVjmVnUgRjM0Psk6LN3QTzoX5Oi4zPzvSSxo3K3CtZ35HngI11S2VKKXt9zxUmhOoKihD73hmku6GChuRaB8Qrs2x3Qvv2Yxsq1ZUCbvzXI6ZJPSpAYQDeRmuT3z9LCDenDFfDuvwzG0Bl51x1tTQzWT9vXrFX3EaM8qVSbFK0RLTcHM42pEmmkFZnnMC5wrFR0Wq596CiKlhyByOkXLkNgyXrlFVZqK4W9R1qLi/+FilTCTAS9bVmzdvxh/90R/h937v93Dy5En8zd/8Df7tv/23uHgxezbDcmU5pGcvFV5sComjz0Pb9wXYrs7BF0On2ImLsCmhOTE/dZBKmXQLUUcgIuKpNndkEKK8hstfpOtA0Au9EWQLO8FWy36JEnSdbawFPayTba4RYifouKezQK+pS+gjPTBLKvzUWC5lsuCYVPLkQdD3uJSJvmvxg5/LkahWyTBh60GY1Cmn7yXbXItKj2JcMsU/dUq1tUJwHAmbypsoEKF5bLMunGl/vQSn5IY4VZe3md56qSzIDMB2PNiu4DCHpXsc3DHdaT8VWtP4uNhaCI5H6xDs/GRoHk73GOiZ4zL/+W0OTC9ZGqVRiZIBl1yWQoV8jCkDyKNj6dnQyVGJjzvNZ8IVJgyXvps8P5rJJ09LpJ0z04IHg0u5nOS5JVeokCWRcPVUm2V4eOGsgcc3ugjao/65NQPQxvrZIUqQKPOnzP18XX5UTlz30DcG7GryozPneiSLTR/aoEqZFKvrmnQGb8IZ6YVRtyn5fHJS9yv3jb+A+cBz0IsyMwsVirk4U5Nwj/0Q2r4vQrOn+Xfk918sOH0DMMqKYURWxnNnKa5L++ZVuEYBzIK8zH6dHoT75p/D3P8l6AULODcpFHeAPTkB9/gJ6Pv2+SX/VJZv+OX87tGj0HfvhKky2xT3e8bM9PQ0i/8SL730EmfPUBnRvn37uKxJsXLQghHIvV/ClV6BK30aB0goBlFXomFLxTT0Yz9IBg10LnEK9nUicfNKKuuFXHtEOIzEiZeSQZMATBKv7b4At7fDH7YPFbCgrXPlQ3j9pKwuuSPNosPVa/HCWf+lv64E2FtTCuf8O5ytweQVw9ryEJzLH8Adue23WUFoa/fCDYThnXjBbwuEYa7fC3dqHG77CW4SpbUwWnfCuXAEcmLIb6toxFTLw/jwuo5x3+gJW2qB1sgAvAtv+y5USRtqncSESfT3VFLseO/nMRKzcLxLT2WtFIU17GmSwMhtyIvv+o17v4ABJ4RT3Xoq66g0T7BQcn5I4EJy177UNgXZ3+2XbiUdpvS9nwcmR+GeeX3WprysHsbGfUicecMvcyLhs/J6GOv2IkHiv2MD5GEO69BzcNvPInHjkn8uhAatugVGy3a8eCEPMQcIGsBjm4HTPUDXkK+7Q4Gj1gqJJza7EKdeQILWQU5TdZuAuvWfml224h6WMgnlyqRYnZB7n1W7Fs6Vo3BmnjF0v1qzAdaDP6kyxRR3hLQCMPZ8Bl7XadjdF/zAAj1bK5tgrd0FhwY6FDnRCiqgawLOxSPwBsiumwa+qF/XBuvBn4BUnkyKe8A0wojs2Q23/Thk2ruHqF0HY89uTLkBFC71RioU95CPdedsbW3F3/7t36Knp4fLjWZ0Zci6Wo1srywSiQSu9QlcvO0HZQjq2HYPAcduBOE27eY26vS6Ny75ttp0YyQ8lz+7Ny6z5TZhNG2BSwEYsm1O9pDNtgdhn3kDXj8F7ZK9ZteG234SXu81PL7JX97e2knYJ1+cDcrQd5u3I3HqFXgzQRne6Bi8829xR4ocFJj4NK9DixT4ttu0LQ2bYR97IRWUoVfXRMNuvHFJSwVlDApKFNHI2Y9SQRk+BlNjcI79CFq4ADCCQGEFpo0SvH1FyyglGp0GXr8kYJet9ddQ2YgxFOL9di2jFGxoUuCNSwKNZR4KQsBntlO67y04l95PBWW0uk3wxgfhXTk6G5QhBrvhnHwZ+pbDqRNEx9I++wastof9/TjwObbUdrvPz54f6cG7dZXX8eha34L8ofUOTnYBnYN+UIZPhQdc7tVx8aaA2J7UiHIduJ1n4PVc4uwnxQoIzKRFZpQrk2LVQi+DF45kPGP4ftV1Dm7XWWWfqrgz6PnYc4GfmxyU4TYJr7cDzrm3ocvkc1SRHV3APv1a0sY4eR06NtxrJ+D1XuesZoXibgkbcThXj0HOefegz8614wgb2ctaFYr7KjBD5UrkytTY2Mi21GRbPZM9Q+5KipVDwtE4UyYb/RMa7ELSTRFsz0wP22xQu1Zay2+GIq8E3kia9kzy4SzHB7N+1+08h0JtClWFvliwnJ6YnRjMg6TUxZgfVJiLvPYhRNP2jDan8ywHibTiKn87qKRnhrI1uD4aTAWgiC1rPHhd57mTNn8FHtzuC9B3Pg6x+WGcn40XZa7TJWFgD6LtMLyWB3CmJ/vxjNvA4LjEIxsdBN0JOHNEjmkEQHb42T7zmBwByCEqNBv4lGMDkOQmEQyDirJcGk3IAo1mBTX/OFBp1K3R7NvXMajB9jL1c2j/M4JEimWJlyVjRgVmFKsRKjdND96n4/ZchpYMdCsUC6Enov7zLQvcd6CSYEVuYtNpg16ZOJ1nYJB7pUJxl7C8QK/v3juP29d8OQOF4n4PzHzlK19Bd3c3uyq98EKylARgZ6Tf/d3fvZfbp/iEIU2ZhUoephIa20mnItVZkSkbaxnPDKKQ2K+cHM39VXrpd22sKQU8KslJQwvnQ06M5F4rabGQfk162/gwBGXNRAohxzM7DTKvDIPTmfMXB2xgfL4LUoqxPs6YcbUAhqdyi+cOTOoQeaWQeoCzaHLRPyGg6yziMy/gxEtfoDPojQ9zgCxjn+jYlqyBJBvBhd7E49PIs4BYIvc89PWEM3elrgrMrAD4rKZnzCwiOK1QrFRkbHKBiR5A90KFYhEkPdcW6NeQY5MiN3JyjmBeOnQNqkxbxb0gsVCgnTqtKhCvWF18rMDMt771LRYao+wY0paZgdyZNmzYcC+3T/EJQ6U8C0GaJL6obWYmxTxoOonnmZkWzBSoWVA4lkV1DYxOASKcP8/KWwQWsGk2A/NdvYJhyETc/+4ci2cRn0TEysyMibo6ZGCB7aOyKOlBky7CC2Tm5lkeBAlRei5CC8xXEJD+NtPx0ufUsJO70gLHmV2mpjKDXCJcAE0T8477PMwAJhOAuUiWv6FnCT7N3U7FsoO0rueWMimNGcWqxAplBP61kmqIUNqzQ5UyKe4AschzbcG+hyJVMp59IpkgqOtQcQ9Iu59zf5fu9yQxkGW6QnHfBmZ+7dd+DZWVlfjZn/1ZHDly5N5vleJTw9JdVBdlf4MLB4BAYoQDE1RmJPJLs84nCsp4Otd9UhAn/YEdm4KgjrSVPXCgVTQhIQK41ufbRac/zOXkCERBac5ghahvg7x9NaPNIC2cW1fhDd6AVtGY+YX+TqwtycxIOXfLgNa4Levyefsat8K9dATixllsrM49utZcKeCefR167yWsr8o+H70415RqcF79Ntdf62vWzUufFtW+Vs08DAtaXhGQLBOjFxFz+2NAIgohNP6uufsZiMKK+euNFMLTAvz/piaRnyOGU5YvYWmZKTOk4SPnZCUplh9zzdBVKZNi1WIGICrqYe54AnrtWg7OkJC8ue1RaNWt6n6luCM8IzCrUTcX6sOowMyCUL8COQaEtKomdoRUKO4ag+73jTC3Pw69bqNvzFG/kT+TpiNNVyhwvwdmbt68iW9/+9sYHBzE4cOHOUvmt37rt9Dbm6YtolgRmM40djSQu1DmWxxlfRxqjMJsP5LSbjHW74UIZ+qf02dj3R4418/yZ7fjJMwtDwJpWTL21WPs6JQ+0snfLaqAsW4XXr3kP9wHYgF/vjTROBLmM7cenp+1UdkMvaIeXte5VJNW08qdKdJeYWHi3uswNh30R294YTZC/eexq95JZRdMxoBhWQix9oE5KQcC2roH/I7HSC9k1zmUht15QRdNAHubPYScUb/muv041hR5aCzNzMwh56ODaz0Eklov7hvPQ6/fDK2MNHx8vCsf8AsGSjLLlWgbjF3PwO0573+2grxf9oUjsE+/zgLMzoV3YJ94CUbT1owAGgdwtj2G93r8YNmJLh0H10lE5jzLSJB4bzOpGfdmBNyMDfughxYYGVMsT/Ff5cqkWKV4ehhGYxvsM6+z0x/f/y6+B/viERhNbZAfz2xScZ9Bmav0fKPnXAaBMKwdj3PgRpEbW4TZgXPuoJsoqmQ3TJku5qdQfEzIwt5o3gr73FtwLh+F23MJzqWj/Nlo2sbTFYrVhJDzakE+Gn19ffizP/szDtRcunQJTz/9NGfSfO5zn8soc1rOjI+Pc2nW2NjYfecqJeNRJGIJeFYIUVvDZEwibAmELYmAiHHGi5wa5zIjLknyPMj4NGR0kktrRCACSec5OgkZnfBHUciC2/O1AGRsChplbFghGNLheWRs2s/+sIKIIoSpuEDMlqgJT8Md6IFZvsafLxGDllcMSdo1XPM9AWnHU226Z7PODNWKawWk72JA0PaRiLBjc5unB6B5NjzSYvEcaPmlsI0gbGlhbNrjF9q8sAHdiyMkEvAm/LppLb8EMWnAggNQLTUFavKL4WoWEtLE6JTHwZaCkIAlbBhOFN74EGve0AhuQg8j4ekYm/I407IgKKDDgeVM8ToEjfpGCuipAzhxeBMjEFaQUzRdYULYMbiTo9ACQV/wl6yvE5OsKaMVlHBQhgNQczEDsMgCdGzAP2eBMG8LHeOpOAVkBCIByS/t0wmB6bhEXlAgaEoEvThkbAwyOgWRV8iBND09ZfRT5n6+Lj8qb1/yYDvAljo/OnOtV2IiBjy1bWXcgxUrg+VwTTpTE3A++H5WPS4KSmvbn4AZXqA8VaGgAN/0OGxbwjA1zjylZ6sIRThbxjGCMJ0otEgRVgJLcV1OTjswpQcT0bR+XTFgBTAwEUFhoYtgUGXNKO4OlxxSj7/Iv7G5UB/X2Pk0dOpLKxSrhLsONVJJ06FDh3DlyhX+O3v2LL7+9a+juLiYtWgoo0axfBGBEMz4NBJHvoNw0zaEq9fBjE/Cfvv74NwOSvWt3wTT1ZB4+6/8L1FGC+nBkINSUhjW3PlZOPRQ7jwP9LX7bfueg11ai2nHwpsXfGHZR9fmI0wDVIOdEOd/ACpSKlizAYUV9UD/COTVD5Egu+iCcn8dl44AjsOBCfPgl+FZ1ZCX32UHIs5deeDzQEEF8Nbz1D3x5zvwHBxH4vTtAnQP04tpCM9sKYCuu9AuvgE50M0//NJDPwGph3G0Q2JgnDoQFmqK/eyQW+TsDaCiQGJvcwSGF4N74gUO+lDuTvlD/y/gusDbfwkaF3KqW4F1h2C4USSO/i1bYFsoQPlDnwVsG0geO7dpK7SWXRywst/9a1+ssmw7sGkTeZcD7/y1f4jX7geq6qC7NhLv/KX/3VAJ0LIZpp3IHpQh7DgSsThkaSt6hoHTSaOmxzZ5qMh3YMbGYb/5PKfK5W3/LPKoEzc0BJx/EXQmrX3PQV8zm8WjWLkZM6qUSbEqiUdziqSTS4zgZ5IKzCgWwbEh3/9bv5+zfi9Q2QpMDqWewXLX08AKCcwsBWPTEkeuUU8qH4+sy0ekFLhwHehIaiY/3aZhEeU7hWJRBPV3swRlkBysFeTcqlCsIoy7yZT50z/9Uw6+dHR04Atf+AKef/55PP7445iamsJv/MZvcICmqyv5hqtYtoj8Elj7vwhvoBvepXeB1l1+8IU6uIM9/t+2R2e/QO1zHI/gTgMnXstsI8eDs29guvXJlNvPa1f9splD+XEOyjA3LgETg5DF1bPfHR/w/2agAIbnYiwGFJfXzVpDH/1+xiq1sjXwui8BUiCuPZBq//E5YGOlh7XpVqrv/BW8Q3+fLcNnuDXHBCrhCHhSQpB+Tvp33/qLzBntGM7e9LC90k1zBRmfP1/Ct5CUnFKUTPUdPAW8dSo1C6VWi8JCGGSRnV7nHh0Gzr2deS6y4CQSeOWc77iVaqNVXXwDqG+bbTxFwaw5LOi+pVjWdtmqlElxHyAXs0dV9zDFnZD+O7n8gf+XjnrhW5B0B8fXk92xdNTzR3FPWOx+TgOkCsX9HpihMqUXX3wR69atw8/93M/ha1/7GkpKSlLTI5EIfvVXfxW//du/fS+3VfEJIYTglECnvBmivAEuNBgPfB4eldY4DgT80hf9wJchh2/BrlgHSTkX0oPVfxmiqAzRQAXkQ/+QBUgtewSir5NLYcxNB1AppvDklgiChgfhxiGEhBRN8GrqIVwJh4VpBXRpA0O3oNWsQ7x8HQu4aIko9EtvQOQVI2bkg+aMF6yBvnYvtLoN0BO+N7XUddjTU0CkBDbFPCDwgHDQN2ygutSGluxkedWPw52YgJ6fD+E60HUP1UVAPAE8tM5Gnu7PN+kGcLzTxAOtdNOnIE8Y5v6vwJsYg5kfgUi+HJCIrzs0CK+0Cus9HVHkwzz8U5AxcpQKwvF03l/TEHA7zyGxpg1egpyoChB45Ovw7DhMzfNLsGg/zDzK1YcLAxo8/4W7oY2DQmbTVn7jFpSjMxM4y0KosABPlHhUpwjT1BG3gTCmgfUHeF+0R36az7mWmAYtjf6j1G0xNoBYoBiIOtDgIhhSNfYrBTb6muPKpDJmFKsRKqHNCWmRmeq+pbgD6HdiWhAHfxKGm0jdMKns2n3tT7gkWZGb4jz/gfP5HR4MJ9kP03TYCOHVi4s7fioUd4QV8HUiZwYy06F2mq5Q3O+BmYqKCrz55pvYv39/znnKy8tx/fr1u9k2xadEfDoObXIQ8tqH8CaH2QZR7noWGOmDd+2Y78gUyodo3smBm7evaJiMAnkhDXtbNmE8ClzslJiKAQVhYFNtMYprC2Ac+y7rzIi8EoS3Pwmvtwte1xmALLQLSjm4MmkU4912HbEEUFloYcfO59A1KNFxCYg7QGleCG2bPoPJqIcz5wUSLlBVKPBAXRPQcRIJypwhPZnSapituzEdt/Hq5SBId257vUBT4STc9rOwb7ezPg65MFitO2BPjkKeeok7Y62HvorNJVE4Hadg9/sZXqGKRjzcsgNn+8Jo79f4pXd9lcT6EhPupffgDfQAmga9ugVGwzYc79ZwY9gX+d20xkR5gYlz1yX6xgVMHWguc9GyZgsu3gI6ByUsA3hsXQJBZwLO1eOQo30s8kuq83pNC9xL78KhTCXSedl4AJphwDn3BuT4ELTKJhhrd7Hg5VwoqHV9NIhTNzREgsCmGg8VeR7sEy9DTo+xWLO5/VF4o/1wrp9J6gIVQW/ZwefkjcsGpuNAYVhD2xoHxSEXARWgWfZQAC+9I6wyZhSrFamb0Os2sAjkXFh0dBEbZIWCcMwQjH1fhBjvg3P1BGSy76M3tsF88Cd5oESRm4Au8aWt05C3rsPuPk8dSc72tdbuxpMbiyA1pS+juAdoBl+T7vXT8ybpNFipKfFfxeriI8W033vvPS5X+uM//uNUUOZP/uRP0NTUxMGan//5n0c87mcc0Ih8Q0PDJ7PVinuG49gQwz1wT77A9fkUqNA2HIA32APv1MtsWU1tcnoc3rk34N24hP1Nce60lOQB3YMSH7ZLdjeitrFp4L2rErfGdMgNh/xRqG1PwqUAz+UjQGzSX97YINxjP0Jkuhdl+f532+o1HO+QuHADiNn+VwcnBF4/L2HoGnTdb2sujsE9/QrczrOsqUKRdG/wJuwPnkdYTvN20UtpU8EU7OMv+B14svH2XHj9nUgcfR5mMABoJgsCB7wYEh/+EB4Fb1yH/7zb13h5jYVRXhb91eVNw37/+/AoG4jSKx2bl+0e/xFaivz56IU4Pyjw2jmgd0zw9lLK76VeHe9eFdhU7QsOrykBgolR2B/8CJIssHnGKNz2E3DOvwOTat6phCoQZiFg+9gLfMz42MWnMZlfD2/zo5zpxFhBeC17MbVmF8ZtXyyZzskHHRraBzRIypaREnr9Jrg3r/I66Jzy8iZH4Jx+DbK/B49vTPB3R6fBAbjecR1OjswcxfJBacwo7hek0CAoON2yI+X0RwMHxsb9QEEZpOqoK+4A9r2gDGAatEj2fWigwrl4BF7nGf6dKXJjygTcqx/AufIBm0T4/boB2Md+DG28H4amHkCKu8cWFqbKN8Fbf2i2tD8Y4c9TZRt5ukKxmvhITx7SjTl/PmnZC7DQLzkwka7Mr/3ar+EHP/gBvvnNb34S26n4hJDxOLwr72e0kbMSifBmnb/zNCJJy+c1JQLX+rIv99wNCTu/GjBNdjzC7atZ56N1t1VG2Z6bNFH6k8Jxc7l4U6KlktyDgAJ3BKCO1LyFuRwA2t8wjX2tgDd8K7tomGvD6TwHfc8z0PY9B/fWtexikokorMF2VORL1Je4MG6c5e/OOybRCYSme1k7p7EcuNrrl37NZXRaYDwmOCiztXySrf/8kNSc3Ri+zY5UyC/lkWHn2omM6Xb9TrzZHsY7ww3oa/kMpnb+JEY2Poej8U145XIQ1UVpb+igoJAGO1LB/68VV8JNsxhPx2k/DsPNrKs/1aMhbqsO6nKHg4Jpn+n/VcaMYjVCZanOsRfgDt3izEFz26PQG7fAvXEZzsmXodm+jpdCsRCGE2O79WzQgItG5U2KnAgnBq83e1a8S32bpJ6eQnE32FLHq1eCeG+iFUPrP8/93cF1n8ORibV47So5rKbUKhWKVcFHGlo6deoUvvGNb6Q+f+c738EDDzyA//W//hd/rqurw7/7d/8O//7f//t7v6WKTwbKOEkXtZ1pyyWwyBkbU7DMPDhu7lF5mkalSGbNBrhjvgV1VmJTML0EmspD6B/L/SZJGRwbAkBxBDCHOnOmGXtDt2BJFxWRBLyuzpzL8wZvwGjcCmEE2KI7F/pgJypr1yNiehA3c89nDrajrKgBJXkGrt7OvR83R4CWSkCTDpykNXf2/bgJo3k76/tQinA6th7iLBz6O9rtjxinE02Ay6dmxH/pHEUTpDcT5nOX+6TZyQBVfobAH9kwK1ZgxsxSbpBC8Qkho5Mc0KbyT4dKQOdO5+fZ7D1MocgKifTb2d29CG9y1Ld/VmRFjvUvfI0uJtKtUNwBpJFIg0zDUwJHpkJZpy+gOqZQrDg+0lD4yMgI22PPQDozzzzzTOrznj170NOT++VVsQzRsvwEFknhFZqOhJ35VXonNOYErlmM1I5BmIvU/Gsav/yTQG7OdSYnkXaMZyygeZLUF5BCT/1/1uUZpr9Q+qP/z4VhwvE0OJ6AWGB50rB4Htq+ucchHUtPOiTRMU5/k567faYFSZ3GLOciXeQ16ybr87MlSPuGO6GLpflr8zd+gc1ULBM41qZKmRT3A/rC9zCR7ZmmUMxlkd8J9xEUuVmoH8bPIHUdKu6exW7n6navWG18pJ80BWVmBH0TiQROnDiBffv2paZPTEzAXOwlXLGskOTGk1+a2WiYEOGC7F+wgqm6fnKpywsC2xsE9q8T/O/B9QI7GgX2tvj6KiPlOyEixVlf+AlRVIVRO4D+CRL/zb2dtcVA36jE4ATglLfknE+vXYsJN4juYZ3LgHLOt2YDXCng9ncuOJ9TswVdoyY6RgJwazflnM+u2oTboyQALFFflns/6soEjrcDUWlCq2jMMZeAVlIL98K78MYHIYpmg6GEMdGHojQX7Yxpuv9STgGiGQIGENSpwYOglxozmH2t4UJIM7Nel9YT4O8qVlopkwrMKFYjpLtFbjpZp+UVQy7ywqhQMIbFgvfZp5msW6TIjZZfkrNfp5VUw9OV9ofi7gkYkqUOskHtJEKtUNy3gZlnn32WtWTefvtt/Pqv/zrC4TAefPDB1PQzZ86gpSX3S7Ni+eGKIPQtD2dYjLrdZ6FvfXR+Jommw9j2GDpG/Bf76/0S+9cKdPRLHLkicaxDsngvaa1cuCnx2nmJdzrDeK8rCLnl0fmpF1YI2qZDON5j8STHkdjZND89IxIAmioEuof8F9DO8TBk866snXISt33pgomxKOAECqGvWT9/vqJKdpeyh/shLx+FKKyAVl4//+BUNGFYL2eXIkqjnMxvAIqq580mazehN1HApUO3R4CqIoGC0PyHxZZaF5p0EXOAt9pDrI+QzfrV2HQAHkW9krXuRst2PyCWRO86gT1rptjZKWO/BLCrSeBKWikVZdfsb5Uwek7xZ/v6WZhbD8/vUBkmzLaH4eiz20PL39ssEcz1VFQsX7ts5cqkWKW4ehD61sfmZxMaFvS2w3C1+enuCsVcEiIP5uYH59urCw3m1kdgG9kHMBQ+jhGEseWhzFRNIhBmIe6oVNeh4u7RPYn9rZ6f9Z3ergEHqG9rKLF3xepCSJamvzMGBwfxpS99Ce+88w7y8vLw7W9/G1/84hdT0x977DHOoPmP//E/YiUxPj6OwsJCjI2NoaAgR6bIKmV4UsKxPZRY0yymiNFeIFIMrWYthGfDHbwJUC0xCdGW18HVgugcNVnzhYIlpzolOzHNQIGBy7d9l6Z0aotcbK+ahjF4nW2bUVILvbgSMS2Mrn4P046GpnLBujThgGC3J3JmImvs4jxw6dTNEb+tpgioDMdh2JNwb7WzpoBe2cC23BNeGNcH6aYtUBjRUGZNIeBOpRyXtKpmeKFCXB4JY613FYiOY6JmDwr1SWixCX8+AWhVrfBCBRhJBNAz5Hc9GsqAQjMGMTUKt7eDs0+06ha4gXwMxoJsl03aLo1lAqbhYWJa4saIgGVI/m5AdzE4ZeHWqETQAFoqBMJyHN7YALtKiWAYOm2fYcEd6QeGbgChArbk1oSEN9wLb+Q2OzGJqlbE9Qj6RyUGpjQUBDzUlvq23r2jHoamNBSGPNQUawiKOERvO7yJIWiUHVXZCM1z4PZ3QVIdfWE5tNJaOEO3YBfX43x/COV5HsoLBczoCPS8QhjWpx+cuZ+vy4/K88c9VBSS+LTfSb49KnHlNvCVBwQ75CkUq+WanIx6sOBAc2N8D8PkMFBYCb2sFo4IwtM0hINKEFKxMBNRCdOzYSHK2nTeaB9njeqVjXCMAGIIoSC0Mu6dS3FdjkclgohBd6IsAkwmCJQpoxVXwTby4UogHFR1Joq7YyrqQhcOHM/A7REPI1ENJSEPVcUaTM2BI3VEQio4o7hPAzMz0M2fAjM6+RenMTw8zO3WErzErfTO5lJBD1eyoyaR18c3A/lUIiNdOK/+CU/XH/0aNE1ja0nn1W9zm/nIT/Go0kTCwMtnZ5dFQYEH1gq8dyX3T+ozbTYCiVG4QzfhtZ8kMRVYh/8fSN1APG7j3A0NN8YMbK0DAiZwc8gXzH10bQwFBRanAtiOwK2BGKqMEQTKq3i5rm1jcsrBUCKM5gr2pMHQpIbTXZKDPVvq/O271gtMxcGlVwVByVkup7qAWyO+/Xdbnb+dZ7spSwZYW0k23tQicbpLoL3fn6elys9SOHoF6B0Hdje6qC+IsXiuffZNYHoMYt9zMPJKeHndN4Bjt4En2ySXf1Gy2o/OSsRiwOd3ADNB//dOAbdt4LM7fT0aIT0kXvsrQE5D2/8F6JFCXrH96p/yNum7noKWX8YW2s573/PPz6Nf48JbISUSyXNmPPrTrA0kElEk3vpL/9y2UplZEVtcsvU4Zckc+CJkMA/e5DDcD37Io2HGwa/AyPv0r4v7+br8qHz/uIfqQqAhGZjpHZW4fBv48l4BbTFRIoViBV2TQxN+Nibxxd3J7DAP+Nvj/vQn2ygor37zisUDfGNRwdm+X9jla1XQM/17x4BNtVR2DBSEVkZgYSmuS3rGvH0p8zqkRN+/O+H3tZ5oEygIq+tQcXfYk+O4MWbiWE8An98FGJpvbPGDE8Ce+jjWFNhL0j9VKD4pPlaYkR4A2Sgp8V9CFSsH6UlsrBUcwHgl6YT+mdaxVI2b+9qfwJ37nZE+OBffQ2LbVzKq4UjfhBTSFyI+HYV24vm0hdkcxHBvXIIWLMDmUCGq8ipxeSDIWTLl+S4eXxtD4OpbkJsOQRg6ztwMo2swiIBZjTVTLkzhoX/KxPCUHxCsLKKbt2Dbato3Kmu6dNO3sK4uAjau8TN9tjUIJBzJgRpieBJ482Lm9pL2zUQMMOHixoh/uZzt8f/S6RnRUT14Frg5uwBx/TQ6Kh/hwM8MVGa0s8FFPOZCl36q9PdPzj9Oo1MCR69JHG4YR1D6KUnee38LUnshe9gZzx33+Ivzz09vO5yrx5Lz+Tiv/Smn+nMZUxJ3jg03f9exYdO8sy3KXWEF4IfXPdjnjnB5nCjbxkE1+s2vjFcLheLOSH/G0Ev0XFhcXaFYhLgjeGDqkc0CR9slZwFT2fSBdZRlKDE6RYGZpd7K5Ut6VvTc65CeO+k6dwrFx0VLTKNyrBuHWzbj6NUgxmP+oOrhlhjyBs5BBBsAqMCMYvWg8r8+QWIJ/8kUtJbvqxGVOUzHJfa0CFQXuPA8CU0rgmzeDohCiLomdhvi5KihPoDKgorr4D5QhyIdKAkBJRFgY70/WgIhOdODSnp2NbqwdIkpW8MH1zVELCBYUAD3oX8A05DwjnwP0AXsYDGclkNc8oPXvovKQ8+iotR/sJu6Bu/NvwH2fg6OGeHMne31El2DAk+QFq/Q4Ukd6zQP3z8p8LntFESJAp6LXQ0h/OCUxhkpTeV+jIG262+PSzzQChRa5CsNVBeaXI7VUuGPkhHdg0BHP7Chxi9BEhA4sFbi9QuCR9dc1+Y2CIMDK1tqPHjWXmite4DeK8Dl9yE2PowaD1hDjpsSeP40sK1ewLNdmKaGh9cJzpp5bqcLzUmADnLMtvBuO1CW5+HJLVRXWwBZvxnoj0PfdwgJcoein9PezwInX4S2+7OAHqAIG7xzrwNldZAVTTBLayFJI2jrs0DvRWibH4LrSkjYHKBBQRmMtochXAeeYcA9+iJgT3C2DB76KWiaDu/cGWD4rD+/YvnbZXsup5PTHyJNFEJXAsCKVUcoKQlyoAkoL3ThSXpmCZxr19Ex4d/jFYrFMHWJCzeA1qDEng2S+zk0Gh+NSrx8CXhss8r2WIiZoNWTG4FgUPr9NYP6V4IH6eYk1CsUHw8zAK3nLPILSrCvtQmOK33n0dvdQM85iLp1S72FCsXSlzKtNu51GuhkTGJgHOgc8A8t6T6UF5CD0fJ70E/FPeiexy/87X0Sw9Ma8gIe2uo0JFyBa32+hkxewE/vpc7L1T6JiSiQHwLWV1MAReAq6crEgcKwX/5DP6tLtySmEhpKwh5aKgXrpJy5oSGaAEojQFMlPcAlZ6/EbIGyfD84MhkXuNbr8YhWRYFfnuHYEudvUcmVQE2hizVlBme6XLntwXEFqoqA1pIY9PF+uDcuQroO9MomJCo3YHBKZ6FiqnmuKxGcNROc6IHXdQ7S86Ct2YBESSP6xnV0DfrnjMqhSvMkBsZcdA7pnKbbUu6hOE9D/6iLTnJ94jYXpXlUbqWje9jvjGyvp7RogZ4hid5RyiSSaKnUUBT2YNw4Cwz2+A+blp3QTQPuzWvwhm9BWEHoDZvhhEpwaSDADlRBU2JtlYaQJdHeCwxNkRK93xYxXejXjwHj/axFo63dDd2Jw+2+yKVI5KxFy7PNPJy7ZWIspqEw6GFttUDImwSun4ScHoeWVwK9fiMcPYgTN4OYSojUOQtoDnRTXxKBteVQNrFS+O4HHhoKoqi88QZ/Hq19ABfHSvD5XQIBc/nddxQrk+VwTU5FPehwEHU0XO0FJuK+5kBLFd2vXHhCR0hpzCgWIR534HkCCU/jvs8IZcxYQCs9Hw1/UC0SWhm/o6W4LiejknIyMW1ruHrbQ9SmPpPfd7I00gURMAMr4/gpli9OdAo2Aoi5esa7x9pKgaDuwkQcRiiy1JupUNwzVMbMPYaCMu9d9dNgZxickCiOAPvWLr/gjCkExhMCb16isgd/29ZValx7/e4VmRpxp9ERaqN9m4FGlwbGBU52zrZROVDnALC3RcN4zA/qDE9q6BgAHt7gj2benPTn6xiQeGijQFUhcKITeKAZuNYHLkGaUfqn+ajT9PBGgfFpYDpBbTqu9FHWi8DghOCRmubiGLxL78Eb6ExtS7y2Dcc7gL4JmaFPQOt4cG0NjOGX/fkaduG9qwKj07Pzra0G7/94dLZjMTCuoTSfsm8MXg7RP66jqsDDriYXJ7t1hE2S3xF444IvVOwj0DcmUVcqsKWkHkb7cSCUz4GdxPs/AChbJlmc5A30wKvfBi2wBcOTlKkicGtEYtMaX//nap+/vJvDElvrddSVNkDrOQ/R0AZtagSJky+nfJJJO4bEjCkzxtLr+TzQH4kjH2wyUTI9AZC+DP3dugJzxxNYW16F1y7raedMR5kSVlsZGTMyrajNdVLtCsVqwhAOesc1fNAxm4lK96v2QeCh9RpKI/RSrV4IFQsjWCdPsE7KjIPdMJUlD5M7pIbqfFWLsxAaXHQPazjbk9lfI5fOhzfqiJiSEpIVirvC1QKsF5n+7kG/s64BcoXVUEXRVIViFbF8a2xWKH1jpA8yv31kyp+23HBcFx90+FoUMxTlCba+Tn+pa60UOH498y2PMirOds9/86PvnemmrI7ZIBQt/8PrAhur/BdGggIqJ65LVBYKFJiALUkXZv42ktAXPfy3UilpEhIr7ujz3Y7I1rlMHwPSgjJk2ThmlKFvQstaG905pAENWyHyS9DvFGJ0enZbadRnbIqCMvODaEMT/nZTLfoM9JJA8+5vBQ5u8PVsZoMys/z/2XsPKLuy6sz/Oze8VDknSVXKObXU6tx0opsmuQEzBI+N8bKxscE2zH/ZxgFsjMFjZjA2Zswa2wwwxgM2NsGmDXRENB3UrZbUyjmUKqty1Qs3nf/a575c71WVpCrVq9L+rfVUeufed3M497t7f5uqO8WNKlUm3Fi3B86pl9OiTDbapUPoqIrlFKGkkOu68tzloW3iVDSp/5uVtbCPPlfwSdw59jw21sVy2l7uDMHp2J1pIEPho8+hJhDN22caoqSGMYsglSl5bulG+v+syzBLDdvTsP+CVvAcePmcNqPPGcMQCdfv02T3fVJQFK/D3eNpoWo4+V576X7dBT9CmWGuF4po23++8DBqj0kW4ZmlBd955pBYwkunLxWChsWSvjOlguX6VYry2/KFBTJUJDEkBaX2yGmMFildiQSTfEHE8XIPOYqooWnct813+S8GiVrlwVxhgiopNVYJNFRImP0nc39QtxznRoo7910aBOymDXDrV+H8iG/Cm6K5WqjS18Wgst2UOpXN2QGBpkpXleme7reXhgT0ZeugRcpV+lIxtJFuVFKFrCwotYlSu7IfRMiwEDUtgJ0gZ+XCEyM/HDuac7LTvrSM8tzx6Pe2NWWf0YMQU7pQ2qA6c8jkSQgII6BK3RNUrYZhlhKkExczFqVhlILLMDPhuLkGttmQWFNsGOMzNFG8v0YvJ22+9zBzQMKmIh2Fh1E7WR4wzFKCn7jmEDlD6gANK7nUAjm7tmtZbHm14830g7zrbyqAlgyMp2xYasv/QfZvkz+WQhT8qZwpOmFKGxkB+60zHQPTLVdmRC81udz55rWpt31U53PmCU452wsvZ+EIKKZ0Se8eipIhw2ddh0hW0uJdxyw5Zjio+ZhnZsNMxwnrCtPD5xlTEvCByCwxWJiZQyJBDcvriz90t9cLNU4pQS764bwUTYp0CeZFu5A3DDmhZz+sawLQi6xO0PTfSGUTCZIvTe5VtCLke9W8cJrKXBffdmQMTNWjsqGolYFxqSJJ7MZcZ3YxdFmlAxVjWR1gDpyBMXgeHdW5IUPkB9NKlZSK0FZDnjG5bavqPQxHNRW9MN1vl9dJuN1n4MWjENV+GlIhvOo2FU2UTX3l1HS42jIBDHYpM2EEciN/0ugGZKAsJ3qC9mfQy5tBIAzXjOCOtQK3rxVqPWifUWUtpnRJCWdCOhCaAWiGqrZFFArTZ5jFDF2T6N5TiJBJVfT4oGdmhu6BdCwVgl6AVBa5nTI+tXmp1dmQJ6FZWl1dZpFCzxLZzx7ZqH6sydd7ZmnBl845pq3GdwzPh9papnlgXyjKwgZ2r/RyYjgm4xI7V4opaVg723PbyORt87LCN+ety/0qTylorN0dHk736zmdn1tWChUSS1WsSADooLLWeZD4s71d4EhWPjNdqMnD5uKAn3Y1ghqgtjU9XMYmUCOHk0aQuZAQtarBA84dhBy9gpbgeM4+o2WprxA5PjIpqiNAwATGs8Kc68o9VJdJ/Pg48OIZYNMyMSWNi2iploh4k0B8QvnLGOv3KNEkH9m2AZcnIzmRKmubKe0r9wa0sQ0wooPq/3ZsAsbGO6fOlLbfuj04PZTby7xlWQLGxf25I264G3vPhZXJ2itnJcpDwN3rgAg5GjOlL8w4tl8WjI6pZCoTRzsxSw1TeNixIk/1T0L3GDJVZ5iZCBnALR2iYPzqlmVUOptjZqbDFK6qypmPluzXGcXUU4a5CoJwsLOj8DBqZyGeWWpwuZU5hqou3b0eymfkUrL0MkXKtNWWXkUmwnY8VAclHtoicbKbSkZSCVISZoAHtwgc7/IwHhOq2tSqRuD+zQInuj1MxASEIONe4L5NfttkXKAyLLGxjXKBPAR0iogRqIl4WN9KN2oy1PWjZKhKFbU5rlTVkGi8Y91UktsvZ32qV8KyocqMkwBjO1Kp4/RbipRZ2SgwHpNKULEdYNAOoXHz6yCGuuF1HlVVaQKT/bh9TTO6RwXOD0gVMUL7oaNeIDTaCbeiWj25mtEB3LOuDp3DWnqfRRPAvRsEuq44qjQ2iUgk5jTX6OgacFAZ1lUG0ZoGV5kX903oalmoL+I6Eg9s9oUpKpdNUUmrG/2S6cb5k0BZFWAG4EmJwO1vhXvxKLzhXsAMQe/YAq+iCeM9AbWuoYDEumZNvYE6epm2k18ue12LhsqQB/3UYX96Fw4Dm+6Gedtb4Z4/BDk5AkGVn1ZuhxOsxPBlQ/22gvZPq0CZTEDoOiT9trwW3vLtODxYgaFJ/xgl359TPX6W1KaQhM5POwsKRWKplL0CpKJilOGvbkKQ+W/CUld3jphhlhpxaaC12kFVxMPxboHJhFD/p+taSPdgwUCRQAiGSeN4HqpC1M/RVN+H/NoiQYn1LRrKg1T8gN9bTocrdKxukqpfc7JHIm4J1JYD61qobL0Hb4Z0coaZDY7Q0Fju4f5Nuv/sERcoD0tsaNFQZrpwPT7GmKWFkNTjv8kZGxtDVVUVRkdHUVmZ5a56HXieh7jtXzBCpoQ2Kx+QGw+JG08clrirHaiu9pRQQuLC+Ss6msuAUISMFgV0XcK1gKjrh/g6ni+0iMS4enr3AmXKe1TXJLTJESAUUg+IKn1G0/DUMR3lQWDLchIvBOK2xMtn/fRQEoDoP6Ym8dJ54PZVvjBA5bsDuocjRwS2bKHvLqQnMG5p+MkJKFFoVZM/PYq6OdYFLKsFdi+LQ5c2HDOMwUkT9eUSCYdmIRDUPQxFNdXmJhJ+v0E3YU1OIlBWBtvzI3pMzcX3Dmh4604PLj3dkogSMPDtV4CfucVV4guEhGGY+M5+4LFd/jwEJPpGqWoI8NhOibinqTaK8Pnhq8CjOx0IqsQkNBzuC6F7DHh4vQPNpWXR0BsLq+3y4BYKZ5Nqe5Jh8ugQ0NDgG1tqtN094HQPRec48BxbpbB4tIMsG0YkBM21ITVDCW8YugQ0rVfrQebE6DsJ1K6AaQgIz0VchPHDI0ZBI2eKVnpkm0DZAoiK83FeLkYoWu3ls350GkVj5ZOwJb63X2KDdxx1VFXLDGJ8ZAKvBW9X59Z0IecMs9jOyZFJ/571+i1A2HCUETBd17pHdbx6AXj9VoHKCB/zzPSMRSWePCKxo52iWSn1Wqj7rXSBxw8DD20RqFkk186FOC8HxiSePSbx5u3k1SfVeUjpS119Aof7gQe20Iu6xbH9mNKFIsXphemKKoFg0FOm0nScJRIaLo1KrKgnYZ6PM2bpwBEz8wQJMZn85dK9aFAparqh7j0P1FXQmyJgVaPA0S6Jo+mxcrW7ezYIvHxG4tH2bjiv/lC1keyULz0Ze96MC4kGCE0gZlFFKuCZY1Onp5bBlegcddE/quN7B7Ln62+7cweAh7dQ51vDRIyq0Aj0jkJ9sqdHkUrbWgX0i8ewT7sN/aMSzTVAa41QgtPAmEDnoB99s6EtpMpiEkGzAvd3jMF85V/hrLsHT42sUe0kzhA7OwSOdfnjfvfVqQmvL5wRiASA/jGBrStomSW+c8D/m4J8e65ETfz0pKF8XFKpXt89aEw5FS9cAfpHBW5pl3jqWGrlpm676nKg6fxTMDq2wjv0tGpLGdib2x8Akm048SJyl/pFxHa+BU9dqseW5QJOkdAKOjZo/zALK54Sp3pkQWEmvevI8FfP9Zhh2Z1ZalA0I/HEkcJdGL5eMVfT98mU4s29WFJVppq8woVMhpQH3n8con+n3pfoRR3DXC9UeelEN/XtyepAU/1sqr53vl+qirL5FVIZZrHDwsxNDokV1WV+TnVNWMI0czu2b90JGIZ/k/3uq35bTRh4405SADKGMNr9Pw9d1+E4DuSz/6jaRFkNOirJoDczPTKUJe8WMuwdnvRv5+THEg5TJykj7Ty2y0+jodSnJ4/4BsGRkIZ1YSQFDb8j0F7vG4BR6Wy6WNNFWzcDMNbvRlufp6JXqPz3ilq/00VVpS94QFMt/VZiWQ3wylmgdwwYjZWh+cFfhAGJbabEC5cFVtQAt6z25zYwAVy+AtyzFqiv8pfzwCHggg013rJ6v+1kp1RCDt1IyHOIbiwkIFHEA0UFvf1Wv43WiaJUyNysMpmSpcpfKy8bgbXNEkL6OfC09LtX+tuPHkyeTKpmFMmi1y8DQmXpbSfufTcMMgLO6hmJ7Q/CqGqAMzoAeegp1Raursab6/xtPB3FDJ6ZG0OqNHCxEsEyO5VJCypxRkh/ZE5lYpYa5PGV4k07fcF7Mg788LDfxtcrZjZkG4puavPTnEls2HfWbwvlFUVgcqG+Voqf2eWfd6OTUC+SKIuJz0NmLqB+ckooXVVPUeqA4yDtOZkazjBLBU5lmocwUEotoOiQ7mF/01K0BhnOBs3Si5yZiHswhYDl+UIJpQRVhAWaq/yHuqEJapcqJLWxUiLkTcIdGQDGB4GKOhjVDYhrZegb8x/wyTuGUieCOtA5LDEe8z12Lg95aK8Drox5mEgA9eWUJ0qRGhoGJ4DJBOUqC1SF/bShnmEPMZvSlYRaHtIYekYoPYyqN+kIag7KEIU70AnhJCDqliERqoGFAPpGpBKXWqqpCpYvNHUPUUpQcl+YlBLkt9E6ttUK1bmnVKTsfRYxbAQSw/D6L6k0I62xHfFANaK2rsajG0JrrUC5iAHxcXgDnYARgN64HI4ewagdQO+IH51D8yCbFlr33lGploEMhi2HUqD8VCw6PurLU2XXJQZGXZQFgKYaSofyQzqvjEsV1dRYpcGADX2sF95IP0RZNfTaZsT1MlwZF2pfktjTVAmEvAm1z+T4EERFLURtI3TXhTfSBzkxDFHViPFAI17sjKibXzYU4n3bGqHSnm7GtIlS4JVzHs73+///2dvI2yl3X5BZ9+MHJTbF9qGmwfcvil6+iANl9+F1GwUaq0rvusMsTkrhnKSISUO4sKSOK+q+I9U9h+49Ghm2Skq95N46Mz3jMQ8jk0BzOAo5Pgg50q/82vTaFgzbYQQD+qJJiVuI85IiOQPUB3HjcId6gOgYRE2z6mNEZVh5DIb5PGSuk8mYC116sIWh+r8knlIRjroKAVM6cIWGsnCRsk0MswjhiJk5hrxTjnTK9IMUQaatZJy7eTn5zZTWjZ4e8uIusPe4VKIHQeayZUGBfWd83xSiLCjRZAzDOfg4QB4pSWwzAGx/I05016iwQiJoSNxLD4SVwKvngfUtLhorKPRcgyf9C+jJZNnTXSv97UPiCZkOUyWgnR0aDncJFSEwafmlsg9epF/5v3UdGxv0c3BPPa++k5BB43aV1+BwMt0olfpBy0BGweQ/k2ojsYGEkuPdfhsZ15E3DQlDFDJJnOiWWFUvsNEYhXb+NdVmlTXiQE81ekYy82gIReFe2AsMJX9IgURnXoZcswd9Yh1O9Zvq7RFFJR3t9A0GM1BkjZ+rTSlYlN9et07gwAWZFEh0JeqURQT2n5OIWiIn0umedQaqJkYhLx5W28DTdIjtj+JUTx1GYpqKTKJ9Zmfvs/pl0CNlsPb/yE99URxFOBDCvdvfiGcuVClRkaiOUCUuMi/mztVCkl12nv5PZtLZpKNiVA173Tf/TYblc8QMs9QwhYMxy8BPTvi+Fj4kbJNhu4aA4IOemRnNk2gJTcB5+XEgkbkxO5qO6l2PwtOpjCaHzRQjIG1okwNwDvxIFXsg5MXXVNGBsl2PYtItQ4ECpQxzVdBL2DE7oJ5RsqP5TZ2eMwxUmtRhZWGGWTrwE9ccMzxBuY9T28/1+xEppQY9y9Eb+ZQoQ5Cr/qGLGVGG2NYcg3H0qRxRRmFbMI49ha3NmXwY+t2+s1KZ1xKuK/D8aRJlcn9KKTlUDWFlY6aNBAlKVWpPZkl1NIikKONDIseamihEUpRRaDoSDetxuGtqWef+Mf/NTl1WrnjPiL+MVZFMGwkjBAlDKc5d0TEaagWCEYiKOvR59egZyZwydeUS5WPnc0SZ9HKe2YeVFRNKQKH0o57hfFHG58AFfx39dfXXPTtqhcyNaRtRmlY2tC1/elqD07o5q9GFduQJbG+JF91n5ppbYB96JkuUSWLFYRx/Bg+ujWPP8hgeXDOJO2suwjjyBOzYDLlOzLySbcpcyKA5dVppIBdU3Rdnkq0cD8ksNSxp4IXT2aKMT8KGMsnmIh3MbDA1G+7RvTmijMJz4R58Alp+X4fJQZcJtZ1SokwKGRuHc+IFhLS8PgbDXANxz8SLp3NFGYK+UzsNZ5ilBAszcwiVdKboi2Kc6pZqnFKC3sAPTeT2ZCnSIt93pMqIqxtuIWR0HNVGbg4MhRtaroY71gDjcT+NqBAknFBKTzY9w34KE4WmD07kbi+KnjEGzuW0aXWtOD+apajkQUa6y+ty53FxQE5tu+JHzmRzajAM2bwWTstGnB7MLcK6tjYO7XLGIjkfs/8UGquoUpTAxStFR1PrSOtKKSfklZNNXblQ26gQtE3HabNXZC20nUBETqj87qn7TIOknLD8jmgSSmsKelE0nfl3RA78K/Rjz0AOdQFOMhSKWbBzlHyYUv/PJyO+UKUwjYUZZklDLxFIhCkEid82KzPMLBBO3E9fKgSZ0cUnbvQiLSq88WElYhXkSid0qjTJMNeJ5Yh0NH4+1E7DGWYpwcLMHEJRDGTgWgwyfC211IJChqKFHuYE1ZCchkLDadrkc2LZ0690/vzUV+mb89E2y4baNDtPWNADiLvFQxmV0W7e4JT57tTxci/yVJ5a6kFIIzB1WTTa4cU7H8KOqnlQlE8x49ac5SuwmWY6XsjPKNv4V2FbKlJnyj5RLs4zvMWijlZ8MrfDxeUVFl6YSR6/hY6j1DFCYozQ6ATR5sz8Vzo2Ej/5FrzRgeubEMPMETNVXZruWsswaYqJCkmkzREz0yHt+PTDZ9i+DDMbXHl9wxlmscHCzBxCfiDTlW5rqfHHKSXoTfyUZSrgqO/oIf9tfCGE5g/Pgn5POf8vnSB/leKHWcicmp5B3jOUajQW9Y2EsyGzPrumPadNjl9BW3nxTkJDhW9gnNNWCQxH89oqaPq5bS0VNrSxHugj3WisyO1oDERNoKal6Hyd2pXqDS4ZIFNETDEoKobWldY5U2I985BB27EYatvmpVJ54Sr18DJlnzkWhBJxirxhoFLLZt4CGAFlJsssHHR+pHxlCqYyZQkzqpSZmLuIGTk5ChkdhduTG6XGMAsFRXQWgwRuMnJnmBkxgv79rQha+c1rOD8b9MpkGcpCBCPTbluGmS10Pc+rd5CGXkDSMwTDLCVYmJlDNE0oo9lC4gu1kZcIjVNKBHUPm5ZNTfNZ25w73pmhEOSKrQWnIVdsU8Oz2dAKBDQPIzaJPxKt1YVfY25oFTinyl9n2NgmlNcKCRX0YJntBUPGtJOBWoiyqpyHxzpjvGCHnTb36ubcVCISjWhfdGa1UWTLsjqBruHcfdZeFVdhuaL3NDbUx3MEq3ODJpyOXQUFKzLAi4YblV/M+X6p1rMQtG4U1UDrStthY954hdpSLKvxYHrRnIgWSrvqHA8W3Wfe2BXoy9YVnJ6+chtcipbJXo81uyHN4mlizPzjzpDKlI6YSZn/0uFCAg0Nu855p1LhvCvJ2pQMs8AYwkt7kOVD10pTcMgMMzN0XxNrbi08sGUtPI3ve9PhmWGgfkXBYdq62yC0aRRUhpklAd2b8jySgtrpfsAwSwkWZuYYEgce3CKU4WsK+j+1Tfemb6EwTQ1t1RK3rs4s35Vxv0LR7lV+mW+ie8yA1bwZ+sa7/LchRDACfdPdSDRvUsOJSMCvtESlsX9w2BcUDpzTsLNDYHOrlxatyGT3zrVAKCAxmvSzobSnu9dTqTBXlcOjSlaD4xK3rwHWNGWieE5ciUDb+QaItvXqQVStR+ch3Lve77CntC/yo7l/s8DgWMYosqFS4v5NAv2jXjqaoKlKqvG6hzNtLdUSD2ySCHYd9hukh9CVk6qNppGKXuicrIBx21sgqpN3Diqr3boW2q5HcWIwnPZEiFoS920SqjoTQetC63T7GqGEG4JEHE1I3L2eSoT745HXD1XJom2VMiambUjbcvsKQD/8o2RjCPraW+Gt3I3zQ4Gi+8w5vR9a+xYY624FAskJhsphbLoLevMquK89669GuALa1vshGjoQCPAriQWPmNFnEzHjpQUZkTwJrjtiJumzoCJninhMMcyNhLzLNrUJbFmeiY6hSEO6Xy2vAxIed2uYmRGU1tvQ4d/nwhV+oxlUYo2+djecYpGljMKBrvoNYtXOdHQMvTDTd7wesroNUnIqGHP9JFyh+so72jPRMfRcQt9XNwEWe4oxSwwhJdtDjo2NoaqqCqOjo6isnJvwVTL5tdzsdKHSvHhEExKvnJO4Y41APBmhQm/cg7pUz3gxW6TbAhpFsUiERBya50FqGmIypMpjW54GKYUSFqizTIcVXVDz22xXqjYhJExdUyk3LnWAkvNwXAlPCpzp9ct3U2nr1hqKQnLgOH6Chi4khNChwYGmDOYkpGaiezyI8jClffjTo3+6h4AV9YAj/Tb6rXSj0I2w3wahFHfbEqpvQW3UqkPCsYGIGYdGHTjyidGDSDgBCLJqSd4MaJuQr1BIi0NIMqER8IwAPM+DK0JKEKL1MmmZYcGWAbV+1DYWlSr0PhLMbGND83D4Ij10uPCkplJSAqrEuoDtUJu/fJTaIoUGYcegeS6k0CHNoNpncZsqYPnb3dQ8JSppngWR3GdCM+AKA6YzqXa4FAJeIAIRHYc0gsqbhkpvByLT5F8t0vNyMfKvL3mqYhdVdtuzWqA9WcUrRf+oxI+PS+ycfBZl67ap48g+dwgvBu7HrlUCqxqv/dpjH3sebvcZ5U1k3vIw9Iblc7BGzGKlFM7JiZjEWYpCbPZgebpfJZ7uWQZwqleqc6UsxOIMMz1UrfGZoxKPbvf9Uvz7qKbuo999VcMj2wQqI6XZbyuF85LSvs/0SWxf7qmqjhSxSf0GGGG8eFaql3EV4cWx/ZjSJR5L4OXzBvaslrC9TN+W+u2vnAd2d7gIhUvwrTfDXCOcjT1PkDiQ8oUoZSg1YnWTwL8fmFp+lG6sXcMS/aPAHWsFXjhNrXSjTYZzpBG4fa1Qpeuy2ygKhSouUfnwzkGJtS2aioChdKSGSk1FARy8KJU4RFCEDG0zKg+dgioSneiW2LPGUCp5VUTAPn0A47Vr8eKlCCYThnpLSukcXcmS1/kuusd7fHWdBCiiMhxWb1dHo0JFv5wdoGghgddOSVjJqlnUyd+6QuDSaAgrG0KA5+Dpo0ZWWfHceTRXh7Ch2VUpUeHTzwF956BrOgx6E+c6KvJAiUq73oxwKEg2rUAogjMDukpXSqWjVIYpUgnQJodgjnQh2rwNj+9PdW6m5sjdtS6iopTK7UG4z31Dpa6kDjtz+wOwDz2t/p/KgDF3PuSXy/ZcTHmfFQhBu/VnYHJufclAYiYdGyTgiSIRM+lUJs0X/AiNBDgSLJX4eB3zj01AlFVCjg0CM5g9MsyNwHI81JVr+N4BLec6TOLMvRsFbHb/ZWYBvRSi/kb/OFV9CWM0KtVLktoyP7J2NCYXjTCzEFAUcEVI4Dv76TzM5JsbulT9RTZlZeYCPT6GWxoEXj5XjZ5RavEPrJYqYGf9MHTqloSL5LYyzCJkEUgHzHxCD3KvXcqIMiEDKnKGoPbb1ghsaZSI5/VPaiJknoucTvHmFuBoT24bEQlIrKgX+OlJCSpkFAoAFwakCkvcs0bgldNS+ctSZMxzJ2V6uej3tFzkv3K6l97AqCGAZ6Ps2ON4XcceWOFa6AETpwYyijmJIxQ5kqqiRAKQrgPrGoFT/ZQeJFRJ7o4GqeZBYghNf0d7RkyjKBh6G7SumTr6EhRBqSonJYWZ1XXAhAv0jSTnoUnomkBYxIGBSzDW7IKoqIGUASA+DBEuh9t5HLL/LLBqB1yp49BFX5wiUYuq7ngeMBIDnj8lce/6WkTKJ6F7Npqrg+hNzodSms6cBqjIJ/2WXhRcGZUwAlruybzjoakmvw3tvmFJulqCBgSCgJXMJbPi0By6y5Vf3UHEzBspTxlKfaPPdOWyRbZDnvDLfF13KlNsXIWny4kRSIvLnzILj65rePls5sAuCwCTli9QUvvd6zlahpkZup7Sy6d9Z3w/u9UNwLHLfp+A+iUhk5WF6YgEBJ5P9teof1Se7BPSPeroZamiOxnmutEE9IP/gVvad8BZ0wHbrIDpjMMYvADt4EFgz1sWegkZZukIM3v37sVnP/tZ7N+/Hz09Pfj2t7+Nxx57LOdt8Sc+8Qn83d/9HUZGRnDXXXfhb//2b7F27dr0OENDQ/jwhz+Mf//3f1dvid/xjnfgr/7qr1BevnAPl67rp+FEkyEJFNFAIoRegulMJHyQgHHPegGyEqFoFqoCFCBhxPAFipjle828YbufRkMpWjQetQV1X7+mNlEh8FA9iRTJNgfoHpIoDwkVev76rSRyUPls3xPAkxJHuyTu3kjii8BIlN7AABvahBJB6AZPy9I3InG6l7Yr+cBIlC2/FYEVu+FReo8FxF1gXQuwvkWqVCSaL60XbXdIimIRiFkegjW+ETCVubakjsmEv5zkZ3PnGg+2p6f3GVVRunMNhU4KRC2BBEzctc4vkU3zmCQ/GOrYtfueOC61JYAJLYTwXT8HQ0tAUC4U+XJU1EAEIxCbXqdSr7zxYeiGiduXR2DpEdge1PQo5Y38iNprHBWiPxhYgQAEbmn3oLX7YZwUXbR1s0DQ8BAUtDFjKDOjEEYI8p53q4dzYcchEzHIQAj6Pe9GQkRy9lngnnYE7REVeiwpBDkYVmWR3deeUWlN3UOeenMY0CUinBKwoKQiZOghgo636SNmsvaV7ldmup5y2XT9VcJMLTnsBWYsj8owN4KETdXogFtWCnWPoO8qkl0CPz0lC54jDJMPCTB9wxIPbPH7JbEE0N7o34cpXS6oUoiZYpD/3fpWv5ACCVupfp2uSew9lrkvMcx1QSbTt70dnlkOxxWIW4AIVkFbvg1a00rA4PgCZmmxoEf05OQktm/fjl/6pV/C29/+9inD/+Iv/gJ//dd/ja9+9atYuXIl/uiP/giPPPIIjh07hlDINy79uZ/7OSXqPPHEE7BtG+9///vxgQ98AP/0T/+0AGvke8tQZZ9Xz2eiUOihijqRbTXS9z8pMciU9sAFiYEx/3tzVeZN0qDv/alEjrs3CPVGcjhZuIdCfm9d46cwjWZFz9SVk5mwhgt9EpdHKN1GKLNGipgh8SIFlRbf2S6U+e+xLt8bYFu7wP5zvrCVglKVyJx4PA68cFpidSPQWivw0hlKPfLHoa26ptk3A3vyuN8j2LrMUya6+85RB97f7hRUsKXNQ3udgx+e8FOD3rjdQ/coRbDk7rPt7X46yP7zmbZbOgR6RyU6B/02EpBuXaVjLCZx9LI/j7dvnYR3/gisS8czofZmEOb2++EEKyFf/YFqcl73SzjSSdPK9GBIwLtznYnJuIeXzmowTeDhTcD+iwI9I77XDFEW1HH3Og3BkXOQx18Ayqph3vIIHBJXRvqSCxeAc8vP4MXLHoYnM8cdiU63LzNhvPpdVUJbbZfqJhi3vhFR28BPT1GLb3K8e5UvrDELHDGTLGFPom9+JFQqKian4hv5D5Gwcj2dYzo2PBeCqpcYJmBzxAyz8NB5sGslpdZK9XCYgszeX7fJF+YZZiboXk8vavaf89A/lrl20suhO9YJFQXCFIe2E0Ub/+REbr+OfAFft9kXTRnmepFSg21G8NIZ6sdm2mvKKKK/Ur0EZZilxIK+Dn/00UfxqU99Cm9729sKvq39/Oc/jz/8wz/Ez/zMz2Dbtm342te+hu7ubnznO99R4xw/fhw/+MEP8Pd///e47bbbcPfdd+MLX/gCvvGNb6jxFgISD0i8yE5zp/9TGw0rNSgF52hnRpQhdq4EXr2QEWUIMhElwST7wkht+aIMMThBQo+HDW1+J5oicShFKfvmTVB6zrFuicqwxFgUaKr0xaBsUYYgEYSEj2AytHhVky/yZHfAaQhF1ZAnDVUrouCB5mqB509rOR0EelA9fFnHaEyoak+rGsjgWM8R0gj6P7WReR2lXqXaXj7np2WlnoFp2rQNaF40z9tWA3LoMtxLx3J9aOwE7FefgAl/obV73o0L/RmBJwWtO3V0asr9U/OhDa4SrXxRJgNty70nBZwGv/S1vuNhOMeey4gytLwrd2NfV1mOKEPQd2r3Vu7KbJeRPjgnXkQ4mBl3YEzgtUseEgnuYZVCxIxKZZquKlN22XZNg3a9ETMUjkaQKEMRM5zKxJQAFNGQL8qkqgkeukBG8/yqnpmZgCHxWmeuKENQP43SiVnfmx56KZUvyhA9I74vIEXcMsz1YmlBvHw29+UiQd9fPuchTnYBDLOEKNk8hfPnz6O3txcPPUReGT7kOk8CzAsvvKC+09/q6mrs3r07PQ6NTylNL730UtFpJxIJ5WKf/ZkLqKJQtnFtPjSMxiklKC2HInxy2lyBPmWyldsZzhZqCHroyxdlUvSNCjieQGuVn0JDn0J0XqEHS4GOemAk6hvyFeJcHxnyCrTX042/+AMnbWMSSTa0SCV8FONYt0B9mYvNbRIne4rHvp/qkdjclrfMgxKttZnvNBfyzNnQArSFx+Gef63wxDwX3kAnjLvfqdKLzmQ0lBxoG5AAtonmKwQuDBY+TWmbRqlTVNemKinJwa6c4U5VmxLJCkHtdmXeig1e9kuIZtE1JJBwb8xlYr7Oy8UMWQKlhRlVtWzqOKmjV2SlSgpNh5CZ8u/XhJPIEmZMyJQXEXPTUIrnJAny+aJM9kNhqmIew0yH7Qp1fyvERNxPkStVSuG8nEj4L5IKcXEgWQmTYa4TshMo2o8dz0TDM8xSoWSFGRJliKamppx2+p4aRn8bGxtzhhuGgdra2vQ4hfjMZz6jRJ7UZ/nyuSkBSxEV00XF0LBSKxhR6EFvNm1kVjtTx4UEhhUNfnRHMUhgoSiA2go/Kma6adG4lJo0Ps3zIc2L0pXKAhJjieKH92RC+POW/v+nmx753OS3hc2pHTlK96J5UyWbYngTI8rThYx+i4lQBG2Lhkp/u0/3cK0qWtUvh6rtXeCGNh22LLB9kqlNOU03KGBmvs7Lpe4xk46YyU5xUtEzlMokrztiRugmBNWS51Smm45SPCdnuu9wCgUzG2Y6TlJ+c6VIKZyX5ItXDOpbpV4qMMx8nqfT9aMZZjFSssLMfPKxj30Mo6Oj6U9nZ+echXaSKWExyJNFVfYpIaiyT7Y1hWor4DyU30ZmsqkUn0KI5G9Odfm5yMVIpWhQlaTqsuJCAnmvkOgxNAHUlhcfrzLsP6hSqlJtpLgKVhWR6kGXLH+q8qt/Z0HGwPnCEo1Pb4tyxiujedKjsIAoryk6Pa2qAd7kqJp3vuCTTU0Zvc3zjxfaPsUoDwug5zRUWas875GANr0KGNDy7mi0gdV0spZX+OUvF/N5uRQ6JdosqjKpkVIkI2auy4AxJdKlImbY/PemoxTPSWX0WwR1CSuxeyxTmhTq+2RTPs1xttCUwnlJfa1izNRvYZjZQtH60w7n6z2zxCjZS2dzc7P629eXm+9B31PD6G9/PxUOzuA4jqrUlBqnEMFgEJWVlTmfuYDKJa9vyXlvnYba1rYINU4pYeq+6W42ui6V4W42kwmpTN1ykFBRHYWg3wc0ia5RP7qk2E18TROlQ/mGySR4UNWgQmxopWpBEt3Dvsljsc735mUC5wckTvUKLM/ygpkyXitw/oqOF88IrGstvs/WNAsczerz0PTaakW6fDVBHZAVdVRyGzg9Wg599c7CMzUD0Opa4b74XQSsEWxsLbxwtA1oe1Gqk+tJrG0qLLBUhaUfuTM2qCIjRMvqnOHG4Hm0VRf+bVu1q4bn0LwGkiIjsljZ4ItiN4L5Oi+XuseMEl+kB41qwmcLM7i+VCaZipDRDeUxQxEz1xOBwyw+SvGcDGhAXUXh45BSXalyHsPMRFCX6v5WCDIWJW+8UqUUzkuKEC720o36dWG9xMLDmUWJITy0VBe+prfWSBgzvIBkmMVGyQozVIWJxJWnnnoq3UZ5tOQdc8cdd6jv9JfKaFO57RRPP/00PM9TXjQLAb1luWejX146Bf2f2krxDUw4qCnRY2Wj/7aReOYIsGW5wIq6TAzGy2eAbSsElmV5q1Bp0t2rRM5Fk8an321eLvDjo34bVTG6c51QVX6yBQ66ea9spOpKftupbol7NghVNSgFPYxuWgY0VgFHLvttxy5L3LtR5Ig9JNTsaBeoCEmc6vHbyGPmvo0SZVnbPWgAt6/2EAm4OHoZGJggA2QXd62fus+orW80U36VSkFS25neTLUbmjYt87k+v+HwJUBWNMDYcLv/MJvaLuU1COx6FHbCf9iV+/8DLTW+j0z2myVad5reeDKt60dHdLWd1jV5OSITbUsq362d9b2U3H3fhb5mN9CyNr0jtYsHsb1pEsvrcm9q9J3atYuHkgsn1O+MNbuw92gw3bSq0S+HGaD658yCQBEytC804YuMxSJmqHqYn76ULczI64+Y0Q1lKqxSmSj/zmVLTGZh0YWHPas1NGffdwTQ3gBsbBMcMcPMCgkX61uFus+l+j5EUxVVe6GqdvzANx20yag/VJ8lktI9am0z9R0Ei/jMnBA0Xezo0NBWm3s8LauVqnIqDWeYpYSQC3j1nJiYwJkz/lP5zp078bnPfQ7333+/8ohZsWIF/vt//+/48z//85xy2a+99lpOuWyq7ERRNF/60pfS5bLJDPhqymWT4EN5uhQSOhdvHmiTxi0gkXyGoZQVPxWntKJlsonFPVieX+LQ0IC+IYm2BnpDn2lTKS3KlyXZpme1uWT267dRpMzpPops8X1caLU9VyofGTLcI58d6jzTGyvb8+eRagtoNhxpqnZqozDFoO4pvxT1W+mLK6bw4FAZvaT3DIU70nhkVEttMtlGlQFc11OpV6k28kgdS+hqWdPjCQeWNJSxZCoNKyBcWFLPaQsZLuJOsk34yxfQHdiOX6aVsklM4fjbxk34vhxCgzSDcGMTMAIhuK4L1yzDvksBdDQIVEeEWj4l0Eio0uVUXt1zXRi6UG8EaJlpG9A8aNoU6aSW3Y1BOpbyAfGMgDrGhJOAdOxkWxAOArCz9hn91vQSEI4F6dqqFLI0gjh5JYBlNVn7x/AQXMA40bk+LxcjVN3i+GWpOsBn+6QyyH50hzbFoPrwBRt3hI9Dq/cNnb2xQRwYbkJrSzl2rpohFrgI9ulX4F4+pcq8e6MDcE+9jOC9/wUiXDEn68YsPkrhnCT/rdExiboq/35C9wq6TFGkzMvHgVs2CFVNj2Gmw4pOwo4loJVV5/R96DhyE1EVEWJEyrEYWIjzks5DadH7J+rHZffhJIZj9JIsmWrNMNfBZNTBi2c03LZWwk32+ek4M4TE86eBO9d4KItcWx+HYUqRBT2aX3nlFSXEpPjoRz+q/r7vfe/DV77yFfzO7/wOJicn8YEPfEBFxlA5bCqPnRJliK9//ev40Ic+hAcffFBVY3rHO96Bv/7rv8ZCQg/HlAc/XS58qREOaUgFoAxNSBzqgvrklHxOcu9Gv0T0HWsFfpQuQCTVQ//ODoGXz/otJ3um/vaBzcDTR3PbH9nu+8skzh2BPP2SOiizD0yZ/B66650wKiqROPYCZOex9HiiqQMHy+7DpUHqBPjTprentgOV+lQoMKwsKHFPxyS0YAgvntUxNEECRP7yaqgtl7hjpQXtua+rFtLmg3WtOFf7IE71p5ZSR2sN1PZAfBzWT/8NnueikHegu3wjTpTfrkpuUzSOX/1q6nbqHZHY0Gaozs9/viZU5EpduVBiH92UqBrC8S6JHS066k/8CMiqmGPe8jCMhowZYHZy0uC4TO4zOjinHqAUEVVXkepM8avnhcZ1ZTqiajqPGY1qM2n5qUxSRQ9eM7alRDtCRcwk05tYmGEWEqpE92I6C3PqtZPNIJnZIGwL+qvfg7fqVqB6OWxHg0al1qMDCJx5Ed6W1wGLRJhZCAbH/ejlDW1CvXik845eml1gt3LkAAEAAElEQVQc9/t+D21hUYa5fqjPOxQF/vNQpn+fP3waa0+GWXQsqDBz3333TRvuSALHJz/5SfUpBkXXXE10DDMzM8ZQ0XCqPpTXLGbxWzlt4yyDt/JmQg4x+fOdaVnUMDUS+XDo04+XPx3yc8lrpPFSk5xpxrMJnMreJBQRdDwpktHDeXZlL3898iY4TQg2pWiRgFboAZ9StahjxZQOtK9Tnr70t1BVN08dfKTOZAmQlH4ED951lIGjSCzlL0Mk/6YqNTHMQjHjPYYzKJhZQTdXF9qZFxHEiwjSNS47VZNTmWaEKle9et4/4fL7JgzDMMzVw49hjCJhu0jYmkpHooiMh7b46Vd2VogvpcAc60x65qynFBtgezvQVOmLaCqVSQNuX0O+MkBLja/e0G27Z0hiXaufg/zgFv+3YdOD4/gpSSMTEmbzBphGAHbj2tz0JmcM2lCXetB0xoagdWyF17Edjh5W45FwsVkDVjdK9fxIfhypEtaVYYlNDVEI1/J77LqJIacclWYCGtVzdGO4d7WLSS+k5kXTIyicmSJuKvRJlfKDO98GqQdUSlLcMbDcA1Y0+esbNCTijsBYlJ6Ny2FufQj6cCecZdtUGpGqbBQbhDj5HETrGiwzBXQhVW42GfhurI9D92wV5XAlEcT+Syaaq4SKXKLOzht3+ClZCdv3uzE0AVPzMDQONIZtiB0PqodylW7SsAoxz4Az4ST3Ge0bCc2Kq7SlgG7iDVtDEJ6HgBeDpI6obiAuwoi5AYQD/JarlKBzgNLYCPpbqOMrXc8XCrMiZoTuR8zI6zGZoTQ8PemAmYycKVROnWFuJOTrVRYB7l8vVSoTXbPpek33pyePiBmreDCMwgwCoXJot78dwolT5Qh13fSMELyz+6GVVS30EpY0teXA3e1AXY3jbz/qT1FatBnCM8c1rsrEzAlkBUEvE9uqXKyuiUOHDRcmzg6H0D2q88tEZsnBhzSDibjEhX6qKuQ/+JOu8YZtAqd6pfK1UG/tk+aKG5YJ7D0lMRkFykmg2SRUSs2lK77RKHWK717vhxxSuhNpISmD3COdEl1DUgk1JBhQCGxZgCoj0VL4HerNy9ZBH5N45Zz/QEkX3c3LKtFc4UH/6b+qNtGwAvH1D+LVsxJXxv11ILGIzImrApSq4//2zds9tBgjcA79FHLsiv/bjq2oaVoF9+BzcMcH/bayKpRvvBvDohY/PuWfEmQsTD4vbvc5yLOvqDa5840YMcuUB0yqhHYqxejgRalC7Im68lbs6FiGQxczy1df0Yjdt7wNQnPwxCESZYA7VtrQBi/B2/8yPMsvRVxbvwJvWH87RrwyPHvM/+3ta4HJuMCJbvLZ8ffPsloNW5visF9+3E9jIh+bO9+NM706TveTqEXiD/DQ+hhCvYfhdJ5Qbwfp4d1YvgFawwpYr/7Ib9MNBJZtRGjFRgCcplJKOHkRM3SOqQpcWVFSlK6UL8zQyL4wcx0RMxQdkxJktGTEDAszzAJD/mL3rtOUGfylK37EGInQq5uFSpU1VMIpd22Y6TEjZcCet8LrPALvwmHAtX0D9ebVygjfS17zmMKQx0dDVRTu8X3wBi74L76o8uTKnbh/7WpIrUjJJoa5Csg78g0bEkDnYYiDmX7s1raN2Lphi3qZyzBLCda0b3LilqcqCh3vzpTifWCTnyNM1Y1Sb+jpgfB8P5TYcO9av+3uDcDBix4uDCRL9lJJ8GaBw51StaVCyqly076zEpeHMik6JDBQBaPRGNCcLMNNxrYkeiQccvrP5I++ekFiwKmC1rLKH2/dfdh7Argynnk4jVnAS2ckYpbAhha/LehOwH7l8bQoQ4e73roOzivfh0yKMoScHIW7/z9Ra0ymKziNxYC9xyXiLVv8h9KyakTDzXjuZEaUISW/tlzg+VMZUYYYnBD4yQmpSqenoGV99oSmjI0JiirShrvgHfsJkBRl/BEvwTvwA1QbvmcMbZvRKHC4M+OdQNu1c1DgpYtBuKv2qDax8W6c6DdxoldL77M1DTYCl/bDu3jUv5mpHenCvXgUbtcp6MvW+W2uA/fiYdU5dRJZy8IsOClRlEhFzuRHzZBJ9JSqTEInZ3c/zakAklL4Zqqw5CQyHjOkCpHww8IMs8DQ4X/gQu59h+5dJ7uB0710j+GoP2ZmrIQNr/MY5NlXfVEmlb7UcxrO0Z/4VeiYopgyDufQU5D95zOdPduCd+olyL5zEILNnpjrhyK99fMvQ3Tm9mNF5xHoF/Znzl2GWSKwMHOTYzkCZ/py23Rd4PxA4fHJTJeiMQhPCvQM53aCq8uAgbHMd3qTSQ+WQxOFp3emF2ivF1OqzFAZ7WyOdgGJ9j3Q6tpwZVJX5reFoKicjkaBN23z4PaeB5zMiNrKbXC7Txcu+Ss9OOdfw12rM8Oo03+mj+p674a3+UEc68rtqHU0AKcLGBynRCYSnaojmTZa5sEJqVKTDCcG78zLBX8ro2OQ0VE0VvrbhrZRIQYnNSTKmtQDs1XTjrMDuadze1Uc6EnWIs/D6zkHrW5ZTpt7+SQ0m4WZUvaYSbVlQ1ExlOZHYfhpkqlMXpFUJufES0g8+dVpI2BUxEwqlUlN01Adb4ZZSGxPQ+9IYfHlbB9gedytYWaG7nXy0pHCA4e6oFF6DlMUkZgE0i+9cpHnD0BwX4KZA3THUv3VQnjdZ6BR9VOGWUJwD+Ymh6Iw8h/0yFtlOgPFmA00VPrGb9lQKhJFrmRTVeYLFNPNPxURkCJh+4JONhSR4mkBiJpmDCTTgwoxPOn/NXUXciRXcRKV9cBIEZWDho/1I6jlKj4kKDnljXAC5RiezF3QyrDAyOR0yyJRkSp1laR/3PfugecA8eI/liMDWF7npy1NV2VkPKEBgZDyWsjfZ7q6YclpjQ9zmzxVdYcpHcjfKRUpkzpPUpFtKchHplDEDKbxmHH7L6m/9snC4qA/o6xUJkI3OZWJWXCiieI3JzrcuSoTMxvUtWyaqEEvOk1Hg4E3rkpeFob6ERzJwMwBfp+0eD9WWtxnZZYWLMzc5OQLIKpthirJJMBQVEy+6RY9ROYbL8YSvv9LMUSBokL5Qk1qOTW6CMcnUDZN6nJqXhIaRCi3iJ4kL5bQNOUvgxF4eSWiwwEJ3Z6E5tlT1oMEpNA060bjUypWNuUB33dHhT+kKt4U/HGFesCg9Z4uMD9kSvUAXWifyZly5LM9SVJkP4gzC46bVWwpZaY4JZWJImZknvmvwLQRMylRTg73FBwsaTiFC2cdo+r/WRFoDLMQBM3pU5V0jcsyMTOTfW0rODzAHinTIcLTFCmmqoCF+hcMc7UYxvUNZ5hFBgszNzlUyaKpSk4RRuqK6BfloYxwYxr+9xT0DEjiTLaAQVE1YbN4GebWWqB3JHf+y+uBruHctpWNgNl/At7lk1hWU9xFgDxuRqMSPzmhQ1tOZrZZy3f2APQVm4v8EtA6tuO17lylZW0zIM7sQ+D8Pqxvzp3rxSsSq/JSrrKhykoDo8h5WG6r0/DtVwBphIC23OVLoxvQqhvUtiOPkLbawqORx02ZN64elgPxYdSV526zK4kQREVdwd9Su5wcyW2rblKVp5jSgQpdpITKdCpTXkRA2vw3O5UpebwVinxTb6CsmDK9lrEJZSY8hVTKUl4qE0fMMAsNVcFLeYHl01ApVQU7hpkJzwgC9csLD6SXOsFphAcGIlLlV7YqNKx5ld/HYZjrxQhCVBTuBKv+LZ3HDLOEYGHmJicS0rCzQ0NVJNOZpYpIu1eLKWk4kQBw5zqBwTF/3DN9EnesFao9BVVounWV8NN1snxf7lovpogzJCSsbBDKxDFFQwVVHBLozHjzorFKYk2DA5zbr76b3UdUpaL8yBpK/SER44XTwFAMcANlMDbdlUnxsKLwYhMQ6++YEqYjVu6EW1aPzqFM2+ZlQHliAIiNw+s5g7qIjTVNmeFkyktRDCsbcpeDlmv3KuDCgF+BiqDx7lzjqTLXxFMHdBjtm4E8nxeKWNFveQNOD4eVt8xLZ6galkBNXh+RtuU9q+IwzvzUbzj2DPas9HL22eHeEOyN90NEcistiUgljPV74FAlilRbWTXMLffAiEwTUcQsTLnsVMRMkVQmJd5QJRqVvpSBRi9YXntyBEdDu/Gs+TD6tBY/7Dx/nJQAk/1WmVKZ2GOGKQFhhu5D+RGMlWGJXSs1REL8pp6ZmUA4BGPjnUD+y4tgBMbORyCCeR0gZoqwZdzyhinijKhqhL5mN8zpwokZZpbokQqY2+4r2I+ldhrOMEsJIQu+Lr25GBsbQ1VVFUZHR1FZWYmbkYmYVOa0VI0oEgQqgn71C2obj0GlD5EAQ1HkYwkqse1Hy1SFyGzRj4yZjEMJAzQeRXpQ9SLyhiEvlrApyZ5U/Y58aKoiQIie+aSLiQRVh5KojGgI0HhSV/OMO755bkAHQt6EeqCkfFKtshaOWQ5Lmmp5KeWHhAtDp9QNoTxtKHKntgwIawkYbhze+JDKJ9eqGuAYIWiuDW9siJI9oFfWw9UDSMgghpK2L/RbUzgIupPwRgeUkKNV1mNSr1Smx+Q9Qw/MZHbsuBKaEMrfhqKJaN1M4cJyBUYmPJiGUNuARJmoayjvGRJWqC0o49DsGNzxIYhAWEUxnLwSwvGejGZK09yyTCghazzqIhwQ6o2xKRPQrAnIiRGIcDm8cBUcLaS273hMoizkjxeQCZUCRjnzWqQCIlSuzGJJcJLRcTVPejvYOVmG5mqBUKA0qprweQl8/1VPVSgjM+y4LZVQR6XnaT+leP7gMCYmbWxrz9XZT16yYBnleP2e3G3nXD6FH11swKRehVbrPO7YUaWO7WzomLde/B6MzXerDpD6HQl5iSiCdzw2r+vMlC6lcE5ORh0YuubfdxJQ95mK5D2G9ElN9xAJc3g7Mz2TCYnJmER1IK6MbL3JUWiUnhOqgDQjSLj0cqo07oWleF5SHyMgHWjUv6CCBYkotPJqyGAZRicCiFQIlIX43S8zN7iTY8qXkY41UVap+qw6/WWYJQb3XhhFeVigPAzU513nSGgho99sQiGKYsl8p/clKlKjCrgyJvH4QV/r29jipyqd6pLoVFkzEm/YLtBSk93ZMVCWVbkoe755LUBZRc6BS4GylTm/9adLbVRC2D7yE3i9Z6He8d/zHj8X5MdfV+PI8hrotzwKIxxOTy84ZXoU9lOtOhuxhMTeE1IJQbQe7fW++EMPykR7nYvt5V2QA5eByydUW2TFJlRtvCNrerqaR01Z9vrT/MMwqmoxEZf4wcFMlE0Kms/BixK3rhRorNZhxwUef43GCiNghFERbsDkAIlb/vj3bxboyEm7MoBIGVDbhOEJiSfVb2mZy7C8vhnneoHuZMrVI9um981hbiwUHZP2mClWLtvz/WTy0YQHV059sKCKX47Wpv6f0IIqnQl5wkw6MibPY0ayxwyzwNDLgqdf8///4DqgrRoYGpL4z4t+28NbFnTxmEUCFTn4sbpVh7ChOYS1LXXoHgH2JQNJ791YqB/CZEcMv3CaotMieGhjBKTfn+oFjiVtyx7etjhELWZxoEQY+tS1LPSiMMy8wsIMM6dYWf4Xx3v8TzaFUivmA+W7QeUwUw0/+X9TfTakd1UmrFQCO8XFvCqRCVeDHLwMdJ3IzCMRVf4dIt/duNgyy+Le80TUBvYeB7ZkpcXTMg3mFY/IXs58stNgLg76n4XYP8xVpDLle8x4BcQbUUiYoeN26rHnxaOwlEQoYYkwZKyAAXA6lSmvKhOnMjELTHbVpadOTR3O1zBmNmQfJyd6/U82FmvQ00LFD1I8eXzqcHphwDAMw1wdLMwwaRK2VJ0VeqBLpbNQuGqKVFgvRXZQApxIRtpkj1cRAlY3AWdzK1Urbunw039oXCEkykOaEi7oDShNjyoQBUyhRJV4wlMihakDgYAB1/UQtUS66kYkqMFxXViWH2FCvw1mmdgYpolEQzswOQjttrfD9vwHTENzIQ89qVJ/YOaGhsQtT5WdTpkihwIabMtSD6lBCGxoDuDQZb2goWprWQKicyBHWNEaO1S4NP0gaEqYho7JhKfSrYgIVXzSNdjRGIR0oIsQIgF9ShnyFE1V5L9D293Dpjbfm2ddfQJVIRdRW8OpwZCKrqkLxuHFPSUIiaAfAiQTMUjpIWT6rwB3tgMrKmMqqsKTGk4NhXGqZ2pVLWbhoHNDnY/a9OWySXzRVeJhLlTFzCtgI2YnbEihIWI4sGRIpbnNzmPGAFwWZpiFhVI0icd2+fcsSjOliDFDE3j8EF3D+E09MzNUvID6F5QqTKmilJpNYgN5w1E0SCVHy0xLyvduUxt5+wl1n6K07tcuAuPxmat7MszVYkWjENJT/ZdApECoPcMsAfgxjIHtSOWP8tolv0NCHjMbW32vFDICHkt6zFAbVWt6/rRUHjAU5nvbGqjfnuiWymOGOjOblgmsbJR4MuMtq1KY+kaBn5yQygOFbuqbl0uEDInnTvlpOJRGdWuHh85BD6f7ddVJaqiQ2LLcheVIvHxOU9EglFq1ZblELA7sv0gCDdBU6Y9XFpAwqMdFz5ENK5BoXIeTPR4uDGrqIZfC3jdtfQNCsJV4k4LEohPdwOUhX1ohk99NtWPwzh+E7LugOv/trWvQuHYL9p4vU2JSCjI6bipLQI5nwk9I+JkMN+Gp1/wOyuZlArVlEoc7qdS4VALIPWttlHtj8E6/AjnSB6O2BdtXPIAXzk7t0VDqGC3j/vNU9UpgXQtw30YJ49CPIMeHURUqR8vGu6C5DryD+2FNku9MBYzVO5VHiH1kL+TkKIzVu/HY9tWQw72QBw7AiZHHTDXWr9mFtZvrYAS4N1oqpCpdp8x/SWijyJgpVZmkUEl3+ahxvanCTILC2nQgYnoYtIPwokljpWxImNGNnGgvVV7W8yBdZ8ZSswwzX5BX15t2aLg8LHCyWyiPmcqIwOY2SsX0+IGQmRVhQ2LPGhITBE71ZPo+q5uE+msYdAFmka8Y1Iehfl3vCPD8qWS/rtz3w6PKaGGTXhbwycjMjSCDsQHIs/uVFxT5IlqrdwGVjQhEuM/KLC3Ymesmh97K94wAPz7uizP0MEgGvS+fkzjXL1Fb7reRELPvrMS5AakiX6iNqhFRyeiXz/pCDbWNRP2b9OC4wF3r/Hk8vBU41iVx4IJvCEzjDU5QWo7EWFxgXbPftrnFxf4LEq9d1tVNntr6xgSePiqga2Qkl2wbBZ4+KhEMaMpElwSX7hGBJ48ITCQyHamECGHvSYFTfboSdGi8S0ManjoqEM96lCXB49ljUkWgkMhDn/byCdj7vgfZfRpwbfWg6l06huDhx/G6VZOZ8te1JE4JIJz0vxEatNa1SGx5I/aei6h50hKFTYGnjkq17LQOdWSZ44zA2ffvkEPdZIoDeeUyagcO4K7Vloo8IughY30LsLpRKFGGfkvb8MAF4GiXgLvxfvVbEoL08QG4B0moGfSnNzkC+7Vn4Pac9csNSg9643J4nSfgHX7GL5dN440Pwj3wI4jBS+whUoKh9tnVx0ikcQtEzFDkUz6UAuUW6BgnkqluYcNVb55sq0BVJkpZyhdfUmlNfIwwCwhFLJ7qE3jlnP9mXt13JoGfngJ6RrXp80EZJokQHhyHfOJy+z6HLkr18kT3pskJZuiVAI5elsr/Lt2vG/f7kpOWgMEKKTMHWIkEZO9ZeIeehJwYVv1Y+qu+k4dkYmr/hWEWMyzM3OSQAEKCSSHO9QOtOUa9SKa7+G0NlfSmqfB0D3dSqpJQ5bQlBC7lebKkoE4QVZihty/0dr6XOtZ50NIdvCiwtc3L6ZzTPLL9VqhjcOQykEg+eQ6MeaqjVcijgN6QWZajUqRIXMqOgGmr9mD2nSxYRhjxCQRHL+PeDUIJMrTcz52U6B8TcO58L5w9P4uLtXfgidOZqJqVjcCJHj/9K8XOlji8E8/7K5KF1nkYdSf/A/eusVRJ2Ie2UDUeMtmjalW5i0I+N7ZB5a116MvWwTl7sOA2di8dg968yp++0CAvFB7PO72v8DozCyvMZJ0SKlw870BwpTaldHxqXE9Q6l1mfEpnsxx/ghHTD71JWAXOf8eCyPaXIZJCTTrNiWEWAFvqOFPsvnOJhEfu1jAzQ9e9g0nD6HzO9PrHGVMc29PQmedRl92vG4+xyQxz/WiOpSJlCiHPvqKGM8xSgnswNzkUSTKdWSwJN5SHnYKe8aiNKvekvGEKQVEnlDHRPey/jZpu+iSUtFQD/WPFX3VSJE4yQynNlXEKPc59Iu0dEcqDI5Gw0TlcvGPVPaKpFK6YDfQM5w5rLregXblQfKH7z6F/2MKLpyXO9/sP0F3DwKQbwLBbjkOdeo6IUhURUwx6DdiQVMK7AJRypPedxMikVNsm32g4G1Xeu6HVD7mmyJ6CE/T8YYFyyMTkNDvN9k2RmZISZlLmv6n/T4mYgVbU/JfI0XGsOBKCjH+BiOELM4XOfyW+5EXMCCMp1BQ5Rty+C3DOZ+UvMsw8QG/ni90p6HppJX3CGGY6yE8uFT1YiPEoCwvTMTTVmiznHKUUMYa5XqRFYZF5+dspKOKbhjPMEoKFmZucQm/as6Fo1PxIDXoTT54wM/2WhpNPzEwRrZSeQR3qbAEoH0obIovHmZY9NS9NCBhacaGH5kWxPHQC5C+fQ+a8+dECOQts+uNkz5eiE6Twq+jkTY90kCnLqlZomg1oBNUDc6EH7vz1oIdtSqGaFk2nmFAI+jsNYqbpMAseMTOlXPY0ETMEGTKmIBNoSwvBEC5M3Z+QJQ3lG5NDAWEmdU4Uq8zknHkVDvklWaqmPMPMCynPpWLMdF9iGGKmYolGtiLOTGG6/hrB5yFzQ07U7A4SwywB+Ii+yQmavslvIUiwoGti9oMgpe6Q2S1SFZOKeIBShQP6fe+oP/1iN2nyWiGBpHsYaKgqfji21XgYnswVKVbU+0a62aysd1VlJzNgYHVjcVFjTYOLQEBDJKRhVVPuwl0YCcJp3Vz0t3bLZlweyV3xVU1+GH3XkFTLlU3PiMTyuty2cTsA0dhRdB56XQvO9FGwi0RdeeH1oG1aRb5nowMqEoZMfgtihgD14E1RMxHA9CMm8qHfy7xKVczCQVFns/KYKRYxk/yhm1XGiUQTS4SUgaqZFC7pO/LEFN9jJk+cnCZixpscS+d/u91nrnZVGWbWhAPFHwrJkD6QFBwZZjroOKmepu9TVvg2ySSpLiver2uolDD4PGTmgkAISFYXnUKoDDCShowMs0RgYeYmJ2j6Xin5HV0SZG7pEDjdk3ngo5vw7WsEupOVi8g3hX6bf3OmTs2e1QJne/3xxqISt66eegcn416ax6Fknnf/iMQt7VNv5lQhgZz+D3VqOcLPuhaBo52Z8SpDEmtaNFWWmqgISqyqnzq9+nIPrbVkTueLK1Rpqrk6M5yqM4xFWoHatim/lc1rcEXW5HjSdDQAQR0YjflpUS3VIqfU5uVBYHm9X44zxfPnA9DX7gZC5BGTi7bxblyJ+73Cg5cEblnpmxxnQ1tzz2rAHDitvrsXjsBYv2fqw7Smw9x0B5wLR/zxRnqhb3/Qj6DJRjehb70fZmTq8jALnMqUHTEjMoINQf4xnjCKRMwkhRk762BNxJQpNp3vNFgXnhJmZCJewGMm76CjY0YISKeAMNN/QQ0XVQ0qpYlh5gtTuKoaYP4xbybvO2Vh9gZhZiYcDmDPKlmw73PHaqruxcLCdJjCK9yvM4GdHRrKQnweMnOAGYS+7YECfVZDtZtlybrtDLNE4JqnjBIRXr+VjHf9CBSKcGmrpcQhMsWl0pFSjbOs1i/XS74mFAFC45UHpfotlZmmsto1ZQItNXRgSeUJQ+PFLIHWaomHtwpcGvQd/Mk4uLHSF3GoxCKNGwjqaCxzUF8pcXFAImpraK3yVFQNGfGtqJMqJ7ylhkpPU+VeDx31EparYXmNp97gREKZQzocNrGpzUZHo6cqLlH1mvZaiYqwRCScETDIpHhnh58XTfMltGAE2uZ7IaKj8Kgyk+ZXW5KhSgTiQRUVQ5HOHQ0C4YDE2KSHFXV+mciIQRWphPLWIe8ZFWVkAHev99vId4c6L1GtApFb3wRvuB+4cgkyVAa9ZQ1cM4T4mKG2XVnAg6kL3L9ZoJ/2z7j/Jo/mFdIs6JMOvOZVEGWVQKQagTsfg3flMrzhPojKOuiNHZCaBr11DbzRKmh2HF5tG4w73ga37yLExCBkVRP0hmWQFE3DlHRVJvp/dsRMKs0wJcJkk2pzbCc3YkarSUfLUOSMJYJT0o8oYkaU54p8qnS2ESgcMTM2qEpYUul1byBLLWWYOSYUMlEDG6/faqBzyK8ISPeD5hqqNEbH+jRpqAyTRSTo4aHNAn2jEgMTOipDLpbXajB1iWCQo0enIxzSUS8dPLxVx8VBiSj16yoEGqsoco3zmJi5wTRNJMpqYNzxdrj9lyDGByArG6A3roDL0TLMEoSFGUY9cFEp6tX0yUnrEVivIj9y2zZODSTBpsgUE5WcikmpaWwtm3rD3rI8u80EzXJbWgTPhAvsXJn/Wx07V00f/EXiTDgM1BXJ8skWZyiipakqex4RIBIB6ltyxm2NAK21uetWFtLQkpeuVB6mSJmpofYr6rPnUQ5QlErbqpyTsiMMdDTlrhf9dnVz9tSCQPtm/5OFtmITQJ9sOrbkrXEYRvm2AluCKemIGVWVKfPdIXMmSmUqIMzoyR+6ViZiRiaisLRWhJNvg0mgSWihqb4whTxm1ETNggbRMjqmwo1FKALYcWUeLEjEYZh5EmeoS755yn2Hg4CZq3voM02gPAKszjl+ONpjNkTC/j1iW4F+HcPMFUokDQZglOf2Y/kBllmKcC+GYRhmkUTMqKpMWalMruWLJFoBo0otJcxkpTKR+a8tgmljbPpra+QxE88pqa1SmVKeMllQWyHzXxJmBOWBB31FVU6OXcsqMwzDMAzDMMxNCQszzLR4noTlSPV3OmzHQzThwcl6ne9exW9jlqdSk1JYBdoKQRVnaB7ktTEdkkpBUxTADYSWPW55sOzp18F1XcQTDiwV/TAX853ddp/teMzCkDqVsosS5FdlcpKii1agMoGWLA/m5qcyicAUYSYnYiYp9qi0pXwoiiYvYkbS+CTkhMrUJx1BwzDzjG07SMQT6i/DXCu27ar+S2KGezVTGMuy1XloZRugMcwcYzsu4nFH/WWYpQpHgjEFIVGFPFfO9knli1IZAtY0p6otZZ4USXiIWgJneoGJBFAdpgpFEroucbwLmIj75rqrGn1vlOyUCxJeJuICp3uhzHQbKoD2BgnbkTjRDeUn01RJqT8SZUGZ8/AZt6Qy2z3VI5UZ6rI6gdYaGi83coBSN7zRK3AvHQM8V/nE6PVt6QfI+WI8JtE1LNAz7JsLrm7yvXsiWcvnuh5iCYlLgx56x3SEDIm1TQ7KQxLhVOmredhnJGbRfjnTKzEWJ18gWj5//+hc4/KGQfuLfIPIM6nwcD+NSXm7JNHzUpm8ZJpSKm0pGz25zx0nS5hJROEYJkzNSgszE+Qxk8gIM9KOFxdmjMCUVKaUCEMRMyrKhsaJjs5uIzDMNZCIWdCtCXiXjgLRUbgVDRDL18MNliNYrFQgw+RhJRzEXB3n+gSGo+TpRvdMqXzjIkF+bzkTiVgCWnwM8uIRIDEJWd0Cp20tEIqkiyswzPViWw6iNj1nUL9fQ3XYw+pmFxFTqgqsDLOU4COamQJFnwyOA3tPUCSK30bfzw9I3LHON/IlgYWiY/rHBF46k4m4oPHODUhldEtGuPSdPnRBvW+TUEa+KUHnfD9w9HLub8/0SVX5aXBCImFn2ui3qbLeCVvicKdUhr4proxLnOwG7t8ElIVE+iHUPvIcvCsZM1JvuBduWRUCu98AUaAi0lyJMj8+LhGzcktmt9eTn05GnJmMSzx9TMB2U/nsQok5G1vopmMjTA7Bc7zPKDqmdwR44XTudicx594NvnEfc2Og4//ABYk37cwV7FJQAJWR92xAWkv2y6KUsW8qbSl3XJnlQ+NjJWiiNF0vEzEjAupcyYzkCzOFPGJUKlN8MqctHR1D/jJJgcbjiBlmnkgkbIjhy3AOP5NpHOmDc/kY9F2PAnU5RlwMU5TRhI69x2XaRH0QUAUKdq0UaK1yEeLKQtOKo+g7A/fki7nnYedRGLe+CajKM91jmGuAIsqvTAA/PUXlSPx+0uCEhnMDwF3rJBqrXOjJ6GCGWQrwKwFmCnEL2Hc284CfzctnJWJJy4qYLbD//NSR6HevnJNY2Zh52KSOD00zZvnjJxyBo5enTp8eOo93SxVhk8JygEMXpRJzCIoKyRZlUlA/4US3VJEIap7jQzmiTHr5JkfhdJ/xvTTmGErBouXPFmVSXLwCRJPtFI556JL/8J3P8R4NlqPN0z4DXj5XeJ9l7x9m/ukf9bc1VdoqBEWO5fc3qIpZ9jGTSlMqmMqUPP3cpJIjPReW549nJEUbJcwgAGQJMzLlN2MGZmX+q4QZIwCRKtUejEBGi6xU6jd54g7DzBbdicM79pOpA6QH7+iPYU/yscXM7gUK9VMKZfKSYG5J7h5Ph+7GIE++NHWAa8M99hysWJ6hPMNcAxQdv++chvzTlL5TOw1nmKUE33mYKVAKUSFhgaBnPBIBCBqnWKqnGpane1D6DIksxJVpntsogoPKbmfTNwpYrt928UrxCzGJHxRpQw+h7qXjRcfzLp/KMTydKyxH4DK9divCpeSyOx6VJy+eNtQ/4s3LPovPsM9o2zHzD0U4pQSZK2OFj+dCETMkzNCDREp8dJNpSqm0pWwoA0pIT6XMKay4io4hsstlu9DhJuJ5qUxCiTBToFSlPK8mGRv3jX9T8w2GIeMTRdfdHexG4sffgEtl6BnmKlGinlvYU0bGJgBnatUwhsmH7oPUJykEXV4nWFeYFneMOjqF711y7AoEn4fMHJCwRfq5IR9qp+EMs5RgYYa5alK34hl1alm8bSa/2YKDU7+dRrNIR4yo/xSfyXxEy0xZhgJk1nsGY945fgmQs1mYBWcs5ncqwoHiIiUFw0wRZpLfUx2VVJqSloyAyUcTGWFGlcoWweR0MqlMal6eljHHJsHSDKS9bQaiJmLJCC4VFeO5kFkPxl5sHAhSkfskgbCKwJEFTlQ675zjz/vLfv61GU27Gebqr918TDEzM9NRwjbAMzBDYQaGuRHnqeTrPbPEYGGGmQJ5aRXz0yIri3DyRTo9VBbzig2Sj0VeGgaNH0j+lox+i1FdRmHGuW31FYCp+xfgFfXFFfJltf6yC92A3rau6Hh6y2rA9B9S5xJaxtaa4sNX1PnLrmsSdRXFbyhN1dqC7DP2UbsxkDkz0VbjizRkyJyP5VIkTG5b6pxKFaHxnOmFGR0eXEfmlMpW08mqyqTmlWUATKlMqVLZFPX2064anBhMmmWnSmhnpTOpiBkSY5KIQMhXALN9a1LjToyoVEKtZbX//5H+GbcVw2SjhcsBUeT6SMehMffXdWbpQab8dD8sBGnSZJ7PFEevaig6TJTXQOp8HjLXD9XByH+WyD6Hqd/KMEsJFmaYKVBnZfeqwk/vO9qFulASQUNi24rC4+3soJSe3IfFW1cJhAP++EFTYnWWj0wKEg02tQmc65M5wsL2doFwskpCRRhori58kd60TKQrEImqBvWZQjACffkGCG3uDcOCpqaWgZYln6YqMib2/09Vl3au8Nctn5V1HoKGNy/7jP7u6Cg83i61f65qtsw1Ek34x2vqeEh5DxWLmKEoAUrPS3VQSLQhnGQ0TDGxjTKzU2lPVBKbhBlqS42fjpihFKekkKI8ZpLGvwPRADwp0DsZVFqLEl1UOklyXHprSr/LS2Xyx5mazuSN+uZQWvMq9XCd+s4ws8XVwxDrbis4TN90d/r4Y5jpqAgL3LKy8IVzc1sm3ZMpjGsEITq2Tx0gNGgb70Igwuchc/1QDYxb2gv3h3e2ewglnykYZqnAWiMzBUphaKqSeGirwPHLEiNRoCIEbGwTqIxk/CxIhGir9VAZETjZ7ZdgpuEbWwVMQ+Jcv1+Cmcox02+pbHOKcEDDhjaJxmq/5DV5m9SWAxtahTKgDVFkh+ZHyqxrESgLUSfJn2/IFNi9CugfA073SOXFQVEqq5uEml8KLVQGc8eD8AY64XYe98tlN6+G3rYGWniakJ3rpCIk8cAWgbO9Er2j/gM4LRtVPMou500C00NbJE53S/RPaCpaZX2zp8qLX2257Ox9duyyxGiRfUZ/l9dJVIUFjndJjMeBatpny4QaP7s0MzN/0DFOHY6QkRFqKvP6sXRcV5CnzHCvSvsR4XIYa+7IiZhxlZFTqlbBVCiSJmUxQ94clh6BoUv1Rjg7pYkEm1RlJuUxkxRmSJChWggxR8e4paPCTAozCQr5afD9PqTMfRhORs8ov4+86DGKkBHhChWRIyKV8MauXPtGZG5KgiETiaZV0Ctq4Z0/CMTGgPJ66Ku2wwlWIFTs9SrD5FET8fDgFg0nujyMRKn/ILGuVUNlWKZfBDGFCYZDsFZsgahphrxwyC+XXdUMY+VWuIH5qXjJ3HwYho7mShsPbJI43k0RxkKdnxtbgfKA5LLszJKDj2imIBR1QoLKrWuoXJ0f2WEaUx//IkENkaAvRrgeRYqQqELjCdyxTqo0ZOonp6JYcn8r1G/rymk8X8wJGFQWW6Aq7MGVQkXl+PPN/T1F3lD56eYqP2vCNGgZp86DxBlt+QboTR2qagfMEESBCjZzCVXIoYfsLSsk1tkCQsiC5ZDphlNpANvaXdiOq6IYQlcpyBTaZ3tm2Ge0jesrgdsjZCLrp8uYBfYPM39QZTHa1anUvoIRM0nzX7f3nPpOqT+6RVEo5WmPGdfzoMFLCy0FhRmpqWgbqp5km20wRObtUzpiRgtnSmZTKlOylHzfZABNZQn0R4PqU1HtqDeiqapKlMZEZAszlEZIKU+FKi+pCJkyP9yNhBkyiWSYa3koRLgZibL7kxc7A0YowB0a5qoIB3WEg36EL2nc1Ifw79V8P5wNAXUeLoNVUa+iJzXDgBHk85CZezE+GAJuDTqqz0PnaVDlMLEIzyw9+PrJTAs9sBdKyykk0PiIHAFgNlD0TP5vM2+rpp9G0JzdPFIpGDcSU9eS2276ZTRNXX1u9D4j0ebaZSDmeqAKWBShpAlffIwlMhFhBJniUlSMDkcJMlrzShX5JQe7IMT6dMlsz5XQ9OJpbyT2eUIHEjHl7WJra1TETArS40i8scyyTMQMCTPltUq0izo62irimLAMFTGjIqoC4SxhJpmulOUxQ5DnTHpYap1cf130ujZ/nLIqeAOXIB077WnDMFdDMMQ+Fsz1w9ExcyDQMMw844sxDLO04bsRwzDMDYZSlyiViaC/+REzJIqQfKLHx9JmivTBWD9MLasqk0d+McW9EDRdgyt0eGS0Gx2DpYVg5o1PUTOOHoaMjiuRhDxjKAJm0iZ1TyBk+J5HE5av9olAMCPMREeBAEWh5SmBwTA8SjHJQk4M+zUWIpX+dJJ/5fjQNWxBhmEYhmEYhlk6sPzI3BA8T6oogYFxYCIuUV9B6Ur0popDhpmbC9uRKmw+LcwYfmpTzjjJiBg9PgoRKkt6slSoVCAj7PsqScdRqYLTZaFpmoArTOVTA8dCHGGU5UXYUGqTbZQp4UQJLUS4IinMAGHDVZ+hWNIZOjtiZnxYecbkI4Jl8Eb6ctq8cRJmkBmfqutAwJsYhlbTNPsNyNz0UEQZiZuDE+Q5IFFbJlQ1v0IpowzDMMwiv95bwPAEMBKVqI4I5UlJxSrYF5FZarAww9wQUYY60HuPSyQLxKg352TUe+9GoDzEF1bm5iEVHZOKyiWBJlU+O0UqIkaLjSrTXyL1V5cOLIc8XCbgwJw2Yiage4jp5fD69/nz9gKoNXJVoIAukfDKVESNNzbozytUhslxQ007oEmEdA9RR1PnL6UFesO+6OJNDEGrniqq0O8Rn1TpS8pzJhUZQyJTsga4irIJlXHEDHPVnXQ6X358XCJZLV7dT8iz6b5NfrUdhmEYZmkwFgOePSbT/SK63lOxjPs2kSflwi4bw8w1nMrEzDsxG3juZLYo40NRAgcukJcGl6Vkbh7oTT+RLjtv+p4z9MA5JWImMa7EC4UZ9k1OpaX8Z8h4N6ZFlEdNMYIkqIiI7y+DABypK5ElX7yJwveI8XrP+wbZhqlSl0K6q4yFKWKGoltUFA35NSWikHZCiS+FImZSy5wyB1bTnhiaMi6JTRQxwzCzhc4Vup9kRBmfuA28dIYq/PH9hGEYZqlUsPzpyWxRxoe+P39KIm7x9Z5ZWrAww8w74zFM6USn6B0BEnkXXIZZykwkfFNeeuOTEmhItKQHyxSpctg67HSFJBJISMjQnZjqlJC5bkwrT0+nECTCKEEGBuK1q1RbUHeniDcxz09T8shcOOyLKhO2jrDhizjkM0OQMCOCEVXhzCURR3nFFEhlSgkzk35qFIlOFBkzRZiJVKj2bFGKYWYS+hNZ50o2FEnD9xOGYZilAV3r81O9U0zEc/tNDLMUYGGGmXfyle58yOiUYZYKM4kMk3EqKZ/JjaY86ZSAmR8xo8pZZ1U8IsNc3Y7CcqSKRolr5VMiYLIh014i3rAesYb1OSJLehzdQ9zV4KUEoJAvnqiIGRUp44+jQWKSKjNV1AKaAefcQV8tSkX0ZGME1DiUHpWOnLETqhJTNkqocSwVgcMws6GYyJ+C7ycMwzBLg5mu5y6/02GWGCzMMPPOdDmglMYxh5WiGWZBGY1K/Ns+ie++4ikBphDjcSCcVR069X96+5MbMSOhh8JK+8gWZkyZUOG9djQGWwTS4kshUqJNon4tYq6hxBWTxJ4sSHShNCWnfTf0jq3QWlYpc2IqlR0x/adglc5kuhizDOUNo1XVqzQmrX7Z1IpManyhomaoGpRak5F+v728One8iC/UeGNXiq4Dw2QTSQqZhTC0TCQawzAMs7ihZ4Ri/r7UzhW0maUGCzPMvEOpGq25z2Nptq0Q6YgBhlnsXBiQ0DX/Lc/FIloDCTAUMZNdOYnOEapWlh4nIRH0YtDy/VuCZYjISViuhuGoliWsFIb8YwSkElmitq5EnPxOTjqqxqyC1rBcmfuOW9TbEShLCjNExHAxlvB7QaK+DTCD0NrWpYdToFB2sBCV9/aGe9T/VYWmUDkERdLkLGBIedp4SeGGYWbTUV/ZWHjYpmUZ7yaGYRhmcUPX83XNhYetb+HrPbP0YK2RmXeCpsAtq4CqPokzvX6aBlVkIlGmsYrL3TFLJ4Xp0hWgsRIq4uTSFYmNbbnHN41D+dLNuRk9SpykSJoUYxM2wt5EsqR0BppURbIkcK9TTSY00woz6o0SmfvauvKHKTRuqi3mZHT6lABDYkwKip7pnggp8YUqMYntjel1s1yBJy7UwfY03NE6gqYyC6KyFui/AC82rqo45UfL+MsnIMqrWJhhZk3AENiyjKr5SZzs9lNl6fzZslyghU4JMnBiGIZhFj2GLrCuFYgEgeNdUnnKkBizsU1geZ0/nGGWEizMMDeEcEBgUxuwqtE3OqWoAmpjmKXClXHfiI7ERhIfj3T6ZR6zU/moIhMJG/lRYvQ9O5VpPCpR6U2mjX+zCdXXQx+w0Wu2+2UjpxFmUhExg3ETwzETKyqzjGyS6EKqD4k3KShliSoy0XmagqJnSHghPxoyBc4WnM6ORNQwEnKOXSlHY2QIoqJODXPPvwY5MQy9qaPg8omyGng9ZyA9D0LLzFA6Frz+ThWZozcsm3Yd1fieWzCtill6hAJCvS1dUcf3E4ZhmKVMyBRY3STRViOUpwxd70mc4Ze6zFKEhRnmhkEpG6R6M8xSpHtYKn+LipAvvlDnoWsoV5hJRcWQECMhfeNbI6C+U4Uyz1OtmHRNNBsOhD5VaNBCYUQMB+NuhRJlZgoQaAhbODNSBk1INJcnikTVuH4p7CSjCSPtL5Mi9Z2iacKGlW6ntK2zwxE0RRKoDdk4OliBwZiJ+gggKuvgdp5QBsGixo9HHoiaOHKlHJvqJv3IGjITvuzAG+6FXteqxqFS3Na+xyEnhvx5LNsAc9OdBTti3ugArANPAYlJ6O1bYKy7NUfgYZYmdCzw/YRhGObmuN6H+XrP3ARw75VhGGYO6B4Gasv9DgSJkPR/Emuy6R+Tyuw6EB+CffBp2AeegnNyH6pMS735HxgHxieo/qNAJFxcN69KFmpqKcsKsylCc1kCKypiaK+MTTH+TVEZdNA3GVCCEgktw3ET5XnCDBkJU2TNUDw3qfvyeAiWp6GtIo6akI2w4eL8qL+A+ppboDW2Q1+xWW2XkbiB5y7XYMIy8NOuaiXgqEpNwQi87jPqN1J6sA4+DRmfgLH5bmjtm+FdPgH38skpy+1NjsJ65T8hDBNa6xq4F4/CObN/xm3CMAzDMAzDMKUECzMMwzBzUI2JUpHqsjKP6P/Dk7mmvj3DQE0wDvfUPohAEFrzKlVKOnD+BYQMia4hiZHuPjVupLJ4OTNKSdrTPIwVlTMLMxRk0l4Vw7KK4uPWhWxEHQNjlo7uiaBKS2qIJKZMpzZsoXPM95kh6O+5kQhqgiTI+MbCTWUJdE2ElO+M0E3o7ZtVFSca99BAhRJu9rSMKOHnUD+ZGwtodW1w+87DmxyDc/xFyKFu6Kt3+uXBG9uVKbFz4kV4E8Pp5ZGOrcQtijjS198KvW0dtGXrVeqU239xxu3CMAzDMAzDMKUCCzMMwzDXCZnSUbWYmrADOT6oPnURR6U2HbvsqxhUPps8Z6qHT6ooEa1tA7TqBugrNkFIF9WJy+jsd3B8sAxlmESAJlgESpMKGoWjX66F6pCtomFODpXj9HAZKgM2IuZU7xpKV5qwDRXpQlwcC2E4YapomexxKB/r1FBZzm9p3MFYAKuqoyr9iv6OJEycHQmrqBrykrGe+xe4ncf9st2VvkcNoS3fBBGMwHr1R/CiY8p/xj70DGR0FAYJOLq/PFrzSojqJtiH98Ib99OgGIZhGIZhGKbUYY+ZZKUUYmxsbKEXhWGWPBUVFbMybZvv85ImT+lDNBcy9i+0SK4rMTwpMDihIWppyki3pow+ftle6Un0DnvoHKxEBy7AOXBSladW0xcCrWXrcOHKSsjJKxiOB2F6BiqNKOza5YCVFZHSuArNgz0Yc6oxqVVgU8UA4vHpTX3nmmWRUVwar4KheVhdMYx4POMjkyIkgYgeUmlIlWYCI1YIDcFJhDGOeFZATktEx+nhCgRkFLXBGIYTIRwbrUiOO6HGpXTxxpCGIwMVcO0EGlp3wpi8AjtQiVFRh8HLYYzaASXi1ATiaGjcjZrul+E99y0IocGDhrGWWzAwVouhgRBsT0dFwEJj9TY0xvdBvvQfcJdthIxUQ9hxYHwI7uQYPNuBpmvQI+UARfKU10IGwupAEFYUIjoKMTkCGY9BCvL0icArr4GM1AAhMs7Jep+haoR7/kFEC5o9LJ9UPXE60ErQtHA25yXfKxnmxsLnJcMszj4sw1wLQqau6Dcxly9fxvLlyxd6MRjmpmB0dBSVlZVzdl6+7X0fw3t+7VNYaAJeDCQXZCMhkNByU5JMZ0INKYjQ4GhBGO7U6kk3AlcLQEgPmnSKjuMJA64ezqj7ThQCuX40EhocIzdihtDdWM60pdDh6MVTtphro9IdxL0T38PjLx7Cz/7xF+bsvOR7JcPcWPi8ZJjF2Ydl5p8LFy5g5cqVOHDgAHbs2DGn0ybx7dvf/jYee+yxOR13JjhiBkBrays6OzvnXAWltxd0s6RpL+aTeCmsx1JYh6WyHnSeXct5Of26k9hRisgiy1ZsfWh8Cj1ZqLcxdnr5iuMWWKdC61Nsn2RP2yvJfbf4z7MgbLwTr7/jnRj9yKdmtT6zOS/n61558+6nGwNvp8W7jRbDeVmq266U4W22eLfZbPuws+UXf/EXMTIygu985zs57c8++yzuv/9+DA8Po7q6GvPJH//xH6v5Hzx4cFbjkxi8atUqrFu3DkeOHMkZ9pWvfAW//du/rdYpm46ODtVOn4Xkj//4j/Enf/In6v+apqnr56OPPoo///M/R21tbXq8np4e1NTU3PDlY2EmuWOWLVs2b9OnC8hSuPAuhfVYCuuwlNbjWs7LpbbuvD6ly1Jal7lYn/m+V14rS20/zRe8nZbmNiqV83IxbruFhrfZ1cPbbO6gpBnXzY14ng0kvvyX//JfsHfvXrz00ku47bbbsJjYvHkznnzySbXux48fxy/90i+pSKhvfvOb6XGam5sXZNnY/JdhGIZhGIZhGIZhSpTnnnsO99xzD8LhsIoe+s3f/E1MTk6mh//f//t/sXv3bhXVQ8LCe9/7XvT39+dE4VBU3X/+539i165dCAaD+Md//EcVQXLo0CE1jD4kvEwn5vyf//N/8PM///Nq+v/wD/+QM/33v//9SuRITYsiVO677z5cvHgRH/nIR9LtxODgIN7znvegra0NkUgEW7duxf/7f/8vZ36e5+Ev/uIvsGbNGrW8K1aswJ/92Z8VXDYSWkhk2bBhAy5dulR0HQzDUNuH5vvQQw/hne98J5544omccWgZU1FMlmXhQx/6EFpaWhAKhdDe3o7PfOYzRaf/iU98Qo372muv4WphYYZhGIZhGIZhGIZhSpCzZ8/iDW94A97xjneoB36K7iChhgSDFLZt40//9E+VyEKiAnmwUKpUPr/3e7+nUncoWuT1r389/tt/+28qioTSd+jzrne9q+hyPPPMM4hGo0rQ+K//9b/iG9/4RlocuvPOO/H5z39eRTSlpvX//X//H/7t3/5NRfV98pOfTLcT8XhcCUTf//73VUrUBz7wASX47Nu3Lz2/j33sY2pZ/+iP/gjHjh3DP/3TP6GpqWnKciUSCSWwUDrWT37yEyXgzAbaRj/84Q8RCASKjvPXf/3X+N73vod//ud/xsmTJ/H1r39dpWYVEq0+/OEP42tf+5pahm3btuFq4VSmeYSUPVLN6O9iZimsx1JYh6W0HtfCUlt3Xp/SZSmty1Jcn6W+XnMNb6eZ4W107fC2u3p4m109S3mb/cd//AfKy8tz2vJTjChC4+d+7ufSHi1r165VgsHrXvc6/O3f/q2K5KBokRTkAUPDb731VkxMTORMnwQSEmRS0LBUFMlMUITMu9/9bui6ji1btqj5/Mu//IsSgEjcqKqqUtEm+dOi8VORPCkoYoWEmxQf/vCHlUhCAsiePXswPj6Ov/qrv8Lf/M3f4H3ve58aZ/Xq1bj77rtzpk3r96Y3vUmJMyQc0TJMx+HDh9U60zYmcYj43Oc+V3R8ir6h7U3zpXWjiJl8HMdRQhUZEZNgRut2LXBVJoZhGIZhGIZhGIa5gZCg0dXVpcSVbMi7hR70U+a/JLBQpIxpmulx6BGeolcokmTjxo3Yv3+/Sh2iiBn6HaUB0fCjR49i06ZNaUNhMu/NFg5ma/5Lhr6UokPCA0W6EP/jf/wPfPe731URIldr/kvCyKc//WklxNA2sCxLiStve9vbVBtFzpB/zblz51T1pWJVmSgahz5PP/20SvOaDlpXmjZFwJAoQ6lctN4kjpE4VajS0quvvqqErLq6OhW19OY3vxkPP/xwzrg0fxINX3zxRdTX1+Na4VQmhmEYhmEYhmEYhrnBlJWVKQ+V7E9+xAVFhfzqr/6qEhFSHxJgTp8+raJIKJ3okUceUWlElGrz8ssvK2GBIMEjf37XAqURkZhBYgmJGPT53d/9XSXUnDp16qqn99nPflZFxNA0KNLl4MGDah1SyzuTyJLijW98oxKtXnjhhVmNT5E9tI0p4ofSpCiaJ1WpqRC33HILzp8/r9LEYrGYMj7+2Z/92ZxxSLghcYkifq4HTmViGIZhGIZhGIZhmBKExAGKjCFBoVh6DpnpktBAxsDEK6+8MmuhYjbVmSiNifxo8n1rfv3Xfx1f/vKX1byLTatQ+09/+lP8zM/8jIoMIjzPUwIPRfcQlD5E4sxTTz2FX/7lXy66XB/84AeVyPLWt75V+dVQetfV8Id/+Id44IEH1HSofHYhSPAi7x36kChDkTNDQ0PpEts077e85S3KEJmEHkr3uhY4YoZhGIZhGIZhGIZhShCKKnn++eeV2S9FllCkDKUQpcx/yeyWxI8vfOELKvWHUnUowmM2UJoRRYTQdK9cuaLSifKhYZTSQwIJiSDZH6qs9NWvflX5rNC0KLqHxBSaFqVSpeZB5bUpqoTaU8ILVUOi9SIj4l/91V9FX19fep7km0Pr/Tu/8zvKUJcMkClVKLsSVLY/zac+9SmVZkQRPFfDHXfcoYx6Ka2qEOQ/Q9WiTpw4oYQj8tQhrxxKMcuGUrCoMhZVpvrWt76Fa4GFGYZhGIZhGIZhGIYpQUg4+PGPf6yEASqZvXPnTnz84x9PR3g0NDQofxcSDSjihKJXyP9lNlClJ4oAIf8Zmk5+yWqCxBCaLpWizocECSrL/fjjj6vKTL/2a7+mIktoWlTqOmU4TJ4wlHZF7alIFYoEovQlKqnd3NysPF2yoWpMFKVD60o+OjTd7BLg2ZB/DaUkUWoTiT1XA5Xy/vu//3t0dnZOGUamxbQeVIqcvH5oPWhdNW2qjELRNCRSUXUpqkZ1tbD5b9I8iZyfacOnaqszDLOw8HnJMKUFn5MMU3rweckwDLM04IgZQN3QqLQW/WUYpjTg85JhSgs+Jxmm9ODzkmEYZmnAwgzDMAzDMAzDMAzDMMwCwcIMwzAMwzAMwzAMwzDMAsHCDMMwDMMwDMMwDMMwzALBwgzDMAzDMAzDMAzDMMwCwcIMwzAMwzAMwzAMwzDMAmGghNi7dy8++9nPYv/+/ejp6cG3v/3tKfXM83n22Wfx0Y9+FEePHsXy5ctVTfRf/MVfxEISTUjELODykF+JfFmtQDgARIKlW8ZwIuZhcALqUxECWqoFFVPHwJjA8KREVVigqUoi4k3AG+6BHBuEqKyDVtOCuBZB36jEaEygtkyitkJDBDF4/Rcho2MQVQ3QqhoRNSrQNQhMJiQaKgSqy/wD8NKwxGQCaKwEaiMebKmje0giZgNNVUBVGJCeRNeQh4QDNFcLVAdt6G4CLs3DSkBvWA5EKiEcC07fRQjXgtbQDidSi4SroWtQwpUSbTUCkYBEIDECr/8C4HnQmjogg+WAFYPbd0FtD72pA16gDGNOCJeHpVIwaT8GTQ/xhETXsIQugGV1GgK6i3HLQPcwYOj+eBUYB2Jj8AY6ATPoT08PYDARQs+IRNgA2up0RDABOTEMb7AbCEagN66A1Ay448PwhnogQuWqLaFFMDLpYWAcKA/SNtAQQgwY6YUcHYCIVEKra4Oll6NnXE/vs8YqICInIYe60vsM9W3QHEdNX06O+Puxugkww/B6zkBGR9P7TCurxFJkPCYxFoM6bsMm0ForYOoeIkE9Z7xYzELC1dE16MGVUMdPKAA4dIwO++d5U5VAfcSB7sbhDvVCTgxBVNZDr26EJ4LAWA+84V6ISBXcxtXwYGAiAfQOS5h0HNQKGJqE5QpMxCWGJ/1jqNywoDux9DGuNSxX04ghjN5RqHHrKwSaK4GECwyOA0OTEpXJ/R4QLoaimjpm2uuFOnfqzQkgPukf+5oOrWklpBmC5sTh9l4AXAdaYzu8cBV0j86vS0AiClHbAlFeCwkd3lA35MQgUNkAo7YVwrMgx4f8dQyXQ6tfDscwIS4cAXQTWsMyCCMAqWmAlYDXd57qu6rzTgTDap7u2BD0sgq4w31qflptKxAIqWsIzVerqodtVCLuACNRf9+tr43CEJ46hr3BLjW+TstuBqDFY/CsKIQZgjdwCbKhA5quw+27CLg2tMYVEKEKyJ6T6tgX4Qp4Y0OQVc1qvdW5MT6UvMY1wxUB6HAgQmUQtB4AnOgEZGxCTR96AHpTO6QZgBkuyzmG7GjUPzZo3nYcWv0yIFIF/TrOrbgtEU0AXUMSmvCPoUgACJile49hGGZpYcXj0BwL7pXLQGwcoqYZWmUtjEjFQi8as4SwbRu6FYVH/avx1LNHM9xABKZpLvTiMczSFWYmJyexfft2/NIv/RLe/va3zzj++fPn8aY3vQm/9mu/hq9//et46qmn8Mu//MtoaWnBI488goWARIcjnRKXrmTaTvVItNcDm5cDZSUozoxGJX58HEjYmbbDnRJ71gic6ZMYmaTllmg2hmEdehxwrMyI9MC144043lOjxBUiYAD3bQgh2HMWGB1INoYR3v0oLgxUqYeqs31SiVX3bhAYngA6h4CNzR76JzTsO+sLWsTZPl8o2t6h4Wi3gCeBZVUJoP88nJMvpMdzLx0GqhphbHsAOLcfNAWnfSfO9AEnemmb+9v9ZC/QUuVh17IIxPnX/B83roR7Zj/Qczo9PefCIaBlHSbqd+F0T8j/bY/EykZ6ANJwstdfxmM9wIZmgRW1Dk73+qfTxtpxOIefgRzNHATu2QMw1u9BVd1K7O2LoDwArK2dgH3gR5CTo5nxTu+HselOgAQdeqA0A4hVLcOPLwjErIxooHUCd6/SUdV5UokzfqMO85aH0TfSgM4hGlfC0IB7VwuU0UMyiTDLNsIoq4K1/4fqgTiNGURg96NwSOD6SXK7BsKqTauowVKCBI2fnvIwHsuci0cuS+xZraGx0kU4Kc7EYxbO9Ink8aOnjx8SC+l8PtLp/3ZDow09Pgrnlf9UD/2EOv7MIIzdb4RDotdrT8HZ+RZIYeClMx6GJjLzPtYlsW25QGuNVMIo7bMy3QL6z8E58Xx6PI+O8cp6RLY/hEMXw6ptY7NE1BbYe1wq4cVHQteAezboqAs5iAQNHLgg8bqVk3COvwDvSmfmeDv/GvQVm+G1b4Z7/pDf2LEdYqQH1uFnlYCiuHRMiX90fDlGOXBpL7DtQQg3AXv/DyHjE5kNfOoVmDsegNu+Dd7ef4J77gAC97wT7rlD8LpOZeZ98Qi05pXQO7ZBeA6sl76f3HI07ChEWRWM9bfBPvhU8vh8A2xRjYtXgD0tk0rMsg88qYTN9DTPvApj891w61ohO4/D6z4NbftDkFe64JzbnzXvw0BtK4zN98L+yTcgKmph7noDZGwM1v4fAE7WxdAIwKR5hyphjl0BqhrgxaNwDu8FRnrSo9H0xdpbYTevhhkpS4sy4spFWMcz+9GlbVlRB7HjQWjX8AATt6Tan5eHkHMMrWkGNrUBQRZnGIaZZxKJBLSxK3AOPkFvzlSbvHQEMlQOsfvR6xKeGSYbbXIkeV+2ptyX6X7MMEuJkkplevTRR/GpT30Kb3vb22Y1/pe+9CWsXLkS//N//k9s3LgRH/rQh/CzP/uz+Mu//EssFPS2O1uUSUEPEzSs1JiMuXj5rMwRZQjXA145K7G+xe/kb2+OwTj2VO6FkXAsGEefwrbmWLrJcoAXz2qQ6+/JjGfF4Bz9CfYsj6abKNrgwAUPW5f73ylS5uWzU5dxPA5cGpBYXgfoOlBlxCGzRJk0o/1wL5+Edv/PAxtux6Sl4URvbgQE0TOqoXciAK15lRJzpB3LEWUyI55CvRxUAlKK8/1AWcgXn1LQPBypoTwE7Fnpwus6mSPKpDfVyX0IyARI4H9wQxzO2VdzRBkfCef489CXb1DfvGXbsL+nXG2rbEigev58EM7KPVmNLuxDT+GW5sw2djzg+QthOKtuV9/N9o2wDz6dK8oQdgL24R8jkHwwVlgx2Ed/oiIDlgpxy8PRTpkjyqSg88B2M5fEYsdP3ygQtaAivggTNpyDT6ZFmTR2Au5rz0DzPKC+HWZVLc73yxxRJsVrnRKOFOidAOrLBQw3CpklyqQZuwK38zge2ep3hF0IJWRmRJnM+fvCaQlLGCq66+51UFEl2aJMetxLRyFi48DtP6u+UySaky3KJKHoN4eEw5oqf72r6+GcfDFXlFEjerAPPQPDSyq1974XcmIkR5RJ4fWeB6KjcHvPpUWZ9GQmR+F2n4FO52kiCvvoTxEWE9jZ7sEImUroyRZlUjhHn4NOEWHdpwGKBgqGIbNEmTRD3SpCTmx/UEXH0P5yDj2TK8qoCVpwXnsWhhOHdeAJeLYDp/tsjiiTXubTL0PY8fR3zY2r83nKeOODSpiyE3kn9izoH6NozKntZ3qhRG+GYZj5RqdImUNPpkWZFHQ/sE+8ADvGFyPm+nEnx+C89nTBZw+6X9NwhllKlJQwc7W88MILeOihh3LaKFKG2mdS+sfGxnI+c/XQdyYZSVEIGkbjlBK2pxUVjGzX/0tv3ytJDKGHtwJQO4kl2dADgkVv1rPHGx1ABUUCZNE/JtQD6Zt2AP2jMu/RLAM9iLTUCGxbDrgUiVMEefmYSmfSWjbgbH/R0XCqX4ezbCu09q3ApaNFxzO7D6O9JvdBrXNQojUviORMv8D2FR7ayqJKHCoGPYDetRYwpOU/lBZcCemnUZRVwalZjoHxwm/ASXQZ98IqmiCNbUGzJnOEo7gNWAF6mNYhbUsJLgVnSw+5NDy7jdKk3Kt/eLwW5uu8zMZyRMGHWkImRRfCcVyc7S8eeXBRCYXJ4STsJaKFp0lRSk4cTstGlVJHwt5003z9RqChUsKhtKIiyMvHERbx9Dk6WnjWSmylfR/vBzR7Ugk6xaBhRjikRE2P0onyRJkUlAJFoeuEcG14V7oKT9BzIceGgHveA1N4cDuPFZ23c+kY9OUbC0+m74JK4VLrPdLnz1MKaJTGOM11gAQofefD0CgSqIAglKbzKLSKen/6jjVVZEqiUjJpva04PDsB2Vn8mpE9P4/Sl6YZj1LIroaELVUEZjFomEOq7SI6JxmGWXznpUditpfsJOZz5fIN6zcwSxy638aK3JfpmcRJvgBimCXCohZment70dTUlNNG3+kmFZtGrf/MZz6Dqqqq9Ie8aeYC6g/beW+us6Fhc9hnnhPoZf50OC6Uh4GQRW7ASQoNp7f2U2dYeDzy2iD/iKLLmdxuSnCgB+Fi2BZZ40BKiiIo/mBNUT3kf0EfaU9zYbctmJo3ZT+Sl0zO9FwBU5N+wlSeuJE7YgymntzweW+asqGHRFo2egidDpov9LyMRCeh0mFymmhWweDUqI58CnW03On3/VwxX+dlNnQYTXcOJhx/oJQeErRti2C5fspRA6U350cfFTrAk/uIfld83n7CnaDzzSqithCOf4wTM11PSLipb0uKfdMe5wm174UQkFkRH1MgwSZ13M5w8aDpCApxI5FmunOCzlkar+BE8ubhuv5sqb3YQwENtuIQgSBgBHMiWKaM5yQgUnLwNNNT4ybPAzV+/tu7LIQVh5s6Z6bblq6Tmfcsoc2vrl1FoGHTXFZK8py8XvpGyHOoxG6sDDOPlMJ5Oe39ZDadS4aZDTPcl29U/5QpPb74xS+io6MDoVAIt912G/bt24elwKIWZq6Vj33sYxgdHU1/OjunhvdfC0EDynSzGORNESwxnypTl75QUIRw0H+4s7UQIIocLkLzh2dBUTZBPe+CaQaUAW42IZOWATjd7Zv/FqMyTKbKfkqYaGgvOh6ZlEqhQ9NctFUXv2A3VXrQx/t8f5a64p0ar3Y5BqK5y9xQOTUtra3KRfeojrinQ6ttLjo9rWEFzpPtjmZAlFUXH6+yXqVyUErLdMdMdcidGq0RqVapNinoYT+sO76Ja4jyb4oIDiQe0MNsNmbA/yzi8zIbMmymY6kYjZX+tiFDuWVVxY8f/xiQGLABEYz4akrBGRpKINDG+qALMr0u/gDZWi0wNAFYlpj+GCfTO81IC5X5Ilw2ZBR9aRiQZMJLhrpFUFEpRgDuSJ8y1Ss677IqeJqZOV5o3YtNk9IEOzvhGiFlTF10vLpWeKODReZXDRlPnmxmiHaMf73SdOXTUnyabXDIV4lStxo6iq9PbZsScdX/A9Nc42h+NJzOHU0HaopvSzR2QE8KTcrot9i8qxogaVpXAQnYLcUvG2irmSoal/o5eb3+aD85KfHsUTJDZnGGuTkohfNSr/IjDQsSjKh7DsNcL9Pel4WWvC8zC4ll+y9HBsf9v/R9vvnmN7+pCv984hOfwKuvvqr8aSljpr9/mrD0RcKiFmaam5vR19eX00bfKysrEQ4Xf/oKBoNqnOzPXKDrGlY1ipw0khTURsaxerKiR6kQNCQ2F3l2WFHvv40kzgyHINu3FxyP2k8P527vza0ujN7clB599S6cGMytWLJ1uYBtezjaDVVVpK688Am9sU3gXL9E7wg9bdYChUQNIaCvuxXuwHm4T/+jqlyU7Q+TXg4N2NAKyFMvwSPz07Y1uelAKcwg7MZ16B3NPHSTSFJbLlQFnBQ0j8YqgVM9wIsXI9DX7i74oE4PmVRhhrwgzk+UKzPgQojqRkgSW1wb5qVXsaO18JupZdUuzOFLOWknWusaDMZzV3pNgwO994T6v4xH0/41U7bLqh1wjdztYKzZBdcs/vA9l8zXeZlNeVhge3thEYWOvUjW6jdW+9XUCh0/KxsEOpNagtpmyzcXnKZYtRMeCROdh+HaCWxdoRXUcMjgmjxrXjoLDMUAUV4D0KfgMb4HR3r8BaM0ITo3CrGqETAEnd8C+zuDMFZunRpdRQQjSjB0nvoq8OoP1XcSfwphrNsDL3mu2Hqo6DFMlZmUoHf2x/Ce+b/QW9eoqklTJxhQx6M3ONWvRQ1etR1up3/sGmt3wTbCGJokoSlY/PyprAfIVHeoW6U0UUUnqro0dSF16Kt3wqX8dYpdEboyQi6E3rEVnlrWjdANQy1Loc6iqo5WnWVGGKlSxsIFllJtSz2cm+45E7omsLZFFBRf6NpE1Zko6mkxnZPXw8ELflU1ugIe72Jhhrk5KIXzUhohoMgLBG3d7RBBfmBmrh913+3YUnAYtXt5fVbmxkIvRF48LfHDQxJPH/X/vnhm/l+UfO5zn8Ov/Mqv4P3vfz82bdqkPGcjkQi+/OUvY7FTWirBVXLHHXeoSkzZPPHEE6p9oaDqRfdtogorybQEehNeA9VGw0qNQEBHa7WH29ZAmdemOvjbVgBrmwW6kt6avWMGrOaN0DffA6ioCwp3KVPfraYN6BvznxTKgsBtqzy0V5EPw5H0w4qx7X5YNStwftA/5CrCwJ3rhIog2HvSf5C42AfsWaNhXUvmrS89rL5uo4Dj+qWJiQM9YZi3PAKxbJP/9lqJGc0w9rwFHpW9PuWHsxnOBO7bKNFe56UfhpurJB7cJBG8ciqZ1iPhdZ+FsefNEI0dyTwSof5P0zuVFJyoeVmtVMtCpZMJSvGiad+3QeLcgD+DkSgwLCth3vomCKrGo0bUoS9bD/OW1+O1AX/bvUZVe8v8SjCqhLVaYFM9AJpUVab7TNqjpF4bxl3r/G2m9pkBbF0msWOZnRZcVKngtbshVu3CK13hdDTSzg5gfX0c2hXfs4TMfPX2LaraTSragR5ajS33QG9ZBff5f8vZZ6hfgUBgab35qgxJVQ0sZd5Lx9raFv/YKw9lHmrLwkb6+KF9TVDJ+Ac2C/VWIHVM7T1lQqPKQhvuzNqm5dA2vw6ieR3ky99TKWzGuZcR1j3cv0mgPhk5o0SeRuDuDQKTMYndq4SquBO1QzB2Pgws35QWU0iw0299CxKB6rRPzrMnhDoub6XKW8n+Ce33bSsE1rcKPH/G965Z0yyUqBHY82ZoKrfJf9uktazyq3HpwbTQ4A6NwNxyrzoWSThRo1bUwdz1CLyKOnjP/6v/+5e+o5bJ3PmQLyQRVBp+1Q4YG++AdeGyWnY69qUZRuDWN6oS2f6GEypKJ7DnTXCH+2F0bPZFEcPMzG/7A3CTZsXG9vsh6lphuQaOdgkcuCjgRSpg3vpGiNSbW92EvmITzO33w0246vc0P6qQptP1onV95npBFZn2vAVudFKVv6Z1o3NNX7FRLXvmGlcOY9Nd0NvWAv0XYKzeAWEGIAMRGLe9FaKmJRNR07Yexq43wIhkxBaqTGLueFAtV3o/VjWq5aaS5NcC7ecHtwi0JDc5bc4VdVDHZVnW8bvUcT2pSsHT/bW+gjzKFnqJGObmwYxEYGy4A2L1rvSLLboP6DsfAag/ZpRU0VdmkWKEItCWbYCx8c6cZw+6L6v20DQh0My8QpExVCSmL8/iirwaXzk3f5EzlmVh//79OR6zmqap7zN5zC4GhEzFcZcAExMTOHPGfyDduXOnUsTuv/9+1NbWYsWKFSp8s6urC1/72tfS5bK3bNmC3/iN31Altp9++mn85m/+Jr7//e9fVbls8qShPF0KCZ2rNw9x24Od9DgxDYmQWfoa2ETMBbmk0FKHTE/dWMdjviGvSocxXdVGLuiCPCvo7X1ZJRzHUUajUtLbWqkeaKlNS9CrbQmpadAjlcp3IWpp6elVhAUsy016edB8PZSHddi2i7iTapMoD2uwEjZsT6hXo7rwEAoHYFk2tKSHA73tpo6CFbeU6Rz9jlIuAuEQEgnH91gh01BNIhwy4MSjykiU5uLpBoxQGex4DCLpFyJ1A2YojFjcURWXUtEJoZCBRDwBx9PVSpD/TCAYQDTuwk36wQSEh2DIgBsdT3rvCHhmCEYgqKbnev52ohSUYNCAFx1LGkMIuIEgTDMEKxqFJl21jenNVCBgIBaz4ElNrRvZxei6CZdMSSmXWwh4wbLkPvPS+zGzz0aT+0xL77P0/slqE5TuJGnbaTCuoZTvXDIf52V+2WzyaFHHu+HBLJLTl0hYcDzNP/Y0OgYCKsqLjlE6lrVkJA5tP5kgzxIPHjQEyvxORHpfQoNmGki4hto/XjKljNIJKV2Qgun8tHyKrJMwnSgkeaQkfVBcYcATAaUIOl5m3gE6FIXv0ZQ6twKaCyl1uNJfFjrrSHehYy+MKDTPUeNKw0TcCyKkWWlTXzoePEE5UgY0K+afS/RjPQAXujKsVW3Q4BphlR5GIqhaeCHgmGHotMzqmKbjS4fUTLW+OpzMOUbpfNJT86Ny2epv8jygVD9IMuWi4QKuWQGP/rpeOkCMrgNBuIBnZZ0/IZhm0Pdosi3fwUVtVE8tqzLwTV4vdFoiMuuhkHsSWxJJ7yojCJmYTF/jtGCZ70VDkUR50Sh2bNI//9SONGEUCaum6kup7UbpS1cbKVNwmo5/3KRT2mhHLPJz8moYGJN49pjEduMEEqE6nJhowJtvoSi3m0ecYpiFPi8ty1E+XuraJjSYkdyoaIaZK/KfPZiFhV5QUoRMMR7ZLlAZnvv7cXd3N9ra2vD888/nBGL8zu/8Dn784x/jpZdewmKmpCTtV155RQkxKSh/jHjf+96Hr3zlK+jp6cGlS5fSw6lUNokwH/nIR/BXf/VXWLZsGf7+7//+qkSZ+YKEGHpz7bM4OookimRIRbaIKYdL/gWRHvzzX46otyVG7hth8l1IRX1kR+xkskX8+dMDMpWU9kmKHUEza7zUb00gL5ojEKKxcsck8SNYQIXPXVOysJiqvJOIg7wxg6HglOlFQlO3nZ4lbGgFp5ccFqmcMl4gMjV9KFwgr0Yv8NuKsFZgn1XNuH/8Nn96pS8jXj/Z0TGpY68QwWBgyv42TS3rGM3eflP3b/6+nLpnBaY+zguAor/UApizuljnLo+Rt17Z65rbcfbnEgaC4albIzlRLXuqqeXKJpA5DtVRGijmS3RtYceZ5cneT/R/Wr7M1kstp6BIHyOQs9ZqGCmaRfD9l5LknRuiyNtfMzy7hxAzGADoM4eYhlCeMzcrV8Z9cS48cgGm6ALKHlSlxNunsb5gGGZuoZdGCFy/0MwwM8FiTGkxXbGb2QxnClNS3br77rsvbcRYCBJnCv3mwIED87xkDMMwDMOUClfGJMrdEeiVtSraK4wYBsfDaK9fHC9CGIZhGGaxMtOLofl6cVRfX69e9BfymCXv2cXOzfBinGEYhmGYJcTIpIdyZxiorIOIVCHsjnHZbIZhGIa5AVACAFUbLgS1F0gQmBMCgQB27dqV4zHreZ76vpAes3MFCzMMwzAMwywayAw+7mgIeZMQoQqI8mqE3QmMR5N+PwzDMAzDzBsBU6iCFfniDH2ndho+X3z0ox/F3/3d3+GrX/0qjh8/jg9+8IOYnJxUVZoWOyWVysQwDMMwDDMdkwn/b0h3lP8PmbWHMIq4oyvR5kYYITMMwzDMzUwkKHD7Gr/4BHnKUPoSRcrMpyhDvOtd78LAwAA+/vGPo7e3Fzt27MAPfvADNDUlq+EuYliYYRiGYRhm0TDuF+NDOOh3/qhYVsRw08NquDAMwzAMw8w7JMLk1WG5IXzoQx9Sn6UGpzIxDMMwDLNoGI9J6NJGIJSpshUxfX+Z8WTVc4ZhGIZhmMUECzMMwzAMwywaJiZshMlfJqvEuxEMwJQJJdowDMMwDMMsNliYYRiGYRhm0TAe8xD0ohBmJmIGwbBqm4zaC7loDMMwDMMw1wQLMwzDMAzDLBqiloaQjAFZwowIhBGQCURjvtcMwzAMwzDMYoKFGYZhGIZhFgVSSsQ9AwHNgSDX3xRGAEGZQMzmikwMwzAMwyw+WJhhGIZhGGZRkLABCYGgkeslQxpNUHMQcw0l3jAMwzAMwywmWJhhGIZhGGZRELX8v0Fj6rCA7sKFDpuzmRiGYRiGWWSwMMMwDMMwzKIgmvCjYQLm1JSloO4lx7nhi8UwDMMwDHNdsDDDMAzDMMyiIBZzIKQL09CnDAuayXGSUTUMwzAMwzCLBRZmGIZhGIZZFERjDoIyDhEITBkWMDVyB0Y07izIsjEMwzAMw1wrLMwwDMMwDLMoiCVcBEiYMaYKM8IMqmHRqL0gy8YwDMMwzPyxd+9evOUtb0Fra6uqzPid73wHSwkWZhiGYRiGWRTELAHTs1R57GLCTCzO7r8MwzAMM994VgLe5Ai8kX7/rzW/Jm+Tk5PYvn07vvjFL2IpUqCuAcMwDMMwTOkRczRUChtCBKcONEyY0kLcSprNMAzDMAwzL8jYBJyjz8Eb7Eq3aXVtMDffDREun5d5Pvroo+qzVOGIGYZhGIZhFgUJz0BAKxwRQ2HNpnCQcLhrwzAMwzDzBUXG2HmijGof7PLb5zlyZqnCvReGYRiGYUoe15NwYMDU/LLYhQgIB3FvasUmhmEYhmHmCDs2RZRJodrt2A1fpKUACzMMwzAMw5Q8iaSnb0CXRcch0SYhTUhZfByGYRiGYa4D27q+4UxBWJhhGIZhGKbkiSeFGdMQ0wozEhps9v9lGIZhmPnBDFzfcKYgLMwwDMMwDLMoSmUT5jRlC1LRNCkRh2EYhmGYOcYMK6PfQqh2M3zDF2kpwMIMwzAMwzAlTzzmqy2mWbzrEkiKNjGLU5kYhmEYZj7QAkFVfSlfnElVZaLh88HExAQOHjyoPsT58+fV/y9duoSlAJfLZhiGYRim5EnEHRhSQDeKl8NOpTklYg5QxaHUDMMwDDMfUElsY9v9vtEvecpQ+pIZhpgnUYZ45ZVXcP/99yPFRz/6UfX3fe97H77yla9gscPCDMMwDMMwJU/c8mDKBDCNMEOijSYdxOJkPMjCDMMwDMPMFyoyZh6FmHzuu+++JW3uz8IMwzAMwzAlT9yWMD0b0IsLM1rAhCktxBPFS2ozDMMwDMOUGuwxwzAMwzBMyZNwNJjChihelEmJNiTMWBYLMwzDMAzDLB5YmGEYhmEYpuRJuBpMONOOIzQNBmwkph+NYRiGYRimpGBhhmEYhmGYkifhGTA1v2T2dJB4k3CmC6thGIZhGIYpLUpSmPniF7+Ijo4OhEIh3Hbbbdi3b9+043/+85/H+vXrEQ6HsXz5cnzkIx9BPB6/YcvLMAzDMMz8QWZ/NkiYmdn0zxQuEp5+Q5aLYRiGYRhmSQoz3/zmN1Xpq0984hN49dVXsX37djzyyCPo7+8vOP4//dM/4fd+7/fU+MePH8c//MM/qGn8/u///g1fdoZhGIZh5h7bBSS0WQkzhubCksUNghmGYRiGYUqNkhNmPve5z+FXfuVX8P73vx+bNm3Cl770JUQiEXz5y18uOP7zzz+Pu+66C+9973tVlM3DDz+M97znPTNG2TAMwzAMsziwkp4xxiwCYUwhYUsD3hIuqckwDMMwzNKipIQZy7Kwf/9+PPTQQ+k2TdPU9xdeeKHgb+688071m5QQc+7cOTz++ON44xvfeMOWm2EYhmGY+SNu+SKLORthRvdApZtSYg7DMAzDMEypY6CEuHLlClzXRVNTU047fT9x4kTB31CkDP3u7rvvVjnojuPg137t16ZNZUokEuqTYmxsbA7XgmGYa4HPS4YpLUrpnEzEbWXra5ozm/oq8cYBLBsIcUYTs8QopfOSYRiGWaIRM9fCs88+i09/+tP4X//rfylPmn/7t3/D97//ffzpn/5p0d985jOfQVVVVfpDhsEMwywsfF4yTGlRSuekL8wAhjFzt8U0fPEmbs1cwYlhFhuldF4yDMMwc4eQFGZSQqlM5CfzrW99C4899li6/X3vex9GRkbw3e9+d8pv7rnnHtx+++347Gc/m277x3/8R3zgAx/AxMSESoWazdsGurGNjo6isrJyXtaNYZjp4fOSYUqLUjonj58ZxfGBEO5oGoAIhKYdNzE+jn2j7bi9PYHlLeEbtowMc7OdlwzDMMwSTWUKBALYtWsXnnrqqbQw43me+v6hD32o4G+i0egU8UXX/ST0YppTMBhUH4ZhSgc+LxmmtCilc9KyPJjSAvSZc5NMiqqRHhIJNplhlh6ldF4yDMMwS1SYIahUNkXI7N69G3v27MHnP/95TE5OqipNxC/8wi+gra1NhXISb3nLW1Qlp507d+K2227DmTNn8Ed/9EeqPSXQMAzDMAyzeEk4EgYJM9rM93VhmDCljQSnMjEMwzAMs0goOWHmXe96FwYGBvDxj38cvb292LFjB37wgx+kDYEvXbqUEyHzh3/4hxBCqL9dXV1oaGhQosyf/dmfLeBaMAzDMAwzV1iOgAEbQszihYtuqOiahO3diEVjGIZhGIZZWh4zCwXl55KBGufnMkzpwOclw5QWC3lOPvXyKHR7EhtWBGY1/sGLQHWZhtt31M77sjHMQsL3SoZhmKXBoq/KxDAMwzDM0ibh6TDE7FOTDLiw3JlLazMMwzAMw5QCLMwwDMMwDFPS2NKAKWafmmQKEma4i8MwDMMwzOKAey0MwzAMw5QslHFNwoyhzV6YoegaS3IBAIZhGIZhFgcszDAMwzAMU7I4LiCFBvMqdBYScSxZcvUNGIZhGIZhCsLCDMMwDMMwJUvC8f8aVyHMmJoHW5oq2oZhGIZhGKbUYWGGYRiGYZiSJWH5pr/GVfRYDE0CQsCevV8wwzAMwzDMgsHCDMMwDMMwJYsVt9Vf8yoyk1LRNXGbI2YYhmEYhrmJhJn3ve992Lt371xNjmEYhmEYBlbCF2aMqwiZMXW/VLaV4JAZhmEYhmFuImFmdHQUDz30ENauXYtPf/rT6OrqmqtJMwzDMAxzk5KwPAjpQtdnbzJjGCJH1GEYhmEYhrkphJnvfOc7Soz54Ac/iG9+85vo6OjAo48+im9961uwbe4YMQzDMAxz9Vi2B1PaEIY569+YyegaK+UczDAMwzAMc7N4zDQ0NOCjH/0oDh06hJdeeglr1qzBz//8z6O1tRUf+chHcPr06bmcHcMwDMMwSxzLljCkBWizj5jRDR2adNLGwQzDMAzDMDed+W9PTw+eeOIJ9aHQ4ze+8Y04fPgwNm3ahL/8y7+cj1kyDMMwDLMEsRzAgENFlmaPbsCQtoq2YRiGYRiGuWmEGUpX+td//Ve8+c1vRnt7O/7lX/4Fv/3bv43u7m589atfxZNPPol//ud/xic/+cm5miXDMAzDMEuchCugi6uMfBF6UpiZr6ViGIZhGIaZO66i+OT0tLS0wPM8vOc978G+ffuwY8eOKePcf//9qK6unqtZMgzDMAyzxLE9HSbiFAYz699QdI0hHFju1YTZMAzDMAzDLHJhhlKU3vnOdyIUChUdh0SZ8+fPz9UsGYZhGIZZ4liejrB29SlJBlxYzuwNgxmGYRiGYRZ1KhOlMb3//e/HmTNn5mJyDMMwDMMwCgsGDHENwoxwYcnZR9kwDMMwDMMsamHGNE2sWLECrsvVDxiGYRiGmRuklHCkAVPIq/4tiTmUBsUwDMMwDHPTmP/+wR/8AX7/938fQ0NDczVJhmEYhmFuYhwXkEKDoV+bMEPRNgzDMAzDMKXOnPVY/uZv/kalMrW2tqqqTGVlZTnDX3311bmaFcMwDMMwNwEJxxdkrkWYoSgb2zNV1I24qlrbDMMwDMMwi1SYeeyxx+ZqUgzDMAzDMLASjuqqGPrVB/gqMccTKurG5MAZhmEYhmFKmDnrqnziE5+Yq0kxDMMwDMPASthJYebqf6t+YwMJW8I0OGKGYRiGYZjSZc7fIe3fvx/Hjx9X/9+8eTN27tw517NgGIZhGOYmwLIoYgbXJKwYushE3YQDc75sDMMwDMMwJSfM9Pf3493vfjeeffZZVFdXq7aRkRHcf//9+MY3voGGhoa5mhXDMAzDMDcBCcuj0kzQryFkJvWThIq6YWGGYRiGYZiboCrThz/8YYyPj+Po0aOqMhN9jhw5grGxMfzmb/7mXM2GYRiGYZibBNvyYMCGMK7+PVIqysa23HlYMoZhGIZhmBKMmPnBD36AJ598Ehs3bky3bdq0CV/84hfx8MMPz9VsGIZhGIa5SbAcCUPagLj6iBmdxBzpIcHCDMMwDMMwN0vEjOd5ME1zSju10TCGYRiGYZirgSxmVMTMNXj3CkNXoo5lcx+EYRiGYZibRJh54IEH8Fu/9Vvo7u5Ot3V1deEjH/kIHnzwwbmaDcMwDMMwNwmWK6DjGiNehK5EHRZmGIZhGIa5aYSZv/mbv1F+Mh0dHVi9erX6rFy5UrV94QtfmKvZMAzDMAxzk2C7GsxrFGYoysaAC9vlUtkMwzAMw9wkHjPLly/Hq6++qnxmTpw4odrIb+ahhx6aq1kwDMMwDHMTYUkNEe3aI14MOLDcOXsHxTAMwzAMMy/MWW/la1/7GizLwutf/3pVoYk+JMpQGw27GsgwmCJvQqEQbrvtNuzbt2/a8aks92/8xm+gpaUFwWAQ69atw+OPP36da8QwDMMwzEJiSUNFvVwrHDHDMAzDMMxNJcy8//3vx+jo6JR2KqFNw2bLN7/5TXz0ox/FJz7xCRWBs337djzyyCPo7+8vOH5KDLpw4QK+9a1v4eTJk/i7v/s7tLW1Xdf6MAzDMAyzsNjShKHJa/69oXmwvKuv6MQwDMMwDLMoU5mklBAFyiZcvnwZVVVVs57O5z73OfzKr/xKWsz50pe+hO9///v48pe/jN/7vd+bMj61Dw0N4fnnn09XhaJoG4ZhGIZhFi+eJ+EK4/qEGXiw5q6rwzAMwzAMMy9cd29l586dSpChD1VfMozMJF3Xxfnz5/GGN7xhVtOi6Jf9+/fjYx/7WLpN0zSVEvXCCy8U/M33vvc93HHHHSqV6bvf/S4aGhrw3ve+F7/7u78LXee3ZAzDMAyzGLGSGUzGddzKKWLGdv2XNgzDMAzDMEtWmHnsscfU34MHD6qUo/Ly8vSwQCCgolfe8Y53zGpaV65cUWJOU1NTTjt9TxkK53Pu3Dk8/fTT+Lmf+znlK3PmzBn8+q//OmzbVulQhUgkEuqTgipHMQyzsPB5yTClxUKfk1aClBntOoUZwPUMFX2jaew1wyx+Fvq8ZBiGYUpUmEmJHyTAvPvd71bmuzcSz/PQ2NiI//2//7eKkNm1axe6urrw2c9+tqgw85nPfAZ/8id/ckOXk2GY6eHzkmFKi4U+J62EBSB0fcKM7gEOYDkSoQALM8ziZ6HPS4ZhGKbEzX8feOABDAwMpL9TJaXf/u3fVoLJbKmvr1fiSl9fX047fW9ubi74G6rERFWYstOWqEx3b2+vSo0qBKVKkVFx6tPZ2TnrZWQYZn7g85JhSouFPiethKP+Gvq1d1UM3RdjLOvaS24zTCmx0OclwzAMU+LCDPm6PPPMM+r/JIqQLwyJM3/wB3+AT37yk7OaBqU+UcTLU089lRMRQ9/JR6YQd911l0pfovFSnDp1Sgk2NL1CUFRPZWVlzodhmIWFz0uGKS0W+py0kiYzpnntkS6paBs/+oZhFj8LfV4yDMMwJS7MHDlyBHv27FH//+d//mds3bpVVUr6+te/jq985Suzng6VyqZy11/96ldx/PhxfPCDH8Tk5GS6StMv/MIv5JgD03CqyvRbv/VbSpChCk6f/vSnlRkwwzAMwzCLE8v2IKQLTbv2XKZUtE0q+oZhGIZhGKYUmbMakmS2m/KXefLJJ/HWt75V/X/Dhg3o6emZ9XTe9a53qZSoj3/84yryZseOHfjBD36QNgS+dOmSqtSUYvny5fjhD3+Ij3zkI9i2bRva2tqUSENVmRiGYRiGWbzCjCFtiKxqj1dLKtomFX3DMAzDMAyzpIWZzZs340tf+hLe9KY34YknnsCf/un/z96dgElWlffj/557b2299yw9S0/PPsMAwwzrIAqCBiTBjZiFECIEE0xi0AR+McovKq4hihJciMQtxt9fI2o0ccUFQVBAZAZwWGbfl56Znp7earvb+T/vuVW9d0/PdHV1dff38zz1dNetW3ere6rqvvWe93zITD906BBmz559Ssu69dZbzW04jzzyyJBp0s3pySefPM0tJyIiokrj+vIlxYdSp9+VybIck3XjegzMEBER0QzoyvTRj34U//7v/44rrrgC119/PdavX2+mf/e73+3t4kREREQ0FpLkIoGZ8VCObbJuXE+XbLuIiIiIKjZjRgIybW1t6OrqQmNjY+/0t771raiqqirVaoiIiGgG8AIFB5LpcvoZM5JtI8EdGS6biIiIaNoHZoQMWd0/KCOWLl1aylUQERHRDOAGNhyVH/dXlSgwc/rBHSIiIqKJNq5vO+eff74ZylqCMeedd96o/cA3bdo0nlURERHRDOJqG7UqHPdyJOvGCxmYISIiomkamHnjG9/YOxLTtddeW6ptIiIiohnO0w4cqwSBGRXADeIl2SYiIiKiigvM3HnnncP+T0RERDQeHmIlC8xkdUl7btM0onWI4MA26J4OOGdcBGXZk71JREQ0A/GbChEREVWUINQIlQ2nBGNHOpaGF/DrDg0v2PUc/B2bpFI0dC6N+Hm/M9mbREREM9C4v6lIfZnRassUtbe3j3dVRERENAPkC8NbO3apAjOx8S+Iph3tu0jv2Y7fNr4OaVWDi459H41dx2HVzZ7sTSMiohlm3IGZe++9t/d/rTX+5m/+Bh/84AfR1NQ03kUTERHRDOTmPMB0ZRr/shwVZd9IFo5tsQgw9QkO7cDz8fPRpmeb8+TXNVfjygMvIX7WJZO9aURENMOMOzBz0003Dbj/9re/HX/wB3+A5cuXj3fRRERENAO5+UJgxhl/IMVk3XhA3tWoSjIwQ326jxzFYedSLK/Poibm47lj9Th8NIPFZ4ZQqgRRQSIiojHipw4RERFVFDfvm7+xUgVmeoM9RBEd+NibaYCtQsyryqM2HqDazmOPvQK6m93viYiovBiYISIiooriuoH565SgL5NjR8EdBmaov/BEK444zWhMuLAtU/sXTdUe2pxmeMePTPbmERHRDMPADBEREVUU1wthaR+WM/7RlIpZN8UsHCKRPd6GLns2Gqr6hmRvTAWmHlHb8eykbhsREc084/7Gc/vttw+477ouPvKRj6C+vn7A9HvuuWe8qyIiIqIZwPU1YtoDSlDno5h1U8zCIRJHOqO/s5J9mVRVToAYPBzNxLFQ6zGNOkpERFQRgZlnnnlmwP2Xv/zl2LVr14Bp/GAjIiKisfJ8wIZvupeMl2Td2No3WThExVFEj+eTSMVziNvR0OxCzrf6WB5t/jzoXA9UqnZSt5OIiGaOcQdmHn744dJsCREREZFktwQKDkrU9UhZcLRnsnCIhM72oEPNQo0ztO5QXTLEHncWgs6DsBiYISKi6Vpjpq6ubkhGDREREdGAwIwqTdcjyYJw4MFjYIYKgs5j6LIbUZscek5UJ2DqzHSeSE/KthER0cxkTUb6KBEREdFI3NCGo0rX9chBYII9RKKjIwutbNQmhz5WE/flyyo6etj1jYiIyoejMhEREVFFceGULGNG2CpAPuBXHoqYZBitUR0b2l1OakWnrDw68rFJ2TYiIpqZ+C2FiIiIKoqnHcRU6TJsYyqAF9olWx5NbZ35OKqsHOwRvgVX2y46UA/tu+XeNCIimqEYmCEiIqKKIV2ePcThWCXsyqRCk4VDpMMA3boKKWto4d+i6niIbrsRYU9hTG0iIqLpFpjh0NlEREQ0EjN6klJwSpjg4lganmbXFAJ0uhPdVgOqYiMH/qoSCr6KI9vdXdZtIyKimYvFf4mIiKhiuPmo7odjq5JmzHiI8TsIIdfZCddKoSo58vlVFY/Ok65udmUiIqIpFph5+OGHxzTfj370IzQ3N5dqtURERDSN5PNRF5OSZsxIkEepKBuHZrRisEWGxR5JygmhdIiuDM8XIiKaYoGZ3/3d38WKFSvw4Q9/GPv37x9xvksvvRSJxCifhkRERDRjubkoYybmlDBjphDkcXMj1xWhmaErq6XQDFLOyKN+Sa/7lMqj22VdIiIimmKBmYMHD+LWW2/Ft771LSxfvhxXX301vvGNb8B1mQZKREREY+O6xcBM6VJmYvbAbByaubrztgm6WCeJ+6VsD91hFbQuXRFqIiKiCQ/MzJkzB7fddhueffZZ/PrXv8bq1avxtre9DQsXLsQ73vEOPPfcc6VaFREREU1TrheYbiSWU7oyeLHCsorZODRz9QQJJEcZkakoFQvRY9UBuXRZtouIiGa2CSn+e/755+OOO+4wGTQ9PT340pe+hAsuuACXXXYZXnjhhYlYJREREU0DrqfhaBfKKl3GjBMrBGbckbuv0PSn3TzSqgZJ5+RZMKmYRt6qhtvDkZmIiGiKBWY8zzNdma655hosWbIEP/7xj/GZz3wGR44cwY4dO8y0P/qjPyrlKomIiGgakZ5MDnxT56NULNuC0oHJxqGZK0x3IWPVmqDLyaTi0VfkdHeuDFtGREQzXcmqmr397W/Hf/3Xf5mhKN/85jfjYx/7GNauXdv7eHV1NT7+8Y+brk1EREREw3F9hRhK2+VIsm8c7SHvcZSdmSzdnYZWs5FKSNRv9HMhFY+yarrTPmaVafuIiGjmKlnGzIsvvohPf/rTOHToEO69994BQZn+dWjGMqz2fffdh6VLlyKZTOLiiy/GU089NaZt+PrXvw6lFK699trT2gciIiKaXG6gYKvSZrZI9o0Eewp1hWmG6umJasuk4iefN2Zp2NpHmgkzREQ0lTJmHnrooZOvzHFw+eWXjzrPAw88gNtvvx3333+/CcpIkEdGeNq6dSuamppGfN6ePXvwD//wD6aODREREU1NbmjDUXIBXboaM0K6R0nQh2au7pw2haWTdjimYF5S5dHjlfY8JCIiKnlg5rvf/e6Y533DG94wpvnuuece3HLLLbj55pvNfQnQ/OAHPzAFhN/97ncP+5wgCHDDDTfgAx/4AB577DF0dHSMebuIiIiocrhwkFS50gdmVAA3mJAxD2iK6HEtJFR+zPWLkpaPtJ803fQlI5uIiKgiAzNj7TIkH2YSPDkZ13WxceNGM6JTkWVZuPLKK/HEE0+M+LwPfvCDJpvmL/7iL0xg5mTy+by5FXV1dY1pP4ho4rBdElWWyWqTro4hNoaMhtMJzOTDRMmXS1NHJogj6Zx8qOwiGb2p3a8FvDwQT6IS8LOSiGh6GtdPR2EYjuk2lqCMaGtrM/POmzdvwHS539raOuxzfvnLX+KLX/wiPv/5z495u++66y7U19f33lpaWsb8XCKaGGyXRJVlMtqkZCZ4iJv6HqUWUyE8XbIe3DTF6DBAGlVj6sZUlIprZFUVgkzlDJnNz0oioulpSuf0dnd3mxGgJCgjhYXHSjJyOjs7e2/79++f0O0kopNjuySqLJPRJl1fm+IezgSU9XCsEC5ipV8wTQlhpgdZqwaJ2NgDM4m4kiG9kKmgIbP5WUlEND2N66ejT33qU3jrW99qRk+S/0fzjne846TLk+CKbds4cuTIgOlyf/78+UPm37lzpyn6+/rXv753mmToFAsNS8HgFStWDHleIpEwNyKqHGyXRJVlMtpkPusCkjEzAYGZmK3hB3GEWsNivZAZJ5/uga9qkYqffKjsomQsOk960i7qUBn4WUlEND2NKzDzr//6r6borgRm5P/RasyMJTATj8dxwQUXmBGeivVrJNAi92+99dYh869ZswabN28eMO0973mPyaT55Cc/yfROIiKiKSSfl/ofcTh26QMnTiFHOO+GSCU40s5Mk+6J6rIkTyUw44TSvw7pXOlrHhEREZUsMLN79+5h/x8PGSr7pptuwoUXXogNGzaY4bLT6XTvKE033ngjmpubTR9bCQitXbt2wPMbGhrM38HTiYiIqLK5Od/8jTkTEJgpfONxcy5SiVTJl0+VLZ2N6h0mY2OvX2QpIKFcpPPMsCIioolVcVXwrrvuOhw7dgzve9/7TMHfc889Fw8++GBvQeB9+/aZkZqIiIhoesm7hcBMrPSf87FCFo7pLlXPwMxMk84p2No/5cLSEpjJBBX3dZmIiKYZp5QjKXzrW9/Cww8/jKNHj/bWein69re/PeZlSbel4bouiUceeWTU5375y18e83qIiIiocrhuCEv7sIrpLSUUK9QLybtjGymSppe0byGp+oaZHqukFSDtp8z3XOmaT0RENBFK9pPU3//935sRkqRLU01NzYCh/ORGREREdLJRmWLam5ALYKcw1JObj7JyaGbJBHEkrFN/7RNOiKyqlj5wE7JdREREomQ/Sf2///f/TFbMNddcwyNLREREp0xq/zqQAsClZ9kObO3B9U6tKwtNfTrwkUUVau1Tz5aSmjT5fBX89HHEWJuIiIgqPWNGsmKWL19eqsURERHRDOOGFmKYmK5GkoQj2Th5n4GZmSbMppGxapB0Tv21T8Sjr8rpNDNmiIhoCgRm3v/+9+MDH/gAstlsqRZJREREM4gbWHCsiasB48BHob4wzSC5ngxC5SBhhso+NclCbaJ0emIyuYiIiEralemP//iP8V//9V9oamrC0qVLEYvFBjy+adMmHnEiIiIaUV47qIb8wDMxoy86ykc+4MiOM006ExX9TZrsl4GDU4ylxgy0RiZ3as8jIiKalMDMTTfdhI0bN+LP/uzPzNDWrFxPREREp8LVcTTY6QlbfkwFyAcDfzii6S+TCXrrxZwqS8mQ2XmkXX6vJSKiKRCY+cEPfoAf//jHuPTSS0u1SCIiIpohZDhiF3HErHBCAzOZkAVcZ5p0XsPWPhx1evWFEspDxi/9EO5ERERFJcvnbWlpQV1dXakWR0RERDOIjJaklYWYPXGZCTErCv7QzJLxbCSUawpAnw4ZZjujk6XeLCIiotIHZj7xiU/gH//xH7Fnz55SLZKIiIhmCDcX1QFxTmPknLFybA1PxRFqjsw0k2SCmMl6OV0JO0RGVUF70TlKRERUaiXLy5TaMplMBitWrEBVVdWQ4r/t7e2lWhURERFNM7msK5fAiDnWhGbMiHw+QCrJrikzgdYhMkihxj790b4SMTlnqhBkOuHUJ0q6fURERKJk30ruvfdeHlEiIiI6LblcNI513JnArkwy9HEOcLM5pJI1E7Yeqhw6m0HWqsFspwvA6Z1bZshspZDpyaKuvuSbSEREVNpRmYiIiIhOh+tGGQ1OzJ6wdRSDPrmsh/rGCVsNVRA3k0ag5kbBldMUDbMNpNMeWE2RiIgmwoTk8eZyObiupCT3YWFgIiIiGkneDeFoF5Y9cYEZp9BNSroy0cyQ7onqwiQTEpg5vdpCyVg0Ulg6x/OGiIgmRsk6cqfTadx6661oampCdXU1GhsbB9yIiIiIRpL3AUd7pz1yzlg4jg3oEPlCdg5Nf+ls1EUuObD04SmxFBDTLjIDf3MkIiKqvMCMjMj085//HJ/97GeRSCTwhS98AR/4wAewcOFCfOUrXynVaoiIiGiaBmZiKrqIniiWbSEGD3kvyoCg6S+T01A66C38fLpkuO2MP3HZXERENLOVrCvT9773PROAueKKK3DzzTfjsssuw8qVK7FkyRJ89atfxQ033FCqVREREdE0kw9sOJj4TJaYlsDMBKblUEVJuwpJ5Y47Eyth+ch4HJGJiIgqPGNGhsNevnx5bz2Z4vDYl156KR599NFSrYaIiIimoXxoI6bKEJiRjBmfgZmZIhvEkFDeuJeTtGXY7SroYGKzuoiIaGYqWWBGgjK7d+82/69Zswbf+MY3ejNpGhoaSrUaIiIimobyOo64VYbAjBUgF7JLykygtUZGJ5EowXmVcELkrCqE2XRJto2IiKikgZldu3YhDEPTfem5554z09797nfjvvvuQzKZxG233YZ3vvOd410NERERTeMLaBcJxKyJr/0iWTn5cByVYGnq8PLIqGoTVBmvZFxBKxvZdKYkm0ZERFTSGjOrVq3C4cOHTQBGXHfddfjUpz6FLVu2YOPGjabOzLp168a7GiIiIpqmPF8jVDZiZUhkkeBPPoxP/Ipo0nnpHnjWLCRiPQDG130tEY9OznSPi5p5JdpAIiKiUmXMyK9c/f3whz80Q2dL0d83velNDMoQERHRqHKZnPkbK9mQBCOL2xoe4ghCjsw03aV7ovMqGR9/z/1kLDpfMlkOtU5ERBVcY4aIiIjodOSyrvkbj018UV6TlaMU3Nz4C8JSZUtnokK9idj4v+46FuBoD+n8+IbdJiIiGs64P6mUUuY2eBoRERHRWOSyUZAkXoIL6JMpZuVkM/kJXxdNLpPdokMkS1BjRiSUi4zHwtFERFR6Tim6Mv35n/85EomEuZ/L5fDXf/3XqK6uHjDft7/97fGuioiIiKahnBtdQDvOxF/0FoM/eWbMTHsZV5lgSql+L5RhtzMBC0cTEVEFBmZuuummAff/7M/+bLyLJCIiohkk72rE4MKyy5AxU6g3ksuxVsh0l/YdJO3SBeASdoAuvwo6DKEsVgMgIqIKCsz8x3/8R2m2hIiIiGakvAfEdXkyWGzbga39KEuHprWMTiJhRXVmSiEZA4541dC5NFRVbcmWS0RExHA/ERERTaqcbyGmSncBPRrp1hLTLnJRvWGaprSXR0ZVI1Gi+jLFwEyoHOR6MiVbJhERkWBghoiIiCZVLnQQU+XLYIkrDzmfAxVMZ366B66VMsGUUkkmoq/N6R4WjiYiotJiYIaIiIgmVV7HEbfKF5iJSWAm4Og601m6J2f+JuOlC8AVgzzpbHmyu4iIaOaoyMDMfffdh6VLlyKZTOLiiy/GU089NeK8n//853HZZZehsbHR3K688spR5yciIqLKIaM75pBA3C5dl5OTiasAuTBetvVR+aXTUV+1RAmHYHcsDUd7SEcxHyIioukbmHnggQdw++23484778SmTZuwfv16XH311Th69Oiw8z/yyCO4/vrr8fDDD+OJJ55AS0sLXvOa1+DgwYNl33YiIiI6Na4bmLodcVuXbZ2yrjwSZVsflV86G0LpEMkS1pgRMvx22qu4r89ERDTFVdwnyz333INbbrkFN998M8466yzcf//9qKqqwpe+9KVh5//qV7+Kt73tbTj33HOxZs0afOELX0AYhnjooYfKvu1ERER0arLprPkbL2EtkJOR7BxPxeH75cvSofJKuwoJlTfFnkspaXlIM9uKiIimc2DGdV1s3LjRdEcqsizL3JdsmLHIZDLwPA+zZs2awC0lIiKiUshloi4n8RJ2OTmZmFNYN/ukTFtpP4aEKv0Q7Ak7QEZXQYccbp2IiEqn8NWkMrS1tSEIAsybN2/AdLm/ZcuWMS3jXe96FxYuXDgguDNYPp83t6Kurq5xbDURlQLbJdHMbJPZQiHVeLx8xXiLdUeyGRc19VVlWy+Vr25RWqeQsktfpDfpaGStGoSZNOyaOpQbPyuJiKanisqYGa9/+Zd/wde//nV85zvfMYWDR3LXXXehvr6+9yZ1aYhocrFdEs3MNpnNh7C1B9suX2AmHov6t2RzUbYOTS86n0PGqkFyAgpKpxIWtLKQ7k5jMvCzkohoeqqowMycOXPMF7MjR44MmC7358+fP+pzP/7xj5vAzE9+8hOsW7du1HnvuOMOdHZ29t72799fku0notPHdkk0M9tk1gPicEteC2Q0TiwGpQPkcuyOMh256R74Ko7UBJSCKQ6/XRz1qdz4WUlEND1VVFemeDyOCy64wBTuvfbaa820YiHfW2+9dcTnfexjH8NHPvIR/PjHP8aFF1540vUkEglzI6LKwXZJNDPbZM5XiKP0tUBGY1lRMCjLhJlpqac7qh2UTEgWVmlH+0rGtPSVQk9mcoJ6/KwkIpqeKiowI2So7JtuuskEWDZs2IB7770X6XTajNIkbrzxRjQ3N5tUTvHRj34U73vf+/C1r30NS5cuRWtrq5leU1NjbkRERFS5coGDmPLLnsRrAjNeGdN0qGx60lFtmeQEZMxYCkggj3Se5w4REU3jwMx1112HY8eOmWCLBFlkGOwHH3ywtyDwvn37zEhNRZ/97GfNaE5/+Id/OGA5d955J97//veXffuJiIho7LI6gVl2T9kDMzJiT8avuK9BVALpnIajPcSs0mbLFCUtF2meO0REVEIV+aki3ZZG6rr0yCOPDLi/Z8+eMm0VERERlZJ0V84hhYRT/pFl4laAjmDkgQJo6urxbCRV38hFpZawAqT9pBn9SZWzOBIREU1bFVX8l4iIiGaOXCZvRrhJOBOT2TCahC1BoaQJDtH00hMkkLQmrm5RygmQtmrN6E9ERESlwMAMERERTYpMT3Rhm4iX/+tIwgFC5cDNl7fwME0s7XtIqxoknYkLuKXiyoz6lOvunrB1EBHRzMLADBEREU2KTMadtMBMvDDscaYwgg9ND15PF/JWFVLxicvCSiWj87Wb5w4REZUIAzNEREQ0KdLZAJb24TjlL3mXjEVfgdKF4BBND91dUbAkNYHBvpQMmd1v9CciIqLxYmCGiIiIJkXWjYYe7jfYYtnE4jaUDpHN8uJ6OunpcXu7G00U2wLiOo8eDplNREQlwsAMERERTYqMZyGOyclYsSyFhM4hky9/4WGaOD1ZDVuGyrYn9nVNWnn0eBU5uCkREU1BDMwQERHRpMgEcSSsyctYSSgXaY9fhaaTbs9GSuUx0aNYpywfPWHKDJlNREQ0Xvw2QkRERJMigxSSdjBp609YHtJ+fNLWT6UlQZLuIIWqCRwquygVC9Fj1UFn0xO+LiIimv4YmCEiIqKyc3MuPJVA0pm8jAMJCklwiKYH7eZMsCQVm/hgX1VCmeHWezp7JnxdREQ0/TEwQ0RERGXX05Uxf5MTWKT1ZJIxbYJDbp4jM00H2a5u+CqOqjKcU1VJ2/ztKowCRURENB4MzBAREVHZ9fTkzd9UcvK+iiSc6AI+XQgS0dTW1VkYKjs18edU0glh6QDdmXDC10VERNMfAzNERERUdulMAFv7cJzJG9kmVch6KA6xTFNbV9o3Q6CnYhPfPU6KC6dUFt15fpUmIqLx46cJERERlV06DySQhTWJ30RiMdtkPaQzkzcyFJVOV85CSuVglal3XMry0BWwRhEREY0fAzNERERUdj2eg6Sa+NFzRiNBoSSy6GGZkGmhy0+iyipf9lN1LES3VY8wly3bOomIaHpiYIaIiIjKrkenTMbBZEspF93e5HWnotII8zl0WfWoipUv+6k6oU2x4XRHZ9nWSURE0xMDM0RERFRWvucjiyqkYpNfODVle+jWVZO9GTROmY5O+CqB6kT5RvmqSkUBvc4OplwREdH4MDBDREREZdV9osdUT01N4lDZRRIcyqsqeBwye0rrKARHqss4ypeMzGRrD50cmYmIiMaJgRkiIiIqq66u6CK6qmryuxAVg0NdEiyiKaszHY3ylSzDiEz9R2aqVll05if/PCYioqmNgRkiIiIqq65MgJjOIx6b/K8hxeBQd3d+sjeFxqEjHzNBEgmWlFOV46MjrIUOmTVDRESnb/K/EREREdGM0i3DGqMy6nLEHAtxnUNnmhfWU5UOA3ToWlQ75e+OVpMIkbbq4HaeKPu6iYho+mBghoiIiMqqK0giVcZhjU+mSmXRlbcnezPoNOU7O5Cx6lCTLF83pqLaKsv0aTrRni77uomIaPpgYIaIiIjKOiJTD2pRHQtQKaptD51h9WRvBp2m9raoPlBtqvzBteo4YOkA7V3lG6abiIimHwZmiIiIqGw6j3dBKws1SVSMqniIrKpGPlMZ3avo1Jzo9k3h36p4+TNmpKZNjcrgRC5W9nUTEdH0wcAMERERlc0JGdZYa1RXwIhMRTXJqGJsR3v3ZG8KnYbjuQRqrEzZC/8W1Tgu2nU9tO9NzgYQEdGUx8AMERERlU1nWiOFDByncr6CpFIxKB2go7Ny6t7Q2IT5HNoxC3WxyQuK1FUBOasGPW3HJ20biIhoaqucb0VEREQ07Z1wE6hSldVlyLaAaqTRnp6klAs6bZ1t7fCsJOqrJm8b6qUAMIC2tuzkbQQREU1pDMwQERFR2Qr/dqIedfHK6/JRa+dx3K+Z7M2gU9R2PGu6xtWkJi+oFneiLLA2BvaIiOg0MTBDREREZXHiaAdCZaNuEi+iR1KXCJC1apDt5rDHU8nRdBw1Ko3YJI92XmfncMyvhw4rZ7QxIiKaOhiYISIiorJoa8/B0j6qqytvBJu66kJ3lKMsADxVhPksjuk5aIhPfte4xiqNtF2PnqPHJntTiIhoCqqcIRH6ue+++3D33XejtbUV69evx6c//Wls2LBhxPm/+c1v4r3vfS/27NmDVatW4aMf/SiuueYaTCYvCJF3o18EE3GNmHRgr3DZnIcwVFBKoyoVfWnuyYbQUJA9KaYJ9+Q0Qg3YCqgujGQRzSeRPo3qVPSzVSbrQWsF2wqRTMYL8wVmeTZCVKWi0687oyErsJRGddIaMJ+jQqSSDnzfR5jPm+3QdgzxZNxM0/nClzHbQSyZRBC4CHMuFDS04yCWSMHzAuS8aLkxSyOZtOB5HuBKkUcNHUsiHnfg5j0oPyr8qJ044okYPDcPeDJNAfE4YrE4/FwWVuCa/Q1iKcTjcbj5PPyg8HonFGw7hkwuRBBG01LxAI7jwMtlgcA3y1OJpJkW5NJQgRcdl+r66NjlAgTagpL07ELf9SDTA6XluRas6jozzc1mocLADD0br4o62AeZblPEEsqCVRXNl5Ztkdei3zH2M2lAh+a5sarqaL7i61M47lNRzo3OT8eW9PKRf5V3c3mowIdWqvfYDTuf68OV11YrxOwQiUR0XNJZz0yTpp0sHKt0NkRYaAcxx4IfyiHWCE0b0kjI9liA5+necyPhaOQDaXfyUGjmdxwFNwDiloYbyOul4FgaOvQRiznIyWkAZdZT/Kvgm9dY/o87gPbycK0qBCb+rhFXITxYiMOHCgoFTuNJIAzN6R2d53Lux+S0gOXEYLndUVuyHQSImwtqhIHJeJBbXGlzPmtLm/PQ7Hk8BeVmzBbJ82S6WYbWCJ0kLC9rxpcNnThUECC0Y7D9HGRRYTyJnO8gLkVh/SyUnJ+WDcdso5bDDRVG7QeynYGc5ypqA+a9oRqWI5vkA4FXaLcJ+NqBDR++Hw2lK+dGDPLay3pc0w0Clg3lxKBiCYSZrt62YRfaUJH2XOjAg1IKZo99eS9QQDIF244jlPXmpWuFvLgpcxzlvUrlM9H7je3ASUbtbTihlzfHVFkWVDw18nxuDpB5ZanxJOxYAlPBsbRjshsq8SNR2nFCZ3Gs00fLZG8Mjcnxw23wrGY0VvdM9qagocYCukK0Hs2gdj5mjGwm+j5kWxqJ5NR4H6KpR74DQ77bWjbsFLuc0vRUcVdeDzzwAG6//Xbcf//9uPjii3Hvvffi6quvxtatW9HU1DRk/scffxzXX3897rrrLrzuda/D1772NVx77bXYtGkT1q5dOyn70J3V2N4KHDgeXQQsmg2smq9RW4Gp2yKb9dDjWnj+gIWOjEJ1Anj5qhA9OYUXDmp0ZYGaBHD+Mo28r/DiAY3uHFCbBM5eBMRsjWf2AD15oC4VzdeT1XjpkI10HmioUmbaiR6NLYcVci7QUK2wtkWbC9Rn9wF5D5hdo3HuUo3WDjl+Cq4PzK5VOGdRiFTPQWDbkwg9F2rWQoQrz0PYdRzhjk3mwkrNXw5/2XoEB7dDH9wCyMXbnCWwlq/HwUwNNu+PLtYXzwHOmduDcP9L0Ie3mwsyNW8ZwqVnQx/ajfDAC9FBmbcSwZKzELbugt77fHTxt+53ECYSCHf/Fv6xfdGHw8KV8BediecPJ7Gv3TIXfOctDlFdpfHSAY0jnXJ8gGVNFhbP0Yjt2AR9ZJe5+FPnvAqBpRDs2Iiw4yhUPAG9+GyouUuwaW8KbT0ayRiwcr7GggaN2AuPmn1WiSqo9a+B8tLQ259G2NMOlayBt/xcE9jxX3wcOn0CKlUHe/l6qNrZeGJXDbpz2rxmr1yRBbqOQu96BjrbBVXdCG/lBfBTjfjVzkTva3b2Io3auIdUKgqqVbq8Fx3vFw/qwjkGrFscnZOORBELJABn5boR7tgIdLSa455ffA6spiWIpQYGaOQ83n3Mwp5jMOfPggYLaxZqJODj0W22OW/n1GqctyTAiYzCSweL7UDhrGaN+qTGb3YDHWmY1/KKNQHynm3akGyrnC/LmoAls4Ent2tzvq+cZ6HjhEZ1vcLOY7J+wPM1muo0zloUgx0GeHybhYyr0VgNvGyZi668jecP2OjKKlQlgLMXhphVncSmvUBbdxSoufJsGymvG/7u3yI8uscE7tSisxBrXo7g0E4EB6TdBMCcxYgvX4egfR/8Xc9CuzlYDXNhr7wAYbwawZPfgapphF52IYLaGlhuBsGOTQi72qASKdhL1wKzmuE//SPYLWug5rbAtZOIaxfYtQle6y5zbO15S2AtOUdCWPCf/gn8816L1vYYFtfnodsOQ+9+FmGuB6p2DoKVF0DL+dzZiqDzKMLjh6DOuwqOn4cv6z5xxLQpu+VMYN5ShIeOQO97MtrHFedBz12F7UeBXW1O9DrWhzizOYFkvh3h849E+1g/F/aZrwDaW6P9znRCSaB0+XlATSOsRJWZ5m/fCD2rGbHZCxDuehb+8QOABJeaV0EtXGXeg4IDW817iz1/OSDvLa17EBx4yQR1rMb5CFeeDz+RQjzRd75pCfB0n4C37TfQhTbtrDgP1qwFUBJA6ydMdyLYvRnB0b3mvclesByq5azegG2lCjwfx3UDFsZOSJgclajeSuNIjl/6p4rDbS5s7aOuavK/X8l3oVqVRmtPHKsw/eWyHlq7gC2HHeQ8YFa1xtpFPqpjHhKpkYPKRKfClx8le9rh73wm+lyuqgfkc71mFpwqvlfT9KK0/IxZQSQYc9FFF+Ezn/mMuR+GIVpaWvD2t78d7373u4fMf9111yGdTuP73/9+77SXvexlOPfcc01wZyy6urpQX1+Pzs5O1NWN74utZJM88qJGdtCIm3Jte/lZCrWFDJNKIb/kHj4BPLmz7+fL152vceiEhU27+06NBY3yoavwwoGhp8vaFoXj3RqHO6KLTLkG3nGk7/FV8yWDCObidrCLVihsO6zRmYmWIxeRrR0D55FMgletyKL6he8BuULff8tGbP2r4b3wmKQ+wH7Z7yN44VGge9BQlU4M9oY34odba02g59UrM6h58YfQ2UGp6vEUYue8Et7GH/dNS1bDOf934T/+30C8BvGLrob71Pd6Mwt6VTega/XV+MWuKlTFgZevVnj4RcmIGDjbrBqNi1coOI/+BzB3MWJLz4H39A+jX+v77++cFuSWvRw/2dZ30dYyGzhnXhb2E1+HWnmB+WAKf/vzIcfTXnyW+bU9OLitb9qK8+A2rcEPX0zilSs9NHRsgd759JDnWme/EvusZXhmX9+5cPFKYGFDaDJ7yu1U2qXra3Nu7mgd+tilZygsaOxrd96JYwh+870hx11eE+vMSxEvfKGULLBfbZPA5MA2K4G2V69V+O1ujcNdwOvP1djVJm1j6LrPXyZBAI0fPKtw+WpJ3lD4+QvDnRvAhcsVfvJbjZokcNkZCk/tDHG8Z+C6JcvgVWcrHO/UeGYf8IbzArR2Kjy1a2j6wdkLAyxv0vjesw4aAbzqnB54v5bzty/lP3bO5SZQo3vkQrkfJx61r00/MZkjhlKIXfh78KtnQT/y/8G67DrY6RPwNv3UZIL0Zy1cac4777FvmsCCc9al8J7+EXRu0K/aiSrEL7rG/OK6+cRsnN+SR7hnM7Bv85D9sdZfCd2wEHbrFoRNS2G7WXhP/aBv+4rzzV5o1uc+9g1zP3zljfjlNgudw7yOv3O2Ruw33wByGdgXvxHqxCH4234zZN3OGS+Dnr8CwaP/BSRrED/vd+D++vuFrJw+qm42nLNeAe/J70bPW/MyhEf2IDwx6MSU968Nr4VdP9fcNdlER/bAe26YNr38XDjL1plsHrM/6U64T33fvO8NWHdVLWLnXw2rkHU3Ecb7Wdm6/ygeOzgH5zYcRW1Nxf0uZBw97mJrdj5+b00aNQ21k705NAqp5fLjJzpM0FsC5pVgX1uI/dkGvP7sDOJ1DWVZZym/w45VLpvDCwcd7Gob+tnzytUh5s2qzPZNU4uXz0Ed3g5/61NDHnPO2AA9f5XJlieaLioqmdh1XWzcuBFXXnll7zTLssz9J554YtjnyPT+8wvJsBlp/okkQaS9bUODMkKmHWjTZp5Kkncx4EJc+IGFzfsGfslZNldhy6Hhv/i8dFBjWVN00dPcqAYEZcS8ejVsUEbIxfSKeVF3EMlsGByUEXL9/MzhFIKW9X0TwwDB3udhN6+Gqm8ymR9DgjJmZzwEu5/F+kWByS5Idu0fGpQRbhbhsQOw5izqm5ZLIzi6D6rlTDgbfhfBnueHBmVEugPVuSMmG2XtYuD5A0MvvEV7j0J3TgFzWhBfeR78rU8ODQ7I/rbtR7XKmCyHov3HAdeuAuw4rHkrEG55fNjjGex7Cda8pQOn7XoOKSva7tmpPPSuTcM+N9z6JJbUDxzq89m96O0GVskkc2W4oIzYtEfapO7t+mWO3XDx6GP7oPJ9RT/bujEkKCMkyLjtkMZFK6MX2Q0tkykznM37YLoXiZpqOTeke9vQ+dp7pLsZMLcWuGhZlHUzOCgj5Lmb94VYOCu6L93nnh3UfotePGzDD6Nuha88L4C396UBQRlVVRdlaQwOypgFuwgO74A1f1nfNK3hb3kSsUI3KFsH8LfI++zQYxke2mG6iSG5Enrda0yGzpCgjMhnTIZJrL4e+9thuggOF5Qxy9zyOKwwD3/ns7Ch4W/99ZCgjJnv+CFoCeBedA3UinPNsR0clCm+jlsOaljnXh3tj+OY7Jvh+Ds2wg7yZn3Oua822zA4KGMOUddxINsDSMBFumrFU0ODMmYjAwTbfmN+CTTPy2fgvTRCm979HLQbtcvAyyHYv2VIUMYsI9ONsG2Y6GAFaW1zEdN5VFdV7kVbQ730A9RolagrVbTOw0fRbTdiTnXlFNudW2chVA4O7R/mfXUaccPYsEEZsXGvhUxmmO9KRKfI9vImS3U48nltPpeJppGKuuJqa2tDEASYN2/egOlyX+rNDEemn8r8Ip/Pm18Y+t9KQVI5D7WP/PiBE9E8lUTqWMhFbX95P7po6U+uY4e7oBQyXR6XX6CHyxSSbk8jyeSlxkYUlDneM/IvXifSQFAT/bpcFLYfhlU3B9b8pdCtO0deybF9mJtyMa/Gg9MWdaMYTnj8AKyGgecSju6Cmt1iar0EbftHfG7s2E7MrQlMFxbpojKSg+0asSVrTRcLcxE3An38IOYP+rGtrQvRhbLUxBjmwqzwTHORJxeFfZNCc6EqPyrobFRXZliy3ELNiiI5N1y/PFle42mX0lVotHNMsqWEqeXT1TbivGFbFGFxvQAHRmnLkh3mBQrSuTLrRd3khiPtSLr/Cakpc6Rj5GN5oF1j+TygsSY6T0ZypFP1Bntkv4r7Npi0yXReY8MSQPl5qGN7BjyuGpp693c4cpE/uD3o7vbegISpz5MZuUhq2HEE6mUvgxNkERzZO/J8x/bB8XJYvxgIu4eJzBbJeS2BUem6KDVlOo6Osu374dTNhb1gFfa1jzxUy6FOC54TpUJLdybTlWs4ct4U2pxl2aMGQIIje2DPWwqrbvbwQZn+71/SX17Iskdq01pDp6M3FeXmzfEabd2htPESKeVnpfwocShbg0arG1ZFffMYSOob1akuHOis3OARRfYdzphuTA21lXNCyXeeGvRgf2fMZMJNhIn6Dnsq2rtH/pFRukN7YeW8JjR1mR8lRvxcljqTA39MJJrqZuQ7p9SjkbTP4k26SpWCdLmxRxmuUepZWpXVk2nY7RlumuzbaORxUxB40Bk13LSRnuuMcnDkESkgOnCiFV20SAHQ/oGIwWzHFGSVi1lljfICWQ704KCFVBKVaVJjZpQX1xRH1cpcDI+2v1JTBFJA1RzQUQ6qExsSCJPnaskoOMlVjdnHIfthR8kSo52g5rUYuk1ymCu9XZ5kt3rPabN/o53Mhe4iMr8UMhxxfYVjIqEB+ySNo/9pfbJzo/iam/PkJOs2yz7JayPzHj8hNYplhwZdaEr23uBp/Shz7g/+QiTHzxrbm4ItRYSl7Vijth158STOZIK6o2zPgB02r+MoO19Yjqz/ZK9j7/vKydpVYX/N3KPsj5J1h1LEWY7vaO83kvcz1heycFyGex0Hr7uEDbaUn5UnWo8jbdVhTk3lZDeMZE4iizY9G7keDptdqWQwgL1uE+Y4Xea7VSVpSuVwRM1Hpm3kHwEq8TvsqRjtM0pU2nddmqJO9tlYyVF+otNQUWf0nDlzYNs2jhwZ2BdG7s+fP3yJe5l+KvOLO+64w/TFLd727x85E+JUpOIWlhe69AxHHkvGK+qQmywXyVYZPE0KAA/+5V/6cQ9Hpsuv9nJRKRc6/S8cJeNCBnga6UNaamt0ZGBqzEimwEiaG4Ih2S6SPRIc228K+VoLV4/y5DXY05HEgQ4H7oKzR5xNCmiGUkyzHymoif0vws/nYDWPvA5v/pk43GnhaKfG4tkjb8ri2Qrei0+Y0aSsuSN/mVKzmnGwX8aGHD4pjqxbd5tRaqT46vA7IQdbrvD7pVFIoeF40owgI7V0EBs+iKVStQjsgX1166tkZKDydL8bT7usT41+jhW7hYV2AmruwK5e/dlzms1fx7F7u+cNZ9ncaIQvkYhFxXWHI4V443Y0nxzHJXNG3oclc6I6NZv2AC2zRl63LCNRWKZsg9SkGY60Y2l7O2WAISsBLDpzSIaY3bR4xPVY0h4GZbpYc5rNqE0ojI6mBmeYFcmIYHVzgEe/Bt9yYC1aM+J67EVrEMZqTcF0U7x2hOCpFLGWrnwqVWMCoYO77A1Y5tzF8H/1CwQvPY4VTSMHZlbMCeB0H46W78iLNULBSinSWxj1KMx1m0yckUh9nWDfi9Cdx2A1Lhh5vvnLoe2oLapYEqp6hHoUdgxWYQQKGWXNXrR61GNpJUtXdLOUn5V7DudNN6bG2sos+tvf3IaoQe/dM727o0xlB3cfQs6qxvyGyqgt019Tgw2FELv2Tcyw6xP1HfZUNFRbI8bmpSB+zKr8ACxNAbHkST6XWV+GppeKihLIsMMXXHABHnrooQHpz3L/kksuGfY5Mr3//OKnP/3piPOLRCJhCqT1v5WK1IhoGmZxTfXyYYWKI0NWb1iuB/z6Iem3UpS3f4BFCvSeu1QNufiV+zJdHhfbWzXOWxoNr12086jG+iVDP8HlYvasZoWdR6Ln7m/TOHuRGjY1eG1TBurQ1t5pcnFmL1iB8MjuqIuDZM0MuvA0ahqhFqw2o0HJL/LtajbQNPSCTi4wZbQj01WjaPYiMypL2H4I+jffNyOsKLnYHGzBKhz1601w6oWDMoqSGvZiedUCIKFcINdjihY7qy+MPlgGsVdvwMGegQs4b5mC3XnI/B9uewr22sujIMyAnVCm2Ki/78V+0yxT4PVwNlre9uNJ2Oe8euiv6nKhe84VeK617wNQzgkpSFsc/nyijaddSnBww0o1bHBC9iERix6TYdbtEY67OuNlAwJTtQltRvEarKFam2LM330mOoYyDLUUSR78JVXaz4YVCsWu9k8+o7BqvhQAH7pMKZCtEdWn8nxpGyFWD3NNL+fVGQsUHimUYZFA9sXLJStk0L4o4GUrQjiFAM53n7WiIEx9v5HtZNjnTDesBSuHHova2WaUogFdcRJVptiel5VhnwGv4yhiZ7182C9GzlkvRyAZN/Iese8FqPo5sOYMDUTKCEVSHNjb/xLOWwp4Kg5r7RVDs8mcOOyzL0Mg5/gZF8M/tMeMWCSFeAczo0dJBl1uD3DiMGpiPpbPGXqRUJ/SWDJXIXwu+vzwTrSatjIkMCSFetddjkAlTUHwYOPPYS9eM2xwVEah0r70/5PhskPT5cletm7o8U3Vwlm+Hk4hiCKjWcXWXTFsm46tv2LA+SrHcbiAmDV3CVTtCAHb01Sqz0o3m8M+dw6anK4p8QNnPGZhltWBHV21CEfqw0uTJgwCbGmvRi16TPfhSiOjMzXFurArPx9uT+mDMxP5HXasYpaLi5aFw36vu2ApkExx2GwavzBe+Gwc7nP5nMvN40TTScWNyiTDZd90003493//d2zYsMEMl/2Nb3wDW7ZsMbVjbrzxRjQ3N5tUzuJw2Zdffjn+5V/+Ba997Wvx9a9/Hf/8z/98SsNll7qifToXDTG9py06tEvnKJOVUl1hIzIVeZ6HvG/h4PEQbWkbdYnQXCi6oW3qXkh9l9oUsGyOXDwq7GvT6MxGWQqL50gQRmN3mwwTDlNgt2UWTNehfUdDdOUtk7rePNs2hUr3HNOm/7EEqRY2KoShxs6jUTeGpjplhoV2A4XdR7WpxzO/XooHA0mvwxS2VV4Weu4yOI1NZuhZGYJWSR+deStMzQwp2Bse3GJqiWD+Clh1c9HhVZngUKAlm8UyacYq2wFdGNIWC1eZYaYDKcR5aEt0UBaeEQ2V23MC4aGtUMqGWnQO7KRjgjeBDPkrw2U3r0aYasDRTAx7222TwSDDWzu2jeOyOKkp48hoVQpJRyN+fDdwbDd0PAV78VpzkSLFSsPjB02hUPk1PIhXY09HCke7tBnlaak81/IRk9FopG6H/HrestYcd6ndoTpboasa4CxcadI6w8M7obuPm+2X4JUfq8K2o/He12zlXB9OkEFwaBdUuh26rsnUxPCcFLa12qbwrGSZLJol2+wjFpucX7hPtV36gTb1ZOQck7pGUnR6QUOUtTK4i5af7kHQfhiqbS90vArWojPMUNCJ1MAgQzobIO0qM2R1EMr5o9BQJaOZyTDWGhnPwsL6APPrFVxtm7YhbV+G6pasl4QdYO9xG8e6tdmOVXMVtBUV+zX1huzo9ZUv8lsPAYtmR0E9yTSriksbkHVrE6xZOEthdg0gCUzbC+1IhtdeNss3/fkPtkfttz4pmTmyzBAHOx0z/HwiFhXwrrMz5vzVh7eZLm+qeQ1Uqho6l0Fohsv2oeavgl3XACXt6+A2U7NIRjqyZjcjcJLQLz6GsK4pGo4+VQ3HSyOUzLUTrVDJajNsdCjz7X4GVvMZpp0EB47AXrIIyHQhOBQNUy9DzaOmAchnER7cBq9pFfJVTai2XVh+zsynMp3QDQtMUEmrOGyvC37rbhO2sRefA4SuWa+sX7LCzPriCYQ9nQgPFffxDASpWejxbOw+puCFCktmFYqBu2kEB1+M9nHWAuimZaaYYHB4lymKLMEXaUNeLGUuhnS2B4Gsr+cEnObVpl6R1HXpHS47WW2CXWZUtOI+VjcCXhbhga3QXh5W02JYDfOHDG0tH8WyfMnaM8eypsE8X4bNNl2U+gkzXWb7gkM7TJDVrLuqzmTUTKTT/ax88bf78WJ6AS5sakcyYU2NwrLdPn7b2YSXzWlFy8qFk7051M/BbXvwePtinFXXhtl1lXk+yXeajUcacGZiH84+f/m0G5VJ5DM55MKY+cztcS3Mqw2woNEq2485NDPk8znEvOygz+Xlhc9lZszQ9FJxgRkhQ2XffffdpoCvDHv9qU99ygyjLa644gosXboUX/7yl3vn/+Y3v4n3vOc92LNnD1atWoWPfexjuOaaayb9Q604ApOMLDVV+L4MjWyVcFpguoWUYnlSGFrO1v7LG3maHjDEs0yTi/P+r0X0+mhTzHO01ywMpVuQNWSa1spkLPTf16jOUP9pIZTSg6b5ZlsGTxs8JPXwx2S4+YY7xuNZ3tD5JsN42qUE/KwxdHL3g8AE0U5muPNnLOdtcTtkmvwtblMowyMHWt6BUcwv6x876ntblvCbliIxUZKTXLzL/yqKKcq5Jff7PdNsZ/R0Ofeswnx9A1HJc6K/apj1yfKi9crNUlLYWLaxWGxItkW2SKYUp8vCo4wfWV+xvlHvPP02L1qn3MLe7e7dLlmCdIGCrLO47kI5GTOT/BMdO0tqPsl+hhrKUghMLRkpGFOYLgWvzXZE7ba4f9K+ZXnS5s002TcJZhZeX/l/tLbRe7xkOYV5h2vPw723DPe+NJL+yx/NcO9NldYm8+kMfvRbhUa7B2csrMwfJ0by2wMyspnC1RfVwJYIO006P5fFTzblYVsK65q9k5a6mkwyUuBRrxavWdmNmrmj9GOdooGZk30PISq10T6XiaaDigzMlFslfKgR0UBsl0RTu03K14unnj6Ig/5cXDCvE4kKq7F2Mt1pD8+2N+HM1EGsPXfkekxUHnI+PfObPdgVtODcOe2oSVX2+SQj9206VIU63YHLL5oNa4T6buPFz0oioumhsj/ViIiIaEra+dIB7AsWYmmqfcoFZURtdQyLYsewJbsQh/dERaJp8oIyOzbvxs5wiTmfKj0oI6SL6uqGbrSpJmx65pDJzCMiIhpJ5X+yERER0ZSyZ+sBPNO5EPOsNiyYXfkjMY1kSZODetWFxw/Pxv4dByd7c2ak0Pfx/DN78GxmKeY77WiePXW+ujbWWlhRfRy7w8V48jeH4GWi4ulERESDTZ1PNyIiIpoS9rUr1KoerJw/8rC6U4GU7zlrQYBG1YUn2xbgV78+hOOHj/fWI6OJ4+XzJsD306e6sCW/GC3xNqycN3QEvEq3cJaF1dXHcFjPw4+eDXF454HJ3iQiIqpArKDUr/Cl9NMloolVW1s7ZJSk4bBdElVWuzyVNhnNqtHensZ0MDcJWLkAh/R8HNoLYC+QCNOoVhkkLA+OCuFYUpi6WBR7aABhisUTSmpwMcNidcNCDW4EWsEPLTO6XS5MoNuql85AEtaAUiFaYq2osXwcP44pScriLokfxQF3NrYcsVA9t2tS2iURlec7LNHpYGBGCvx1d5u/LS0tk70pRNPeWAsUsl0SVVa7PJU2+T//+xu4Tefjpdz0LUaat1LIIxVFHeTGJJoJyeWW0dr2+wsAGYRsqlNAd3sb6uubJ6VdEtH4sMg2TSSOylQY2vTQoUMlj4LKrxfyQbl///4p3Yinw35Mh32YLvsx1nY2uF1Oh33vj/tTuabTvox1f8bSLifqs/J0TbfXaaLwOE3dYzQV2mWlHrtKxmM2dY9ZpXz+0fTEjBnTh9zCokWLJmz58gYyHd54p8N+TId9mE77cTrtcrrtO/enck2nfSnF/kz0Z+Xpmm6v00ThcZqex6hS2uVUPHaTjcfs1PGY0XTG4r9ERERERERERJOEgRkiIiIiIiIioknCwMwESiQSuPPOO83fqWw67Md02IfptB+nY7rtO/enck2nfZmO+zPd96vUeJxOjsfo9PHYnToes1PHY0YzAYv/EhERERERERFNEmbMEBERERERERFNEgZmiIiIiIiIiIgmCQMzRERERERERESThIEZIiIiIiIiIqJJwsAMAKl/3NXVZf4SUWVguySqLGyTRJWH7ZKIaHpgYAZAd3c36uvrzV8iqgxsl0SVhW2SqPKwXRIRTQ8MzBARERERERERTRIGZoiIiIiIiIiIJgkDM0REREREREREk4SBGSIiIiIiIiKiSeKggjz66KO4++67sXHjRhw+fBjf+c53cO211476nEceeQS33347XnjhBbS0tOA973kP/vzP/7xs2zyduNkcVOhDKwvxqiozLch0Q+kQGgp2dZ2Zls4GCKFgQaM6ZZtpPdnAzNN/mpfpgZJRAiwbTipanp/uhoKGVjacqmr4vo8wnzfTZL5YKmWm6Xwums9Mq0IQeMjnYdbhWAESyQRc14Xt5cxyQ8sx83meD7h5GacA2o4jnowj7/lwfQtKTngVIpl04OVzsHw3eq6TQCwRLU950TQdiyMej8PPZ3vnC8x8SXi5HFTgRfPFE4jF4ghymd5pQbwKsVgM+awLX6tovQ4Qj8eQz+URhFE8NJGwYNs2vGwGKoyOn0ok4TgOsjkfvrbM8UvGtZk23GsRZHqAwjSnujY6xpl077RYdU3v6yjToCzYVdF8YbrLHCcoBauqbuA0y4KViuabanKuRqgB2wISMTXyfDkfQWEQi2RcXovh49Su50G5LqDkuMQQSyZGXGaQluKLslB5jaLjl8vmESB6Lauq4mZaJh8UzgONhK0RhhqWFRbOP2XOSVfbSFgh8kG0D47SsMM8rFgMOd8qtLcQtlJQyoIfhqZdSrtJOmHUDixl2rQs03Oq4YUWEpYLL4j2NWabtcHSPlQg8wGhHYMOQignCe0X2qGy4as4tKUQD7KwtLwH2HDtpNmvuM4Vzk1AJaqBfNosS9sx0y5kfyw/jzCWgOXlC+uJw9UxxOwAlldYjx1HNkyY1yLuF98rFJQlxy2IzmF5cc1568jGyxyF9gPoRDVsmeJ7gGmPCjqWhAo9BCoOt3gsLY1EMhaNYpLPQssxUhYg2yvP8XMy1IlpG3BkH32oRPQepr08dOCb+UJZQ+97QRXsWAyhrNvNRqdBPAlL3h8CV04E816gbRt2MmqXND7Fz5PofY3HlE5PkO0BQmnN6P1sJSIimtGBmXQ6jfXr1+Mtb3kL3vSmN510/t27d+O1r30t/vqv/xpf/epX8dBDD+Ev//IvsWDBAlx99dVl2ebpIJ/NwUq3Q+/4DcLuE1DJGgTrXwXkeuDveAY63QGVqoVevh5h3Xz8alcVurNAbUrhwuUa3VmNlw4ppHNAXUrh5cuyiHcdRLjrWehcD1RtI9Q5V0AfP4Rgz2bofAaqbjbUygsQVjVCP/19hG4WatnZ8BeehaB1F/T+FwA3BzVrITJnvgp72y3sOKLg+sCCBoWLWtJQB7fAO7AV8F1YsxcilOXlc9CbHwFCH2rt5eipX4LtrRb2HQeCEFjYYOHMRRpVgQfvqf81F1/WulchqK6H3r0Z4ZGd5pioeSsQLluLcN9L8A9uMxdo9soLEMxuRrDzGeDYXhNIwsLVsBafieDoHoQ7NgGWA2vlBeicvQrP77dxpEvBsYEVcwIsa/JxqN3BcwcU4g5w9Zk5aDeDcPtvoDuOmIu4cO1VOBGbhef3K7T3SMBAYdU8hebGAM7mR6G7jkUXiOuuADwX/s6N0IXXDMvWQdXORvDCY72vmbv8PFgN8xA881PodCdUdT3Uub8D3XkM/q7noLPdUNUNcFaeB1Q3wt/0k97XzFl5AVBdBzs1Nb6o5jyNwyeAlw5qZF2gsRpYtxiorwJiTl+AxnN99OQVNu9XONatkIgBq+YFaJmtUZWMgopFfqYHet+LCA9tA8IAmLsEasV50Iko+FYkATLd0Yqg3zHFyvORq2rCr/fEcCKtkIoDl50hwSAbzx8AjnZqc24sm6uwbK6FeE8Xgs0/RbD2KhwPk5hVC2xrVdh1DPBl1XXAOS0pxL0Aj25VZh/PWWyhuTFEZ1rjhYMKXRmgOqGwZqGNuXUpxJ7/CcIgRH715Yir6MLj2X02DpywJGaDlU0BzpzrIdz/IgI5z8MA1pwWcz54x1qhd240QQbV0ITYqosQJmoQPPMT+Jkucy7Fz/0dqFwa/vaN0F1t5ty0l5wNa+5iuE89CHvRCtjzlpoYh9Dbn4bbujtqd/OWIrlsHYKjh+Dteta0YzW7GakV5yPs6oYv7SKXhqqdZc5FXVWH4LmfQ/ecgErVwF5/JSwJuGzfiPBEKxBLwG5ZA71gJfxj7Qi3/8IEpuy1r4JXuwA7WkPsbrPM+8CChhBnNwdIpQ8heOlxs49W/VzYZ1+GsKsNgbx3SXupaYC9/FzzfoW2g1CxBPztT0ev/5KzzXtBePwgYDuwl62HmtuCYO9mBIeL+7gEzrL1Zp5g928BLw9r1nxg5YWABJGSqXI1j2nFtLcThxHslvbWA1XTCKw8D2H1LMQYoKEx8uXcSXfA31H8HK2Gls/RWQt7f8AgIiIqF6XNT4aVRyl10oyZd73rXfjBD36A559/vnfan/zJn6CjowMPPvjgmNfV1dVlhhrs7OxEXd3UuAgtFd/3EB7Zh/D5R3qnWUvXwUpWwd/y5JD55eLjYM1a/GZfHIvnAMkYsO1w3+Or53pYnX8Wan/fa+KsfxXCY/sRHtoxZHnO+ldDS7Dj5/8P9mV/guDFXwLHD/Q+Hpz1KjzVuRhtPX3ZDK9YmsWs3T8DutoGLsyyEb/4dXA3Pwr0nID/ypvx2FagJ0qq6SVZAq8+WyG+8TtA5gScS/8Y/lPfi37l7k8uvs6+FN6mn5iAS+xlb4Qn8xUyaIpUVR3s838X/i+/AThx5M77fTy0vSr6Yb+fWVUhXr5K4/vP2fjddUAqdwz+0z+IfpmXzZ+zCMeXXYVfbhtymNDcqLFu9gk4G/8XatEa2A1z4T//2NDXZ9Ga6Lgd2NK3fcvPg1q4EuEvvwnnvKtMEMhcJA5+Lc68BOGcJQgf+3rftLWvBOYtMxk75XYq7dL1NTbv09h1dOhjrzhDYWFjX2CmrTPAIy+Z39kHmF8f4sJlQCrp9AZlgo0PQmc6B87oxBC7+I2wa+rNXS+XBSSwIcGFQcLVr8DG3Eq0dlpYUA+sXazw8xe0CQ7011ClcckqC+hsxa9am8w2P7lDm4BOfxJMedXZymTYvHQIuHi5xv4TCpt2D93v1QuA1U0h3GwWT+2uxiVnavzsBQUv6JvnihUZ1G190AQhBrBjiJ37O/Ce+WkUkDIU7At/D2HNLOhH/j/Yr74R1olD8J752ZB1W/OXw151AbzHvgnVMA+xtZfBffpHQC7KpOkVTyJ2zuXwNv64b5qyEDvvSnjSjgsZceawn3M5gvp50NLOFq1BbOFKeL/paz+9626cD+fsy+D+8pvmfvDKm/DLrQpduYHH0rGA3zk7RPzJ/zJt2l73KiDThWDHxiH746y+CHr+SgTSNmJJxC94DdynfgAUsozMrrz89+HKe8WI+/iTQjZVYR83vBZ2QxOmkkr4rPSzGWgJfu3t+4wpcs56BcJ5K0x2ItFoJDMXR/bAf/4XQx6zW86EWrYOTmpqBPkqoV0SEdEMrzHzxBNP4MorrxwwTTJlZDqNjc7nEW4dGIBxFiwzvyANRzJeFtVGF0stsxW2tw58fFlDbkBQRk4xK1U3bFBG+FufguXmgJUXQ7mZAUEZxOLIJJoGBGUkEFQXdgwNyogwML/cO2ddCvtlb8TRrqFBGSEXptsOa6iLXw/rZb+P4NDOoUEZkc+YX+KtWQtgrboIvlwIDArKCJ3pQnjiCOwzL4FuPgubj6SGBGVEe8YyF4evWAWkkEWw5fEBF5Xuylfg2X3DHiYcPKHgJRqjANGi1fC3/mbY+YIDW2E1LR64fbuf623oVlWteQ2HY45d6A2ctu0pWIVuKZUs52HYoIzYtFsyaKLjLF3Entk7NCgjJHgiWShFQfuRoUEZ4Xvw92yGm4tmtv38sIEuYe18CmfNic6t85YCm/eHQ4IyoiOj0JkF/Jp5OLNZoTuHIUEZIeeVLKMqrk2mjXRz2jzCObP9MOBpGy8eS+LytR62Hw4HBGVqkkBV9ujQoIzZeQ/Boe2w5i/rN1Ej3PIErEIwwnIz8Lf8eth1h627oKRLz5xzgHOvRnBkz9CAhXBzCNsOwJrT3G81oTlH7UWrB8zqb/sNYqbzEBBfuhb+1l8PCcqYdZ9ohZZzdsOboDa8Hu09ekhQxiwvBLYcAtTql5n7dm3jsME1M+/OZ2BLdySt4ch7wc7nBgRl1MLVZj9G3Mdj+03gtf8+yv4EWen6RqfCClwE+14Y9jHJsrK9TNm3iaYelU/D3zb8+1ew/yVYhS6KRERE5TKlAzOtra2YN2/egGlyX349yGaHudAuyOfzZp7+txlL6j30+1XakF+S5KJqOFLjIZ82XTCke0X/6yLJRLFygy7y6mcj7D4+8vpzPSbY4SxZg6Dt0ICHrNrZONwz8JdP6Z4SOz5MekCBdBlQsTjCZD0Onhh5tYc7JMvCMt0fcGzPyMuT7gv1TUDdHOi2/SMv8MhOqDktCBqbcaRz5LomB9qBeQ2yYB+6u33AY76VHDaQVCTdbkw3COkLP/g166VNVzEJavVNCk2XEKQaor8jJclJ0KlQ/6OXBM0KdXcm2njaZecosSMJtkgXuOLFeMco121HOqJj40ldmUK3tuHoY/sKNUwkuJmJ2sVwAg9xXaipAnWSc0O6UgHNsyQQN/I2Hu1UCHQUXHL9gRkwA7ZRuofmNebU2vADhUOdA7tpzakOEWvbOWpbsuTc779M6UZU2G+pSSPdtkZ8fsdRqLXr4QQ5hEf3jjxf29D1hO2HYdXNGTijHOdiYFTO6c5jIy/z2H44tbWwa2dhX/vA/e7vcKcFv25+tEg513uzgwaRfZXHzftSA8L+AWQJ6sxZiGC0fZRjOSg7Rp9oNbVxKlklflZqUy9rhPcwb5j3MKKRzpVCmx5O2NOBSlWJ7ZKIiGZ4YOZ03XXXXSbts3iTosEzlmWNbdqAx+VCL+pW0Z/JErEGdXmRuhH26GnlyrKjIpxOfOAX8CBAzB74BVyKtYaD5hugsC7pCmdbI/fSM0VPlXTOUKY+xIicWHSxpjXUaPPZ8UJh0gD2yNeBiPc+Jisf2k1lNDFHjol30tfHbGehkGHvNKmHIxfRo+3D6Z4PFdAuJVA4muKxldd70GEfcozNfKbo68jnrer/2EmOjxSv7d1Oa/Rzo3i9KefnSIo1imWfTnbOOJbCiQ5ztg05Ria4M0pbMu12SOBAztvCBox2IM1OxKHlPLTs0d8DnBj04PXI+TpcsKu47v7bMey6owLNcjzjg95DBqzakv68hfWcrF0VHjf7NHh/wnD0fbRH2EfzylSuivysPNl72GjnBVHRST9HK7c7XKW1S+la+4sXQ1M3jYiITt+U/gYzf/58HDlyZMA0uS99bFOpkYsq3nHHHaYvbvG2f/8omRDTnJYRR2pnDZwmQYjCKD1DxJIInKreQIwUsS2SLhp5p3bgRYspoFlfuAgZSupPyOgswc+/Yn51HrAdXcewsGZgtkZbF+DPXTni/thSS6WrHeHe57CiaeSLnmVNQCzMIjy2B2rx2SMvb/5y82u/luKvi84acT7VcqapyeO0bsGyWX1dHAZrmQM8vkWOewyqaemAx5z0UcyrH/6LjVwDz64OoU8cMSPODH7N+jY4Fl2Y9OtmIa8Z4tIeAlO8tHjROmQdVXVDLtSlmPDggNlEGU+7rEuNHKSYXdN3nsYcjUWNI2S3SMZdQ/SWKDV11CivNxadCStROI5ybOPJYWdTVbXo9KPHtA6xdJSSIkvmKPSkQzy6BVg8e+Rzd+kcIG5p031LApe1w6/aBHdkRK/qKhdWzDGFfvtr7VTw5kU1iYZjLVgRdUHqvz9zF5uRlsz+ODHTzW9YyjIZb3j0a/BgwV585ojrsResGJJRI9OCIwOnKcmgKQTEZPyngd2sBi1zbgv8h76DYMfTWD535IuF5XMDOIdejJYv53lh5KUhpLh2od0ER/fBbl414GF/3wum8PCo+zjoWMo0PUJbrBQV+VmZrBrxPckU3XYq+5hShXDi0efbcGR0tgou/ltp7VIGKpCu4xt3RyMMEhHRDAzMXHLJJWYkpv5++tOfmumjSSQSJnjT/zZTxatSsNdePuCLrtSXMUVfB/9iJMNer7sCz7RGQa+thzXOX6YGXBD/VuqrnP3qAb+m+4d2wll72dBfh6Uo5lkvh5+O+m2EVgzWma/oe1xrxFpfxPrmvm5V8pm/t7sKetn5Q/ZFRuaQEWECKRq661nUJDSWzh26z7NrtOkuon/5APSWJ6KuSnOXDJnPmtsSDceb7TaBGVvqYDQM7DpnNK+JRkWSGhPH9mJVfTfqUkO/nJy1IEDSCtDaDWw5nIC96sLogq+4vi2PYf3iqI7OYFKU1jkcFfT1tj9tihIPuThRKjqe/YtiWjbs9a9GUOg25R3cgZiM6DQ4UGbHTHFVv3+NjFjcrEfq0pTDeNplMg68bFU0NPmAZTrAhctl5KXokUTcwdoWhaphrt3OXxIOyK7QMlx48zAX2/VNsPsVRA5leHQpHDvMMfXPfBWePxK1lx//VmHlPDXsubFmoWxriOTxLWhMekjYIc7sV3alqDalsXqBwlPPK1MnKWYpbFgZjfzVn7TJl60CYirA0upuPPpiaEYzm1vbF5SSLlCH83XDBhxV/VxYtbOi0cKKktWwV29AUOgmKiPTO2suKQT9BjzbtPdAssjk+ufQVqB2FqymYdqYtCnJJulX50ZGe5IRm8Kj/QIZsYQ5F90TUSEh/5mH4Kw4z4w8NphzxgaEJquiC9j3AqriIVYNCkoVi3EvmRWYEanM/ux9aYS24SC27nIgljLrC/f8FvaClQMv6rqOR0Njz1s6dB9nN5vulTJS2oCC4cvWwx4hoFcpKvGz0reT0es0ODPGicM555W9w9QTjUZGXXLWXjqw22/xc3TdFfBGyZicbJXWLls7tcnklK7Yh0bphktERFNoVKaenh7s2BEViT3vvPNwzz334FWvehVmzZqFxYsXm18JDh48iK985Su9w2WvXbsWf/u3f2uG2P75z3+Od7zjHWakplMZLnumV7Q39TTcHAKpp9JxCLpqFqzmFbB1aH7JluFjVXUj7PlL4drV2N3umDodDVVAyywJlihTH0OKl86qBloaQiTCNPzDu6EyJ6AbFsCZ0wwlQ9se3mmGN5WRU8wQ17GUKZyqct3Qs1tgzVoIJcVUD203xfkgowTNWohcEMPeYxpZ38KihgBzq304bg/CQ9uhZQjaeUvNhZJ0f5LCfUoKdc5fCb92AdKeZZ4rGT0tsyW7QiOVbUN4cKvJDjK/Zlc3mq4+ZlhkuZhauBp2ssoU9g0O74CSDIDmM6BlOM10J/Th7dBWLPrlPFEN1d2G4MguKDsOa9Fq5OON6EgD+09YiNuhCRClnMAUMj7QYSPlhFg9XyEWZhB2HAPa9kIna2A3n4GsXYtjXdr8AiVDLEsmRdJy4RzbaYoMy1DBqnm1iaqa0a46j0JV1cNesBxaOfCP7oPqOgJdMwf2vCXQcoF8eBt093FzjKwFy019kKB1D3T6BKy6uSYIFdgJ4MCLpuCtDLEtxUqD+MBhocvpVNulH0TDZO9r06Z47rx6hab6aPjowdLZAO3dGgc7LVTFAiyZYyHphEgMioq5mYw5D+W8MLVVFqwyv8rHqqoHzufm4bhZBEd2mzosUh9FAhE5uxpHOzRau23UxEMsnqNgWZZpP9JmJKtl6Vxl1h3PtCE8vA3B7GXIVc9HwpHivhb2tGlTI6e5MaqxpLUy03ry0bR51QFcODh0QqM9DdQlo8LcceXDad+LsP0QvEXr0KVr0ZAKTSHcvccVbKVN9k1dLA8rL+f+dujAhz1/BVDTAO0H0bkvdaBmL4bV2GTS+wNpI91t0HVNwMJViPk5UxNG1iOBC5PtIhc1e543GWyS4SXBDRVLmqHYAykELu1u4Qqgqg7KyyM4GLVjNW+5GfLYUQFCea/ody76iME6vjtqA3K+N58hffsQdh4z7UDFU7CbVyJ0EmYIXHmvkS581sKVcFOzkfUs7DkGeKHC4tka9SmNZBBtT/E9CXMWR0NwH9kD3dNu2ovdtAS+k4AT+uaiTWrbBMcPwVl8ZvT+cGS3afeybglSSR2nUPZnhH2U4tzm/KiORvWaSirls9LN5eH4WQStu0zAS4Y6lyHaJ/P9iqbmdx/bzZjC3WFH4X1l/nIEEgiWzKwpYrLb5c82h+bHAfnOc8ZCZQrYExHRFA/MPPLIIyYQM9hNN92EL3/5y/jzP/9z7Nmzx8zX/zm33XYbXnzxRSxatAjvfe97zXxT6UONiIZiuySqLGyTRJVnMtuldF3676c0Vs0HjnRGPx5sWDmlk/GJiCbNSaroldcVV1wRFYEdgQRnhnvOM888M8FbRkRERERERZKlKiTZVG6jjSxJRESjY1ibiIiIiIhOSaYQmEnEoq7X0o2YiIhODwMzRERERER0WoEZyZapisPUQ/P8iqmQQEQ0pTAwQ0REREREpySbBxwLsC1lMmYEuzMREZ0eBmaIiIiIiOiUZFxtsmVE8W+6kEVDRESnhoEZIiIiIiI6JZk8EC8EZGTIbBkoO+9N9lYREU1NDMwQEREREdEp15hJFsZ3VUoh5jAwQ0R0uhiYISIiIiKi086YEXFbAjMs/ktEdDoYmCEiIiIiojELtYYXAPFCxoxwHCDHjBkiotPCwAwREREREY2Z50d/Y/bgjJlJ2yQioimNgRkiIiIiIhqz/DCBGfk/V5hORESnhoEZIiIiIiIaM9frG42piMV/iYhOHwMzREREREQ0rowZ6crk+oDWLABMRHSqGJghIiIiIqIxkwDMkK5MzsCgDRERjR0DM0RERERENGbSZcmxAKVU77TiCE3szkREdOoYmCEiIiIiojFzfd2bIVNUzJ5hYIaI6NQxMENERERERGMm3ZX6d2PqXwjYDSZlk4iIpjQGZoiIiIiI6JRqzPQfkUlI1ybhscYMEdEpY2CGiIiIiIjGTLorDc6YkXozttVXGJiIiMaOgRkiIiIiIjqlrkyDM2aEBGu8gMNlExGdKgZmiIiIiIhozCQrZnDGTLE7E7syERGdOgZmiIiIiIhoTLTW8IO+mjL92TaL/xIRnQ4GZoiIiIiIaExCHd2G68okwRrWmCEiOnUMzBARERER0ZgUuypJod/BJFjDrkxERKeOgRkiIiIiIhoTr9BVadiMGXZlIiI6LQzMEBERERHRmBS7Kg1XY4bFf4mITg8DM0REREREVJKMmeLjREQ0dgzMEBERERHRqQVmRsiYCUK56bJvFxHRVMbADBERERERlaT4b/95iIhobBiYISIiIiKiMWfMSGaMUmrkwAy7MxERnRIGZoiIiIiIaEy8QMMepr5M/+5NxQLBREQ0hQMz9913H5YuXYpkMomLL74YTz311Kjz33vvvTjjjDOQSqXQ0tKC2267DblcrmzbS0REREQ0kzJmhlPMmPGZMUNENLUDMw888ABuv/123Hnnndi0aRPWr1+Pq6++GkePHh12/q997Wt497vfbeZ/6aWX8MUvftEs4//+3/9b9m0nIiIiIprOpH7MSIGZYt0ZdmUiIprigZl77rkHt9xyC26++WacddZZuP/++1FVVYUvfelLw87/+OOP4xWveAX+9E//1GTZvOY1r8H1119/0iwbIiIiIiI6NRJ0GakrEwMzRETTIDDjui42btyIK6+8sneaZVnm/hNPPDHsc17+8peb5xQDMbt27cIPf/hDXHPNNSOuJ5/Po6ura8CNiCYX2yVRZWGbJKo8ldAu3VEyZiylYCl2ZSIimtKBmba2NgRBgHnz5g2YLvdbW1uHfY5kynzwgx/EpZdeilgshhUrVuCKK64YtSvTXXfdhfr6+t6b1KUhosnFdklUWdgmiSpPJbRLU2NmhIwZIY8xY4aIaAoHZk7HI488gn/+53/Gv/3bv5maNN/+9rfxgx/8AB/60IdGfM4dd9yBzs7O3tv+/fvLus1ENBTbJVFlYZskqjyV0C5NV6ZRriDkMT/Q5dwkIqIpz0EFmTNnDmzbxpEjRwZMl/vz588f9jnvfe978eY3vxl/+Zd/ae6fc845SKfTeOtb34p/+qd/Ml2hBkskEuZGRJWD7ZKosrBNElWeSmiX0k1ppK5MQh5jxgwR0RTOmInH47jgggvw0EMP9U4Lw9Dcv+SSS4Z9TiaTGRJ8keCO0JrReiIiIiKiUgZmTpYxw8AMEdEUzpgRMlT2TTfdhAsvvBAbNmzAvffeazJgZJQmceONN6K5udn0sRWvf/3rzUhO5513Hi6++GLs2LHDZNHI9GKAhoiIiIiIxicINULNwAwR0bQPzFx33XU4duwY3ve+95mCv+eeey4efPDB3oLA+/btG5Ah8573vAdKKfP34MGDmDt3rgnKfOQjH5nEvSAiIiIiml6Koy05J60xU7ZNIiKaFpRmfx8z1KBUtpcianV1dZO9OUTEdklUcdgmiSpPudtlOqfxw2c11i0GGqvVsPNsb9VI54HXrKuoiglERBWN75hERERERHRSxS5KJx+VqWybREQ0LTAwQ0REREREJ+UPCsxI4r2/93mEXcd75+GoTEREp46BGSIiIiIiOilvUI2Z8PhBhEf3wd/+G+hst5nGjBkiojIW/33Tm9405nm//e1vn+5qiIiIiIioAvgheoMvGhrBoe1QNQ3QuTSCtoNwWtbAsWFGbpIRnGxr+Do0RERUosCMFBojIiIiIqIZWGMmlwXyWaimJUDnMeju4wO6OUnWzGi1aIiIqASBmf/4j/843acSEREREdEUUwy2KKUQZjrMNJWsBrw8wiN7oAMftmX3BnESsUneYCKiKYJxbCIiIiIiOqn+WTBhTwcQT0DZDlRVnVQChu5p760/wzozRERlyJgZ7Fvf+ha+8Y1vYN++fXBdd8BjmzZtKtVqiIiIiIhoEniB7g286HQHVLImuhNLArYDnemGnZxbmHcSN5SIaCZmzHzqU5/CzTffjHnz5uGZZ57Bhg0bMHv2bOzatQu/93u/V4pVEBERERFRBWTMSOFfnemKujFJdyYFqHjSFAHuX2OGiIjKGJj5t3/7N3zuc5/Dpz/9acTjcfzjP/4jfvrTn+Id73gHOjs7S7EKIiIiIiKaRJIFYwIvbh4IQyCe6nswloDO9fQFZgojOBERUZkCM9J96eUvf7n5P5VKobu72/z/5je/Gf/1X/9VilUQEREREVElBGbyaXNfxRK9j6l4ihkzRESTGZiZP38+2tvbzf+LFy/Gk08+af7fvXs3tNalWAUREREREVVAV6Ywn40m9AvMIJ4EfA8IfFiKNWaIiMoemHn1q1+N7373u+Z/qTVz22234aqrrsJ1112H3//93y/FKoiIiIiIqAIyZnQ+A8TiUFbfpYTUmDFyaTg2M2aIiMo+KpPUlwmlnymAv/3bvzWFfx9//HG84Q1vwF/91V+VYhVERERERDSJJNgiQRdkMwO6MRmFwIzOS52ZeviBZM2rydlQIqKZGJixLMvciv7kT/7E3IiIiIiIaHqQgr62KmbMDAzMKMuOhszO50xWDYv/EhGVOTAjOjo68NRTT+Ho0aO92TNFN954Y6lWQ0REREREkzlcdi4Nq2HekMdVLA7tFQIz7MpERFTewMz3vvc93HDDDejp6UFdXR2U6ktblP8ZmCEiIiIimrpkQI8gBCwVRkV+Y/GhMzlxQDJmUiz+S0RU9uK//+f//B+85S1vMYEZyZw5ceJE7604WhMREREREU1Nxa5Jtvb7gjCDKEcyZrKmuxMzZoiIyhyYOXjwIN7xjnegqqqqFIsjIiIiIqIKUgy02GG+NwgzhARmXHZlIiKalMDM1VdfjaeffroUiyIiIiIiogpTDLRYgRv9M1xXJpnme7AtDY/Ff4mIyltj5rWvfS3e+c534sUXX8Q555yDWCw24HEZNpuIiIiIiKZ4VyY/J0OyAkrGzR6kkEUj3Z38YOD1ABERTXBg5pZbbjF/P/jBDw55TIr/BgFzGYmIiIiIpnzGjARmnDj6jfUxYFQmYWuPgRkionIHZgYPj01ERERERNMxMJOFckYIujiJaJ7AhR9WmZGc+o/WSkREE1hjhoiIiIiIZkDxXy8z7IhMQkkXJ9uGHXrQGgh1ebeRiGhGZ8x86lOfGna6RMiTySRWrlyJV77ylbDtYfqiEhERERHRlKgxo7wsVHX9yDPaMVih2xvMkRGaiIioDIGZf/3Xf8WxY8eQyWTQ2Nhopp04ccIMn11TU4OjR49i+fLlePjhh9HS0lKKVRIRERERUZl4hSCL8qTGzNwR51N2DHaQ6w3MJFhqhojopEoSw/7nf/5nXHTRRdi+fTuOHz9ubtu2bcPFF1+MT37yk9i3bx/mz5+P2267rRSrIyIiIiKiMjLZL0r6J4XASDVmhBOLCgT3y7IhIqIyZMy85z3vwX//939jxYoVvdOk+9LHP/5x/MEf/AF27dqFj33sY+Z/IiIiIiKaWvxAR4EZYY8cmJHCwHYuD9h9dWmIiKgMGTOHDx+G7/tDpsu01tZW8//ChQvR3d1ditUREREREVEZSfaLraIUmBFHZSrWmPGyvd2fiIioTIGZV73qVfirv/orPPPMM73T5P+/+Zu/watf/Wpzf/PmzVi2bNmYlnffffdh6dKlpnCwdId66qmnRp2/o6MDf/u3f4sFCxYgkUhg9erV+OEPfzjOvSIiIiIiIiHZLxbCk2bMmMAMuzIREZU/MPPFL34Rs2bNwgUXXGACI3K78MILzTR5TEgR4E984hMnXdYDDzyA22+/HXfeeSc2bdqE9evX4+qrrzYFhIfjui6uuuoq7NmzB9/61rewdetWfP7zn0dzc3Mpdo2IiIiIaMYzNWZQHDN7lGoI0pUJXu9ziIioTDVmpLDvT3/6U2zZssUU/RVnnHGGufXPqhmLe+65B7fccgtuvvlmc//+++/HD37wA3zpS1/Cu9/97iHzy/T29nY8/vjjiMWi6L1k2xARERERUQlHZdK+CbwohdGL/0JDQcMPRpuRiIhKmjFTtGbNGrzhDW8wt/5BmbGS7JeNGzfiyiuv7NtAyzL3n3jiiWGf893vfheXXHKJ6co0b948rF271owSFQQM0RMRERERlawrk/ZHry/Tr/6MbUlgpkwbR0Q0UzNmpLvRhz70IVRXV5v/T5YFMxZtbW0moCIBlv7kvmTjDEdGfPr5z3+OG264wdSV2bFjB972trfB8zzTHWo4+Xze3Iq6urrGtH1ENHHYLokqC9skUeWZzHYp9WISkjEzWjemfvVnbITwQ/kNmFkzREQTFpiR4r4S/Cj+PxI1aq7j+IVhiKamJnzuc5+Dbdumzs3Bgwdx9913jxiYueuuu/CBD3xgQreLiE4N2yVRZWGbJKo8k9kuTcZM6I5e+Fe++1sWYNlmBCdmzBARjY3SWmtUCOnKVFVVZYr4Xnvttb3Tb7rpJjPy0v/+7/8Oec7ll19uasv87Gc/6532ox/9CNdcc435RSEej4/p14aWlhZ0dnairq5uQvaNiEbHdklUWdgmiSrPZLbL/306xPz8brQkO2DNWzLqvP6uZ/F88hLMmZPChctLWjmBiGhampB3SvmQ+J//+Z8Rux+NRIIokvHy0EMPDciIkftSR2Y4r3jFK0z3JZmvSAoQy9DZwwVlhIwaJR9e/W9ENLnYLokqC9skUeWZzHZpMmaCvCnuezLKdmAhYMYMEVE5AzN//Md/jM985jPm/2w2a4bKlmnnnHMO/vu///uUliX1amS46//8z//ESy+9hL/5m79BOp3uHaXpxhtvxB133NE7vzwuozL93d/9nQnIyAhOUvxXigETEREREdH4hKFGqAF7DF2ZDDtmRnCSkZyIiKhMw2U/+uij+Kd/+ifz/3e+8x1I7yjpeiTBlQ9/+MP4gz/4gzEv67rrrsOxY8fwvve9D62trTj33HPx4IMP9hYE3rdvnxmpqUjSN3/84x/jtttuw7p169Dc3GyCNO9617tKsWtERERERDOaFP4VtpYxs8dw+WA5sEKPGTNEROUMzEi/1lmzZpn/JYgigRipFfPa174W73znO095ebfeequ5DeeRRx4ZMk26OT355JOnseVERERERDSaYoDFhj/Grkwx2L6HPAMzRETl68okWStPPPGE6XIkgZnXvOY1ZvqJEyeQTCZLsQoiIiIiIprEjBlL+6Z+zEk5DqzA7X0eERGVIWPm7//+73HDDTegpqYGS5YswRVXXNHbxUnqzBARERER0VTPmAnGXmOGXZmIiMobmHnb296Giy++2NR/ueqqq3prwCxfvtzUmCEiIiIioikemJEaM5Z98ifYDmy48AM94dtGRDQdlCQwI2SYa7n1JzVm+pMh/Z599lkTsCEiIiIioikUmLEBpcbwBEdGZcqarkwyKIga05OIiGauktSYGSt5YyYiIiIioik4KpM9tksHqUNjSbcnKDPMNhERVVBghoiIiIiIphbPZMxoWPYYM1+kxoz2+z2XiIhGw8AMERERERGN2pVJCv/KMNhjYtlRoeB+3aCIiGhkDMwQEREREdGoXZmk8O+YhsqWDkwKKPZ6YmCGiKjCAjMs/EVERERENLXI6Eo2/LENlV1gW9H3fgZmiIhOjsV/iYiIiIhoRBJcsUIJzIx9QFfb1gMKBxMRUZkDM0EQmGGxT5w4MWD6j370IzQ3N0/EKomIiIiIaAL4fjFjxjnljBkW/yUiKlNg5u///u/xxS9+sTcoc/nll+P8889HS0sLHnnkkd75Lr30UiQSiVKskoiIiIiIysDzQ1g6AJxT6MpUKDLDrkxERGUKzHzrW9/C+vXrzf/f+973sHv3bmzZsgW33XYb/umf/qkUqyAiIiIiokng+2E0/LVlj/k5lm2bYA4DM0REZQrMtLW1Yf78+eb/H/7wh/ijP/ojrF69Gm95y1uwefPmUqyCiIiIiIgmgWeK/57CcNnCiZnuT6wxQ0RUpsDMvHnz8OKLL5puTA8++CCuuuoqMz2TycC2xx5ZJyIiIiKiyuIHKsqYOYUaMzKvPEe6QRER0ehO4d11ZDfffDP++I//GAsWLDBDYl955ZVm+q9//WusWbOmFKsgIiIiIqJJILEVyZg5la5MEpgxXZlM9V/+UEtENOGBmfe///1Yu3Yt9u/fb7oxFQv8SrbMu9/97lKsgoiIiIiIJoGvLdgqhIoGWhobu9CViRkzRETlCcyIP/zDPzR/c7lc77SbbrqpVIsnIiIiIqIy01pHgZlTLICgChkz7MpERFSmGjNSW+ZDH/oQmpubUVNTg127dpnp733ve3uH0SYiIiIioqklMHEVBVvpU3ui1JhBAN8/xecREc1AJQnMfOQjH8GXv/xlfOxjH0M8Hu+dLt2bvvCFL5RiFUREREREVGbF4a5PNWMGVlT8l8NlExGVKTDzla98BZ/73Odwww03DBiFaf369diyZUspVkFERERERGVW7Il0yl2ZFExdGo89mYiIyhOYOXjwIFauXDlkehiG8DyvFKsgIiIiIqKpkjEjz1EafliSyw0iommtJO+UZ511Fh577LEh07/1rW/hvPPOK8UqiIiIiIiozMxo12a0Veu0AjOBZmCGiKgsozK9733vMyMwSeaMZMl8+9vfxtatW00Xp+9///ulWAUREREREZWZVyjee1qBGUvDR1+ZAyIiGl5JQthvfOMb8b3vfQ8/+9nPUF1dbQI1L730kpl21VVXlWIVRERERERUZr4blSWwHXVaGTMhLIQhR2YiIprwjBlx2WWX4ac//WmpFkdERERERJPMM4GZ2IABPsbKthQQRAWE4+zRREQ0opK8RS5fvhzHjx8fMr2jo8M8RkREREREU4/vBbC0D8s59d9zi72fOGQ2EVEZAjN79uxBEAx9x83n86buDBERERERTT2eF8DWvvRlOuXn2nbU/ckt1KkhIqIJ6Mr03e9+t/f/H//4x6ivr++9L4Gahx56CEuXLh3PKoiIiIiIaJL4fggbpxeYcQopM37eB6rjE7B1RETTw7gCM9dee635q5QyozL1F4vFTFDmE5/4xCkv97777sPdd9+N1tZWrF+/Hp/+9KexYcOGkz7v61//Oq6//npTjPh//ud/Tnm9RERERETUxw80bATm+/6pKhYMdl0XAAMzREQT0pVJhsaW2+LFi3H06NHe+3KTbkwyZPbrXve6U1rmAw88gNtvvx133nknNm3aZAIzV199tVn+ybpT/cM//IMpQkxEREREROPnBYCN8LSe6xQKBhdHdiIiogmsMbN7927MmTPH/J/L5ca1rHvuuQe33HILbr75Zpx11lm4//77UVVVhS996UsjPke6Td1www34wAc+wGLDREREREQlIoV7rdMMzNiO1VunhoiIJjgwIxkyH/rQh9Dc3Iyamhrs2rXLTH/ve9+LL37xi2NejqQ5bty4EVdeeWXfBlqWuf/EE0+M+LwPfvCDaGpqwl/8xV+Mc0+IiIiIiKjIDxUc6/SK9yonZkZ08r3TC+wQEc0UJQnMfPjDH8aXv/xlfOxjH0M83td/dO3atfjCF74w5uW0tbWZ7Jd58+YNmC73pd7McH75y1+a4M/nP//5Ma9Hull1dXUNuBHR5GK7JKosbJNElWcy2qWnrdPuyqQsZerTeBwvm4ho4gMzX/nKV/C5z33OdCeyC31JhdSH2bJlCyZKd3c33vzmN5ugTLEr1VjcddddZgSp4q2lpWXCtpGIxobtkqiysE0SVZ7JaJe+tmGfZsaMsHUAn8NlExFNfGDm4MGDWLly5bBdnDxv7MW+JLgigZ0jR44MmC7358+fP2T+nTt3mqK/r3/96+E4jrlJkEiG8Zb/5fHh3HHHHejs7Oy97d+/f8zbSEQTg+2SqLKwTRJVnslol752UBj1+rTYKjAFhImIaIKGyy6SIr2PPfYYlixZMmD6t771LZx33nljXo50g7rgggvw0EMP9Q7FLcEduX/rrbcOmX/NmjXYvHnzgGnvec97TCbNJz/5yRF/RUgkEuZGRJWD7ZKosrBNElWecrdLrTV85Zx2jRkh3aDYk4mIqAyBmfe973246aabTOaMBFK+/e1vm6GyJXvl+9///iktS4bKlmVdeOGF2LBhA+69916k02kzSpO48cYbTZFhSeVMJpOmjk1/DQ0N5u/g6URERERENHbacxGoGGxLnfYybBWaAsJERDTBgZk3vvGN+N73vmdGR6qurjaBmvPPP99Mu+qqq05pWddddx2OHTtmliEFf88991w8+OCDvQWB9+3bZ0ZqIiIiIiKiiePl8wBi6FdC8pTZSsML+N2diGg0SkuO4gwnFe2lgJr01a2rq5vszSEitkuiisM2STTz2mXPsTb8aOcsnF13DLPqTi86s+2wRs5TeM3Lxz5QBxHRTFOSjJmip59+Gi+99FJv3RmpF0NERERERFOP50aDeNjjqP4rIzr5Ombq1SjFLk1ERBMWmDlw4ACuv/56/OpXv+qt8dLR0YGXv/zl+PrXv45FixaVYjVERERERFQmXr4QmHEkMHN6SfZSn0YKCCPwACde4i0kIpoeStLh8y//8i/NsNiSLdPe3m5u8r8UApbHiIiIiIhoavE83/x17NPPdJGYjq9i0J7UqyEiognLmPnFL36Bxx9/HGeccUbvNPn/05/+NC677LJSrIKIiIiIiMrI80Lzd1zDZdvKjOyk811AqraEW0dENH2UJGOmpaXFZMwMFgQBFi5cWIpVEBERERFRGfl+2Duy0ukqZtu4ebdk20VENN2UJDBz99134+1vf7sp/lsk///d3/0dPv7xj5diFUREREREVEaer2HpAOOp2VssHOwX6tUQEVEJuzI1NjYOqKyeTqdx8cUXw3GiRfq+b/5/y1vegmuvvfZ0V0NERERERJPACzQcFYxrGU5hlG3XjerVEBFRCQMz99577+k+lYiIiIiIKpwfKNjWOAMzhfo0DMwQEU1AYOamm2463acSEREREVGF80IF2z79+jLCLgRmfG98AR4ioumsJKMy9ZfL5eC6A4t71dXVlXo1REREREQ0QbTW8LU9rsK/wik83ysUEiYiogkq/iv1ZW699VY0NTWhurra1J/pfyMiIiIioinEd+Eh1pvxcrosU5JSgz2ZiIgmODDzj//4j/j5z3+Oz372s0gkEvjCF76AD3zgA2ao7K985SulWAUREREREZWJdvPwVay3RszpkrFCHATwGZghIprYrkzf+973TADmiiuuwM0334zLLrsMK1euxJIlS/DVr34VN9xwQylWQ0RERERE5eBl4akEUiX4GddWATz2ZCIimtiMmfb2dixfvry3nozcF5deeike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",
      "text/plain": [
       "<Figure size 1131.99x1000 with 20 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Select a few numerical columns to avoid clutter\n",
    "selected_cols = ['age', 'Systolic', 'Family_History', 'diabetes_signal', 'Heart Attack Risk']\n",
    "\n",
    "# Draw pair plot\n",
    "sns.pairplot(hearGardaData[selected_cols], hue='Heart Attack Risk', palette='coolwarm')\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "id": "f9707c5d-40b9-45f9-b8e2-31feaeb08598",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 800x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "plt.figure(figsize=(8, 8))  # Increase size for clarity\n",
    "\n",
    "corr_matrix = hearGardaData.corr(numeric_only=True)\n",
    "\n",
    "sns.heatmap(corr_matrix,\n",
    "            annot=True,\n",
    "            fmt=\".2f\",\n",
    "            cmap=\"coolwarm\",\n",
    "            linewidths=0.5,\n",
    "            square=True,\n",
    "            cbar_kws={\"shrink\": 0.7},\n",
    "            annot_kws={\"size\": 8})\n",
    "\n",
    "plt.title(\"Correlation Heatmap\", fontsize=16)\n",
    "plt.xticks(rotation=45, ha='right', fontsize=8)\n",
    "plt.yticks(rotation=0, fontsize=8)\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "id": "b4d7bbc1-9148-43eb-9f70-683f116c8923",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['age', 'gender', 'height', 'weight', 'Systolic', 'Diastolic',\n",
       "       'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'BMI',\n",
       "       'diabetes_signal', 'Family_History', 'Heart Attack Risk',\n",
       "       'gender_label'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 275,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "id": "945ffe28-a986-484d-8b66-bb2ddd2e6339",
   "metadata": {},
   "outputs": [],
   "source": [
    "hearGardaData.drop(columns=['gender_label'],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 277,
   "id": "2c57fc9e-1e49-48ad-9677-47e15c708685",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 69904 entries, 0 to 69999\n",
      "Data columns (total 15 columns):\n",
      " #   Column             Non-Null Count  Dtype  \n",
      "---  ------             --------------  -----  \n",
      " 0   age                69904 non-null  int64  \n",
      " 1   gender             69904 non-null  int64  \n",
      " 2   height             69904 non-null  int64  \n",
      " 3   weight             69904 non-null  float64\n",
      " 4   Systolic           69904 non-null  int64  \n",
      " 5   Diastolic          69904 non-null  int64  \n",
      " 6   cholesterol        69904 non-null  int64  \n",
      " 7   gluc               69904 non-null  int64  \n",
      " 8   smoke              69904 non-null  int64  \n",
      " 9   alco               69904 non-null  int64  \n",
      " 10  active             69904 non-null  int64  \n",
      " 11  BMI                69904 non-null  float64\n",
      " 12  diabetes_signal    69904 non-null  int64  \n",
      " 13  Family_History     69904 non-null  int64  \n",
      " 14  Heart Attack Risk  69904 non-null  int64  \n",
      "dtypes: float64(2), int64(13)\n",
      "memory usage: 8.5 MB\n"
     ]
    }
   ],
   "source": [
    "hearGardaData.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c55b19a-1144-462a-984e-e570b8bf5411",
   "metadata": {},
   "source": [
    "# 🧪 Model Training and Evaluation\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 278,
   "id": "a1fd0030-f5c8-424b-94a4-17d122906d37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Heart Attack Risk\n",
       "0    34971\n",
       "1    34933\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 278,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData['Heart Attack Risk'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "id": "42cc91d3-4c28-4a87-a37d-28dcd9a9529c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(69904, 15)"
      ]
     },
     "execution_count": 279,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hearGardaData.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 280,
   "id": "e895c220-8b68-4d76-913f-71fbe38181ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# Define features and target\n",
    "X = hearGardaData.drop(['Heart Attack Risk'], axis=1)\n",
    "y = hearGardaData['Heart Attack Risk']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "id": "71af26a5-80b6-43c0-bb92-5b5cfae36269",
   "metadata": {},
   "outputs": [],
   "source": [
    "from imblearn.over_sampling import SMOTE\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# تقسيم البيانات أولاً\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 282,
   "id": "1372064d-0722-454d-9859-00cd29c89544",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-3 {\n",
       "  /* Definition of color scheme common for light and dark mode */\n",
       "  --sklearn-color-text: #000;\n",
       "  --sklearn-color-text-muted: #666;\n",
       "  --sklearn-color-line: gray;\n",
       "  /* Definition of color scheme for unfitted estimators */\n",
       "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
       "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
       "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
       "  --sklearn-color-unfitted-level-3: chocolate;\n",
       "  /* Definition of color scheme for fitted estimators */\n",
       "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
       "  --sklearn-color-fitted-level-1: #d4ebff;\n",
       "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
       "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
       "\n",
       "  /* Specific color for light theme */\n",
       "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
       "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-icon: #696969;\n",
       "\n",
       "  @media (prefers-color-scheme: dark) {\n",
       "    /* Redefinition of color scheme for dark theme */\n",
       "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
       "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-icon: #878787;\n",
       "  }\n",
       "}\n",
       "\n",
       "#sk-container-id-3 {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 pre {\n",
       "  padding: 0;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 input.sk-hidden--visually {\n",
       "  border: 0;\n",
       "  clip: rect(1px 1px 1px 1px);\n",
       "  clip: rect(1px, 1px, 1px, 1px);\n",
       "  height: 1px;\n",
       "  margin: -1px;\n",
       "  overflow: hidden;\n",
       "  padding: 0;\n",
       "  position: absolute;\n",
       "  width: 1px;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-dashed-wrapped {\n",
       "  border: 1px dashed var(--sklearn-color-line);\n",
       "  margin: 0 0.4em 0.5em 0.4em;\n",
       "  box-sizing: border-box;\n",
       "  padding-bottom: 0.4em;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-container {\n",
       "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
       "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
       "     so we also need the `!important` here to be able to override the\n",
       "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
       "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
       "  display: inline-block !important;\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-text-repr-fallback {\n",
       "  display: none;\n",
       "}\n",
       "\n",
       "div.sk-parallel-item,\n",
       "div.sk-serial,\n",
       "div.sk-item {\n",
       "  /* draw centered vertical line to link estimators */\n",
       "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
       "  background-size: 2px 100%;\n",
       "  background-repeat: no-repeat;\n",
       "  background-position: center center;\n",
       "}\n",
       "\n",
       "/* Parallel-specific style estimator block */\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item::after {\n",
       "  content: \"\";\n",
       "  width: 100%;\n",
       "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
       "  flex-grow: 1;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel {\n",
       "  display: flex;\n",
       "  align-items: stretch;\n",
       "  justify-content: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item:first-child::after {\n",
       "  align-self: flex-end;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item:last-child::after {\n",
       "  align-self: flex-start;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-parallel-item:only-child::after {\n",
       "  width: 0;\n",
       "}\n",
       "\n",
       "/* Serial-specific style estimator block */\n",
       "\n",
       "#sk-container-id-3 div.sk-serial {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "  align-items: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  padding-right: 1em;\n",
       "  padding-left: 1em;\n",
       "}\n",
       "\n",
       "\n",
       "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
       "clickable and can be expanded/collapsed.\n",
       "- Pipeline and ColumnTransformer use this feature and define the default style\n",
       "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
       "*/\n",
       "\n",
       "/* Pipeline and ColumnTransformer style (default) */\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable {\n",
       "  /* Default theme specific background. It is overwritten whether we have a\n",
       "  specific estimator or a Pipeline/ColumnTransformer */\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "/* Toggleable label */\n",
       "#sk-container-id-3 label.sk-toggleable__label {\n",
       "  cursor: pointer;\n",
       "  display: flex;\n",
       "  width: 100%;\n",
       "  margin-bottom: 0;\n",
       "  padding: 0.5em;\n",
       "  box-sizing: border-box;\n",
       "  text-align: center;\n",
       "  align-items: start;\n",
       "  justify-content: space-between;\n",
       "  gap: 0.5em;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 label.sk-toggleable__label .caption {\n",
       "  font-size: 0.6rem;\n",
       "  font-weight: lighter;\n",
       "  color: var(--sklearn-color-text-muted);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 label.sk-toggleable__label-arrow:before {\n",
       "  /* Arrow on the left of the label */\n",
       "  content: \"▸\";\n",
       "  float: left;\n",
       "  margin-right: 0.25em;\n",
       "  color: var(--sklearn-color-icon);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "/* Toggleable content - dropdown */\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable__content {\n",
       "  max-height: 0;\n",
       "  max-width: 0;\n",
       "  overflow: hidden;\n",
       "  text-align: left;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable__content.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable__content pre {\n",
       "  margin: 0.2em;\n",
       "  border-radius: 0.25em;\n",
       "  color: var(--sklearn-color-text);\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-toggleable__content.fitted pre {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
       "  /* Expand drop-down */\n",
       "  max-height: 200px;\n",
       "  max-width: 100%;\n",
       "  overflow: auto;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
       "  content: \"▾\";\n",
       "}\n",
       "\n",
       "/* Pipeline/ColumnTransformer-specific style */\n",
       "\n",
       "#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator-specific style */\n",
       "\n",
       "/* Colorize estimator box */\n",
       "#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-label label.sk-toggleable__label,\n",
       "#sk-container-id-3 div.sk-label label {\n",
       "  /* The background is the default theme color */\n",
       "  color: var(--sklearn-color-text-on-default-background);\n",
       "}\n",
       "\n",
       "/* On hover, darken the color of the background */\n",
       "#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "/* Label box, darken color on hover, fitted */\n",
       "#sk-container-id-3 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator label */\n",
       "\n",
       "#sk-container-id-3 div.sk-label label {\n",
       "  font-family: monospace;\n",
       "  font-weight: bold;\n",
       "  display: inline-block;\n",
       "  line-height: 1.2em;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-label-container {\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "/* Estimator-specific */\n",
       "#sk-container-id-3 div.sk-estimator {\n",
       "  font-family: monospace;\n",
       "  border: 1px dotted var(--sklearn-color-border-box);\n",
       "  border-radius: 0.25em;\n",
       "  box-sizing: border-box;\n",
       "  margin-bottom: 0.5em;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-estimator.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "/* on hover */\n",
       "#sk-container-id-3 div.sk-estimator:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-3 div.sk-estimator.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
       "\n",
       "/* Common style for \"i\" and \"?\" */\n",
       "\n",
       ".sk-estimator-doc-link,\n",
       "a:link.sk-estimator-doc-link,\n",
       "a:visited.sk-estimator-doc-link {\n",
       "  float: right;\n",
       "  font-size: smaller;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1em;\n",
       "  height: 1em;\n",
       "  width: 1em;\n",
       "  text-decoration: none !important;\n",
       "  margin-left: 0.5em;\n",
       "  text-align: center;\n",
       "  /* unfitted */\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted,\n",
       "a:link.sk-estimator-doc-link.fitted,\n",
       "a:visited.sk-estimator-doc-link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "/* Span, style for the box shown on hovering the info icon */\n",
       ".sk-estimator-doc-link span {\n",
       "  display: none;\n",
       "  z-index: 9999;\n",
       "  position: relative;\n",
       "  font-weight: normal;\n",
       "  right: .2ex;\n",
       "  padding: .5ex;\n",
       "  margin: .5ex;\n",
       "  width: min-content;\n",
       "  min-width: 20ex;\n",
       "  max-width: 50ex;\n",
       "  color: var(--sklearn-color-text);\n",
       "  box-shadow: 2pt 2pt 4pt #999;\n",
       "  /* unfitted */\n",
       "  background: var(--sklearn-color-unfitted-level-0);\n",
       "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted span {\n",
       "  /* fitted */\n",
       "  background: var(--sklearn-color-fitted-level-0);\n",
       "  border: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link:hover span {\n",
       "  display: block;\n",
       "}\n",
       "\n",
       "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
       "\n",
       "#sk-container-id-3 a.estimator_doc_link {\n",
       "  float: right;\n",
       "  font-size: 1rem;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1rem;\n",
       "  height: 1rem;\n",
       "  width: 1rem;\n",
       "  text-decoration: none;\n",
       "  /* unfitted */\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 a.estimator_doc_link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "#sk-container-id-3 a.estimator_doc_link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "#sk-container-id-3 a.estimator_doc_link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier(random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" checked><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow\"><div><div>RandomForestClassifier</div></div><div><a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.RandomForestClassifier.html\">?<span>Documentation for RandomForestClassifier</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></div></label><div class=\"sk-toggleable__content fitted\"><pre>RandomForestClassifier(random_state=42)</pre></div> </div></div></div></div>"
      ],
      "text/plain": [
       "RandomForestClassifier(random_state=42)"
      ]
     },
     "execution_count": 282,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "#for\n",
    "rf = RandomForestClassifier(n_estimators=100, random_state=42)\n",
    "rf.fit(X_train, y_train)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 283,
   "id": "c19e7b81-128a-41e7-8a2a-44cd170ce29c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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P6/12aTq9OnT5pf0NGnSmL879RmC/fr1i9fPa4ype92yZUsToPR8WbNmNa81GAXH5zr6fob8/vvvZn3I3/US8uc6Mvc5Z86cYd5n/QfbhPC7tYf+x3aVFgAAAACQ8DCGFAAAAABgBYEUAAAAAGAFgRQAAAAAYAWBFAAAAABgBYEUAAAAAGAFgRQAAAAAYAWBFAAAAABgBYEUAAAAAGAFgRQAAAAAYAWBFACAGNS+fXtp0qSJPKtOnjwpHh4esnv3bokL/v77b3nzzTclR44c4u3tLZkyZZI6derIpk2bbDcNABAFXlE5CAAAxH337t2TuKZZs2am3TNnzpQ8efLIpUuXZNWqVXL16tUYu6ZeL0mSJDF2fgBIyKiQAgAQi6pXry49evSQ3r17S+rUqSVjxowydepUuX37tnTo0EFSpkwp+fLlk6VLl7qOWbt2rali/vrrr1KiRAlJmjSpPP/887J//363c//0009StGhRUznMlSuXTJgwwW27rhs+fLj4+/uLr6+vdO3aVXLnzm22lSpVylxD26e2b98utWvXlnTp0omfn59Uq1ZNdu7c6XY+3f+bb76Rpk2bSrJkySR//vyyZMkSt30OHDggDRs2NNfT91alShU5duyYa7seX7hwYfOeChUqJF988UW49+7GjRuyYcMGGTNmjLz44ouSM2dOKV++vAwcOFBefvllt/3eeOMNc2/1vMWKFZNffvnlqe6T2rhxo2m/j4+PZM+eXXr27Gn+3AAAUUcgBQAglml1T4Petm3bTDjVLqjNmzeXSpUqmdD30ksvyeuvvy537txxO65fv34mPGlYTJ8+vTRq1Eju379vtgUEBEiLFi2kVatWsm/fPhkyZIh88MEHMmPGDLdzjB8/XkqWLCm7du0y27UNauXKlXLhwgVZuHCheX3r1i1p166dCWF//PGHCZv169c364MbOnSoue7evXvN9rZt28q1a9fMtnPnzknVqlVN8Fu9erVpY8eOHeXBgwdm++zZs+XDDz+Ujz76SA4dOiQjR440bdL7E5YUKVKYZfHixXL37t0w93n06JHUq1fPdOH9/vvv5eDBgzJ69Gjx9PR8qvukIbpu3bqmQqvvdd68eebedO/ePRJ/8gCAUBwAACDGtGvXztG4cWPX62rVqjleeOEF1+sHDx44kidP7nj99ddd6y5cuODQv6K3bNliXq9Zs8a8njt3rmufq1evOnx8fBzz5s0zr9u0aeOoXbu227X79evnKFKkiOt1zpw5HU2aNHHb58SJE+bcu3bteuz7ePjwoSNlypSO//73v651etygQYNcr4OCgsy6pUuXmtcDBw505M6d23Hv3r0wz5k3b17HDz/84LZu+PDhjooVK4bbjgULFjhSp07tSJo0qaNSpUrmGnv27HFt//333x2JEiVyHD58OMzjo3qfOnXq5Ojatavbug0bNphr/fPPP+G2FwDweFRIAQCIZdrt1kkrd2nTppXixYu71mlXU3X58mW34ypWrOj6Pk2aNFKwYEFTWVT6tXLlym776+sjR47Iw4cPXevKli0boTbq2MwuXbqYyqh22dWuq0FBQXL69Olw30vy5MnNfs5260RJ2sU1ceLEoc6vXV216tipUydX5VOXESNGuHXpDUkrlOfPnzddg7Viqd2ZS5cu7apw6jWzZcsmBQoUCPP4qN6nPXv2mGsEb6tOpqQV2RMnTjzhbgIAwsOkRgAAxLKQAU3HYgZfp6+Vhp3opqExIrS7rk4U9Mknn5ixmtrtVgNxyImQwnovznbrWMvwaLhVOn62QoUKbtuc3WvDo+NCdXyrLtqdtnPnzjJ48GAzo/Hjrvk090nbq+NSddxoSDrjLwAgagikAADEETqW0xl+rl+/Ln/99ZeZEEjp15CPPtHXWil8XMBzzh4bvDroPFYnGNJxoerMmTNy5cqVSLVXq6c6HlTHuYYMrloFzpIlixw/ftyMO30aRYoUMeNKndc8e/asuTdhVUmjep+0CqvjUXXCKQBA9KHLLgAAccSwYcPMI050dl2tBurESM5nnPbp08ds09lhNYxpEJw8ebL07dv3sefMkCGDqSouW7bMdNO9efOmWa9ddWfNmmW6uG7dutWExshWH3XCn8DAQDOB0I4dO0y3WD3n4cOHXRMijRo1Sj799FPTZp1kaPr06TJx4sQwz6cV2xo1apjJinRiIe0qO3/+fBk7dqw0btzY7KOzAetEStq1d8WKFWYfnbFY39/T3KcBAwbI5s2bzXvSbsH6Xn7++WcmNQKAp0QgBQAgjtDZYnv16iVlypSRixcvyn//+19XhVMreD/++KPMnTvXPOZEZ6/VAKvB9XG8vLxMIPzqq69MxdIZ7L799ltThdXz6oy/2lVVw2tk6NhYnV1Xu7tqUNR2axddZ7VUu9rqY180hOoYWt1Hx2k6H0UTko7b1O69H3/8sQmd+j61y66OddVQGfyxLuXKlZPWrVub6mn//v1dFeCo3ietvK5bt86EWB0Xq4/J0WP1ngEAos5DZzZ6iuMBAEAM04l79LmbGhBTpUpluzkAAEQbKqQAAAAAACsIpAAAAAAAK+iyCwAAAACwggopAAAAAMAKAikAAAAAwAoCKQAAAADACgIpAAAAAMAKAikAAAAAwAoCKQAAAADACgIpAAAAAMAKAikAAAAAQGz4f/OcrvYV1IQ4AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x800 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "importances = rf.feature_importances_\n",
    "features = X.columns\n",
    "\n",
    "# Create Series and sort\n",
    "feat_importances = pd.Series(importances, index=features).sort_values(ascending=False)\n",
    "\n",
    "# Plot\n",
    "plt.figure(figsize=(10, 8))\n",
    "sns.barplot(x=feat_importances.values[:16], y=feat_importances.index[:16])\n",
    "plt.title('Important Features')\n",
    "plt.xlabel('Importance Score')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 284,
   "id": "942fcda8-aa91-46ed-b7c1-843c22f89e97",
   "metadata": {},
   "outputs": [],
   "source": [
    "# feat_importances['']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b266a408-e780-4096-a7cf-4a2ab88ae9a6",
   "metadata": {},
   "source": [
    "## all features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 285,
   "id": "c6be9816-5778-4f8f-ad21-4ee0fd6b5166",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy after feature selection: 0.71\n"
     ]
    }
   ],
   "source": [
    "rf_reduced = RandomForestClassifier(n_estimators=200, random_state=55,class_weight='balanced')\n",
    "rf_reduced.fit(X_train, y_train)\n",
    "\n",
    "# Evaluate\n",
    "accuracy = rf_reduced.score(X_test, y_test)\n",
    "print(f\"Accuracy after feature selection: {accuracy:.2f}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a409c69a-db36-4aee-b859-a3415646cd65",
   "metadata": {},
   "source": [
    "## select features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 286,
   "id": "3212adef-5ba8-47dc-992b-d8e78b304a8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "selected_features = feat_importances[feat_importances > 0.02].index\n",
    "X_train_reduced = X_train[selected_features]\n",
    "X_test_reduced = X_test[selected_features]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 287,
   "id": "4ee02831-36d5-42ad-8a38-fc7028f5bc71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy after feature selection: 0.70\n"
     ]
    }
   ],
   "source": [
    "rf_reduced = RandomForestClassifier(n_estimators=200, random_state=55,class_weight='balanced')\n",
    "rf_reduced.fit(X_train_reduced, y_train)\n",
    "\n",
    "# Evaluate\n",
    "accuracy = rf_reduced.score(X_test_reduced, y_test)\n",
    "print(f\"Accuracy after feature selection: {accuracy:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 288,
   "id": "18869005-35ef-4edc-9552-d8d6e1d3065b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "defd6f22-d7b5-495c-9c94-91ebacef08dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 295,
   "id": "c6d45d42-c51b-4e2c-8581-c5aca9cf03f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.72      0.78      0.75      6994\n",
      "           1       0.76      0.69      0.73      6987\n",
      "\n",
      "    accuracy                           0.74     13981\n",
      "   macro avg       0.74      0.74      0.74     13981\n",
      "weighted avg       0.74      0.74      0.74     13981\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from xgboost import XGBClassifier\n",
    "from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay\n",
    "\n",
    "\n",
    "# Train XGBoost with class weighting (if imbalanced)\n",
    "xgb = XGBClassifier(\n",
    "    eval_metric=\"auc\",\n",
    "    n_estimators=200,\n",
    "    max_depth=5,\n",
    "    learning_rate=0.1\n",
    ")\n",
    "xgb.fit(X_train_reduced, y_train)\n",
    "\n",
    "# Evaluate\n",
    "\n",
    "y_pred_xgb = xgb.predict(X_test_reduced)\n",
    "print(classification_report(y_test, y_pred_xgb))\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 299,
   "id": "678e0f1e-4e64-4c78-ba5e-7ac22ddd121a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-6 {\n",
       "  /* Definition of color scheme common for light and dark mode */\n",
       "  --sklearn-color-text: #000;\n",
       "  --sklearn-color-text-muted: #666;\n",
       "  --sklearn-color-line: gray;\n",
       "  /* Definition of color scheme for unfitted estimators */\n",
       "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
       "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
       "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
       "  --sklearn-color-unfitted-level-3: chocolate;\n",
       "  /* Definition of color scheme for fitted estimators */\n",
       "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
       "  --sklearn-color-fitted-level-1: #d4ebff;\n",
       "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
       "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
       "\n",
       "  /* Specific color for light theme */\n",
       "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
       "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-icon: #696969;\n",
       "\n",
       "  @media (prefers-color-scheme: dark) {\n",
       "    /* Redefinition of color scheme for dark theme */\n",
       "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
       "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-icon: #878787;\n",
       "  }\n",
       "}\n",
       "\n",
       "#sk-container-id-6 {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 pre {\n",
       "  padding: 0;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 input.sk-hidden--visually {\n",
       "  border: 0;\n",
       "  clip: rect(1px 1px 1px 1px);\n",
       "  clip: rect(1px, 1px, 1px, 1px);\n",
       "  height: 1px;\n",
       "  margin: -1px;\n",
       "  overflow: hidden;\n",
       "  padding: 0;\n",
       "  position: absolute;\n",
       "  width: 1px;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-dashed-wrapped {\n",
       "  border: 1px dashed var(--sklearn-color-line);\n",
       "  margin: 0 0.4em 0.5em 0.4em;\n",
       "  box-sizing: border-box;\n",
       "  padding-bottom: 0.4em;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-container {\n",
       "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
       "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
       "     so we also need the `!important` here to be able to override the\n",
       "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
       "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
       "  display: inline-block !important;\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-text-repr-fallback {\n",
       "  display: none;\n",
       "}\n",
       "\n",
       "div.sk-parallel-item,\n",
       "div.sk-serial,\n",
       "div.sk-item {\n",
       "  /* draw centered vertical line to link estimators */\n",
       "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
       "  background-size: 2px 100%;\n",
       "  background-repeat: no-repeat;\n",
       "  background-position: center center;\n",
       "}\n",
       "\n",
       "/* Parallel-specific style estimator block */\n",
       "\n",
       "#sk-container-id-6 div.sk-parallel-item::after {\n",
       "  content: \"\";\n",
       "  width: 100%;\n",
       "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
       "  flex-grow: 1;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-parallel {\n",
       "  display: flex;\n",
       "  align-items: stretch;\n",
       "  justify-content: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-parallel-item {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-parallel-item:first-child::after {\n",
       "  align-self: flex-end;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-parallel-item:last-child::after {\n",
       "  align-self: flex-start;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-parallel-item:only-child::after {\n",
       "  width: 0;\n",
       "}\n",
       "\n",
       "/* Serial-specific style estimator block */\n",
       "\n",
       "#sk-container-id-6 div.sk-serial {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "  align-items: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  padding-right: 1em;\n",
       "  padding-left: 1em;\n",
       "}\n",
       "\n",
       "\n",
       "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
       "clickable and can be expanded/collapsed.\n",
       "- Pipeline and ColumnTransformer use this feature and define the default style\n",
       "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
       "*/\n",
       "\n",
       "/* Pipeline and ColumnTransformer style (default) */\n",
       "\n",
       "#sk-container-id-6 div.sk-toggleable {\n",
       "  /* Default theme specific background. It is overwritten whether we have a\n",
       "  specific estimator or a Pipeline/ColumnTransformer */\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "/* Toggleable label */\n",
       "#sk-container-id-6 label.sk-toggleable__label {\n",
       "  cursor: pointer;\n",
       "  display: flex;\n",
       "  width: 100%;\n",
       "  margin-bottom: 0;\n",
       "  padding: 0.5em;\n",
       "  box-sizing: border-box;\n",
       "  text-align: center;\n",
       "  align-items: start;\n",
       "  justify-content: space-between;\n",
       "  gap: 0.5em;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 label.sk-toggleable__label .caption {\n",
       "  font-size: 0.6rem;\n",
       "  font-weight: lighter;\n",
       "  color: var(--sklearn-color-text-muted);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 label.sk-toggleable__label-arrow:before {\n",
       "  /* Arrow on the left of the label */\n",
       "  content: \"▸\";\n",
       "  float: left;\n",
       "  margin-right: 0.25em;\n",
       "  color: var(--sklearn-color-icon);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 label.sk-toggleable__label-arrow:hover:before {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "/* Toggleable content - dropdown */\n",
       "\n",
       "#sk-container-id-6 div.sk-toggleable__content {\n",
       "  max-height: 0;\n",
       "  max-width: 0;\n",
       "  overflow: hidden;\n",
       "  text-align: left;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-toggleable__content.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-toggleable__content pre {\n",
       "  margin: 0.2em;\n",
       "  border-radius: 0.25em;\n",
       "  color: var(--sklearn-color-text);\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-toggleable__content.fitted pre {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
       "  /* Expand drop-down */\n",
       "  max-height: 200px;\n",
       "  max-width: 100%;\n",
       "  overflow: auto;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
       "  content: \"▾\";\n",
       "}\n",
       "\n",
       "/* Pipeline/ColumnTransformer-specific style */\n",
       "\n",
       "#sk-container-id-6 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator-specific style */\n",
       "\n",
       "/* Colorize estimator box */\n",
       "#sk-container-id-6 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-label label.sk-toggleable__label,\n",
       "#sk-container-id-6 div.sk-label label {\n",
       "  /* The background is the default theme color */\n",
       "  color: var(--sklearn-color-text-on-default-background);\n",
       "}\n",
       "\n",
       "/* On hover, darken the color of the background */\n",
       "#sk-container-id-6 div.sk-label:hover label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "/* Label box, darken color on hover, fitted */\n",
       "#sk-container-id-6 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator label */\n",
       "\n",
       "#sk-container-id-6 div.sk-label label {\n",
       "  font-family: monospace;\n",
       "  font-weight: bold;\n",
       "  display: inline-block;\n",
       "  line-height: 1.2em;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-label-container {\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "/* Estimator-specific */\n",
       "#sk-container-id-6 div.sk-estimator {\n",
       "  font-family: monospace;\n",
       "  border: 1px dotted var(--sklearn-color-border-box);\n",
       "  border-radius: 0.25em;\n",
       "  box-sizing: border-box;\n",
       "  margin-bottom: 0.5em;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-estimator.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "/* on hover */\n",
       "#sk-container-id-6 div.sk-estimator:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-6 div.sk-estimator.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
       "\n",
       "/* Common style for \"i\" and \"?\" */\n",
       "\n",
       ".sk-estimator-doc-link,\n",
       "a:link.sk-estimator-doc-link,\n",
       "a:visited.sk-estimator-doc-link {\n",
       "  float: right;\n",
       "  font-size: smaller;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1em;\n",
       "  height: 1em;\n",
       "  width: 1em;\n",
       "  text-decoration: none !important;\n",
       "  margin-left: 0.5em;\n",
       "  text-align: center;\n",
       "  /* unfitted */\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted,\n",
       "a:link.sk-estimator-doc-link.fitted,\n",
       "a:visited.sk-estimator-doc-link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "/* Span, style for the box shown on hovering the info icon */\n",
       ".sk-estimator-doc-link span {\n",
       "  display: none;\n",
       "  z-index: 9999;\n",
       "  position: relative;\n",
       "  font-weight: normal;\n",
       "  right: .2ex;\n",
       "  padding: .5ex;\n",
       "  margin: .5ex;\n",
       "  width: min-content;\n",
       "  min-width: 20ex;\n",
       "  max-width: 50ex;\n",
       "  color: var(--sklearn-color-text);\n",
       "  box-shadow: 2pt 2pt 4pt #999;\n",
       "  /* unfitted */\n",
       "  background: var(--sklearn-color-unfitted-level-0);\n",
       "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted span {\n",
       "  /* fitted */\n",
       "  background: var(--sklearn-color-fitted-level-0);\n",
       "  border: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link:hover span {\n",
       "  display: block;\n",
       "}\n",
       "\n",
       "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
       "\n",
       "#sk-container-id-6 a.estimator_doc_link {\n",
       "  float: right;\n",
       "  font-size: 1rem;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1rem;\n",
       "  height: 1rem;\n",
       "  width: 1rem;\n",
       "  text-decoration: none;\n",
       "  /* unfitted */\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 a.estimator_doc_link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "#sk-container-id-6 a.estimator_doc_link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "#sk-container-id-6 a.estimator_doc_link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "</style><div id=\"sk-container-id-6\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression(class_weight=&#x27;balanced&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-6\" type=\"checkbox\" checked><label for=\"sk-estimator-id-6\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow\"><div><div>LogisticRegression</div></div><div><a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LogisticRegression.html\">?<span>Documentation for LogisticRegression</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></div></label><div class=\"sk-toggleable__content fitted\"><pre>LogisticRegression(class_weight=&#x27;balanced&#x27;)</pre></div> </div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression(class_weight='balanced')"
      ]
     },
     "execution_count": 299,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "log_reg = LogisticRegression(class_weight='balanced')\n",
    "log_reg.fit(X_train_reduced, y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 300,
   "id": "6af395ff-64c7-40dd-a98b-71f8751f5ccc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.72\n"
     ]
    }
   ],
   "source": [
    "accuracy = log_reg.score(X_test_reduced, y_test)\n",
    "print(f\"Accuracy: {accuracy:.2f}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8738b38b-9e9c-47a9-8243-eaa77dff7c59",
   "metadata": {},
   "source": [
    "# 🧮 Predicting Heart Attack Risk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 292,
   "id": "1f35f1c9-b9ef-42d8-96ab-6173d8cf5257",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                 Model  Accuracy  Precision  Recall  F1-score  ROC AUC\n",
      "0        Random Forest      0.70       0.70    0.69      0.70     0.76\n",
      "1              XGBoost      0.74       0.76    0.69      0.72     0.80\n",
      "2  Logistic Regression      0.72       0.75    0.68      0.71     0.78\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score\n",
    "\n",
    "# افترض أنك عندك تنبؤات واحتمالات من 3 موديلات:\n",
    "models = {\n",
    "    \"Random Forest\": (rf_reduced, X_test_reduced),\n",
    "    \"XGBoost\": (xgb, X_test_reduced),\n",
    "    \"Logistic Regression\": (log_reg, X_test_reduced)  # افترض أنك دربت logistic\n",
    "}\n",
    "\n",
    "results = {\"Model\": [], \"Accuracy\": [], \"Precision\": [], \"Recall\": [], \"F1-score\": [], \"ROC AUC\": []}\n",
    "\n",
    "for name, (model, X) in models.items():\n",
    "    y_pred = model.predict(X)\n",
    "    y_proba = model.predict_proba(X)[:, 1]\n",
    "\n",
    "    results[\"Model\"].append(name)\n",
    "    results[\"Accuracy\"].append(accuracy_score(y_test, y_pred))\n",
    "    results[\"Precision\"].append(precision_score(y_test, y_pred))\n",
    "    results[\"Recall\"].append(recall_score(y_test, y_pred))\n",
    "    results[\"F1-score\"].append(f1_score(y_test, y_pred))\n",
    "    results[\"ROC AUC\"].append(roc_auc_score(y_test, y_proba))\n",
    "\n",
    "# عرض الجدول النهائي\n",
    "import pandas as pd\n",
    "df_results = pd.DataFrame(results)\n",
    "print(df_results.round(2))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc6df30a-d8d8-46c9-82cf-c8c021999b81",
   "metadata": {},
   "source": [
    "# 🖼️ Creating a Simple User Interface \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 301,
   "id": "897679cc-4eac-4894-9170-eb92009961c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['heart_attack_predictor.pkl']"
      ]
     },
     "execution_count": 301,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import joblib\n",
    "\n",
    "# حفظ نموذج XGBoost الأفضل\n",
    "joblib.dump(xgb, \"heart_attack_predictor.pkl\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 303,
   "id": "8c794c7b-ebb0-4bb2-8d7a-65bd5e794f86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\u001b[31m:\u001b[39m 1\n"
     ]
    }
   ],
   "source": [
    "# app.py\n",
    "from flask import Flask, request, jsonify\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "model = joblib.load(\"heart_attack_predictor.pkl\")\n",
    "\n",
    "@app.route(\"/predict\", methods=[\"POST\"])\n",
    "def predict():\n",
    "    data = request.get_json()\n",
    "    features = np.array([list(data.values())])\n",
    "    prediction = model.predict(features)[0]\n",
    "    return jsonify({\"prediction\": int(prediction)})\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18340e32-1e3a-490f-a5c1-7f9072bfe364",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c819f85-9ab6-48eb-a876-3d4cea4bf445",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a536f32-c6be-4668-9eeb-9f12af4579b1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d34fef5c-a41b-422c-835a-88c8442638b4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e78a8756-50de-4215-bf37-6fb297563b44",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72d3cbeb-121e-4e19-b41c-d489705ae404",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cba59d10-1236-4bdd-a6d3-c443aaeaab92",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e79ef8b9-a9b6-4c13-98ae-0be9cb353e10",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
