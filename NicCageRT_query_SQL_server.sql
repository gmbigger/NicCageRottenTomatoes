SELECT * FROM NicCageRT

ALTER TABLE NicCageRT
DROP COLUMN F1

-- Slect all data with no NULL values
SELECT * FROM NicCageRT
WHERE Boxoffice IS NOT NULL
	AND RTScore IS NOT NULL
    AND AudienceScore IS NOT NULL;

-- The top ten Rotten Tomatoes rated films    
SELECT TOP 10 * FROM NicCageRT
ORDER BY RTScore DESC

-- The top ten audience rated films    
SELECT TOP 10 * FROM niccagert
ORDER BY AudienceScore DESC

-- The top ten highest earning films   
SELECT TOP 10 * FROM niccagert
ORDER BY Boxoffice DESC