metadata_schema = {
  "type": "array",
  "default": [

  ],
  "items": {
    "type": "object",
    "properties": {
      "key_name": {
        "type": "string",
        "minLength": 1
      },
      "key_type": {
        "type": "string",
        "enum": [
          "text",
          "number",
          "date"
        ]
      }
    },
    "required": [
      "key_name",
      "key_value",
      "key_type"
    ],
    "allOf": [
      {
        "if": {
          "properties": {
            "key_type": {
              "const": "text"
            }
          }
        },
        "then": {
          "properties": {
            "key_value": {
              "minLength": 1
            }
          }
        }
      },
      {
        "if": {
          "properties": {
            "key_type": {
              "const": "number"
            }
          }
        },
        "then": {
          "properties": {
            "key_value": {
              "type": "number",
              "minimum": 0,
              "maximum": 5000
            }
          }
        }
      },
      {
        "if": {
          "properties": {
            "key_type": {
              "const": "date"
            }
          }
        },
        "then": {
          "properties": {
            "key_value": {
              "type": "string",
              "pattern": r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))"
            }
          }
        }
      }
    ]
  }
}
