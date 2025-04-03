# German Credit Data Codebook

## Basic Information
The dataset is retrieved from UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data). The dataset was originally created by Professor Hans Hofmann. This dataset classifies people described by a set of attributes as good or bad credit risks. Comes in two formats (one all numeric). Also comes with a cost matrix for which we are not going to use. 

## Variable Declarations

### Attribute 1: Status of Existing Checking Account (Qualitative)
- **A11**: ... < 0 DM  
- **A12**: 0 <= ... < 200 DM  
- **A13**: ... >= 200 DM / salary assignments for at least 1 year  
- **A14**: No checking account  

### Attribute 2: Duration in Months (Numerical)
- **Description**: Number of months the credit is granted for.

### Attribute 3: Credit History (Qualitative)
- **A30**: No credits taken / all credits paid back duly  
- **A31**: All credits at this bank paid back duly  
- **A32**: Existing credits paid back duly till now  
- **A33**: Delay in paying off in the past  
- **A34**: Critical account / other credits existing (not at this bank)  

### Attribute 4: Purpose (Qualitative)
- **A40**: Car (new)  
- **A41**: Car (used)  
- **A42**: Furniture/equipment  
- **A43**: Radio/television  
- **A44**: Domestic appliances  
- **A45**: Repairs  
- **A46**: Education  
- **A47**: (Vacation - does not exist?)  
- **A48**: Retraining  
- **A49**: Business  
- **A410**: Others  

### Attribute 5: Credit Amount (Numerical)
- **Description**: Total amount of credit granted.

### Attribute 6: Savings Account/Bonds (Qualitative)
- **A61**: ... < 100 DM  
- **A62**: 100 <= ... < 500 DM  
- **A63**: 500 <= ... < 1000 DM  
- **A64**: ... >= 1000 DM  
- **A65**: Unknown / no savings account  

### Attribute 7: Present Employment Since (Qualitative)
- **A71**: Unemployed  
- **A72**: ... < 1 year  
- **A73**: 1 <= ... < 4 years  
- **A74**: 4 <= ... < 7 years  
- **A75**: ... >= 7 years  

### Attribute 8: Installment Rate (Numerical)
- **Description**: Installment rate as a percentage of disposable income.

### Attribute 9: Personal Status and Sex (Qualitative)
- **A91**: Male - Divorced/Separated  
- **A92**: Female - Divorced/Separated/Married  
- **A93**: Male - Single  
- **A94**: Male - Married/Widowed  
- **A95**: Female - Single  

### Attribute 10: Other Debtors / Guarantors (Qualitative)
- **A101**: None  
- **A102**: Co-applicant  
- **A103**: Guarantor  

### Attribute 11: Present Residence Since (Numerical)
- **Description**: Number of years living at the current residence.

### Attribute 12: Property (Qualitative)
- **A121**: Real estate  
- **A122**: If not A121: Building society savings agreement / life insurance  
- **A123**: If not A121/A122: Car or other, not in attribute 6  
- **A124**: Unknown / no property  

### Attribute 13: Age in Years (Numerical)
- **Description**: Age of the aadpplicant.

### Attribute 14: Other Installment Plans (Qualitative)
- **A141**: Bank  
- **A142**: Stores  
- **A143**: None  

### Attribute 15: Housing (Qualitative)
- **A151**: Rent  
- **A152**: Own  
- **A153**: For free  

### Attribute 16: Number of Existing Credits at this Bank (Numerical)
- **Description**: Total number of existing credit agreements with the bank.

### Attribute 17: Job (Qualitative)
- **A171**: Unemployed / Unskilled - Non-resident  
- **A172**: Unskilled - Resident  
- **A173**: Skilled employee / Official  
- **A174**: Management / Self-employed / Highly qualified employee / Officer  

### Attribute 18: Number of People Being Liable to Provide Maintenance for (Numerical)
- **Description**: Number of dependents financially supported.

### Attribute 19: Telephone (Qualitative)
- **A191**: None  
- **A192**: Yes, registered under the customer’s name  

### Attribute 20: Foreign Worker (Qualitative)
- **A201**: Yes  
- **A202**: No  

### Attribute 21: Target (Binary)
- **1**: Good credit risk  
- **2**: Bad credit risk  