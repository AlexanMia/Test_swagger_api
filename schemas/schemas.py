class Schemas:
    CREATED_PET_SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "category": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "name"
                ]
            },
            "name": {
                "type": "string"
            },
            "photoUrls": {
                "type": "array",
                "items": [
                    {
                        "type": "string"
                    }
                ]
            },
            "tags": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
                            "name": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "name"
                        ]
                    }
                ]
            },
            "status": {
                "type": "string"
            }
        },
        "required": [
            "id",
            "category",
            "name",
            "photoUrls",
            "tags",
            "status"
        ]
    }

    PLACE_AN_ORDER_SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "petId": {
                "type": "integer"
            },
            "quantity": {
                "type": "integer"
            },
            "shipDate": {
                "type": "string"
            },
            "status": {
                "type": "string"
            },
            "complete": {
                "type": "boolean"
            }
        },
        "required": [
            "id",
            "petId",
            "quantity",
            "shipDate",
            "status",
            "complete"
        ]
    }

    AVAILABLE_STATUS_SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "pending": {
                "type": "integer"
            },
            "available": {
                "type": "integer"
            },
            "sold": {
                "type": "integer"
            }
        },
        "required": [
            "pending",
            "available",
            "sold"
        ]
    }

    COMMON_INFO_ABOUT_ACTIONS_SCHEMA = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "code": {
                "type": "integer"
            },
            "type": {
                "type": "string"
            },
            "message": {
                "type": "string"
            }
        },
        "required": [
            "code",
            "type",
            "message"
        ]
    }
