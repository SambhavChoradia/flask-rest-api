# coding: utf-8

from flask import Blueprint, request
from flask_apispec import marshal_with, use_kwargs
from flask_jwt_extended import current_user, jwt_required, jwt_optional

from blog.exceptions import InvalidUsage
from blog.profile.models import Profile
from blog.profile.serializer import profile_schema

blueprint = Blueprint('profiles', __name__)

@blueprint.route('/api/profiles', methods=('POST',))
@jwt_required
@use_kwargs(profile_schema)
@marshal_with(profile_schema)
def create_profile(first_name,last_name,phone_number,age, **kwargs):
    user = current_user
    if not user:
        raise InvalidUsage.user_not_found()
    profile = Profile(user,first_name,last_name,phone_number,age).save()
    return profile

@blueprint.route('/api/profiles/', methods=('GET',))
@jwt_required
@marshal_with(profile_schema)
def get_profile():
    user = current_user
    if not user:
        raise InvalidUsage.user_not_found()
    return user.profile
