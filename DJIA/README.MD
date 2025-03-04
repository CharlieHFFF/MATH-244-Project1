
# Codebook for Dow Jones Dataset

## Overview
This dataset contains historical stock market data for the Dow Jones Industrial Average (DJI). The dataset includes daily stock information such as the opening price, closing price, highest and lowest prices, and trading volume.

## Variables

1. **date** (`datetime`):  
   - Description: The date of the stock market data entry.  
   - Format: YYYY-MM-DD  

2. **close** (`float`):  
   - Description: The closing price of the Dow Jones Index on the given date.  
   - Unit: USD  

3. **high** (`float`):  
   - Description: The highest price reached by the index during the trading day.  
   - Unit: USD  

4. **low** (`float`):  
   - Description: The lowest price reached by the index during the trading day.  
   - Unit: USD  

5. **open** (`float`):  
   - Description: The opening price of the Dow Jones Index at the start of the trading day.  
   - Unit: USD  

6. **volume** (`int`):  
   - Description: The total number of shares traded during the day.  
   - Unit: Number of shares  

## Notes  
- The dataset spans a specific date range, which should be checked for completeness.  
- Missing values, if any, should be handled appropriately based on the analysis needs.
