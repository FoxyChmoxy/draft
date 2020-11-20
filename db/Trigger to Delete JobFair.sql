USE adv
GO
CREATE TRIGGER JobFair_DELETE
ON JobFair
AFTER DELETE
AS
INSERT INTO JobFairLogs (ProjectId, EmployeeId, RManagerId, Hire)
SELECT ProjectId, EmployeeId, RManagerId, 0
FROM DELETED