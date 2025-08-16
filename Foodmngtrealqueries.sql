SELECT 
    city, 
    COUNT(*) AS total_food_receivers
FROM 
    receivers_data
GROUP BY 
    city
ORDER BY 
    total_food_receivers DESC;
    
SELECT 
    city, 
    COUNT(*) AS total_food_providers
FROM 
    providers_data
GROUP BY 
    city
ORDER BY 
    total_food_providers DESC;
    
SELECT 
    Type, 
    COUNT(*) AS top_food_providers
FROM 
    providers_data
GROUP BY 
    Type
ORDER BY 
    top_food_providers DESC;
    
SELECT 
    Type,
    COUNT(*) AS top_food_receivers
FROM 
    providers_data
GROUP BY
    Type
ORDER BY 
    top_food_receivers DESC;
    
Select
sum(Quantity) AS total_quantity
FROM food_listings_data;

SELECT 
Location,
COUNT(*) AS top_citiesforlistings
FROM 
food_listings_data
GROUP BY Location
ORDER BY top_citiesforlistings DESC;


SELECT 
    Food_Type,
    COUNT(*) AS top_food_types
FROM 
    food_listings_data
GROUP BY
    Food_Type
ORDER BY 
    top_food_types DESC;
    
SELECT 
    food_listings_data.Food_Name,
    COUNT(*) AS total_claims
FROM 
    food_listings_data
JOIN 
    claims_data 
    ON food_listings_data.Food_ID=claims_data.Food_ID
GROUP BY 
	food_listings_data.Food_Name
ORDER BY 
    total_claims DESC;
    
SELECT 
    food_listings_data.Provider_Type,
    COUNT(*) AS top_provider
FROM 
    food_listings_data
JOIN 
    claims_data 
    ON food_listings_data.Food_ID=claims_data.Food_ID
WHERE 
claims_data.Status="Completed"
GROUP BY 
	food_listings_data.Provider_Type
ORDER BY 
    top_provider DESC;
    
SELECT 
    Status,
    COUNT(*) AS total_claims,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims_data),
        2
    ) AS percentage_of_total
FROM 
    claims_data
GROUP BY 
    Status
ORDER BY
percentage_of_total DESC;

SELECT 
    AVG(Quantity) AS average_quantity
FROM
    food_listings_data;
    
    
SELECT 
Meal_Type,
COUNT(*) AS top_meal
FROM 
food_listings_data
GROUP BY Meal_Type
ORDER BY top_meal DESC;

SELECT
Provider_Type,
SUM(Quantity) AS Provider_quantity
FROM food_listings_data
GROUP BY Provider_Type
ORDER BY provider_quantity DESC;





