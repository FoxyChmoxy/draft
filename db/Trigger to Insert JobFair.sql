USE adv
GO
CREATE TRIGGER JobFair_INSERT
ON JobFair
AFTER INSERT
AS
INSERT INTO JobFairLogs (ProjectId, EmployeeId, RManagerId, Hire)
SELECT ProjectId, EmployeeId, RManagerId, 1
FROM INSERTED