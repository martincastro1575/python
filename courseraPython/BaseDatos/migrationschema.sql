BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS 'currency'(
    'code' text,
    'name' text,
    'symbol' text,
    PRIMARY KEY('code')
);
COMMIT;