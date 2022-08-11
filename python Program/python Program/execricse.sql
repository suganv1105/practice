/* Update the part to be recalled */
UPDATE Car_Parts
SET part_recall = 0
WHERE part_name = 'Jetrag 6 Speed' and manufacture_start_date < date("2012-04-13") and manufacture_end_date > date("2012-04-13");

SELECT CO.customer_id, CO.vin
FROM Customer_Ownership as CO
  LEFT OUTER JOIN Car_Vins as CV ON (CV.vin = CO.vin)
  LEFT OUTER JOIN Car_Options as COpt ON (COpt.option_set_id = CV.option_set_id)
  LEFT OUTER JOIN Car_Parts as CP on (CP.part_id = COpt.transmission_id)
WHERE CP.part_recall = 1 and part_name='Jetrag 7 Speed';

/* Finds the top sellers by purchase price for the past year */
SELECT B.brand_name, SUM(CO.purchase_price)
FROM Customer_Ownership as CO
  LEFT OUTER JOIN Car_Vins as CV on (CO.vin = CV.vin)
  LEFT OUTER JOIN Models as M on (CV.model_id = M.model_id)
  LEFT OUTER JOIN Brands as B on (B.brand_id = M.brand_id)
WHERE CO.purchase_date > date('now','-1 year')
GROUP BY B.brand_name
ORDER BY SUM(CO.purchase_price) DESC
LIMIT 2;

/* Finds the top sellers by units sold for the past year */
SELECT B.brand_name, COUNT(B.brand_name)
FROM Customer_Ownership as CO
  LEFT OUTER JOIN Car_Vins as CV on (CO.vin = CV.vin)
  LEFT OUTER JOIN Models as M on (CV.model_id = M.model_id)
  LEFT OUTER JOIN Brands as B on (B.brand_id = M.brand_id)
WHERE CO.purchase_date > date('now','-1 year')
GROUP BY B.brand_name
ORDER BY COUNT(B.brand_name) DESC
LIMIT 2;

/* Count of purchases aggregated by year, month, and week */
SELECT STRFTIME('%Y', CO.purchase_date) Date_Year, STRFTIME('%M', CO.purchase_date) Date_Month, CV.brand, strftime('%W', CO.purchase_date) Date_WeekNum, Count(CO.vin)
FROM Customer_Ownership CO LEFT OUTER JOIN Car_Vins CV ON (CV.vin = CO.vin)
GROUP BY STRFTIME('%Y', CO.purchase_date),STRFTIME('%M', CO.purchase_date), CV.brand;
