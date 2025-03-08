from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            data = [[*map(str,x)] for x in data]
            # [*map(lambda x : ",".join(x),data)]
            return("Pending...",data)
        case CSVExportStatus.PROCESSING:
            return("Processing...","\n".join(map(lambda x:",".join(x),data)))
        case CSVExportStatus.SUCCESS:
            return("Success!",data)
        case CSVExportStatus.FAILURE:
            result = [[*map(str,x)] for x in data]
            return("Unknown error, retrying...", "\n".join(map(lambda x:",".join(x),result)))
        case _:
            raise Exception("Unknown export status")  
