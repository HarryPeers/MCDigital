"""
Database tables:

blogs:
    PK BIGINT ID

    TEXT Title
    LONGTEXT Description
    BIGINT Owner
    BIGINT CreatedDate (utc timestamp)
    BIT status (approved/denied)
    
users:
    PK BIGINT ID

    TEXT Email
    BIT Admin

"""

class database:
    def __init__(self):
        pass