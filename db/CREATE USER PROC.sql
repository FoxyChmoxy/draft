use adv
GO
CREATE OR ALTER PROCEDURE CreateNewAccount @username nvarchar(30)
AS
INSERT INTO dbo.Account
VALUES (NEWID(), CONCAT(@username, '@', 'example.com'), @username, '123qwe', 1, GETDATE(), GETDATE(), 'system', 'system', NULL)
GO