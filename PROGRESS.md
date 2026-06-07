# ML Project Progress Log

## Stage 1: Project Setup & Data Loading ✅
Status: Completed

### Goals Completed
- Created professional ML folder structure
- Initialized Git repository
- Configured Python environment
- Downloaded Ames Housing dataset
- Built reusable CSV data loader using pathlib
- Connected notebooks with src/ modules

### Key Learnings
- Difference between notebooks and reusable modules
- Why raw data should remain immutable
- Using pathlib instead of hardcoded paths
- Basic pandas workflow
- Modular project organization
- Git initialization and commits

### Files Created
- src/data/load_data.py
- notebooks/01_exploration.ipynb
- README.md
- .gitignore
- requirements.txt

---

## Stage 2: Exploratory Data Analysis ✅
Status: Completed

### Tasks Completed
- Dataset overview
- Missing value analysis
- Target variable analysis
- Correlation analysis
- Boxplots and distribution analysis
- Heatmap visualization
- Numerical vs categorical feature separation

### Key Findings
- SalePrice is heavily right-skewed
- Strong outliers exist (luxury homes)
- Missing values often represent feature absence
- OverallQual strongly correlates with SalePrice
- Garage-related features are important predictors

### Key Learnings
- EDA is hypothesis-driven
- Correlation does not always imply causation
- Outliers can be valid business observations
- Business reasoning is critical during analysis

### Files Updated
- notebooks/01_exploration.ipynb
- src/visualization/visualize.py

---

## Stage 3: Data Cleaning ✅
Status: Completed

### Cleaning Decisions
- PoolQC missing values treated as absence of pool
- Fence missing values treated as no fence
- Alley missing values treated as no alley access
- Garage-related missing values interpreted as no garage
- Basement-related missing values interpreted as no basement
- LotFrontage used median imputation due to skewness
- Electrical used mode imputation
- Duplicate rows were not found

### Reusable Utilities Built
- fill_categorical_none()
- fill_numerical_median()
- fill_numerical_mean()

### Key Learnings
- Missing values require business understanding
- Different columns require different imputation strategies
- Median is safer for skewed numerical data
- Preprocessing should be modular and reusable
- Validation after transformations is critical

### Files Updated
- notebooks/02_preprocessing.ipynb
- src/data/preprocess.py

---
## Stage 4: Feature Preprocessing ✅
Status: Completed

### Tasks Completed

* Created train/test split
* Separated features (X) and target (y)
* Identified numerical columns
* Identified categorical columns
* Applied OneHotEncoder to categorical features
* Applied StandardScaler to numerical features
* Created ColumnTransformer for unified preprocessing
* Successfully generated processed training and test datasets
* Learned fit() vs transform() workflow
* Pipeline abstraction
* End-to-end preprocessing workflow
* Model training integration
* Production inference workflow
* Retraining strategy for new data

### Key Learnings

* Test data must never be used during fitting
* Data leakage can significantly inflate model performance
* OneHotEncoder converts categorical values into machine-readable features
* StandardScaler normalizes numerical feature scales
* ColumnTransformer applies different transformations to different feature groups
* fit() learns preprocessing rules
* transform() applies learned rules
* New production data should only be transformed, never fitted

### Important Concepts Understood

* Train/Test Split
* Data Leakage
* OneHotEncoder
* StandardScaler
* ColumnTransformer
* Pipeline Architecture
* Numerical vs Categorical Features
* Production Inference Workflow

### Example Results

* X_test_processed.shape = (292, 265)

### Current Understanding

A new house received after deployment:

1. Is NOT merged with training data
2. Is transformed using the fitted preprocessor
3. Is passed to the model for prediction
4. May later be included during periodic retraining

### Remaining Work
--
## Stage 5: Feature Engineering ✅
Status: Completed

### Features Created
- HouseAge
- TotalBathrooms
- TotalSquareFeet
- TotalPorchArea
- Remodeled
- YearsSinceRemodel
- TotalRooms

### Key Findings
- TotalSquareFeet became the 2nd strongest feature in the dataset
- Engineered features can outperform original features
- Feature engineering requires domain reasoning
- Correlation analysis helps evaluate feature usefulness

### Key Learnings
- Difference between preprocessing and feature engineering
- Creating meaningful aggregate features
- Avoiding target leakage
- Evaluating engineered features using correlation

## Stage 6: Pipeline Integration ⏸️
Status: Not Started
