/*
Here are links to help you get started with Stream Analytics Query Language:
Common query patterns - https://go.microsoft.com/fwLink/?LinkID=619153
Query language - https://docs.microsoft.com/stream-analytics-query/query-language-elements-azure-stream-analytics
*/
SELECT
    GetRecordPropertyValue(GetArrayElement(results, 0), 'gender') AS gender,
    GetRecordPropertyValue(GetArrayElement(results, 0), 'name.first') AS firstname,
    GetRecordPropertyValue(GetArrayElement(results, 0), 'name.last') AS lastname,
    EventProcessedUtcTime, PartitionId, EventEnqueuedUtcTime
INTO
    [maincontainer]
FROM
    [pythonfeeddata]