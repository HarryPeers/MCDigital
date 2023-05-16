"""

blogs:
    PK BIGINT ID

    TEXT Title
    LONGTEXT Description
    BIGINT Owner
    BIGINT CreatedDate (utc timestamp)
    BIT status (approved/denied)

"""

class blog:
    def __init__(self):
        pass