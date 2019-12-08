from marshmallow import Schema, fields, pre_load, post_dump


class ProfileSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    age = fields.Int(required=True)
    # user_id = fields.Int(required=True)
    # ugly hack.
    # profile = fields.Nested('self', exclude=('profile',), default=True, load_only=True)

    class Meta:
        strict = True


profile_schema = ProfileSchema()
