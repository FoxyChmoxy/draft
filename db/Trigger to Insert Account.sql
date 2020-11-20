USE adv
GO
CREATE OR ALTER TRIGGER Account_INSERT
ON Account
AFTER INSERT
AS
INSERT INTO AccountLogs (AccountId, Operation)
SELECT Id, 'New user was added, email: ' + Email
FROM INSERTED