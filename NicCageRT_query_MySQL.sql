USE niccagert;

SELECT 
    *
FROM
    NicCageRT;

-- Select all data with no NULL values
-- We will save this query so we can updload it to a data viz program
SELECT 
    *
FROM
    NicCageRT
WHERE
    Boxoffice IS NOT NULL
        AND RTScore IS NOT NULL
        AND AudienceScore IS NOT NULL;

-- A few other queries to analyze the data

-- The top ten Rotten Tomatoes rated films    
SELECT 
    *
FROM
    niccagert
ORDER BY RTScore DESC
LIMIT 10;

-- The top ten audience rated films    
SELECT 
    *
FROM
    niccagert
ORDER BY AudienceScore DESC
LIMIT 10;

-- The top ten highest earning films   
SELECT 
    *
FROM
    niccagert
ORDER BY Boxoffice DESC
LIMIT 10;