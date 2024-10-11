from flask import jsonify


def populate_object(obj, data_dictionary):
    fields = data_dictionary.key()

    for field in fields:
        try:
            getattr(obj, fields)
            setattr(obj, field, data_dictionary[field])

        except AttributeError:
            jsonify({'Error': f'record has no attribute: {field}'}), 400