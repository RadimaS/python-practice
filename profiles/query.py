import graphene
from graphene_django import DjangoObjectType
from profiles.models import Profile


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)

    def resolve_all_profiles(root, info):
        return Profile.objects.all()


