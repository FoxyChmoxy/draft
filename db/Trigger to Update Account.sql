USE adv
GO
CREATE OR ALTER TRIGGER Accounts_UPDATE
ON Account
AFTER UPDATE
AS
INSERT INTO AccountLogs (AccountId, Operation)
SELECT Id, 'Account is updated: ' + Email
FROM INSERTED