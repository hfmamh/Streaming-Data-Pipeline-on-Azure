SELECT
    TOP 10
    JSON_VALUE(doc, '$.gender') AS genero,
    JSON_VALUE(doc, '$.firstname') AS nombre,
    JSON_VALUE(doc, '$.lastname') AS apellido
FROM
    OPENROWSET(
        BULK 'https://xxxxxxxxxxxxxxxxx.dfs.core.windows.net/xxxxxxxcontainer/stream/user_gender/**',
        FORMAT = 'CSV',
        --PARSER_VERSION = '2.0',
        fieldterminator ='0x0b',
        fieldquote = '0x0b'
    ) with (doc nvarchar(max)) as rows