from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from .subject import Subject


class User(Subject):
    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }

    uuid = Column(String(36), ForeignKey(Subject.uuid), primary_key=True)
    name = Column(String(256))

    groups = relationship('Group', viewonly=True, secondary='t_membership')
    memberships = relationship('Membership', back_populates='user')

    def __init__(self, uuid, name=None):
        self.uuid = uuid
        self.name = name
