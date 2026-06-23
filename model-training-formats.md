- pickle -> pkl 
- ONNX format --> .onnx 

Training Data 
     |
Traing a Model
     |
Save the brain ->.pkl|onnx
     |
Load the brain later
     |
  Predict

  Area  Price
  1000 40L
  1200 45L
  1500 50L
  1800 60L
  2200 85L
  2500 90L
  2700 95L
  3000 100L

  - Split Point at 2000

  Left: 
  1000 40L
  1200 45L
  1500 50L
  1800 60L
  -------
       48.75L
  
  Right:
  2200 85L
  2500 90L
  2700 95L
  3000 100L
  --------
      92.5
 is > 2000
 No -> 48,75L
 Yes -> 92.5L
 -----------
 1460 rows 5 features

 Tree-1 Area>2000 

 Tree2 
 Bedrooms > 3 

Tree-1 -> 90
Tree-2 ->85
Tree-3 ->88

Tree-4 ->92
---------------

avg: 89 lakhs

---- 4 features
--- 10k records
Tree-1
area and Bedrooms
Tree-2
Bathroom
Garden

Tree-3
Area
Parking
